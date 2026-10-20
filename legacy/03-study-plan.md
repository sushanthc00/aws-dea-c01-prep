# C. Study Plan

> 14-day plan (primary) and 7-day crash plan (backup)  
> 2 hours/day = 28 total hours

## Udemy Course Recommendation

**Primary course** (Third-party — Udemy):  
[Stephane Maarek — AWS Certified Data Engineer Associate (DEA-C01)](https://www.udemy.com/course/aws-data-engineer/)  
- ~15 hours of video content  
- Covers all 4 domains  
- Includes practice questions  
- Well-structured for your timeline  
- Since you have Udemy Professional, this is free for you

**Practice exams** (Third-party — Udemy):  
[Tutorials Dojo — AWS DEA-C01 Practice Exams](https://www.udemy.com/course/aws-certified-data-engineer-associate-practice-exams/)  
- 4 practice exams (260 questions)  
- Detailed explanations  
- Closest to real exam difficulty

---

## 14-Day Plan (Recommended)

### Phase 1: Foundation (Days 1-4) — Build AWS Mental Model

#### Day 1: Exam Orientation + S3 Deep Dive
- **Objectives**: Understand exam structure, master S3 beyond basics
- **Topics**: Exam domains, S3 storage classes, lifecycle policies, versioning, S3 Select, event notifications, access points
- **Resources**:
  - Read `01-exam-breakdown.md` (15 min)
  - Read `02-skills-gap-analysis.md` (15 min)
  - Stephane Maarek course: S3 sections (45 min)
  - [S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/) (15 min)
  - [S3 FAQ](https://aws.amazon.com/s3/faqs/) — skim the data lake and analytics sections (30 min)
- **Exercise**: Create a decision tree: "Which S3 storage class for ___?"
- **Knowledge check**: Can you explain S3 Standard vs IA vs Glacier Instant vs Glacier Flexible vs Deep Archive?
- **Milestone**: S3 storage class decision matrix complete

#### Day 2: AWS Glue — Part 1 (ETL Core)
- **Objectives**: Understand Glue architecture, crawlers, Data Catalog, ETL jobs
- **Topics**: Glue components, crawlers, classifiers, Data Catalog, databases/tables, Glue ETL jobs (PySpark), job bookmarks, Glue Studio
- **Resources**:
  - Stephane Maarek course: Glue sections (60 min)
  - [AWS Glue Concepts](https://docs.aws.amazon.com/glue/latest/dg/components-key-concepts.html) (30 min)
  - [Glue Job Bookmarks](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html) (15 min)
  - [Glue FAQ](https://aws.amazon.com/glue/faqs/) (15 min)
- **Exercise**: Diagram the flow: S3 → Crawler → Data Catalog → ETL Job → S3
- **Knowledge check**: What's the difference between a Glue crawler and a Glue ETL job? When do you use job bookmarks?
- **Milestone**: Can explain Glue end-to-end pipeline

#### Day 3: AWS Glue — Part 2 + Athena
- **Objectives**: Glue advanced features, Athena for serverless querying
- **Topics**: Glue DataBrew, Glue Data Quality (DQDL), Glue Schema Registry, Glue Streaming ETL, Athena basics, partition projection, CTAS, workgroups, Athena Federated Query
- **Resources**:
  - Stephane Maarek course: Glue advanced + Athena sections (60 min)
  - [Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html) (15 min)
  - [Athena Partition Projection](https://docs.aws.amazon.com/athena/latest/ug/partition-projection.html) (15 min)
  - [Athena CTAS](https://docs.aws.amazon.com/athena/latest/ug/ctas.html) (15 min)
  - [Athena FAQ](https://aws.amazon.com/athena/faqs/) (15 min)
- **Exercise**: Write pseudocode for a CTAS query that converts JSON to Parquet with partitioning
- **Knowledge check**: When would you use Athena vs Redshift Spectrum? What is partition projection?
- **Milestone**: Glue + Athena fully covered

#### Day 4: Amazon Kinesis (All Flavors) + MSK
- **Objectives**: Master the streaming services decision tree
- **Topics**: Kinesis Data Streams (shards, consumers, enhanced fan-out), Kinesis Data Firehose (delivery streams, transformations, buffering), Kinesis Data Analytics (Apache Flink), Amazon MSK (MSK Serverless, MSK Connect), Kinesis vs MSK decision
- **Resources**:
  - Stephane Maarek course: Kinesis + MSK sections (60 min)
  - [Kinesis Data Streams Key Concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html) (15 min)
  - [Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) (15 min)
  - [MSK Overview](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) (15 min)
  - [Kinesis FAQ](https://aws.amazon.com/kinesis/data-streams/faqs/) (15 min)
- **Exercise**: Build a comparison table: Kinesis Streams vs Firehose vs Data Analytics vs MSK
- **Knowledge check**: A company needs real-time analytics on clickstream data with sub-second latency. Which Kinesis service? What if they need exactly-once processing?
- **Milestone**: Streaming services decision tree complete

### Phase 2: Core Services (Days 5-8) — Deepen Knowledge

#### Day 5: Amazon Redshift
- **Objectives**: Understand Redshift architecture, performance tuning, data loading
- **Topics**: Redshift architecture (leader/compute nodes), RA3 vs DC2, Redshift Serverless, distribution styles (KEY, EVEN, ALL, AUTO), sort keys (compound, interleaved), COPY command, Redshift Spectrum, materialized views, concurrency scaling, WLM
- **Resources**:
  - Stephane Maarek course: Redshift sections (60 min)
  - [Redshift Best Practices](https://docs.aws.amazon.com/redshift/latest/dg/best-practices.html) (20 min)
  - [Distribution Styles](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html) (20 min)
  - [Redshift FAQ](https://aws.amazon.com/redshift/faqs/) (20 min)
- **Exercise**: Given a star schema, choose distribution and sort keys for fact and dimension tables
- **Knowledge check**: When do you use KEY vs ALL distribution? What's the difference between Redshift Spectrum and Athena?
- **Milestone**: Redshift architecture and tuning understood

#### Day 6: IAM + KMS + Security Foundations
- **Objectives**: Master IAM policy evaluation, KMS encryption patterns
- **Topics**: IAM policies (identity vs resource-based), policy evaluation logic, IAM roles, cross-account access, service-linked roles, KMS (CMKs, envelope encryption, key policies), S3 encryption options (SSE-S3, SSE-KMS, SSE-C, client-side), encryption in transit (TLS)
- **Resources**:
  - Stephane Maarek course: Security sections (45 min)
  - [IAM Policy Evaluation Logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) (20 min)
  - [KMS Concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) (20 min)
  - [S3 Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) (15 min)
  - [IAM FAQ](https://aws.amazon.com/iam/faqs/) (20 min)
- **Exercise**: Write an IAM policy that allows a Glue job to read from S3 bucket A and write to bucket B
- **Knowledge check**: Explain the difference between SSE-S3 and SSE-KMS. When would you use a resource-based policy vs an identity-based policy?
- **Milestone**: Can write and evaluate IAM policies

#### Day 7: Lake Formation + Data Governance
- **Objectives**: Understand Lake Formation's permission model, data governance patterns
- **Topics**: Lake Formation permissions (grant/revoke), data filters (column/row/cell-level), Lake Formation vs IAM for data access, blueprints, governed tables, data lineage, Glue Data Catalog integration, tag-based access control (LF-TBAC)
- **Resources**:
  - Stephane Maarek course: Lake Formation sections (45 min)
  - [Lake Formation Permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html) (30 min)
  - [Lake Formation Best Practices](https://docs.aws.amazon.com/lake-formation/latest/dg/best-practices.html) (20 min)
  - [Lake Formation FAQ](https://aws.amazon.com/lake-formation/faqs/) (25 min)
- **Exercise**: Design a permission model where analysts can see all columns except PII columns
- **Knowledge check**: How does Lake Formation differ from S3 bucket policies for data access? What are data filters?
- **Milestone**: Lake Formation permission model understood

#### Day 8: EMR + Step Functions + Lambda Patterns
- **Objectives**: Understand EMR vs Glue decision, orchestration with Step Functions
- **Topics**: EMR architecture (master/core/task nodes), EMR on EKS, EMR Serverless, EMRFS, Glue vs EMR decision criteria, Step Functions (Standard vs Express), state types, error handling, Map state, Lambda event sources, concurrency, DLQ, destinations
- **Resources**:
  - Stephane Maarek course: EMR + Step Functions + Lambda sections (60 min)
  - [EMR Best Practices](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan.html) (15 min)
  - [Step Functions Concepts](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) (15 min)
  - [Step Functions FAQ](https://aws.amazon.com/step-functions/faqs/) (15 min)
  - [Lambda FAQ](https://aws.amazon.com/lambda/faqs/) (15 min)
- **Exercise**: Design a Step Functions state machine that orchestrates: Glue Crawler → Glue ETL → Data Quality Check → Notification
- **Knowledge check**: When would you choose EMR over Glue? What's the difference between Standard and Express Step Functions?
- **Milestone**: Orchestration and processing services covered

### Phase 3: Operations + Practice (Days 9-11)

#### Day 9: CloudWatch + CloudTrail + EventBridge + Operational Patterns
- **Objectives**: Master monitoring, logging, event-driven automation
- **Topics**: CloudWatch metrics/logs/alarms/dashboards, Logs Insights, CloudTrail (management vs data events), EventBridge rules/schedules/targets, operational patterns (retry, DLQ, alerting), troubleshooting common pipeline failures
- **Resources**:
  - Stephane Maarek course: Monitoring + Operations sections (45 min)
  - [CloudWatch Concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) (15 min)
  - [CloudTrail Concepts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html) (15 min)
  - [EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) (15 min)
  - Review `05-service-primer.md` operational sections (30 min)
- **Exercise**: Design a monitoring setup for a Glue ETL pipeline (what metrics, what alarms, what logs)
- **Knowledge check**: How do you detect a failed Glue job and automatically retry it?
- **Milestone**: Operations and monitoring covered

#### Day 10: Data Formats, Partitioning, Cost Optimization + Gap Review
- **Objectives**: Consolidate cross-cutting topics, fill gaps
- **Topics**: Parquet vs ORC vs Avro vs JSON (when to use each), compression (Snappy, GZIP, ZSTD, LZO), partitioning strategies (Hive-style, too many partitions), file sizing (small files problem), cost optimization patterns (S3 tiers, Redshift reserved nodes, Athena scan reduction), DynamoDB (streams, TTL, global tables), RDS/Aurora basics, QuickSight basics
- **Resources**:
  - Stephane Maarek course: remaining sections you haven't covered (45 min)
  - [Athena Performance Tuning](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning.html) (15 min)
  - Review `05-service-primer.md` for any gaps (30 min)
  - Review `10-cheat-sheet.md` for quick refresh (15 min)
  - Skim remaining FAQs for services you're less confident on (15 min)
- **Exercise**: Given a scenario with 1 million small JSON files in S3, design the optimal storage strategy
- **Knowledge check**: Why is Parquet better than JSON for Athena queries? What's the small files problem?
- **Milestone**: All services covered, ready for mock exams

#### Day 11: Mock Exam 1 + Review
- **Objectives**: Take first mock exam, identify weak areas
- **Topics**: All domains
- **Resources**:
  - Take `06-mock-exam-1.md` under timed conditions (75 min)
  - Review all answers with explanations (45 min)
  - Use `08-weakness-diagnosis.md` to analyze results
  - OR take Tutorials Dojo Practice Exam 1 on Udemy
- **Exercise**: For every wrong answer, write a 1-sentence correction
- **Knowledge check**: Score target: 75%+ means you're on track
- **Milestone**: First mock exam completed, weak areas identified

### Phase 4: Refinement (Days 12-14)

#### Day 12: Targeted Review + Mock Exam 2
- **Objectives**: Address weak areas from Mock 1, take second mock
- **Topics**: Focus on your weakest domain from Mock 1
- **Resources**:
  - Re-read relevant sections of `05-service-primer.md` for weak areas (30 min)
  - Re-watch Stephane Maarek sections for weak topics (30 min)
  - Take `07-mock-exam-2.md` or Tutorials Dojo Practice Exam 2 (60 min)
- **Exercise**: Create flashcards for your most-missed concepts
- **Knowledge check**: Score improvement from Mock 1?
- **Milestone**: Second mock exam completed, improvement measured

#### Day 13: Final Gap Closure + Practice Questions
- **Objectives**: Close remaining gaps, build exam stamina
- **Topics**: Weakest remaining areas
- **Resources**:
  - Tutorials Dojo Practice Exams 3-4 on Udemy (60 min)
  - Review wrong answers thoroughly (30 min)
  - Re-read `10-cheat-sheet.md` (15 min)
  - Review `11-must-know-checklist.md` — check off everything you know (15 min)
- **Exercise**: For any unchecked items on the checklist, do a 5-minute deep dive
- **Knowledge check**: Can you check off 90%+ of the must-know checklist?
- **Milestone**: All major gaps closed

#### Day 14: Exam Eve — Final Review
- **Objectives**: Consolidate, build confidence, rest
- **Topics**: High-level review only
- **Resources**:
  - Read `09-exam-strategy.md` (20 min)
  - Read `10-cheat-sheet.md` one final time (15 min)
  - Skim `11-must-know-checklist.md` (10 min)
  - Light review of any remaining weak spots (30 min)
  - **REST** — do not cram. Sleep well. (remaining time)
- **Exercise**: None — just review
- **Knowledge check**: Do you feel confident about the top 8 services?
- **Milestone**: Ready for exam day

---

## 7-Day Crash Plan (If Time Runs Out)

| Day | Focus | Time | Key Activity |
|---|---|---|---|
| 1 | Exam overview + S3 + Glue basics | 2h | Stephane Maarek: S3 + Glue sections |
| 2 | Glue advanced + Athena + Kinesis | 2h | Stephane Maarek: streaming + querying |
| 3 | Redshift + Lake Formation | 2h | Stephane Maarek: storage + governance |
| 4 | IAM + KMS + Security | 2h | Stephane Maarek: security sections |
| 5 | EMR + Step Functions + Operations | 2h | Stephane Maarek: remaining sections |
| 6 | Mock Exam 1 + Review | 2h | Take exam, review wrong answers |
| 7 | Mock Exam 2 + Final Review | 2h | Take exam, read cheat sheet, rest |

**7-day strategy**: Skip hands-on entirely. Focus on video course + practice exams. Read cheat sheet daily.

---

## Minimum Viable Pass Plan (Absolute Minimum)

If you can only do 10 hours total:
1. Watch Stephane Maarek course at 1.5x speed, skip sections you're confident on (7 hours)
2. Take 1 practice exam (1.5 hours)
3. Review cheat sheet (30 min)
4. Read exam strategy (30 min)
5. Review wrong answers from practice exam (30 min)

---

## High-Confidence Plan (Extra Time Available)

If you can do 3+ hours/day:
- Add hands-on labs for Glue, Kinesis, Redshift
- Take all 4 Tutorials Dojo practice exams
- Read AWS whitepapers on data analytics
- Do the AWS Skill Builder exam prep course
- Build and use the mock exam website for additional practice

---

## Topics to Safely De-Prioritize

If running low on time, these can be skimmed:
1. QuickSight details (1-2 questions max)
2. RDS/Aurora deep dive (you know relational DB concepts)
3. VPC networking details (focus only on VPC endpoints)
4. DynamoDB advanced features (you have basics)
5. EMR deep dive (focus on Glue vs EMR decision only)
6. Specific Flink/Kinesis Data Analytics syntax

---

## Final 24-Hour Revision Plan

| Time Before Exam | Activity |
|---|---|
| 24 hours | Read `10-cheat-sheet.md` |
| 20 hours | Review `11-must-know-checklist.md` |
| 18 hours | Re-read wrong answers from mock exams |
| 12 hours | Read `09-exam-strategy.md` |
| 8 hours | Stop studying. Relax. |
| Night before | Sleep 7-8 hours minimum |
| Morning of | Light breakfast, review cheat sheet one last time |
| 30 min before | Arrive early, breathe, trust your preparation |
