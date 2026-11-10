#!/usr/bin/env python3
"""Before a workflow commits what a crawl wrote: no pre-signed storage address and no credential-shaped token in a plain-text file.

2026-11-10 19:38Z: the merge of a mailbox-crawl run (5,971 mailbox rows, 2,764 store rows, the run's done lines) was refused twelve times by
GitHub's push protection — one row's evidence address was a pre-signed S3 address (X-Amz-Credential=AKIA…&X-Amz-Signature=…), which the
scanner reads as an AWS key. The workflow ended green and nothing was saved. The crawler now keeps the address that was asked
(ap_crawler.stable_url); this guard is the net under every writer: a third party's key or signed address never belongs in the dataset.

  python3 tools/secret_guard.py [paths …]      default: the files `git status` shows as changed or new under data/ and coord/
Each plain-text file (csv, tsv, jsonl, json, md, txt) is rewritten when a line holds one of the patterns:
  a signed address  -> cut at the "?" (the query carries the key id and the signature)
  a key-shaped token (AWS access-key id, Google API key, Stripe live secret, Slack / GitHub token, a private-key header) -> "[credential removed]"
Compressed files are not opened (the scanner does not read them either). Prints what it changed; exit status 0.
"""
import os, re, subprocess, sys

SIGNED = re.compile(r"""(https?://[^\s"'<>,;|]+?)\?[^\s"'<>,|]*(?:X-Amz-Signature|X-Amz-Credential|X-Amz-Security-Token|AWSAccessKeyId|X-Goog-Signature|X-Goog-Credential|GoogleAccessId)=[^\s"'<>,|]*""", re.I)
TOKEN = re.compile(r"(?<![A-Za-z0-9])(?:A[KS]IA[0-9A-Z]{16}|AIza[0-9A-Za-z_\-]{35}|sk_live_[0-9A-Za-z]{20,}|rk_live_[0-9A-Za-z]{20,}|xox[baprs]-[0-9A-Za-z\-]{20,}|gh[pousr]_[0-9A-Za-z]{36,}|"
                   r"github_pat_[0-9A-Za-z_]{40,}|-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----)")
TEXT = (".csv", ".tsv", ".jsonl", ".json", ".md", ".txt")


def changed():
    out = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "--", "data", "coord"], capture_output=True, text=True).stdout
    return [l[3:].strip().strip('"').split(" -> ")[-1] for l in out.splitlines() if l[:2].strip() and not l.startswith(" D") and not l.startswith("D ")]


def clean(path):
    try:
        with open(path, encoding="utf-8", errors="surrogateescape", newline="") as f:
            s = f.read()
    except OSError:
        return 0
    if not (SIGNED.search(s) or TOKEN.search(s)):
        return 0
    n = len(SIGNED.findall(s)) + len(TOKEN.findall(s))
    s = TOKEN.sub("[credential removed]", SIGNED.sub(lambda m: m.group(1), s))
    with open(path, "w", encoding="utf-8", errors="surrogateescape", newline="") as f:
        f.write(s)
    return n


def main():
    paths = sys.argv[1:] or changed()
    total = 0
    for p in paths:
        if os.path.isdir(p):
            fs = [os.path.join(d, x) for d, _, xs in os.walk(p) for x in xs]
        else:
            fs = [p]
        for f in fs:
            if f.lower().endswith(TEXT) and os.path.isfile(f) and os.path.getsize(f) < 200 * 1024 * 1024:
                n = clean(f)
                if n:
                    total += n
                    print("secret guard: %d signed address(es) / token(s) removed from %s" % (n, f))
    print("secret guard: %d file(s) looked at, %d removal(s)" % (len(paths), total))


if __name__ == "__main__":
    main()
