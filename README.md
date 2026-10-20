# AWS Certified Data Engineer – Associate (DEA-C01) — refreshed prep kit
**Last verified: 2026-10-20** · Exam target: **Sun 1 Nov 2026 (IST)** · Based on **exam guide v1.1 (published 2025-12-12)** · Branch `refresh-2026-10` (nothing pushed).

## Exam facts snapshot (official, verified 2026-10-20)
DEA-C01 is current (no successor found) · 65 Q (50 scored + 15 unscored) · MC (1 of 4) + multiple-response (2+ of 5+) · 130 min · pass **720/1000** (scaled, compensatory) · USD 150 · EN/JA/KO/ZH · Pearson VUE centre or online · valid 3 y · retake after 14 days · ESL +30 min available.
Weights: **D1 34 % · D2 26 % · D3 22 % · D4 18 %**. Full detail: `guide/00-exam-overview.md`, `docs/exam-intel.md`.
**New in v1.1:** LLMs in pipelines, Iceberg/S3 Tables, vector indexes (HNSW/IVF), Bedrock Knowledge Bases, SageMaker Catalog & Unified Studio (domains/projects), governance & sharing patterns; AWS SCT dropped from scope.

## How to use this in 12 days
1. **Today:** book the exam / ESL +30 / check ID name (see `study-plan/12-day-plan.md` "Do today").
2. Follow `study-plan/12-day-plan.md` day by day (≈3.5 h weekdays, 6 h weekends): learn from `guide/` + `cheatsheets/`, practise from `practice/`.
3. Spaced review: flashcards (`practice/flashcards.csv`, Anki-importable) + error log (`practice/error-log-template.md`).
4. Mock 1 on Day 8 (Tue 27 Oct), Mock 2 on Day 11 (Fri 30 Oct): `practice/mock-1`, `practice/mock-2` (+ Skill Builder Official Pretest). Score with `practice/scoring-sheet.md`.
5. Day 12: light review only. Exam day: `docs/exam-day-playbook.md`.

## Study order
`guide/00-exam-overview` → D1 (1.1 → 1.4) → D2 (2.1 → 2.4) → D3 (3.1 → 3.4) → D4 (4.1 → 4.5) → `guide/X-cross-cutting` → cheatsheets `00`, `12`, `05` → practice sets.
If behind: use the fallback list in the 12-day plan (cheatsheets first, never skip Kinesis/Firehose/Glue/S3/Redshift/DynamoDB/Lake Formation/IAM-KMS, two mocks).

## Directory map
| Path | Content |
|---|---|
| `guide/` | self-contained study guide by domain/task statement (D1–D4, cross-cutting, exam overview) |
| `cheatsheets/` | 13 one-pagers: per-domain, master decision tree, **limits sheet (cited)**, formats, Redshift, streaming, Glue, Lake Formation/security, acronyms, confused pairs |
| `practice/` | 200 original questions: 2 × 65 mocks + 70 topic-set (answers in separate files), scoring sheet, error-log template, 153 flashcards, build scripts |
| `study-plan/12-day-plan.md` | day-by-day plan, mocks, fallback, exam-day logistics |
| `docs/` | audit, exam-intel, gap-analysis, sources, changelog, open-questions, progress, exam-day playbook, hands-on labs |
| `legacy/` | original April-2026 kit and mock-exam app (moved with `git mv`, history kept; superseded) |
| `DEA-Complete-Guide.md` | generated single file: `bash build_complete_guide.sh` (PDF only if pandoc is installed) |

## Tag legend (used everywhere)
**✓** verified against an AWS page on 2026-10-20 · **~** established knowledge, not re-fetched · **(S)** secondary source only · **[UNVERIFIED]** tracked in `docs/open-questions.md`.

## Honest status
Verified: exam facts, domain/task statements, in-scope services, main quotas (Kinesis, Firehose, Lambda, SQS, Step Functions, S3, DynamoDB, Athena, MSK, MWAA, Glue properties, KMS rotation, CloudTrail Lake, etc.). Not yet independently audited: all practice questions/explanations and most "~" claims (Phase 5). See `docs/PROGRESS.md` and `docs/open-questions.md`.
