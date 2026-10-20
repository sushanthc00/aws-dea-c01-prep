# Exam guide notes (official) — fetched 2026-10-20
Sources: https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html (+ -domain1..4, dea-01-in-scope-services, dea-01-out-of-scope-services, dea-01-revisions); https://aws.amazon.com/certification/certified-data-engineer-associate/

## Facts
- DEA-C01 still current; no C02/successor/retirement notice on cert page or guide. Guide **v1.1 published 2025-12-12** (v1.0 first release). Updates are published ~1 month before they are reflected in the exam.
- 65 Q: 50 scored + 15 unscored (unidentified). MC (1 of 4) and MR (2+ of 5+). No penalty for guessing; unanswered = wrong. Pass/fail; scaled 100–1000, min 720; compensatory (no per-section minimum). 130 min. $150 USD (+FX). Langs: EN, JA, KO, ZH-Simplified. Pearson VUE test center or online proctored. Valid 3 yrs. Cert page does not state retake policy.
- Target: 2–3 yrs data eng, 1–2 yrs AWS. Out-of-scope tasks: ML training/inference, language-specific syntax, business conclusions. "General concepts of vectors" now listed under recommended knowledge.
- Weights: D1 34, D2 26, D3 22, D4 18.
- Skill Builder: Official Practice Question Set + Official Pretest (exam prep plan) https://skillbuilder.aws/category/exam-prep/data-engineer-associate-DEA-C01

## v1.1 changes (official revisions page)
- Knowledge+skills merged into one skill list per task.
- NEW skills: 1.2.10 LLMs for data processing; 2.1.7 open table formats (Iceberg); 2.1.8 vector index types (HNSW, IVF); 2.2.6 business data catalogs (SageMaker Catalog); 2.4.6 vectorization (Bedrock knowledge base); 4.1.7 domains/domain units/projects for SageMaker Unified Studio; 4.5.6 data access via SageMaker Catalog projects; 4.5.7 governance framework + data sharing patterns.
- Reworded: 2.1.3 (HNSW with Aurora PostgreSQL; MemoryDB key/value); 2.4.4 lineage (SageMaker ML Lineage Tracking, SageMaker Catalog); 3.1.6 (DataBrew, SageMaker Unified Studio); 3.2.3 SQL in Redshift AND Athena; 4.2.5 role/tag/attribute-based; 4.3.4 "in transit or before transit"; 4.5.4 AWS Config; 4.5.5 data sovereignty.
- In-scope ADDED: Aurora, Amazon Q, Bedrock, Kendra, AWS Data Exchange, S3 Tables. REMOVED: Cloud9, CodeCommit, AWS SCT (but skill 2.4.3 still says "AWS SCT and AWS DMS Schema Conversion").
- Out-of-scope REMOVED: Honeycode, WorkDocs, Amazon Timestream, CodeWhisperer (due to deprecations). Timestream is not on the in-scope list either -> low priority.

## In-scope services (v1.1, non-exhaustive)
- Analytics: Athena, EMR, Glue, Glue DataBrew, Lake Formation, Kinesis Data Firehose (guide's name), Kinesis Data Streams, Managed Service for Apache Flink, MSK, OpenSearch Service, Amazon Quick (QuickSight successor name), SageMaker AI
- App Integration: AppFlow, EventBridge, MWAA, SNS, SQS, Step Functions
- Cost: Budgets, Cost Explorer. Compute: Batch, EC2, Lambda, SAM. Containers: ECR, ECS, EKS
- Database: DocumentDB, DynamoDB, Keyspaces, MemoryDB, Neptune, RDS, Aurora, Redshift
- Dev tools: CLI, CloudFormation, CDK, CodeBuild, CodeDeploy, CodePipeline, Amazon Q. Web: API Gateway
- ML: SageMaker AI, Bedrock, Kendra
- Mgmt: CloudTrail, CloudWatch, CloudWatch Logs, Config, Managed Grafana, Systems Manager, Well-Architected Tool, Data Exchange
- Migration: Application Discovery Service, Application Migration Service, DMS, DataSync, Snow Family, Transfer Family
- Network: CloudFront, PrivateLink, Route 53, VPC
- Security: IAM, KMS, Macie, Secrets Manager, Shield, WAF
- Storage: Backup, EBS, EFS, S3, S3 Tables, S3 Glacier
- Out-of-scope (notable): FinSpace, X-Ray, FIS, AppSync, Amplify, SES, IoT*, Elastic Beanstalk, App Runner, Lightsail, Outposts, SAR, Migration Hub, Mainframe Modernization, DevOps Guru, Connect/Chime/WorkMail, Elemental/IVS media.

## Task statements & skills (v1.1)
### D1
- 1.1 Ingestion: 1.1.1 streaming sources (Kinesis, MSK, DDB Streams, DMS, Glue, Redshift); 1.1.2 batch (S3, Glue, EMR, DMS, Redshift, Lambda, AppFlow); 1.1.3 batch config; 1.1.4 consume data APIs; 1.1.5 schedulers (EventBridge, Airflow, time-based; jobs & crawlers); 1.1.6 event triggers (S3 events, EventBridge); 1.1.7 Lambda from Kinesis; 1.1.8 IP allowlists; 1.1.9 throttling/rate limits (DDB, RDS, Kinesis); 1.1.10 fan-in/fan-out; 1.1.11 replayability; 1.1.12 stateful vs stateless.
- 1.2 Transform: 1.2.1 containers EKS/ECS; 1.2.2 JDBC/ODBC; 1.2.3 integrate multiple sources; 1.2.4 cost; 1.2.5 pick transform service (EMR, Glue, Lambda, Redshift); 1.2.6 format conversion CSV->Parquet; 1.2.7 troubleshoot transforms; 1.2.8 create data APIs; 1.2.9 3 Vs; 1.2.10 LLMs for data processing.
- 1.3 Orchestrate: 1.3.1 Lambda/EventBridge/MWAA/Step Functions/Glue workflows; 1.3.2 perf/availability/scalability/resiliency/fault tolerance; 1.3.3 serverless workflows; 1.3.4 SNS/SQS alerts.
- 1.4 Programming: 1.4.1 optimize code runtime; 1.4.2 Lambda concurrency/perf; 1.4.3 languages; 1.4.4 SWE best practice (git, test, log, monitor); 1.4.5 IaC; 1.4.6 SAM; 1.4.7 mount storage volumes in Lambda (EFS); 1.4.8 CFN/CDK; 1.4.9 CI/CD; 1.4.10 distributed computing; 1.4.11 data structures/algorithms (graph, tree).
### D2
- 2.1 Store: 2.1.1 cost/perf selection (Redshift, EMR, LF, RDS, DDB, KDS, MSK); 2.1.2 config for access patterns; 2.1.3 use cases (HNSW + Aurora PG; MemoryDB); 2.1.4 migration tools (Transfer Family); 2.1.5 remote access (Redshift federated queries, MVs, Spectrum); 2.1.6 locks (Redshift, RDS); 2.1.7 open table formats; 2.1.8 vector index types HNSW/IVF.
- 2.2 Catalog: 2.2.1 consume via catalog; 2.2.2 technical catalog (Glue DC, Hive metastore); 2.2.3 crawlers/schema discovery; 2.2.4 partition sync; 2.2.5 connections; 2.2.6 business catalog (SageMaker Catalog).
- 2.3 Lifecycle: 2.3.1 COPY/UNLOAD; 2.3.2 S3 lifecycle tiering; 2.3.3 expiration; 2.3.4 versioning + DDB TTL; 2.3.5 deletion for legal; 2.3.6 resiliency/availability.
- 2.4 Modeling: 2.4.1 schemas Redshift/DDB/LF; 2.4.2 changing data characteristics; 2.4.3 schema conversion (SCT, DMS Schema Conversion); 2.4.4 lineage; 2.4.5 indexing/partitioning/compression; 2.4.6 vectorization (Bedrock KB).
### D3
- 3.1 Automate: 3.1.1 MWAA/Step Functions; 3.1.2 troubleshoot managed workflows; 3.1.3 SDKs; 3.1.4 EMR/Redshift/Glue features; 3.1.5 data APIs; 3.1.6 prep (DataBrew, SageMaker Unified Studio); 3.1.7 Athena; 3.1.8 Lambda automation; 3.1.9 EventBridge events/schedulers.
- 3.2 Analyze: 3.2.1 visualize (DataBrew, QuickSight); 3.2.2 verify/clean (Lambda, Athena, QuickSight, Jupyter, Data Wrangler); 3.2.3 SQL views Redshift/Athena; 3.2.4 Athena Spark notebooks; 3.2.5 provisioned vs serverless; 3.2.6 aggregation, rolling avg, grouping, pivoting.
- 3.3 Monitor: 3.3.1 extract logs; 3.3.2 logging/monitoring for audit; 3.3.3 alerts; 3.3.4 perf troubleshooting; 3.3.5 CloudTrail; 3.3.6 troubleshoot Glue/EMR; 3.3.7 CW Logs; 3.3.8 analyze logs (Athena, EMR, OpenSearch, Logs Insights).
- 3.4 Quality: 3.4.1 checks in processing; 3.4.2 rules (DataBrew); 3.4.3 consistency; 3.4.4 sampling; 3.4.5 data skew mechanisms.
### D4
- 4.1 AuthN: 4.1.1 SGs; 4.1.2 IAM groups/roles/endpoints; 4.1.3 Secrets Manager rotation; 4.1.4 IAM roles for Lambda/API GW/CLI/CFN; 4.1.5 policies for S3 Access Points, PrivateLink; 4.1.6 managed vs unmanaged; 4.1.7 SageMaker Unified Studio domains/units/projects.
- 4.2 AuthZ: 4.2.1 custom IAM; 4.2.2 Secrets Manager / Parameter Store; 4.2.3 Redshift DB users/groups/roles; 4.2.4 Lake Formation (Redshift, EMR, Athena, S3); 4.2.5 RBAC/TBAC/ABAC; 4.2.6 least privilege.
- 4.3 Encrypt/mask: 4.3.1 masking/anonymization; 4.3.2 KMS; 4.3.3 cross-account encryption; 4.3.4 in transit / before transit.
- 4.4 Audit logs: 4.4.1 CloudTrail; 4.4.2 CW Logs; 4.4.3 CloudTrail Lake; 4.4.4 analyze logs; 4.4.5 EMR for large log volumes.
- 4.5 Privacy/gov: 4.5.1 Redshift data sharing; 4.5.2 Macie + LF PII; 4.5.3 prevent backups/replication to disallowed Regions; 4.5.4 Config; 4.5.5 sovereignty; 4.5.6 SageMaker Catalog projects; 4.5.7 governance framework/data sharing patterns.
