#!/usr/bin/env python3
"""Apply option-text patches to practice/src/<set>-p*.txt.
Patch line: set|question_number|letter|new option text   (set = m1, m2, t). '#' lines ignored.
Usage: python3 tools/apply_option_patch.py tools/patches/<file>.txt"""
import sys, re, glob, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
patches = {}
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip() or line.startswith("#"):
        continue
    s, n, L, text = line.split("|", 3)
    patches[(s, int(n), L)] = text.strip()
applied = set()
for s in ("m1", "m2", "t"):
    for path in sorted(glob.glob(os.path.join(ROOT, "practice", "src", f"{s}-p*.txt"))):
        src = open(path, encoding="utf-8").read().split("\n")
        cur = None
        for i, l in enumerate(src):
            m = re.match(r"@@Q (\d+) \|", l)
            if m:
                cur = int(m.group(1))
                continue
            m = re.match(r"^([A-F])\. ", l)
            if m and cur is not None and (s, cur, m.group(1)) in patches:
                src[i] = f"{m.group(1)}. {patches[(s, cur, m.group(1))]}"
                applied.add((s, cur, m.group(1)))
        open(path, "w", encoding="utf-8").write("\n".join(src))
missing = set(patches) - applied
print(f"applied {len(applied)} of {len(patches)} patches; missing: {sorted(missing)[:10]}")
