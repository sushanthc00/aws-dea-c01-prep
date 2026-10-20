# Fact-check report (independent, 2026-10-20)

Scope: `cheatsheets/05-limits-and-numbers.md` (all numbers) and the 58 lines in `docs/notes/factcheck-sample.md`. Official AWS sources only.

## (a) Summary (approximate counts of individual numeric/factual claims)
| Verdict | 05-limits (~125 claims) | Sample (58 lines) |
|---|---|---|
| CONFIRMED | ~103 | ~42 |
| WRONG | 1 (+1 imprecise) | 0 |
| OUTDATED | 2 | 4 (TTL, CodeCommit, 45% x2) |
| UNVERIFIABLE (not fetched / no source found) | ~18 | ~12 |

Fully confirmed on official pages: all KDS, Firehose, Lambda, SQS, Step Functions, DynamoDB, Athena (incl. capacity reservations), S3 performance and lifecycle numbers, MSK Serverless limits, Glue worker types/retries/concurrency/versions, KMS Encrypt 4 KB, Lambda ESM ParallelizationFactor <=10, exam facts (65 = 50 scored + 15 unscored, 720, 34/26/22/18, USD 150, 130 min), Python UDF EOS 2026-06-30, Glue 5.1 library versions, EMR 5.36/6.6-6.15 to 2027-06-30.

## (b) Claims that are WRONG / OUTDATED / UNVERIFIABLE
| file:line | claim | verdict | correct value | URL |
|---|---|---|---|---|
| cheatsheets/05-limits-and-numbers.md:63 | Redshift min TLS 1.2 enforced from 2026-01-31 | WRONG | Enforcement starts **2026-10-31** (rejects TLS 1.0/1.1; provisioned + serverless) | https://docs.aws.amazon.com/redshift/latest/mgmt/behavior-changes.html |
| 05-limits:63 | concurrency scaling for KDS MV refresh "patch P203, Aug 2026" | WRONG (minor) | P203 first shipped **2026-07-06** (builds through 2026-08-26); feature itself confirmed | https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html |
| 05-limits:63; 07-redshift.md:8; 1.2-transform.md:62 | Serverless 3-yr reservations "up to 45 %" | OUTDATED | 45% is the No-Upfront 3-yr figure; All Upfront 3-yr now advertised as up to 50% (What's New 2026-07) | https://aws.amazon.com/about-aws/whats-new/2026/07/redshift-serverless-three-year-auri/ ; https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-redshift-serverless-three-year-reservations/ |
| 05-limits:57; 2.3-lifecycle.md:31 | DynamoDB TTL deletes within ~48 h of expiry | OUTDATED/imprecise | Docs now say "typically within a few days" after expiry (no 48 h guarantee); free, no WCU, appears in Streams (confirmed) | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html |
| 1.4-programming.md:61 | "CodeCommit out" (not usable) | OUTDATED | AWS announced CodeCommit returned to GA (new sign-ups open, Nov 2025); the pricing page still shows the 2024 closure, so confirm in console. Exam in/out-of-scope status not re-verified | https://aws.amazon.com/blogs/devops/aws-codecommit-returns-to-general-availability/ |
| 05-limits:60 | Athena DML timeout default 30 min | UNVERIFIABLE | Quotas page says adjustable up to 240 min; default value not stated there | https://docs.aws.amazon.com/athena/latest/ug/service-limits.html |
| 05-limits:17 | each EFO consumer ~2 MB/s/shard | UNVERIFIABLE on quotas page | Not stated on the quotas page (stated in KDS EFO docs, not fetched) | https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html |
| 05-limits:44 | Express = at-least-once async / at-most-once sync | UNVERIFIABLE | Not on quotas page (not fetched: workflow-type page) | https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html |
| 05-limits:53 | Glacier retrieval times (Exp 1-5 min, Std 3-5 h, Bulk 5-12 h; DA Std <=12 h, Bulk <=48 h); PUT 5 GB; object 5 TB; multipart >100 MB | UNVERIFIABLE (not fetched; storage-class page gave only "minutes to hours") | check S3 restore/FAQ pages | https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects-retrieval-options.html |
| 05-limits:57 | Item 400 KB; partition 3,000 RCU/1,000 WCU; RCU/WCU sizes; query page 1 MB; LSI 10 GB | UNVERIFIABLE (not on the quotas page fetched; widely documented elsewhere) | | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html |
| 05-limits:65 | Glue 5.1 Python 3.11 / Spark 3.5.6 / Iceberg 1.10.0 / Hudi 1.0.2 / Delta 3.3.2 / Scala 2.12.18 | CONFIRMED via search snippets only (Glue docs; page not fully read) | | https://docs.aws.amazon.com/glue/latest/dg/release-notes.html |
| 05-limits:66 | EMR 7.0-7.10 extended through 2027-08-31 | UNVERIFIABLE (conflict) | AWS announcement says 2027-08-31, but release 7.10.0 lifecycle table shows Aug 15 2027; check per-release table | https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-standard-support.html |
| 05-limits:69 | "Not yet verified" list (MSK provisioned, KMS request rates, MWAA, OpenSearch, Redshift node limits) | not audited (no numbers given) | MSK Serverless numbers in guide/D1/1.1-ingestion.md:55 ARE confirmed | https://docs.aws.amazon.com/msk/latest/developerguide/limits.html |
| 01-d1:16 | Bedrock LLM-in-pipelines = task 1.2.10, "new v1.1" | UNVERIFIABLE | Exam guide page fetched states 50 scored/15 unscored/720/weights but no version number; domain 1 and Revisions pages not read | https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html |
| 02-d2:39; 2.4-modeling.md:31 | SCT removed from in-scope list; DMS Schema Conversion | UNVERIFIABLE (in-scope list not fetched). DMS SC facts confirmed: Oracle->Aurora/RDS PG & Redshift targets, Db2 LUW/z/OS and SAP ASE -> PostgreSQL | | https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html |
| 2.4-modeling.md:32 | SQL Server->PG/MySQL, PG->MySQL, MySQL->PG pairs | UNVERIFIABLE per pair (not individually checked) | | same as above |
| 10-lakeformation.md:48 | SageMaker Unified Studio domain/domain unit/project/catalog model | UNVERIFIABLE (not fetched) | | |
| 2.1-stores.md:17, :21 | MemoryDB durable/vector search; S3 Tables managed Iceberg + auto maintenance | UNVERIFIABLE (not fetched; believed correct) | | |
| 08-streaming:13 | Firehose destinations incl. Snowflake, Iceberg, HTTP, Splunk, Redshift, OpenSearch | CONFIRMED (also S3 Tables, Datadog, New Relic, MongoDB etc. exist) | | https://aws.amazon.com/firehose/features/ |

Notes on confirmed items worth remembering: Redshift Python UDF end of support after 2026-06-30 and new-UDF creation ended 2025-10-30 (confirmed). Firehose "other Regions" Direct PUT 100,000 rec/s, 1,000 req/s, 1 MiB/s confirmed. Step Functions distributed map 10,000 child executions and redrive window 14 d confirmed. Lambda: 1,000 concurrency, 1,000 envs/10 s, 10x sync rate, 6 MB/1 MB/200 MB payloads confirmed. Lambda timeout can be up to 90 min only for Lambda Managed Instances async/ESM (not a conflict with 15 min). MSK Firehose source "10 MB max record" without Lambda confirmed.

## (c) Pages used
- https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html
- https://docs.aws.amazon.com/firehose/latest/dev/limits.html
- https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html
- https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html
- https://docs.aws.amazon.com/step-functions/latest/dg/service-quotas.html
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html
- https://docs.aws.amazon.com/athena/latest/ug/service-limits.html
- https://docs.aws.amazon.com/athena/latest/ug/capacity-management.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html
- https://docs.aws.amazon.com/msk/latest/developerguide/limits.html
- https://docs.aws.amazon.com/glue/latest/dg/add-job.html
- https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html
- https://docs.aws.amazon.com/redshift/latest/mgmt/behavior-changes.html and cluster-versions.html
- https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html
- https://aws.amazon.com/certification/certified-data-engineer-associate/
- Web searches: Redshift 3-yr reservations, EMR support dates, Glue 5.1 versions, DMS Schema Conversion, CodeCommit, Firehose destinations.
