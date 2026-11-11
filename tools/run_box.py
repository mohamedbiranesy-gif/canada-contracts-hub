#!/usr/bin/env python3
"""A time box and a state file for a reader that many threads feed (tools/org_extras.py, tools/org_contacts.py).

Why (2026-11-11): both readers wrote their whole state every five minutes, from whichever worker thread had just finished a site, to one
temporary path. With 230,000 records and 40 threads sharing the interpreter a write came to take longer than five minutes, so a second
write started on the same path while the first was still running, and the first one's rename put the second one's half-written file
under the published name. `timeout` stopped the reader in that state on two of the eight runners of run 42958065125: two truncated .gz
files, a merge that crashed on them, a refresh pass of 16 runner-hours left unmerged.

  StateFile  one write at a time, each to a path of its own; the next one no sooner than `every` seconds after the last one ENDED.
  Box        the reader stops by itself at its deadline (or on SIGTERM): no new site is started, the sites being read get `grace`
             seconds, then the main thread writes the state once more, alone, and leaves.
"""
import gzip, json, os, signal, sys, threading, time
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
