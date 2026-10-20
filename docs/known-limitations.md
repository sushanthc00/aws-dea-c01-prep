# Known limitations (2026-10-20)
Read this before trusting any specific number or question.

## 1. Verification status
- **Independent audit** (one Sonnet subagent, 37 tool calls; report `docs/notes/factcheck-report.md`): audited every number in `cheatsheets/05-limits-and-numbers.md` (~125 claims) plus a seeded random sample of 58 claim lines (~15 %) from guide/cheatsheets (`docs/notes/factcheck-sample.md`). Result: ~145 confirmed, **1 real error (Redshift min-TLS date, fixed → enforcement from 2026-10-31, re-checked by me on the official page)**, 3 outdated/imprecise (Serverless reservation % (45 % No Upfront; up to 50 % All Upfront), P203 date, DynamoDB TTL timing — all fixed), ~30 not verifiable from the pages it fetched (below).
- The audit sampled **claims, not the 200 practice questions** — questions and explanations were not independently checked beyond my own scripted QA and self-review.
- Everything tagged **~** in guide/cheatsheets is established AWS behaviour I did **not** re-fetch today; **(S)** = secondary source only; **[UNVERIFIED]** items are listed in `docs/open-questions.md`.

## 2. Unverified or conflicting items (high-level)
| Item | Status |
|---|---|
| Athena DML default timeout (30 min) | quotas page says adjustable up to 240 min; default not stated there |
| Kinesis EFO ~2 MB/s per consumer per shard | well-known; not on the quotas page |
| Step Functions Express delivery semantics (at-least-once async / at-most-once sync) | not on quotas page |
| Glacier retrieval times, S3 PUT 5 GB / object 5 TB, DynamoDB 400 KB item / 3,000 RCU / 1,000 WCU partition / LSI 10 GB | well-known, not fetched |
| EMR 7.0–7.10 extended support end (AWS announcement: 2027-08-31; per-release lifecycle table shows 2027-08-15 for 7.10) | conflicting official statements |
| SageMaker Unified Studio / Catalog model (domains, domain units, projects, subscription → grants) | only a short official intro page was retrievable; rest from secondary sources (S) |
| CloudTrail Lake | official note: not open to new customers from 2026-05-31; exam guide v1.1 still lists skill 4.4.3 |
| CodeCommit | removed from exam scope list ✓; separately AWS says the service returned to GA (Nov 2025) — irrelevant to scope |
| Athena workgroup data-usage controls; DataBrew ruleset details; Quick/SPICE limits | page content not retrieved |
| DMS Schema Conversion per-pair support beyond the pairs on the doc page | the doc page's table was used; pairs not individually re-checked |
| Glue 6.0 (Spark 4.1.1, Python 3.13) | confirmed from Glue job-properties page; exam relevance minimal |
| MSK provisioned, OpenSearch, MWAA scaling limits, KMS request rates, Redshift node limits | not researched (listed as not verified in the limits sheet) |
| Exam retake wait (14 days), reschedule rules | from AWS policy pages / search summary; page text of the retake policy itself not opened |
| Sunday test-centre availability and accepted IDs in India; Pearson prohibited-items list | not verified |
| Question style trends | only the exam guide's response-type description is official; "scenario/qualifier style" is anecdotal. Official Skill Builder questions were not accessible |

## 3. Practice questions
- Original, first-draft, 200 Qs; **not** copied from any exam. Answer positions balanced (MC A/B/C/D ≈ 25 % each) and domain proportions match 34/26/22/18.
- **Length cue:** an automated check found the correct MC option was the longest in 85 % of items in the first draft. I rewrote distractors/trimmed answers; remaining: correct option is longest in **41 % (Mock 1) / 62 % (Mock 2) / 76 % (topic sets)** of MC items, median length ratio vs distractors **1.08 / 1.16 / 1.19** (mild). Don't use option length as a clue; real exam options are usually more uniform.
- Several distractors are still weaker/more obviously wrong than real exam distractors; real stems are usually longer. Treat scores as a rough proxy; use Skill Builder's **Official Pretest** as the harder benchmark.
- Seven questions per mock are "select TWO of 5" (the exam guide describes multiple-response as 2+ of 5+); the real exam may include "select THREE" items — not drilled.
- Difficulty tags are my estimates. Some questions assume an unstated best practice (e.g., "least ops" preferring managed services); where the official docs differ, the docs win.
- Fixed in QA: 3 questions' explanations lumped options (split). Open: 8 questions where the correct option is a short service name that is marginally longer than other service names (harmless).

## 4. Snippets
- JSON policies/state machines and Python blocks in the guide were syntax-checked by script (`tools/verify_repo.py`: 4 JSON, 3 Python blocks). **cfn-lint and a SQL parser were not available**, so CloudFormation/SAM YAML, SQL (Athena/Redshift), shell/CLI and PySpark/Glue snippets are **untested** and marked as such in the guide. Runtime identifiers (e.g., `python3.13` in the SAM sample) may be deprecated; check the Lambda runtimes page.

## 5. Scope and structure
- The old April-2026 kit is preserved in `legacy/` (not corrected, except where the new docs list corrections). Old mock exams there use outdated names; use `practice/` instead.
- 15 of the exam's 65 questions are unscored and unidentifiable; the exam guide says content can change with ≥ 1 month notice — recheck the guide's Revisions page before exam day.
- No PDF was produced (pandoc not installed); `DEA-Complete-Guide.md` is the single-file version (`bash build_complete_guide.sh`).
- Nothing has been pushed to GitHub; all work is on local branch `refresh-2026-10`.
