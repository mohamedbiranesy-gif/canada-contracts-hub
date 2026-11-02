#!/usr/bin/env python3
"""Peek at the first lines of a zipped JSON-lines download by streaming only the first chunk (raw inflate of the first local entry).
usage: python3 -I zippeek.py <url> [nlines]"""
import sys, struct, zlib, urllib.request
url = sys.argv[1]; nl = int(sys.argv[2]) if len(sys.argv) > 2 else 3
r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "contracts-research/1.0"}), timeout=120)
buf = r.read(400000); r.close()
assert buf[:4] == b"PK\x03\x04", buf[:200]
fnlen, exlen = struct.unpack("<HH", buf[26:30]); method = struct.unpack("<H", buf[8:10])[0]
name = buf[30:30 + fnlen].decode(); data = buf[30 + fnlen + exlen:]
print("entry:", name, "method", method)
out = zlib.decompressobj(-15).decompress(data) if method == 8 else data
for l in out.decode("utf-8", "replace").splitlines()[:nl]:
    print(l[:700])
