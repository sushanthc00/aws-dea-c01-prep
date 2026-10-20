# Exam intel — as of 2026-10-20
Label key: **[OFFICIAL]** AWS exam guide/policy page fetched today; **[OFFICIAL-WN]** AWS What's New/docs seen via search snippet (not opened); **[SECONDARY]** third-party/aggregator, treat as unverified; **[ANECDOTAL]** community reports. Details in `docs/notes/exam-guide.md`; URLs in `docs/sources.md`.

## 1. Which exam version?
- **DEA-C01 is the current exam.** No C02, successor, rename or retirement notice on the cert page or exam guide [OFFICIAL]. A web search for DEA-C02 found nothing [no evidence either way beyond official pages].
- **Book DEA-C01** (only version available). The exam guide was revised to **v1.1 on 2025-12-12** (effective in the exam ~1 month later, i.e. ~Jan 2026) [OFFICIAL]. Your old repo (stamped April 2026) was written against v1.0 content; v1.1 is what you will be tested on. See §4.
- Guide says revisions are published at least one month before they reach the exam [OFFICIAL] — a new guide before 1 Nov would not affect you; re-check the guide's Revisions page the night before for peace of mind.

## 2. Exam facts [OFFICIAL unless noted]
| Item | Value |
|---|---|
| Questions | 65 = 50 scored + 15 unscored (not identified) |
| Types | Multiple choice (1 of 4); multiple response (2+ correct of 5+). Guide mentions only these two types (no ordering/matching listed) |
| Duration | 130 min (≈2 min/question) |
| Scoring | Scaled 100–1000, pass = 720; pass/fail; compensatory (no per-domain minimum); unanswered = incorrect, no guessing penalty |
| Cost | USD 150 (+ possible FX charges; local taxes may apply [UNVERIFIED for India]) |
| Languages | English, Japanese, Korean, Simplified Chinese; localized exams can toggle to English |
| Delivery | Pearson VUE test centre or online proctored (OnVUE); online available for all exams |
| Validity | 3 years |
| Retake | Fail: wait 14 calendar days; unlimited attempts; full fee each time; passed exam can't be retaken for 2 years [OFFICIAL via AWS After-Testing/FAQ pages, seen in search summary; page text not opened] |
| Reschedule/cancel | Up to 24 h before; each appointment reschedulable twice; <24 h or no-show forfeits fee; medical/emergency exceptions via Pearson VUE |
| ESL accommodation | +30 min for non-native English speakers: request once in AWS Certification account (Request Exam Accommodations → ESL +30). Applies to future registrations. Worth doing if not already — **do it before scheduling** |
| ID | Government-issued ID; a secondary ID is always required; name must exactly match AWS Certification account name; online vs in-person ID rules differ |
| Online rules | No breaks, can't leave camera view; proctor communication required; arriving >15 min late or failing the system test forfeits the fee |
| Test centre | Unscheduled breaks allowed but timer runs; can't leave the building |

**India / IST notes**
- English-language proctors are available 24x7 [OFFICIAL]; so any IST slot is feasible online. A test centre on Sunday depends on local availability [UNVERIFIED — check Pearson VUE scheduler].
- Pearson VUE shows slots in your local time zone; confirm the time zone on the confirmation email [general practice, UNVERIFIED].
- Passport recommended as primary ID for online; confirm accepted IDs in the scheduler [OFFICIAL says passport is required as primary if no qualifying local ID; secondary ID always required].
- If you fail on 1 Nov, earliest retake = 15 Nov [derived from 14-day rule].
- Prohibited items/desk rules are on Pearson VUE pages, not AWS (not fetched) → `docs/open-questions.md`.

## 3. Domains and weights [OFFICIAL]
D1 Ingestion & Transformation 34% · D2 Data Store Management 26% · D3 Operations & Support 22% · D4 Security & Governance 18% (unchanged from v1.0). Approx. scored questions of 50: D1 17, D2 13, D3 11, D4 9.
Task statements (v1.1): 1.1–1.4, 2.1–2.4, 3.1–3.4, 4.1–4.5 — 4 + 4 + 4 + 5 = **17 tasks, ~120 skills**; full list in `docs/notes/exam-guide.md`.

## 4. v1.1 delta vs your old guide (the biggest finding)
**New skills (8)**: 1.2.10 LLMs for data processing · 2.1.7 open table formats (Iceberg) · 2.1.8 vector index types (HNSW, IVF) · 2.2.6 business data catalogs (SageMaker Catalog) · 2.4.6 vectorization / Bedrock knowledge bases · 4.1.7 SageMaker Unified Studio domains/domain units/projects · 4.5.6 data access via SageMaker Catalog projects · 4.5.7 governance data framework & data-sharing patterns.
**Reworded emphasis**: 2.1.3 HNSW with Aurora PostgreSQL (pgvector) and MemoryDB for key/value; 2.4.4 lineage via SageMaker ML Lineage Tracking & SageMaker Catalog; 3.1.6 DataBrew & SageMaker Unified Studio; 3.2.3 SQL in **Redshift and Athena** (views); 4.2.5 role/tag/attribute-based authz; 4.2.6 least-privilege custom policies; 4.3.4 encryption "in transit or before transit"; 4.5.4 AWS Config; 4.5.5 data sovereignty.
**In-scope added**: Aurora, Amazon Q, Bedrock, Kendra, Data Exchange, **S3 Tables**. **Removed**: Cloud9, CodeCommit, **AWS SCT** (skill 2.4.3 still mentions SCT + DMS Schema Conversion — keep both, low weight).
**Out-of-scope list removed**: Timestream (deprecated for new customers [UNVERIFIED]; not in-scope either → minimal coverage), Honeycode, WorkDocs, CodeWhisperer.
**Listed-name quirks**: guide lists "Amazon Kinesis Data Firehose" (service renamed Amazon Data Firehose in Feb 2024 [OFFICIAL-WN]; exam text may use either — know both), "Amazon Quick" (QuickSight family rename, see §5), "Amazon MemoryDB for Redis" (guide wording), "S3 Glacier".
**Old-repo status**: old guide lacks vectors/pgvector/Bedrock KB/LLM, SageMaker Catalog/Unified Studio, S3 Tables, Iceberg, Aurora as a distinct topic; uses outdated "Kinesis Data Analytics" and "Governed tables".
**Scope note (explicit)**: ML training/inference, language syntax, business conclusions are out of scope [OFFICIAL] — don't over-invest in SageMaker modeling.

## 5. Service changes since ~April 2026 (and just before) — verification status
| Area | Change | Status |
|---|---|---|
| Glue | **Glue 5.1** (Spark 3.5.6, Python 3.11, Scala 2.12.18; Iceberg 1.10.0, Hudi 1.0.2, Delta 3.3.2; Iceberg v3 support; LF fine-grained access incl. write ops for Spark DataFrames/SQL). GA'd in 33 regions Feb 2026, all commercial+GovCloud Apr 2026, EU Sovereign Cloud Aug 2026. Glue 6.0 referenced (Spark 4.0) in S3 Tables v3 item | [OFFICIAL-WN, search snippets]. Glue 6.0 details [UNVERIFIED] |
| Redshift | Patch cadence P200–P203 (Apr–Aug 2026); concurrency scaling now covers KDS streaming-ingestion MV refresh (P203, Aug 2026); new array functions for SUPER (Mar 2026); autonomics extra compute (Feb 2026); Serverless 3-yr reservations up to 45% (Feb 2026); min TLS 1.2 enforced from 2026-01-31; **scalar Python UDF end-of-support after 2026-06-30** (creation ended 2025-11-01) → Lambda UDFs; datashare consumer-group function removal 2026-02-16; system-table long-term retention in S3 Tables (Aug 2026) | [OFFICIAL-WN snippets] |
| S3 Tables / Iceberg | Iceberg v3 types (Variant Jul 2026; deletion vectors, row lineage, geometry/geography, nanosecond timestamps ~Sep 30 2026) — need Spark 4.0+ (Glue 6.0+/EMR 8.1+); GovCloud Feb 2026. **S3 Vectors GA at re:Invent 2025** (up to ~1B vectors/index [SECONDARY]) | Dates SECONDARY — treat as **optional depth**; core exam fact = S3 Tables is managed Iceberg table storage with auto-compaction |
| Lake Formation | Jun 2026: table permissions extend to direct underlying S3 data access (SELECT=read, SUPER=read/write via scoped credentials; EMR 7.13+); NZ region Feb 2026; cross-account sharing enhancement Feb 2026 [headline only] | [OFFICIAL-WN snippets, non-English text] |
| SageMaker / DataZone | SageMaker Catalog = evolution of DataZone; domains have V1 (DataZone portal) vs V2 (Unified Studio) versions; IAM-based vs IDC-based domains; custom asset types in IAM domains (Jul 2026). Unified Studio is the exam-named workspace | Mostly SECONDARY; verify in Phase 3 from docs |
| EMR | Sep 2026: extended support at no extra cost for 5.36, 6.6–6.15 (best-effort security through 2027-06-30) and 7.0–7.10 (through 2027-08-31); EMR 7.13 supports LF S3 access; EMR 8.1 referenced | [OFFICIAL-WN snippet] |
| Athena | Managed connectors for 12 sources (Apr 2026); Capacity Reservations 1-minute min & 4 DPU min (Feb 2026); IAM-based auth for S3 Tables/Iceberg MVs (Mar 2026) | [SECONDARY: China-region release notes] |
| Lambda | Node.js 20 EOL Apr 30 2026; Python 3.9 deprecated (Dec 2025); block-create/update dates pushed to 2027 [SECONDARY]; Node.js 26 / Python 3.15 indicative Nov 2026 | Runtime numbers are NOT exam-critical; only the concept of runtime deprecation |
| Quick | QuickSight family → Amazon Quick Suite (Oct 2025) → **Amazon Quick** (2026); QuickSight continues as a component; Q Business moved to maintenance for new customers (~Jul 31 2026); Kendra successors named | SECONDARY; exam guide itself says "Amazon Quick" → use "Amazon Quick (formerly QuickSight)" |
| Firehose | Renamed Amazon Data Firehose (Feb 2024); APIs/IAM/metrics unchanged | [OFFICIAL-WN] |
| Zero-ETL | Sources per Glue docs: DynamoDB, Oracle Database@AWS, SaaS (Salesforce, SAP, Zendesk…); Redshift zero-ETL sources: Aurora MySQL/PG, RDS MySQL/PG/Oracle [SECONDARY], DynamoDB; DynamoDB zero-ETL to SageMaker Lakehouse doesn't consume table capacity | Verify exact list in Phase 3 |
| MSK, MWAA, OpenSearch, Step Functions, EventBridge Pipes, DMS, AppFlow, Keyspaces, Kinesis quotas | **Not researched/verified yet** | → verify via docs in Phase 3 (quotas pages) — do not rely on old repo |
| Timestream | Not in either list now; deprecated for new customers [UNVERIFIED] | Minimal |

## 6. Question-style trends
- **Official**: two response types (MC, MR with "select TWO/THREE"); distractors are "plausible responses in the same content area"; options test cost/performance/function differences between services; skills lists are action-oriented ("configure", "troubleshoot", "implement") [OFFICIAL, exam guide]. Official sample material = Skill Builder Official Practice Question Set + Official Pretest (not fetched; login-gated) — use them yourself, they are the best signal.
- **Anecdotal** (widely reported, unverified; do not over-weight): scenario stems with qualifiers (LEAST operational overhead, MOST cost-effective); heavy on Glue/S3/Redshift/Kinesis/Lake Formation/IAM-KMS combos; troubleshooting scenarios; several "choose two" items.
- Old exam-prep wisdom ("ordering/matching questions") is **not** listed in the current exam guide response types → my practice set will use MC and MR only unless Skill Builder shows otherwise.

## 7. Implications for the 11 remaining days
1. Keep the D1-heavy weighting but add a compact "v1.1 new topics" block (vectors/pgvector/HNSW/IVF, Bedrock KB, LLM in pipelines, Iceberg/S3 Tables, SageMaker Catalog/Unified Studio domains-projects, governance/data-sharing patterns) — ~8 task skills, maybe 3–6 exam questions total.
2. Replace outdated names (Kinesis Data Analytics → Managed Service for Apache Flink; Firehose; QuickSight → Quick; Governed tables → removed).
3. Book the exam slot now if not done (reschedulable free until 24 h before).
