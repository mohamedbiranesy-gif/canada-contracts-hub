#!/usr/bin/env python3
"""A time box and a state file for a reader that many threads feed (tools/org_extras.py, tools/org_contacts.py).

Why (2026-11-11): both readers wrote their whole state every five minutes, from whichever worker thread had just finished a site, to one
temporary path. With 230,000 records and 40 threads sharing the interpreter a write came to take longer than five minutes, so a second
write started on the same path while the first was still running, and the first one's rename put the second one's half-written file
under the published name. `timeout` stopped the reader in that state on two of the eight runners of run 42958065125: two truncated .gz
files, a merge that crashed on them, a refresh pass of 16 runner-hours left unmerged.

  StateFile  one write at a time, each to a path of its own; the next one no sooner than `every` seconds after the last one ENDED.
  Tried      the sites a reader could not read, remembered between runs (the state file holds only what was read): a runner starts from
             nothing, so every run asked every failing site again — 48,000 sites a run on 2026-11-11, among them the sites that refuse
             the reader ("refused sites are not asked again", coord/DECISIONS.md). One line per try, in append-only shards in git.
  Box        the reader stops by itself at its deadline (or on SIGTERM): no new site is started, the sites being read get `grace`
             seconds, then the main thread writes the state once more, alone, and leaves.
"""
import datetime, glob, gzip, json, os, re, signal, sys, threading, time
from concurrent.futures import ThreadPoolExecutor


class StateFile:
    def __init__(self, path, rows, every=900, level=6, label="organisations"):
        """rows: a function that returns the list of records to write (it takes its own lock)"""
        self.path, self.rows, self.every, self.level, self.label = path, rows, every, level, label
        self._busy, self._last, self._n = threading.Lock(), time.time(), 0

    def _write(self, note):
        rows = self.rows()
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
        self._n += 1
        tmp, t0 = "%s.%d.%d.tmp" % (self.path, os.getpid(), self._n), time.time()
        try:
            with gzip.open(tmp, "wt", encoding="utf-8", compresslevel=self.level) as f:
                for d in rows:
                    f.write(json.dumps(d, ensure_ascii=False) + "\n")
            os.replace(tmp, self.path)
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)
        print(time.strftime("%H:%M"), "wrote", self.path, len(rows), self.label, "in %d s" % (time.time() - t0), note, flush=True)

    def maybe(self, note=""):
        """from a worker thread: write when it is time and nobody is writing. Never waits, never raises."""
        if time.time() - self._last < self.every or not self._busy.acquire(blocking=False):
            return False
        try:
            if time.time() - self._last < self.every:
                return False
            self._write(note)
            return True
        except Exception as e:
            print(time.strftime("%H:%M"), "state file not written (%s): the one before stays" % e, flush=True)
            return False
        finally:
            self._last = time.time()
            self._busy.release()

    def final(self, note=""):
        """from the main thread, at the end: waits for a write in progress, then writes (three tries)"""
        with self._busy:
            for _ in range(3):
                try:
                    self._write(note)
                    self._last = time.time()
                    return True
                except Exception as e:
                    print(time.strftime("%H:%M"), "state file not written (%s), trying again" % e, flush=True)
                    time.sleep(10)
        return False


class Box:
    def __init__(self, minutes=0.0):
        self.deadline = time.time() + float(minutes) * 60 if minutes else 0
        self.stop = threading.Event()
        try:
            signal.signal(signal.SIGTERM, lambda *_: self.stop.set())
        except ValueError:  # not the main thread (a test harness): the deadline alone
            pass

    def over(self):
        return self.stop.is_set() or bool(self.deadline and time.time() > self.deadline)

    def run(self, fn, tasks, workers, grace=45):
        """fn(task) for every task, on `workers` threads. True when every task was done; False when the time box (or SIGTERM) ended the
        run first — the tasks not started are dropped, the ones in progress had `grace` seconds, some threads may still be running."""
        if not tasks:
            return True
        left, lk, idle = [len(tasks)], threading.Lock(), threading.Event()

        def guarded(t):
            try:
                if not self.stop.is_set():
                    fn(t)
            finally:
                with lk:
                    left[0] -= 1
                    if left[0] == 0:
                        idle.set()

        ex = ThreadPoolExecutor(workers)
        for t in tasks:
            ex.submit(guarded, t)
        while not idle.wait(2):
            if self.over():
                break
        if idle.is_set() and not self.stop.is_set():
            ex.shutdown()
            return True
        self.stop.set()
        idle.wait(grace)
        ex.shutdown(wait=False, cancel_futures=True)
        return False

    @staticmethod
    def leave(code=0):
        """end the process now: worker threads still inside a slow site are not waited for (the state was written without them)"""
        sys.stdout.flush(); sys.stderr.flush()
        os._exit(code)


class Tried:
    """reader \t site key \t date \t status — one line per try that did not end in a record."""
    REFUSED = re.compile(r"^(?:robots|blocked|http_40[13]|http_429)$")          # the site says no: asked again after 30 days
    NOTHING = re.compile(r"^(?:no_contact|no_page|not_html|http_40[4-9]|http_410)$")  # it answers and has nothing for this reader: 21 days
    # anything else (no answer, a server error, a redirect that leads nowhere): 2 days after the first two tries, then 14

    def __init__(self, reader, folder=""):
        self.reader, self.last, self.new = reader, {}, []
        self.today = time.strftime("%Y-%m-%d")
        for p in sorted(glob.glob(os.path.join(folder, "org_tried_*.gz"))) if folder else []:
            try:
                with gzip.open(p, "rt", encoding="utf-8", errors="replace") as fh:
                    for l in fh:
                        f = l.rstrip("\n").split("\t")
                        if len(f) >= 4 and f[0] == reader:
                            o = self.last.get(f[1])
                            self.last[f[1]] = (max(f[2], o[0]) if o else f[2], f[3] if not o or f[2] >= o[0] else o[1], (o[2] if o else 0) + 1)
            except (OSError, EOFError):
                continue

    def wait(self, key):
        """True while a site that failed before is not to be asked again yet"""
        o = self.last.get(key)
        if not o:
            return False
        try:
            age = (datetime.date.fromisoformat(self.today) - datetime.date.fromisoformat(o[0])).days
        except ValueError:
            return False
        days = 30 if self.REFUSED.match(o[1]) else 21 if self.NOTHING.match(o[1]) else 2 if o[2] <= 2 else 14
        return age < days

    def note(self, key, status):
        self.new.append("%s\t%s\t%s\t%s\n" % (self.reader, key, self.today, (status or "?")[:40]))

    def save(self, path):
        if path and self.new:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(self.new)
        return len(self.new)
