# Audit — 2026-10-20 (Phase 0)

Method: structure/heading skim, size counts, targeted grep. No full reads. Findings marked *suspected* are unverified until Phase 1/2.

## Resume check
- Branches: only `main` (+ origin/main). No `refresh-2026-10` existed; created from `main` @ 92739ed.
- No `docs/PROGRESS.md`, no prior partial work. Starting fresh.

## What exists (13 md files, ~3,490 lines, ~205 KB, plus a Flask app)
| File | Lines | Content |
|---|---|---|
| README.md | 50 | Kit overview; exam date ~8 May 2026 (stale) |
| 01-exam-breakdown.md | 85 | Format/domains; "last verified April 2026" |
| 02-skills-gap-analysis.md | 52 | Personalised to an earlier profile |
| 03-study-plan.md | 272 | 14-day / 7-day / minimum / high-confidence plans; Udemy-centric |
| 04-resource-pack.md | 101 | Official + third-party links (link rot likely) |
| 05-service-primer.md | 588 | 15+ services, one section each (thin on D2/D4 depth) |
| 06/07-mock-exam-1/2.md | 964 / 815 | 130 questions each *(grep count; includes answer/explanation lines, true Q count to verify)* |
| 08-weakness-diagnosis.md | 67 | Framework |
| 09-exam-strategy.md | 109 | Tactics |
| 10-cheat-sheet.md | 86 | 1-page; selection, encryption, dist styles, numbers |
| 11-must-know-checklist.md | 166 | Per-domain checklist |
| 12-mock-exam-app-spec.md | 137 | Spec for local mock app |
| mock-exam-app/ | — | Flask app, `questions/exam1.json`, `exam2.json` (grep shows ~10 `"id"` each → sample only *suspected*) |

Format: GitHub-flavored md, numbered flat files, no index/TOC beyond README, no docs/ dir, no sources file, no changelog.

## What's missing
- Date-stamped sources per claim; inline citations for limits.
- Per-task-statement coverage (guide is service-centric, not task-statement-centric).
- Service coverage gaps (grep for S3 Tables, Iceberg-as-primary, zero-ETL, SageMaker Unified Studio/Lakehouse, DataZone, Express One Zone, Vectors: no hits except "Governed tables"): Lake Formation depth (LF-tags, hybrid access, cross-account), Macie, Glue Data Quality/DQDL, DMS/SCT/CDC, DataSync/Transfer Family/AppFlow/Snowball, Keyspaces/Timestream/DocumentDB/Neptune/MemoryDB comparison, Redshift deep (WLM, concurrency scaling, Spectrum, data sharing, zero-ETL), MWAA, OpenSearch, QuickSight, EMR Serverless/on-EKS, Managed Service for Apache Flink, PrivateLink/VPC endpoints, Secrets Manager vs Parameter Store, IaC/CI-CD (CDK/CFN/SAM), SQL transform patterns.
- Comparison tables required by brief (streaming ingest, transform engines, analytics engines, DB selection, orchestration, migration/transfer, LF vs IAM vs bucket policy).
- Scenario worked examples, hands-on snippets, distractor traps.
- Mock-exam metadata: no objective mapping, difficulty tags, or per-distractor rationale *(to verify)*; no domain tracker.
- Exam-day logistics for India/IST, online-proctoring checklist.
- docs/: sources, changelog, open-questions, coverage matrix, known limitations.

## Likely wrong / outdated (suspected; verify in Phase 1–2)
1. **Date/schedule**: README targets ~8 May 2026; plans are 14-day/April-based. New date ~1 Nov 2026.
2. **Exam version**: guide assumes DEA-C01 is current. Must check for successor/revision (e.g. a C02) before Phase 3.
3. **Service names**: "Kinesis Data Analytics (Flink)" used throughout (03:257, 05:62/217/229/239, 10:17/42) → current name Amazon Managed Service for Apache Flink; Kinesis Data Firehose → Amazon Data Firehose *(suspected, verify)*.
4. **Governed tables** (05:194) presented as a Lake Formation feature → believed deprecated/discontinued; Iceberg/S3 Tables replace it *(verify)*.
5. **Exam facts** (01): cost $150, 65 Q (50+15), 130 min, 720/1000, languages, validity 3y — re-verify against current exam guide; languages list may have grown.
6. **Exam in-scope services appendix** not diffed — likely new entries since April.
7. Glue versions / Python & Lambda runtime EOLs, Redshift/Athena feature statements, quotas in 10-cheat-sheet "Key Numbers" — uncited, unverified.
8. Resource pack (04) and study plan (03): third-party course/price claims (Udemy, "$") unverifiable; links may be dead.
9. Mock questions may reflect old service names and lack objective mapping; judge against official sample-question style only (no brain-dump content).
10. `Last verified: April 2026` stamps everywhere → all stale by 6+ months.

## Structural issues
- Flat, service-ordered files; no domain→task-statement spine; weights (34/26/22/18) not reflected in depth (primer: D1 services dominate, D4 under-covered).
- Duplication across 01/09/10/11; checklist and cheat sheet not tied to primer sections.
- Personalised (profile-specific) text in 01/02 should be generalised or kept clearly separate.
- App spec (12) and app are tangential to exam content; keep untouched, update question JSON later only if practice set is exported.

## Proposed handling (decided, no blockers)
Keep all original files (renamed/moved only in Phase 3 via `git mv`, logged in CHANGELOG). Add `docs/`, then rebuild into domain-structured `guide/`. No destructive removal.
