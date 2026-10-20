# Practice material (original questions, exam guide v1.1 aligned)
Status 2026-10-20: **Mock 1 and Mock 2 done (2 × 65 questions)**. Topic sets (70 questions), error-log template and flashcards: pending (Phase 4.3 rest, 4.4).

| Path | Content |
|---|---|
| `mock-1/part-{1,2,3}-questions.md` | Q1–22, Q23–44, Q45–65 |
| `mock-1/part-{1,2,3}-answers.md` | answer, domain, skill, difficulty, why correct, why each distractor is wrong |
| `mock-2/…` | same structure, different scenarios |
| `scoring-sheet.md` | blank answer grid + domain tracker per mock |
| `src/` + `build_practice.py` | source of truth; regenerate with `python3 practice/build_practice.py` (also prints QA stats) |

How to sit a mock: all 3 parts back to back, 130 min, no notes, flag-and-return, answers closed until done. Score each domain in `scoring-sheet.md`.

Composition per mock: 65 Qs = D1 22 · D2 17 · D3 14 · D4 12 (official weights 34/26/22/18). 58 multiple-choice (1 of 4) + 7 multiple-response (select TWO of 5) — the only two types the current exam guide lists. Answer positions balanced (see QA line printed by the build script).
Difficulty tags are my estimate (E/M/H). Questions are original scenario items written from the exam guide skills and cheatsheets — nothing taken from real exams.

**Caveats (honest status):** first-draft; not yet independently fact-checked (Phase 5). If a question conflicts with the official AWS docs or Skill Builder, trust the docs and tell me so it goes in `docs/open-questions.md`. Mock questions are single-sentence-qualifier style and somewhat easier than the real exam's longer stems; use the Skill Builder Official Pretest as the harder benchmark.
