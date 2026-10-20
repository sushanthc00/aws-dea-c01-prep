# Gap analysis (Phase 2) — 2026-10-20
Baseline: old kit (13 md files + Flask mock app, written ~Apr 2026 against exam guide v1.0) vs exam guide v1.1 (2025-12-12). Evidence: greps of old files + `docs/exam-intel.md`.

## A. Outdated / wrong statements
| # | Old statement (file) | Correct / current | Source |
|---|---|---|---|
| 1 | Exam date ~8 May 2026, 14-day plan (README, 03) | Exam ~1 Nov 2026; 12-day plan in `study-plan/` | user brief |
| 2 | "Last verified April 2026" (01) | stale; guide v1.1 published 2025-12-12 | exam-guide revisions |
| 3 | "Kinesis Data Analytics (Flink)" (03:257, 05:62/217/229/239, 10:17/42) | Amazon Managed Service for Apache Flink | in-scope list |
| 4 | "Governed tables" as LF feature (05:194) | not in guide; Iceberg/S3 Tables replace it *[deprecation date UNVERIFIED]* | exam-intel |
| 5 | "QuickSight" (01:64, 10:34, 11:86) | guide says "Amazon Quick" (rename chain from secondary sources) | in-scope list |
| 6 | "Kinesis Data Firehose" | renamed Amazon Data Firehose (guide still prints old name) | WN 2024-02 |
| 7 | Kinesis record 1 MB implied (10:82, 11:22) | record payload now up to 10 MiB; shard still 1 MB/s in, 2 MB/s out | KDS quotas ✓ |
| 8 | Kinesis retention 24 h–365 d; Step Functions 1 y / 5 min; Lambda 15 min / 10 GB (10:79-86) | correct ✓ — keep | quotas pages ✓ |
| 9 | Exam facts $150, 65Q (50+15), 130 min, 720/1000, 3 y, 4 languages | correct ✓; add compensatory scoring, 14-day retake, ESL +30, ID/online rules | exam guide ✓ |
| 10 | S3 Select listed must-know (01) | believed closed to new customers (2024) *[UNVERIFIED]* → de-prioritise | open-questions |
| 11 | Udemy course advice (03) | third-party/personal; keep only as optional, labelled | — |
| 12 | Sample stem "500 GB JSON from IoT…" (01:78) | rewrite as original (rule 8) | — |
| 13 | Mocks 06/07 (~130 grep hits each; app JSON only 10 Qs each) | audit needed: old names, no v1.1 topics, no objective mapping | audit |

## B. Missing in-scope services/skills (v1.1)
- **New skills, zero coverage**: 1.2.10 LLMs in pipelines · 2.1.7 open table formats · 2.1.8 vector index types HNSW/IVF · 2.2.6 business catalog (SageMaker Catalog) · 2.4.6 vectorization/Bedrock KB · 4.1.7 SageMaker Unified Studio domains/units/projects · 4.5.6 Catalog projects access · 4.5.7 governance framework/sharing patterns.
- **Services**: S3 Tables, Aurora/pgvector, Bedrock, Kendra, Amazon Q, Data Exchange, Managed Grafana, Systems Manager, API Gateway, SAM/CDK/CFN/CodePipeline, ECS/EKS/ECR/Batch, DocumentDB/Keyspaces/Neptune/MemoryDB, AppFlow, DataSync, Transfer Family, Snow, DMS depth, CloudTrail Lake, Config, Macie, Secrets Manager vs Parameter Store, PrivateLink/endpoints, AWS Backup, EFS (Lambda mount).
- **Skill-level gaps**: shard math, stateful/stateless, replayability, IP allowlists, throttling, fan-in/out, Redshift locks/federated/MVs, Athena Spark notebooks, rolling-average/pivot SQL, data skew, sampling, LF-tags/hybrid/cross-account, KMS cross-account, data sovereignty, Redshift data sharing.

## C. Weighting vs official
| Domain | Official | Old coverage | Verdict |
|---|---|---|---|
| D1 34 % | Glue/Kinesis/MSK/EMR/Lambda/SFN | ~8 of 15 primer sections | OK, thin on orchestration/programming |
| D2 26 % | stores, catalog, lifecycle, modeling | S3/Redshift/LF only | under |
| D3 22 % | ops, analysis, monitoring, DQ | CloudWatch/CloudTrail only | under |
| D4 18 % | authN/Z, encryption, audit, governance | IAM + KMS | under |

## D. Missing decision guidance
Comparison tables (streaming, transform engines, query engines, DB selection, orchestrators, migration/transfer, LF vs IAM vs bucket) → now in `cheatsheets/00` and `12`; to be expanded in guide with scenarios, traps, snippets. Also missing: troubleshooting tables (partly in cheatsheets 03/07/09), cost, HA/DR, Regions, Well-Architected, quotas.

## E. Structure issues
Flat service-ordered files, no task-statement spine; no metadata docs (now added); duplication across 01/09/10/11; mocks mixed with study text; small JSON question sets; personalised sections (02, 03).

## F. Proposed structure (non-destructive)
```
README.md · study-plan/12-day-plan.md ✔ · cheatsheets/ ✔
guide/00-exam-overview.md
guide/D1-ingestion-transformation/{1.1-ingestion,1.2-transform,1.3-orchestration,1.4-programming}.md
guide/D2-data-store-management/{2.1-stores,2.2-catalog,2.3-lifecycle,2.4-modeling}.md
guide/D3-operations-support/{3.1-automation,3.2-analysis,3.3-monitoring,3.4-data-quality}.md
guide/D4-security-governance/{4.1-authn,4.2-authz-lakeformation,4.3-encryption-masking,4.4-audit-logs,4.5-privacy-governance}.md
guide/X-cross-cutting.md
practice/ (mocks, topic sets, answers, tracker, error-log, flashcards.csv)
docs/ (audit, exam-intel, gap-analysis, sources, changelog, open-questions, coverage-matrix, known-limitations, exam-day-playbook, hands-on-labs)
legacy/ (old 01–12 + mock-exam-app moved via git mv; banner "superseded")
DEA-Complete-Guide.md (script-built)
```
Discards a large part of the user's work? **No** — old files move to `legacy/`; valid content reused; fixes logged in CHANGELOG.

## G. Phase 3 plan
D1 → D2 → D3 → D4 → X, one file per task statement, ≤600 lines; reuse cheatsheets as base; fetch only missing pages (MSK, MWAA, OpenSearch, EMR, DMS, Redshift data sharing, KMS). Budget ≤12 fetches, ≤10 searches.
**Order decision (user, 2026-10-20): practice first** — mocks (2×65 Qs) before Phase 3.
