#!/usr/bin/env python3
"""Generate practice/scoring-sheet.md (blank answer grid + domain tracker) from practice/src. Run from repo root after build_practice.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glob, re
from build_practice import parse, SRC, ROOT

def load(key):
    qs = []
    for f in sorted(glob.glob(os.path.join(SRC, key + "-p*.txt"))):
        qs += parse(f)
    return qs

out = ["# Scoring sheet & domain tracker", "",
       "Use one sheet per sitting. Fill **Your answer** before opening any answers file, then mark ✓/✗ after review.",
       "Domain weights (official, v1.1): D1 34 % · D2 26 % · D3 22 % · D4 18 %. Real exam: 50 scored + 15 unscored of 65; scaled score 100–1000, pass 720 (compensatory) — raw % below is only a proxy.", ""]
for key, title in (("m1", "Mock Exam 1"), ("m2", "Mock Exam 2")):
    qs = load(key)
    out += [f"## {title} (65 questions, 130 min)", "", "Start time: ____  End time: ____  Flagged count: ____", "",
            "| Q | Domain | Skill | Type | Your answer | ✓/✗ | Guess? (Y/N) |", "|---|---|---|---|---|---|---|"]
    for q in qs:
        out.append(f"| {q['n']} | {q['dom']} | {q['task']} | {q['typ']} |  |  |  |")
    out += ["", "### Domain tracker", "",
            "| Domain | Questions | Correct | % | Target |", "|---|---|---|---|---|"]
    for d, w in (("D1", 22), ("D2", 17), ("D3", 14), ("D4", 12)):
        out.append(f"| {d} | {w} |  |  | ≥ 75 % |")
    out += ["| **Total** | **65** |  |  | ≥ 75–80 % (advice, not official) |", "",
            "Wrong or guessed → add a row to `practice/error-log-template.md` (topic · why wrong · one-line rule).", ""]
open(os.path.join(ROOT, "scoring-sheet.md"), "w", encoding="utf-8").write("\n".join(out))
print("written scoring-sheet.md")
