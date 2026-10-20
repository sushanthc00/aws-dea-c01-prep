#!/usr/bin/env python3
"""Scripted repo checks. Run from repo root: python3 tools/verify_repo.py
Checks: internal links, leftover TODO/TBD, outdated service names outside legacy/, JSON blocks, Python blocks,
practice QA (counts, balance, duplicate stems, MR option counts), flashcard CSV."""
import os, re, sys, json, ast, csv, glob, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)
md_files = [p.replace("\\","/") for p in glob.glob("**/*.md", recursive=True) if not p.startswith("legacy") and not p.startswith("DEA-Complete") and "node_modules" not in p]
problems = []

# 1. internal links
link_re = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(#[^)]*)?\)")
for f in md_files:
    txt = open(f, encoding="utf-8").read()
    for m in link_re.finditer(txt):
        tgt = m.group(1)
        if tgt.startswith(("http://", "https://", "mailto:")):
            continue
        path = os.path.normpath(os.path.join(os.path.dirname(f), tgt))
        if not os.path.exists(path):
            problems.append(f"BROKEN LINK {f}: {tgt}")

# 2. TODO / placeholder markers
for f in md_files:
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        if re.search(r"\b(TODO|TBD|FIXME|XXX)\b", line):
            problems.append(f"TODO {f}:{i}: {line.strip()[:80]}")

# 3. outdated names (allowed only where explicitly marked as former/old)
old_names = {"Kinesis Data Analytics": "Managed Service for Apache Flink", "Governed tables": "removed", "QuickSight": "Amazon Quick"}
for f in md_files:
    if f.startswith(("docs/", "practice/README")):
        continue
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        for old in old_names:
            if old in line and not re.search(r"formerly|former|old name|renamed|was |old |superseded|\(former|replac|→|not in|no longer|removed|rename|legacy|Quick", line, flags=re.I):
                problems.append(f"OLD NAME '{old}' {f}:{i}: {line.strip()[:90]}")

# 4. code blocks: JSON + Python syntax
blk_re = re.compile(r"```(\w*)\n(.*?)```", re.S)
checked = {"json": 0, "python": 0}
for f in md_files:
    txt = open(f, encoding="utf-8").read()
    for m in blk_re.finditer(txt):
        lang, body = m.group(1), m.group(2)
        if lang == "json":
            checked["json"] += 1
            try:
                json.loads(body)
            except Exception as e:
                problems.append(f"JSON invalid {f}: {str(e)[:60]} :: {body[:50]!r}")
        elif lang == "python":
            checked["python"] += 1
            try:
                ast.parse(body)
            except SyntaxError as e:
                problems.append(f"PYTHON syntax {f}: {e.msg} line {e.lineno}")

# 5. practice QA
sys.path.insert(0, "practice")
from build_practice import parse
for key in ("m1", "m2", "t"):
    qs = []
    for p in sorted(glob.glob(f"practice/src/{key}-p*.txt")):
        qs += parse(p)
    n = len(qs)
    stems = collections.Counter(re.sub(r"\W+", " ", q["stem"].lower())[:120] for q in qs)
    dup = [s for s, c in stems.items() if c > 1]
    if dup:
        problems.append(f"DUP STEMS {key}: {dup[:2]}")
    for q in qs:
        letters = [o[0] for o in q["opts"]]
        if q["typ"] == "MC" and (len(letters) != 4 or len(q["ans"]) != 1):
            problems.append(f"MC shape {key} Q{q['n']}")
        if q["typ"] == "MR" and (len(letters) < 5 or len(q["ans"]) < 2 or "Select" not in q["stem"]):
            problems.append(f"MR shape {key} Q{q['n']}")
        opt_text = [o[3:].strip().lower() for o in q["opts"]]
        if len(set(opt_text)) != len(opt_text):
            problems.append(f"duplicate option text {key} Q{q['n']}")
        if not q["expl"].count("\n- ") and not q["expl"].startswith("- "):
            problems.append(f"thin explanation {key} Q{q['n']}")
        correct_lens = [len(q["opts"][ord(a) - 65]) for a in q["ans"]]
        other = [len(o) for i, o in enumerate(q["opts"]) if chr(65 + i) not in q["ans"]]
        # longest-option bias flag
        if q["typ"] == "MC" and correct_lens[0] == max(correct_lens + other) and correct_lens[0] > 1.5 * (sum(other) / len(other)):
            problems.append(f"correct option much longer than distractors {key} Q{q['n']} (bias risk)")
    dist = collections.Counter(a for q in qs for a in q["ans"] if q["typ"] == "MC")
    print(f"[practice {key}] n={n} MC-positions={dict(sorted(dist.items()))} MR={sum(q['typ']=='MR' for q in qs)}")

# 6. flashcards
rows = list(csv.reader(open("practice/flashcards.csv", encoding="utf-8")))
bad = [i for i, r in enumerate(rows) if len(r) != 3]
if bad:
    problems.append(f"flashcards bad rows {bad[:5]}")
print(f"[flashcards] cards={len(rows)-1}")
print(f"[code blocks checked] {checked}")
print(f"[md files scanned] {len(md_files)}")
print("PROBLEMS:", len(problems))
for p in problems:
    print(" -", p)
sys.exit(1 if problems else 0)
