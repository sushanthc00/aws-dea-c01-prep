#!/usr/bin/env python3
"""Random ~15% sample (cap 70) of numeric/factual claim lines from guide/ and cheatsheets/ (excluding the limits sheet,
which is checked 100%). Seeded for reproducibility. Run from repo root."""
import glob, re, random
random.seed(1020)
BS = chr(92)
files = [f.replace(BS, "/") for f in glob.glob("guide/**/*.md", recursive=True) + glob.glob("cheatsheets/*.md")]
files = [f for f in files if not f.endswith("05-limits-and-numbers.md") and not f.endswith("README.md")]
cands = []
for f in sorted(files):
    for i, l in enumerate(open(f, encoding="utf-8"), 1):
        t = l.strip()
        if len(t) < 40 or t.startswith(("#", "```", "|---")):
            continue
        if re.search(r"\d", t) and ("✓" in t or "~" in t or re.search(r"\b(MB|GB|KB|TB|min|sec|days?|hours?|shards?|DPU|TPS|per)\b|%", t)):
            cands.append((f, i, t[:400]))
n = min(70, max(40, int(len(cands) * 0.15)))
samp = sorted(random.sample(cands, n))
out = [f"# Fact-check sample (seed 1020): {len(samp)} of {len(cands)} numeric/factual claim lines (~{round(100*len(samp)/len(cands))}%)", ""]
for f, i, t in samp:
    out.append(f"- `{f}:{i}` {t}")
open("docs/notes/factcheck-sample.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(cands), len(samp))
