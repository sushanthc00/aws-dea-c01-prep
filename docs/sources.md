# Sources (accessed 2026-10-20 unless noted)
## Phase 1 — exam reality
- Exam page: https://aws.amazon.com/certification/certified-data-engineer-associate/ — format, cost, languages, delivery, validity
- Exam guide v1.1: https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html — response types, scoring, domains
  - Domains: `.../data-engineer-associate-01-domain1.html` … `-domain4.html`
  - In-scope: `.../dea-01-in-scope-services.html`; out-of-scope: `.../dea-01-out-of-scope-services.html`; revisions: `.../dea-01-revisions.html`
- Before testing: https://aws.amazon.com/certification/policies/before-testing/ — reschedule/cancel, ID, online proctoring, ESL +30
- During testing: https://aws.amazon.com/certification/policies/during-testing/ — breaks, conduct, late arrival
- After testing / FAQ (14-day retake; seen in search summary only): https://aws.amazon.com/certification/policies/after-testing/ , https://aws.amazon.com/certification/faqs/
- Skill Builder exam prep: https://skillbuilder.aws/category/exam-prep/data-engineer-associate-DEA-C01 (link from cert page; not opened)
## Service changes (via search; headline-level, to be re-verified in Phase 3)
- Glue 5.1: https://aws.amazon.com/about-aws/whats-new/2026/02/aws-glue-5-1-eighteen-additional-regions
- Redshift: https://aws.amazon.com/about-aws/whats-new/2026/08/redshift-concurrencyscaling-for-kds-streams/ ; https://docs.aws.eu/redshift/latest/mgmt/behavior-changes.html
- S3 Tables Iceberg v3 / Variant: https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-s3-tables-variant-iceberg-v3/ ; https://docs.aws.eu/AmazonS3/latest/userguide/working-with-apache-iceberg-v3.html
- Lake Formation S3 access: https://aws.amazon.com/de/about-aws/whats-new/2026/06/aws-lake-formation-access-data-amazon-s3/
- EMR extended support: https://aws.amazon.com/about-aws/whats-new/2026/09/emr-extended-support-migration/
- Lambda runtimes: https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
- Firehose rename: https://aws.amazon.com/about-aws/whats-new/2024/02/amazon-data-firehose-formerly-kinesis-data-firehose
- Glue zero-ETL: https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html
- Secondary (unverified): atlan.com Quick Suite/Quick & DataZone pages; factualminds.com; hpcwire S3 Tables v3; Athena release notes on docs.amazonaws.cn
## Cheatsheet limits (fetched 2026-10-20)
- KDS quotas: https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html
- Firehose quotas: https://docs.aws.amazon.com/firehose/latest/dev/limits.html
- Lambda quotas: https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html
- S3 performance: https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html
- S3 lifecycle transitions: https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html
- DynamoDB quotas: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html
- SQS message quotas: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html
- Step Functions quotas: https://docs.aws.amazon.com/step-functions/latest/dg/service-quotas.html
- Athena quotas: https://docs.aws.amazon.com/athena/latest/ug/service-limits.html
## Phase 3 D1 fetches (2026-10-20)
- Lambda + Kinesis ESM: https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html
- MWAA environment class: https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html
- MSK quotas: https://docs.aws.amazon.com/msk/latest/developerguide/limits.html
- Glue job properties (versions, workers, Flex, timeout): https://docs.aws.amazon.com/glue/latest/dg/add-job.html
- DMS S3 target: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html
- EventBridge Scheduler: https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html
