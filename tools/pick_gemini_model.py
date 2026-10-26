#!/usr/bin/env python3
"""Choose Gemini models that actually answer right now for this API key.
Lists the key's models, ranks them (Flash first, then Pro, then Flash-Lite; newest version first; stable before
preview), sends each a 1-line probe, and keeps the first two that answer. A preferred model (env PREFERRED or
repository variable GEMINI_MODEL) is tried first. Writes model1=/model2= to $GITHUB_OUTPUT and prints the choice.
Usage: GEMINI_API_KEY=... python3 tools/pick_gemini_model.py"""
import json, os, re, sys, urllib.error, urllib.request

KEY = os.environ.get("GEMINI_API_KEY", "")
BASE = "https://generativelanguage.googleapis.com/v1beta"
SKIP = re.compile(r"image|tts|audio|live|embed|robotics|computer|vision|aqa|learnlm|gemma|nano|banana|veo|imagen|native|dialog|thinking-exp", re.I)


def call(path, body=None, timeout=30):
    r = urllib.request.Request(BASE + path, data=json.dumps(body).encode() if body is not None else None,
                               headers={"x-goog-api-key": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        return json.loads(resp.read())


def rank(n):
    v = re.search(r"gemini-(\d+(?:\.\d+)?)", n)
    fam = 0 if ("flash" in n and "lite" not in n) else 1 if "pro" in n else 2 if "lite" in n else 3
    return (fam, -(float(v.group(1)) if v else 0), 1 if re.search(r"preview|exp", n) else 0, 1 if "latest" in n else 0, n)


names, tok = [], ""
try:
    while True:
        d = call("/models?pageSize=200" + ("&pageToken=" + tok if tok else ""))
        names += [m["name"].split("/")[-1] for m in d.get("models", []) if "generateContent" in (m.get("supportedGenerationMethods") or [])]
        tok = d.get("nextPageToken")
        if not tok:
            break
except Exception as e:
    print("could not list models:", e, file=sys.stderr)
cands = sorted({n for n in names if n.startswith("gemini") and not SKIP.search(n)}, key=rank)
pref = os.environ.get("PREFERRED", "").strip()
if pref:
    cands = [pref] + [c for c in cands if c != pref]
print("candidates:", ", ".join(cands[:12]), file=sys.stderr)
ok = []
for n in cands[:10]:
    try:
        call("/models/%s:generateContent" % n, {"contents": [{"parts": [{"text": "Reply with the word OK."}]}]}, timeout=40)
        ok.append(n)
        print("answers:", n, file=sys.stderr)
    except urllib.error.HTTPError as e:
        print("skip %s: HTTP %s" % (n, e.code), file=sys.stderr)
    except Exception as e:
        print("skip %s: %s" % (n, e), file=sys.stderr)
    if len(ok) == 2:
        break
m1, m2 = (ok + ["", ""])[:2]
print("model1=%s model2=%s" % (m1, m2))
if os.environ.get("GITHUB_OUTPUT"):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write("model1=%s\nmodel2=%s\n" % (m1, m2))
