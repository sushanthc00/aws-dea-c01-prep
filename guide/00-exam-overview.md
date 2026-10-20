# 00 — Exam overview (DEA-C01, exam guide v1.1) — last verified 2026-10-20
Sources: exam guide + cert page + policy pages (see `docs/sources.md`). Everything below marked ✓ was read on the official pages today.

## Facts ✓
- **DEA-C01 is the current exam**; no successor or retirement notice found. Guide v1.1 published 2025-12-12 (effective ~1 month later); new guide versions are published ≥ 1 month before they affect the exam.
- 65 questions = 50 scored + 15 unscored (unidentified); multiple choice (1 of 4) and multiple response (2+ of 5+); no penalty for guessing; unanswered = wrong.
- 130 minutes · scaled 100–1000 · **pass 720** · pass/fail · compensatory (no per-domain minimum) · USD 150 · languages EN/JA/KO/ZH-Simplified (can toggle to English) · Pearson VUE test centre or online proctored · valid 3 years · retake after 14 days (unlimited attempts, full fee) · ESL +30 min accommodation available.
- Target candidate: 2–3 years data engineering, 1–2 years AWS. Out of scope: ML training/inference, language-specific syntax, business conclusions.

## Domains and weights ✓
| Domain | Weight | Tasks |
|---|---|---|
| D1 Data Ingestion & Transformation | 34 % | 1.1 ingest · 1.2 transform · 1.3 orchestrate · 1.4 programming |
| D2 Data Store Management | 26 % | 2.1 choose store · 2.2 catalog · 2.3 lifecycle · 2.4 modeling |
| D3 Data Operations & Support | 22 % | 3.1 automate · 3.2 analyze · 3.3 monitor · 3.4 data quality |
| D4 Data Security & Governance | 18 % | 4.1 authN · 4.2 authZ · 4.3 encryption/masking · 4.4 audit logs · 4.5 privacy/governance |
≈ 17 + 13 + 11 + 9 scored questions out of 50.

## What changed in v1.1 (study these first if you used older material) ✓
New skills: LLMs in pipelines (1.2.10) · open table formats/Iceberg (2.1.7) · vector index types HNSW/IVF (2.1.8) · business catalogs/SageMaker Catalog (2.2.6) · vectorization/Bedrock Knowledge Bases (2.4.6) · SageMaker Unified Studio domains/units/projects (4.1.7) · data access through Catalog projects (4.5.6) · governance framework + sharing patterns (4.5.7). In-scope added: Aurora, Amazon Q, Bedrock, Kendra, Data Exchange, **S3 Tables**; removed: Cloud9, CodeCommit, **AWS SCT** (skill 2.4.3 still names SCT + DMS Schema Conversion). "Amazon Quick" and "Kinesis Data Firehose" appear under those names in the guide (Quick = QuickSight family; Firehose = Amazon Data Firehose).

## How to use this guide
`guide/D1…D4` = full explanations per task statement (concept, when/when-not, limits with citations, traps, scenarios). `cheatsheets/` = fast recall. `practice/` = 200 questions + flashcards. `study-plan/12-day-plan.md` = day-by-day. Tags: ✓ verified against AWS docs on 2026-10-20 · ~ established but not re-fetched · (S) secondary source · [UNVERIFIED] listed in `docs/open-questions.md`.
