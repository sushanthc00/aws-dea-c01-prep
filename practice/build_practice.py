#!/usr/bin/env python3
"""Build practice/*.md from practice/src/<set>-p<N>.txt and print QA stats.
Source format: '@@Q n | MC/MR | Dx | task | E/M/H | answers' + stem + options, '@@E' + explanation lines.
Usage: python3 practice/build_practice.py   (run from repo root)"""
import re, sys, glob, os, collections

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
DOM = {"D1": "Data Ingestion and Transformation", "D2": "Data Store Management",
       "D3": "Data Operations and Support", "D4": "Data Security and Governance"}
DIFF = {"E": "Easy", "M": "Medium", "H": "Hard"}
SETNAME = {"m1": ("mock-1", "Mock Exam 1"), "m2": ("mock-2", "Mock Exam 2"),
           "t": ("topic-sets", "Topic Set")}

def parse(path):
    txt = open(path, encoding="utf-8").read()
    out = []
    for blk in re.split(r"^@@Q ", txt, flags=re.M)[1:]:
        head, rest = blk.split("\n", 1)
        n, typ, dom, task, diff, ans = [x.strip() for x in head.split("|")]
        body, expl = rest.split("@@E", 1)
        lines = [l for l in body.strip().split("\n") if l.strip()]
        opts = [l for l in lines if re.match(r"^[A-F]\. ", l)]
        stem = [l for l in lines if not re.match(r"^[A-F]\. ", l)]
        out.append(dict(n=int(n), typ=typ, dom=dom, task=task, diff=diff,
                        ans=[a.strip() for a in ans.split(",")],
                        stem="\n".join(stem), opts=opts, expl=expl.strip()))
    return out

def main():
    stats = {}
    for key, (folder, title) in SETNAME.items():
        files = sorted(glob.glob(os.path.join(SRC, key + "-p*.txt")))
        if not files:
            continue
        os.makedirs(os.path.join(ROOT, folder), exist_ok=True)
        allq = []
        for f in files:
            part = int(re.search(r"-p(\d+)\.txt", f).group(1))
            qs = parse(f)
            allq += qs
            lo, hi = qs[0]["n"], qs[-1]["n"]
            qmd = [f"# {title} — Part {part} (Questions {lo}–{hi})",
                   "", "Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.", ""]
            amd = [f"# {title} — Part {part} Answers & Explanations (Q{lo}–{hi})", ""]
            for q in qs:
                sel = "Select ONE." if q["typ"] == "MC" else f"Select {'TWO' if len(q['ans'])==2 else 'THREE'}."
                qmd += [f"### Q{q['n']}", "", q["stem"], "", *[o + "  " for o in q["opts"]], ""]
                if q["typ"] == "MR" and "(Select" not in q["stem"]:
                    qmd += [f"*({sel})*", ""]
                amd += [f"### Q{q['n']} — {', '.join(q['ans'])}", "",
                        f"- Domain: {q['dom']} ({DOM[q['dom']]}) · Task/skill: {q['task']} · Difficulty: {DIFF[q['diff']]} · Type: {q['typ']}",
                        q["expl"], ""]
            open(os.path.join(ROOT, folder, f"part-{part}-questions.md"), "w", encoding="utf-8").write("\n".join(qmd))
            open(os.path.join(ROOT, folder, f"part-{part}-answers.md"), "w", encoding="utf-8").write("\n".join(amd))
        stats[key] = allq
    # QA report
    for key, qs in stats.items():
        nums = [q["n"] for q in qs]
        c = collections.Counter(q["dom"] for q in qs)
        pos = collections.Counter(a for q in qs if q["typ"] == "MC" for a in q["ans"])
        mr = sum(1 for q in qs if q["typ"] == "MR")
        print(f"[{key}] questions={len(qs)} sequential={nums==list(range(1,len(qs)+1))} domains={dict(sorted(c.items()))} MC-answer-positions={dict(sorted(pos.items()))} MR={mr}")
        for q in qs:
            letters = [o[0] for o in q["opts"]]
            if q["typ"] == "MC" and (len(q["ans"]) != 1 or len(letters) != 4):
                print("  WARN MC shape Q", q["n"])
            if q["typ"] == "MR" and (len(q["ans"]) < 2 or len(letters) < 5):
                print("  WARN MR shape Q", q["n"])
            if any(a not in letters for a in q["ans"]):
                print("  WARN answer not in options Q", q["n"])
            # each wrong option should be discussed
            for L in letters:
                if L not in q["ans"] and not re.search(rf"^- {L}\b|^- Correct .*\b{L}\b", q["expl"], flags=re.M):
                    print(f"  WARN no explanation for option {L} in Q{q['n']}")

if __name__ == "__main__":
    main()
