# 12-Day Plan: Tue 20 Oct → exam Sun 1 Nov 2026 (IST)
Assumptions: weekdays ~3.5 h (2 h learn · 1 h questions · 0.5 h spaced review), Sat/Sun ~6 h. Exam v1.1 weights: D1 34 · D2 26 · D3 22 · D4 18 (see `docs/exam-intel.md`). Study sources: `cheatsheets/` (verified), old `05-service-primer.md` (use for concepts only — stale names: Kinesis Data Analytics = Managed Service for Apache Flink; Governed tables removed), AWS docs only for gaps. The rebuilt `guide/` (Phase 3) and `practice/` (Phase 4.3) will replace the old files as they land; until then use Skill Builder's free **Official Practice Question Set** and **Official Pretest** [OFFICIAL, link in `docs/sources.md`] plus old mocks 06/07 (check names against cheatsheets).

Tag legend for cheatsheets: ✓ verified 2026-10-20 against AWS docs (cited); ~ well-established, not re-fetched.

## Do today (Day 1, before studying) — logistics, 20 min
1. **Book the exam** (Pearson VUE, via your AWS Certification account) for Sun 1 Nov. Choose online (OnVUE) or centre; Sunday centre slots in India [UNVERIFIED] — online is 24x7 for English proctors [OFFICIAL]. Free reschedule/cancel until 24 h before; each booking reschedulable twice [OFFICIAL].
2. **ESL +30 min** if English isn't your first language: request once in your AWS Certification account *before* booking [OFFICIAL]. If already booked, check whether it applies [UNVERIFIED].
3. Check your AWS Certification account name == ID name exactly. Mismatch = turned away, fee forfeited [OFFICIAL].
4. Create `practice/error-log.md` (template arrives in Phase 4.4; for now a table: date · Q topic · why wrong · rule to remember).

## Cadence rules
- **Spaced repetition**: every day starts with 20–30 min recall of Day −1 (cheatsheet closed, write the table from memory), and 10 min of Day −3 and Day −7 flashcards/cheat lines.
- **Questions**: always timed ≈ 2 min/question. Every wrong *and* guessed answer → error log (one-line rule). Re-read the error log on Days 8, 10, 12.
- **Weights**: if time conflicts, protect D1 and D2 (60 % of score), but D3/D4 contain cheap points.

## Daily schedule
| Day | Date | Hrs | Theme | Read/learn (cheatsheets) | Practice & checkpoints |
|---|---|---|---|---|---|
| 1 | Tue 20 | 3.5 | **D1a Streaming ingestion** | 08-streaming (KDS, Firehose, MSK, Flink, DDB Streams), 05-limits (Kinesis/Firehose/SQS), 01-d1 (1.1.1, 1.1.7, 1.1.9–1.1.12) | Shard-math drills (5 problems); 15 Qs streaming |
| 2 | Wed 21 | 3.5 | **D1b Batch + Glue + transform choice** | 09-glue, 06-formats, 00-which-service (transform engines), DMS/AppFlow/DataSync/Transfer rows, 01-d1 (1.1.2–1.1.6, 1.2.x) | Review D1; 20 Qs batch/Glue/formats |
| 3 | Thu 22 | 3.5 | **D1c Orchestration + programming** | Step Functions Std vs Express, MWAA, EventBridge/Scheduler, Glue workflows; Lambda concurrency/EFS/SAM/CFN/CDK/CI-CD; LLM-in-pipeline concept (1.2.10: Bedrock/Lambda step in pipeline, embeddings) | Review D1a/D1b; 25 Qs orchestration + Lambda |
| 4 | Fri 23 | 3.5 | **D2a Stores: S3, Redshift, DynamoDB, DB selection** | 02-d2, 07-redshift, S3 classes/lifecycle (05-limits), DB comparison table | Review D1c; 20 Qs stores |
| 5 | Sat 24 | 6 | **D2b Catalog, table formats, modeling, migration + D1 consolidation** | Glue Data Catalog, crawlers, partitions (MSCK/projection), Iceberg/S3 Tables/Hudi/Delta, schema evolution, DMS CDC, **vectors**: pgvector HNSW/IVF, MemoryDB, Bedrock KB (2.1.3, 2.1.8, 2.4.6), SageMaker Catalog/lineage (2.2.6, 2.4.4) | 40-Q mixed D1+D2 timed (80 min) + 60 min review; flashcards Day 1–4 |
| 6 | Sun 25 | 6 | **D3 Operations + D4a IAM/KMS** | 03-d3 (troubleshooting list, Athena, Quick, DataBrew, Glue DQ/DQDL, CloudWatch/CloudTrail/Logs Insights, skew/sampling); 04/10 (IAM, KMS, Secrets vs Parameter Store, VPC endpoints) | 35 Qs D3+IAM/KMS; build "troubleshooting symptom→fix" list from memory |
| 7 | Mon 26 | 3.5 | **D4b Lake Formation, Macie, masking, audit, governance** | 10-lakeformation-security, CloudTrail Lake, Config, Redshift data sharing, Macie, residency/sovereignty, SageMaker Unified Studio domains/projects & Catalog (4.1.7, 4.5.6–4.5.7) | 25 Qs D4; review Day 5–6 flashcards |
| 8 | Tue 27 | 3.5 | **MOCK 1** (65 Q / 130 min, strict) + review | — | Mock 1 (Skill Builder Official Pretest if available, else old mock 06 re-checked), then 90 min review: domain tracker, error log |
| 9 | Wed 28 | 3.5 | **Remediation 1** | Re-study weakest 2 domains/tasks from Mock 1 using cheatsheets; 12-confused-pairs; 00-which-service decision tree from memory | 30 Qs targeted at weak areas |
| 10 | Thu 29 | 3.5 | **Cross-cutting + second pass** | Cost optimization, HA/DR, Regions, Well-Architected, provisioned-vs-serverless (3.2.5); re-read 05-limits; flashcards all | 35 Qs mixed; error log full re-read |
| 11 | Fri 30 | 3.5 | **MOCK 2** (65 Q / 130 min) + review | — | Mock 2 (new `practice/` mock when ready, else old mock 07); target ≥ 80 % before sitting |
| 12 | Sat 31 | 2 (light) | **Final review** | Cheat sheets skim only: 12-confused-pairs, 05-limits, 00-decision tree, error-log; **no new topics** | Logistics check, system test, sleep by 22:00 IST |
| — | **Sun 1 Nov** | — | **EXAM** | 30 min skim of error log max | See exam-day below |

Pacing check: Day 5 and Day 8 gates — Day 5 mixed score ≥ 65 % else drop Day 10's cross-cutting block and add D1/D2 remediation; Mock 1 ≥ 65 % else add a second remediation evening on Day 10.

## Mock protocol
65 Q · 130 min · no notes · flag-and-return · 3 passes (answer sure ones; return to flagged; final 10 min review). Scoring: raw % ≈ proxy only (real exam is scaled 100–1000, pass 720, 15 of 65 unscored [OFFICIAL]). Treat ≥ 75–80 % on realistic mocks as "ready" [advice, not official].
Track per domain: D1/D2/D3/D4 % — anything < 70 % goes to the next remediation block.

## If you fall behind (priority fallback; cut from the bottom)
1. **Never cut**: Kinesis/Firehose/MSK selection + shard math; Glue (crawler, catalog, bookmarks, DQ, troubleshooting); S3 formats/lifecycle/partitioning; Redshift (dist/sort, COPY/UNLOAD, Spectrum, data sharing); DynamoDB access patterns; Lake Formation + IAM + KMS cross-account; Step Functions vs MWAA vs EventBridge; two mocks (or one + review).
2. Cut next: SAM/CDK/CI-CD detail, containers (EKS/ECS) beyond "when", Lambda mounting EFS, data structures/algorithms (1.4.11), Managed Grafana, Batch, Data Exchange, Kendra/Q.
3. Cut last-before-never: v1.1 additions (vectors/HNSW/IVF, Bedrock KB, LLM integration, SageMaker Catalog/Unified Studio) — learn the **one-paragraph definition + when-to-use** only (~45 min total); these are 8 of ~120 skills.
4. If Mock 1 is skipped, run Mock 2 only on Day 10 and use Day 11 for remediation.

## Exam-day logistics (IST)
- Night before: ID + secondary ID ready; name match; charge laptop; online: quiet private room, clear desk, no second monitor, system test done (failing it forfeits fee [OFFICIAL]); sleep.
- Check in early: arriving **>15 min late forfeits the fee** [OFFICIAL]. Online: **no breaks, can't leave camera view** [OFFICIAL]; test centre: breaks allowed but the timer runs [OFFICIAL]. Water/toilet before.
- During: 130 min for 65 Q ≈ 2 min each; first pass ≤ 90 min; flag & return; no penalty for guessing — never leave blanks; MR items: pick exactly the number asked.
- Result: pass/fail shown by AWS; scaled score and domain table follow [OFFICIAL]. Fail → retake after 14 days [OFFICIAL via search summary] (earliest Sun 15 Nov).
