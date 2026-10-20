# F. Mock Exam 2 — AWS Certified Data Engineer Associate (DEA-C01)

> 65 questions (50 scored + 15 unscored) | 130 minutes | Passing: 720/1000
> Original questions — different scenarios from Mock Exam 1.

---

## Questions

### Q1 | Domain 1 | Ingestion | Difficulty: Medium
A company receives 10 GB of JSON log files every hour from application servers. The data must be transformed to Parquet and stored in S3 partitioned by date. The solution should be fully managed and serverless. Which approach is best?

A. Kinesis Data Firehose with format conversion enabled
B. AWS Glue ETL job triggered by an EventBridge schedule
C. Lambda function triggered by S3 event notifications
D. EMR Serverless with a scheduled Spark job

### Q2 | Domain 2 | Storage | Difficulty: Medium
A data engineer stores 500 TB of data in S3. Access patterns vary: some data is accessed daily, some weekly, and some hasn't been accessed in over a year. The engineer wants to minimize storage costs without manually managing data movement. Which solution is best?

A. Create lifecycle rules to transition data through storage classes on a fixed schedule
B. Use S3 Intelligent-Tiering
C. Move all data to S3 Glacier
D. Use S3 Standard for all data

### Q3 | Domain 1 | Streaming | Difficulty: Hard
A data engineer has a Kinesis Data Stream with on-demand capacity mode. The stream receives variable traffic — 1,000 records/sec during off-peak and 100,000 records/sec during peak. A Lambda consumer processes the records. During peak times, the Lambda function falls behind. What should the engineer do?

A. Switch to provisioned mode with more shards
B. Increase the Lambda function's batch size and parallelization factor
C. Add a Kinesis Data Firehose delivery stream between the stream and Lambda
D. Increase the Lambda function's memory allocation

### Q4 | Domain 4 | Security | Difficulty: Medium
A data engineer needs to grant temporary access to an S3 bucket for a third-party auditor. The access should expire after 24 hours and be limited to read-only operations on a specific prefix. Which approach is most secure?

A. Create an IAM user with access keys and delete the user after 24 hours
B. Generate a pre-signed URL for each object the auditor needs
C. Create an IAM role with a trust policy for the auditor's AWS account and a session duration of 24 hours
D. Make the S3 prefix publicly readable and remove access after 24 hours

### Q5 | Domain 3 | Orchestration | Difficulty: Medium
A data pipeline has three independent ETL jobs that can run in parallel, followed by a final aggregation job that depends on all three completing successfully. Which Step Functions pattern implements this?

A. Sequential Task states for all four jobs
B. A Parallel state containing three Task states, followed by a Task state for the aggregation job
C. A Map state processing the three jobs, followed by a Task state
D. A Choice state that routes to each job based on conditions

### Q6 | Domain 1 | ETL | Difficulty: Medium
A Glue ETL job reads from a JDBC source (MySQL) and writes to S3. The source table has 500 million rows. The job is slow because it reads the entire table through a single JDBC connection. How can the engineer improve performance?

A. Enable Glue job bookmarks
B. Use hashfield or hashexpression to parallelize the JDBC read
C. Increase the Glue job timeout
D. Switch to a Glue Python Shell job

### Q7 | Domain 2 | Redshift | Difficulty: Medium
A data engineer needs to load data from S3 into Redshift. The S3 data is split into 16 files of equal size. The Redshift cluster has 4 compute nodes. What is the optimal number of files for the COPY command?

A. 1 large file
B. 4 files (one per node)
C. 16 files (or a multiple of 4)
D. 100 small files

### Q8 | Domain 4 | Governance | Difficulty: Hard
A company uses Lake Formation for data governance. A new requirement states that the marketing team should only see rows where `region = 'US'` in the customer table. Which Lake Formation feature implements this?

A. Column-level permissions
B. Data filters with row-level security
C. Tag-based access control (LF-TBAC)
D. Lake Formation blueprints

### Q9 | Domain 1 | Streaming | Difficulty: Medium
A data engineer needs to deliver streaming data from Kinesis Data Streams to Amazon Redshift in near real-time. Which is the recommended approach?

A. Kinesis Data Firehose with Redshift as the destination
B. Lambda consumer that writes to Redshift via JDBC
C. Kinesis Data Analytics writing directly to Redshift
D. Glue Streaming ETL writing to Redshift

### Q10 | Domain 3 | Monitoring | Difficulty: Easy
A data engineer wants to query and analyze CloudWatch Logs from multiple Glue ETL jobs to identify common error patterns. Which CloudWatch feature is best for this?

A. CloudWatch Metrics
B. CloudWatch Alarms
C. CloudWatch Logs Insights
D. CloudWatch Dashboards


### Q11 | Domain 2 | Data Lake | Difficulty: Medium
A data engineer is building a data lake and needs to ensure that the Glue Data Catalog stays in sync with the actual data in S3. New partitions are added daily. Which approach keeps the catalog updated with minimal effort?

A. Manually add partitions using ALTER TABLE ADD PARTITION
B. Schedule a Glue crawler to run daily
C. Use Athena partition projection
D. Use MSCK REPAIR TABLE in Athena

### Q12 | Domain 1 | Transformation | Difficulty: Hard
A data engineer has a Glue ETL job that joins a 1 TB dataset with a 50 MB lookup table. The job is slow due to shuffle operations during the join. Which optimization should be applied?

A. Increase the number of DPUs
B. Broadcast the small lookup table using a broadcast join
C. Repartition the large dataset before the join
D. Convert both datasets to Avro format

### Q13 | Domain 4 | Encryption | Difficulty: Medium
A company policy requires that all Redshift data be encrypted at rest. The company wants to manage the encryption keys and have the ability to rotate them. Which encryption option should be used?

A. Redshift default encryption (AES-256)
B. AWS KMS with an AWS managed key
C. AWS KMS with a customer managed key (CMK)
D. Hardware Security Module (CloudHSM)

### Q14 | Domain 3 | Event-Driven | Difficulty: Medium
A data engineer wants to trigger a Step Functions state machine whenever a new file arrives in a specific S3 bucket prefix. The trigger should be reliable and not miss any events. Which approach is recommended?

A. S3 event notification → Lambda → Start Step Functions execution
B. S3 event notification → EventBridge → Start Step Functions execution
C. CloudWatch alarm on S3 object count → Lambda → Start Step Functions
D. Periodic Lambda function that lists new S3 objects

### Q15 | Domain 2 | Query | Difficulty: Medium
A data engineer has an Athena table with data stored as Parquet in S3. Queries that select specific columns are fast, but queries that filter on a non-partition column are slow. What should the engineer do?

A. Add the filter column as a partition column
B. Use Parquet's row group statistics and ensure the data is sorted by the filter column
C. Switch from Parquet to JSON format
D. Increase the Athena workgroup query timeout

### Q16 | Domain 1 | Ingestion | Difficulty: Easy
A data engineer needs to replicate data from an Amazon RDS MySQL database to Amazon S3 in near real-time for analytics. The replication should capture inserts, updates, and deletes. Which service should be used?

A. AWS Database Migration Service (DMS) with CDC enabled
B. RDS automated backups exported to S3
C. AWS DataSync
D. MySQL native replication to an EC2 instance

### Q17 | Domain 4 | Access Control | Difficulty: Hard
A data engineer has a Glue ETL job that needs to access three different S3 buckets, a Redshift cluster, and the Glue Data Catalog. Following the principle of least privilege, how should permissions be configured?

A. Attach the AdministratorAccess managed policy to the Glue job's IAM role
B. Create a custom IAM policy with specific permissions for each resource and attach it to the Glue job's IAM role
C. Use S3 bucket policies to allow access from any IAM role
D. Create separate IAM roles for each resource and switch between them during the job

### Q18 | Domain 2 | Storage | Difficulty: Medium
A data engineer needs to choose between Amazon DynamoDB and Amazon Redshift for storing user activity data. The data will be used for two purposes: (1) real-time lookups by user ID and (2) weekly aggregate reports across all users. Which approach is best?

A. Store all data in DynamoDB
B. Store all data in Redshift
C. Store data in DynamoDB for real-time lookups and replicate to Redshift for aggregate reports
D. Store data in S3 and use Athena for both use cases

### Q19 | Domain 3 | Troubleshooting | Difficulty: Hard
A Glue ETL job that has been running successfully for weeks suddenly fails with a "No space left on device" error. The job reads from S3 and writes to S3. What is the most likely cause?

A. The S3 bucket has reached its storage limit
B. The Glue job's shuffle space on local disk is exhausted due to a large shuffle operation
C. The Glue Data Catalog has reached its table limit
D. The IAM role has lost S3 write permissions

### Q20 | Domain 1 | Data Formats | Difficulty: Medium
A data engineer is designing a data pipeline where the output will be queried by Athena. The queries typically select 5 out of 200 columns and filter by date. Which combination of format and organization maximizes query performance?

A. JSON files partitioned by date
B. Parquet files partitioned by date
C. CSV files with Athena partition projection
D. Avro files partitioned by date

### Q21 | Domain 4 | Compliance | Difficulty: Medium
A data engineer must ensure that all API calls made to AWS services in the data pipeline are logged for compliance. The logs must be stored for 7 years and be tamper-proof. Which configuration meets these requirements?

A. Enable CloudTrail with log file integrity validation and deliver logs to an S3 bucket with Object Lock
B. Enable CloudWatch Logs for all services and set retention to 7 years
C. Enable VPC Flow Logs and store in S3
D. Use AWS Config to record all resource changes

### Q22 | Domain 1 | Streaming | Difficulty: Medium
A data engineer is using Kinesis Data Firehose to deliver data to S3. The business wants the data organized in S3 by the event timestamp in the data (not the delivery time). Which Firehose feature enables this?

A. Firehose buffer configuration
B. Dynamic partitioning with inline parsing (JQ expressions)
C. Firehose data transformation with Lambda
D. S3 prefix with Firehose timestamp expressions

### Q23 | Domain 2 | Redshift | Difficulty: Medium
A data engineer has a Redshift cluster that experiences slow query performance during peak hours when many analysts run queries simultaneously. Which Redshift feature automatically adds temporary capacity to handle the burst?

A. Elastic resize
B. Concurrency scaling
C. Workload Management (WLM)
D. Redshift Spectrum

### Q24 | Domain 3 | Operations | Difficulty: Medium
A data engineer has a Step Functions state machine that orchestrates a daily ETL pipeline. The pipeline failed last night and the engineer needs to understand which step failed and why. Where should they look?

A. CloudWatch Logs for the Step Functions execution
B. Step Functions execution history in the AWS Console
C. CloudTrail logs for Step Functions API calls
D. S3 access logs

### Q25 | Domain 1 | ETL | Difficulty: Medium
A data engineer needs to process data from an S3 bucket that contains a mix of CSV, JSON, and Parquet files in the same prefix. The Glue ETL job should handle all three formats. What is the best approach?

A. Create separate Glue crawlers for each format and separate ETL jobs
B. Use a single Glue crawler with multiple classifiers and a single ETL job that handles the DynamicFrame schema
C. Convert all files to a single format before processing
D. Use Athena to query all formats and export to a unified format

### Q26 | Domain 4 | Network | Difficulty: Medium
A data engineer has a Glue ETL job that needs to access both an RDS database in a VPC and the Glue Data Catalog (which is a public AWS service). The company's security policy prohibits internet access from the VPC. Which configuration allows this?

A. Add a NAT gateway to the VPC
B. Configure the Glue job with a VPC connection and add VPC interface endpoints for Glue
C. Move the RDS database outside the VPC
D. Use AWS PrivateLink for RDS only

### Q27 | Domain 2 | Data Modeling | Difficulty: Hard
A data engineer is designing a Redshift schema for an e-commerce analytics platform. The most common queries aggregate sales by product category and time period. The `sales` fact table has 10 billion rows, the `products` dimension has 50,000 rows, and the `time` dimension has 3,650 rows (10 years of daily data). What is the optimal distribution and sort key strategy?

A. sales: KEY on product_id, products: KEY on product_id, time: KEY on time_id; Sort key on sales: time_id
B. sales: KEY on product_id, products: ALL, time: ALL; Compound sort key on sales: (time_id, product_id)
C. sales: EVEN, products: EVEN, time: EVEN; No sort keys
D. sales: ALL, products: ALL, time: ALL; Sort key on all tables: primary key

### Q28 | Domain 1 | Streaming | Difficulty: Hard
A data engineer is processing IoT sensor data through Kinesis Data Streams. Some sensors send duplicate messages due to network retries. The downstream system (DynamoDB) must not contain duplicate records. Which approach handles deduplication?

A. Enable deduplication on the Kinesis Data Stream
B. Implement idempotent writes in the consumer using a conditional expression in DynamoDB
C. Use Kinesis Data Firehose which guarantees exactly-once delivery
D. Set the Kinesis Data Stream retention to 24 hours to prevent duplicates

### Q29 | Domain 3 | Data Quality | Difficulty: Medium
A data engineer wants to implement data quality checks that run automatically as part of a Glue ETL job. If quality checks fail, the job should stop and not write bad data to the target. Which approach is best?

A. Add Glue Data Quality rules as a step in the Glue ETL job with a stop-on-failure configuration
B. Create a separate Lambda function that validates data after the Glue job completes
C. Use Athena queries to check data quality after loading
D. Implement custom validation logic in the Glue PySpark script

### Q30 | Domain 2 | Lake | Difficulty: Easy
A data engineer needs to create a central metadata repository that stores table definitions, schemas, and partition information for data stored in S3. This repository should be accessible by Athena, Redshift Spectrum, and EMR. Which service provides this?

A. Amazon DynamoDB
B. AWS Glue Data Catalog
C. Amazon RDS
D. AWS Systems Manager Parameter Store

### Q31 | Domain 1 | Ingestion | Difficulty: Medium
A company needs to ingest real-time stock market data from an external API that pushes data via WebSocket. The data must be stored in S3 for batch analytics. Which architecture is most appropriate?

A. API Gateway WebSocket API → Lambda → Kinesis Data Firehose → S3
B. Direct WebSocket connection from EC2 → Kinesis Data Streams → Kinesis Data Firehose → S3
C. API Gateway REST API → Lambda → S3
D. AWS AppFlow → S3

### Q32 | Domain 4 | Security | Difficulty: Medium
A data engineer needs to ensure that a specific IAM role can only start Glue ETL jobs that have a specific tag (environment=production). Which IAM feature enables this?

A. IAM permission boundaries
B. IAM policy condition keys with aws:ResourceTag
C. Service Control Policies (SCPs)
D. IAM access advisor

### Q33 | Domain 2 | Performance | Difficulty: Medium
A data engineer notices that Athena queries on a Parquet dataset are scanning more data than expected, even though the queries only select 3 columns. Investigation reveals the Parquet files are 2 GB each. What might be causing the excess scanning?

A. Parquet files are too large — Athena reads entire row groups even if only some columns are needed
B. The Parquet files use row group sizes that are too large, reducing column pruning effectiveness
C. Athena cannot perform column pruning on Parquet files
D. The Parquet files are not compressed

### Q34 | Domain 3 | Automation | Difficulty: Medium
A data engineer needs to automatically start a Glue ETL job whenever a DynamoDB table export to S3 completes. The export is triggered by another process. Which event-driven approach is most reliable?

A. Poll S3 periodically using Lambda to check for new export files
B. Use EventBridge to capture the DynamoDB export completion event and trigger the Glue job
C. Use DynamoDB Streams to detect the export
D. Use CloudWatch Alarms on DynamoDB metrics

### Q35 | Domain 1 | ETL | Difficulty: Hard
A data engineer has a Glue ETL job that processes data incrementally using job bookmarks. After a job failure, the engineer needs to reprocess data from a specific point in time. What should the engineer do?

A. Delete the job bookmark and rerun the job
B. Reset the job bookmark to a specific run ID and rerun the job
C. Create a new Glue job with the same configuration
D. Manually delete the processed files from the target and rerun

### Q36 | Domain 4 | Governance | Difficulty: Medium
A data engineer needs to implement tag-based access control in Lake Formation so that users with the "department=finance" tag can only access tables tagged with "department=finance". Which Lake Formation feature provides this?

A. Lake Formation data filters
B. Lake Formation tag-based access control (LF-TBAC)
C. IAM resource tags
D. Glue Data Catalog resource policies

### Q37 | Domain 2 | Storage | Difficulty: Medium
A data engineer needs to store reference data (country codes, currency mappings) that is read frequently by multiple Lambda functions and Glue ETL jobs. The data is small (< 1 MB), changes rarely, and requires millisecond read latency. Which storage option is most appropriate?

A. Amazon S3
B. Amazon DynamoDB
C. AWS Systems Manager Parameter Store
D. Amazon ElastiCache

### Q38 | Domain 1 | Transformation | Difficulty: Medium
A data engineer needs to flatten nested JSON data in a Glue ETL job. The JSON contains arrays of objects that need to be exploded into individual rows. Which Glue transform is most appropriate?

A. Relationalize transform
B. Map transform
C. Filter transform
D. ResolveChoice transform

### Q39 | Domain 3 | Cost | Difficulty: Medium
A data engineer runs multiple Glue ETL jobs daily. The total cost has increased significantly. Analysis shows that several jobs are using 10 DPUs but only utilizing 30% of the allocated capacity. What should the engineer do?

A. Switch all jobs to Glue Python Shell
B. Reduce the number of DPUs allocated to under-utilized jobs and enable auto-scaling
C. Move all jobs to EMR for better cost control
D. Schedule jobs to run during off-peak hours for lower pricing

### Q40 | Domain 2 | Redshift | Difficulty: Medium
A data engineer needs to export the results of a Redshift query to S3 as Parquet files for consumption by Athena. Which Redshift command should be used?

A. COPY
B. UNLOAD
C. CREATE EXTERNAL TABLE
D. INSERT INTO


### Q41 | Domain 1 | Ingestion | Difficulty: Medium
A company has 100 TB of historical data in an on-premises Hadoop cluster (HDFS). The data needs to be migrated to S3. The network bandwidth is limited to 100 Mbps. Which migration approach is most practical?

A. Use AWS DataSync over the internet
B. Use AWS Snowball Edge devices
C. Use S3 Transfer Acceleration
D. Set up AWS Direct Connect and transfer over the network

### Q42 | Domain 4 | Security | Difficulty: Medium
A data engineer needs to rotate the encryption keys used for S3 server-side encryption without re-encrypting existing objects. Which encryption option supports this?

A. SSE-S3
B. SSE-KMS with automatic key rotation
C. SSE-C
D. Client-side encryption

### Q43 | Domain 3 | Operations | Difficulty: Hard
A data engineer has a complex data pipeline orchestrated by Step Functions. The pipeline processes data from 50 different source tables. If one source table's processing fails, the pipeline should continue processing the remaining tables and report failures at the end. Which Step Functions pattern achieves this?

A. Sequential Task states with Catch blocks on each
B. Map state with error tolerance (maxConcurrency and toleratedFailurePercentage)
C. Parallel state with 50 branches
D. Choice state that skips failed tables

### Q44 | Domain 2 | Data Lake | Difficulty: Medium
A data engineer needs to implement a slowly changing dimension (SCD Type 2) in a data lake on S3. The solution should support querying historical versions of records. Which approach is recommended?

A. Overwrite the data in S3 with each update
B. Use Lake Formation governed tables with Apache Iceberg (supports time travel)
C. Store each version as a separate S3 object with a version suffix
D. Use S3 versioning to maintain historical versions

### Q45 | Domain 1 | Streaming | Difficulty: Medium
A data engineer is using Kinesis Data Firehose to deliver data to S3. The data needs to be partitioned in S3 by a field in the data payload (e.g., `country_code`). Which Firehose feature enables this?

A. Firehose prefix expressions with timestamp
B. Dynamic partitioning
C. Lambda transformation
D. Firehose buffer configuration

### Q46 | Domain 4 | Governance | Difficulty: Medium
A data engineer needs to share specific tables from the Glue Data Catalog in Account A with data analysts in Account B. The analysts should be able to query the shared tables using Athena in their own account. Which approach is recommended?

A. Copy the data to Account B's S3 bucket
B. Use Lake Formation cross-account data sharing
C. Create IAM roles in Account A for Account B users
D. Make the S3 bucket publicly accessible

### Q47 | Domain 2 | Query | Difficulty: Medium
A data engineer has an Athena workgroup used by a team of 20 analysts. The monthly Athena bill has been increasing due to some analysts running expensive full-table scans. Which Athena feature can limit costs?

A. Athena query result caching
B. Per-query and per-workgroup data scan limits
C. Athena reserved capacity
D. Athena query queuing

### Q48 | Domain 3 | Monitoring | Difficulty: Medium
A data engineer needs to detect when a Kinesis Data Stream's iterator age exceeds 1 hour (indicating the consumer is falling behind). Which monitoring approach is correct?

A. Create a CloudWatch alarm on the GetRecords.IteratorAgeMilliseconds metric
B. Check the Kinesis console manually every hour
C. Create a Lambda function that queries the stream's metrics
D. Enable enhanced monitoring on the Kinesis stream

### Q49 | Domain 1 | ETL | Difficulty: Medium
A data engineer needs to process semi-structured data (nested JSON with varying schemas) in a Glue ETL job. Some records have fields that others don't. Which Glue feature handles this schema variability?

A. Glue DynamicFrames (which support schema-on-read)
B. Glue DataBrew
C. Glue crawlers
D. Glue classifiers

### Q50 | Domain 4 | Security | Difficulty: Hard
A data engineer has an EMR cluster that processes data from S3. The security team requires that the EMR cluster can only access specific S3 buckets and that all S3 access is logged. Which combination of configurations meets these requirements? (Select TWO)

A. Configure the EMR cluster's IAM role with permissions limited to specific S3 buckets
B. Enable S3 server access logging on the target buckets
C. Use S3 Block Public Access on all buckets
D. Enable EMRFS consistent view
E. Create a VPC endpoint policy that restricts S3 access to specific buckets

### Q51 | Domain 2 | Storage | Difficulty: Easy
A data engineer needs to store the results of Athena queries for 30 days so that repeated queries don't incur additional scan charges. Which Athena feature provides this?

A. Athena query result location in S3 (results are cached automatically)
B. Athena workgroup query result reuse
C. Athena materialized views
D. Athena CTAS tables

### Q52 | Domain 1 | Ingestion | Difficulty: Medium
A data engineer needs to ingest data from multiple AWS accounts' CloudTrail logs into a central data lake for security analytics. Which approach is most scalable?

A. Configure an organization trail in AWS CloudTrail that delivers logs to a central S3 bucket
B. Create Lambda functions in each account to copy CloudTrail logs to a central bucket
C. Use AWS DataSync to replicate logs from each account
D. Enable CloudTrail Lake for cross-account querying

### Q53 | Domain 3 | Operations | Difficulty: Medium
A data engineer has a Glue ETL job that occasionally fails due to transient network errors when connecting to an RDS source. The engineer wants the job to automatically retry on failure without manual intervention. Which approach is simplest?

A. Configure the Glue job with a maximum retry count
B. Use Step Functions with retry logic to run the Glue job
C. Create a CloudWatch alarm that triggers a Lambda to restart the job
D. Implement retry logic within the Glue PySpark script

### Q54 | Domain 2 | Redshift | Difficulty: Hard
A data engineer has a Redshift cluster with a table that receives frequent small INSERT operations from an application. Query performance on this table has degraded over time. What is the most likely cause and solution?

A. The table needs to be vacuumed to reclaim space and re-sort rows
B. The table needs more distribution keys
C. The Redshift cluster needs more compute nodes
D. The table should be converted to an external table

### Q55 | Domain 1 | Streaming | Difficulty: Medium
A data engineer needs to process streaming data from Kinesis Data Streams and write the results to both S3 and DynamoDB simultaneously. The processing includes filtering and enrichment. Which approach minimizes operational overhead?

A. Two separate Lambda consumers — one for S3, one for DynamoDB
B. Kinesis Data Analytics (Flink) application with two sinks
C. Kinesis Data Firehose for S3 delivery + Lambda consumer for DynamoDB
D. Glue Streaming ETL with two output targets

### Q56 | Domain 4 | Compliance | Difficulty: Medium
A data engineer must implement a data retention policy that automatically deletes data older than 2 years from the data lake. The data is stored in S3 with Hive-style date partitioning. Which approach is most efficient?

A. S3 lifecycle rules based on object creation date
B. Scheduled Glue ETL job that deletes old partitions
C. S3 lifecycle rules with prefix-based expiration matching the partition structure
D. Manual deletion by the data engineering team quarterly

### Q57 | Domain 2 | Data Lake | Difficulty: Medium
A data engineer is implementing a data lakehouse architecture. The team needs to support ACID transactions, schema enforcement, and time travel on data stored in S3. Which open table format is natively supported by AWS Lake Formation?

A. Delta Lake
B. Apache Hudi
C. Apache Iceberg
D. All of the above are equally supported

### Q58 | Domain 3 | Troubleshooting | Difficulty: Hard
A data engineer's Athena query returns zero results, but the engineer knows the data exists in S3. The table was created using a Glue crawler. What are the most likely causes? (Select TWO)

A. The Glue crawler created the table with the wrong S3 location
B. The data files are encrypted and Athena doesn't have KMS permissions
C. The Athena workgroup has a query result limit of zero
D. The Glue crawler inferred the wrong schema or SerDe for the data format
E. The S3 bucket is in a different region than Athena

### Q59 | Domain 1 | ETL | Difficulty: Medium
A data engineer needs to merge new data with existing data in S3 (upsert operation — insert new records and update existing ones). The data is stored as Parquet. Which approach is recommended?

A. Overwrite the entire dataset with each update
B. Use Lake Formation governed tables (Apache Iceberg) which support MERGE operations
C. Write new data to a separate prefix and use Athena views to union them
D. Use S3 versioning to track changes

### Q60 | Domain 4 | Security | Difficulty: Medium
A data engineer needs to ensure that data flowing from Kinesis Data Streams to a Lambda consumer is encrypted. Which encryption mechanism protects data at rest in the Kinesis stream?

A. Kinesis server-side encryption using KMS
B. TLS encryption (enabled by default)
C. Client-side encryption in the producer
D. VPC endpoint encryption

### Q61 | Domain 2 | Performance | Difficulty: Medium
A data engineer has an Athena table with 5 years of data partitioned by year/month/day. Most queries filter on the last 30 days. The engineer wants to improve query planning performance for these recent-data queries. Which approach helps?

A. Use Athena partition projection with a date range
B. Create a separate table for the last 30 days
C. Use Athena CTAS to create a materialized view
D. Increase the Athena workgroup DPU allocation

### Q62 | Domain 3 | Operations | Difficulty: Easy
A data engineer wants to receive an email notification whenever a specific Glue crawler completes its run (success or failure). Which is the simplest approach?

A. EventBridge rule matching Glue crawler state change → SNS topic → Email subscription
B. CloudWatch alarm on crawler duration → SNS → Email
C. Lambda function that polls crawler status → SES email
D. Glue workflow notification

### Q63 | Domain 1 | Transformation | Difficulty: Medium
A data engineer needs to apply a complex transformation to streaming data in Kinesis Data Firehose before delivering to S3. The transformation requires calling an external API for data enrichment. Which Firehose feature supports this?

A. Firehose format conversion
B. Firehose data transformation using Lambda
C. Firehose dynamic partitioning
D. Firehose buffer configuration

### Q64 | Domain 4 | Governance | Difficulty: Medium
A data engineer needs to implement a data classification system where tables in the Glue Data Catalog are tagged with sensitivity levels (public, internal, confidential, restricted). Access should be granted based on these tags. Which approach is most scalable?

A. Create separate Glue databases for each sensitivity level
B. Use Lake Formation LF-TBAC with sensitivity level tags
C. Create IAM policies for each sensitivity level
D. Use S3 bucket policies based on prefixes

### Q65 | Domain 2 | Architecture | Difficulty: Hard
A company is designing a real-time analytics platform. Requirements: (1) ingest 1 million events/sec, (2) provide sub-second query latency for dashboards, (3) store raw data for batch analytics, (4) minimize operational overhead. Which architecture meets all requirements?

A. Kinesis Data Streams → Lambda → DynamoDB (real-time) + Kinesis Data Firehose → S3 (batch)
B. MSK → Flink → Amazon OpenSearch (real-time) + MSK → S3 Connector (batch)
C. Kinesis Data Streams → Kinesis Data Analytics → Amazon OpenSearch (real-time) + Kinesis Data Firehose → S3 (batch)
D. API Gateway → Lambda → Redshift (real-time) + S3 (batch)

---

## Answer Key

| Q | Answer | Domain | Topic |
|---|---|---|---|
| 1 | A | 1 | Ingestion |
| 2 | B | 2 | Storage |
| 3 | B | 1 | Streaming |
| 4 | C | 4 | Security |
| 5 | B | 3 | Orchestration |
| 6 | B | 1 | ETL |
| 7 | C | 2 | Redshift |
| 8 | B | 4 | Governance |
| 9 | A | 1 | Streaming |
| 10 | C | 3 | Monitoring |
| 11 | B | 2 | Data Lake |
| 12 | B | 1 | Transformation |
| 13 | C | 4 | Encryption |
| 14 | B | 3 | Event-Driven |
| 15 | B | 2 | Performance |
| 16 | A | 1 | Ingestion |
| 17 | B | 4 | Access Control |
| 18 | C | 2 | Storage |
| 19 | B | 3 | Troubleshooting |
| 20 | B | 1 | Data Formats |
| 21 | A | 4 | Compliance |
| 22 | B | 1 | Streaming |
| 23 | B | 2 | Redshift |
| 24 | B | 3 | Operations |
| 25 | A | 1 | ETL |
| 26 | B | 4 | Network |
| 27 | B | 2 | Data Modeling |
| 28 | B | 1 | Streaming |
| 29 | A | 3 | Data Quality |
| 30 | B | 2 | Lake |
| 31 | B | 1 | Ingestion |
| 32 | B | 4 | Security |
| 33 | B | 2 | Performance |
| 34 | B | 3 | Automation |
| 35 | B | 1 | ETL |
| 36 | B | 4 | Governance |
| 37 | B | 2 | Storage |
| 38 | A | 1 | Transformation |
| 39 | B | 3 | Cost |
| 40 | B | 2 | Redshift |
| 41 | B | 1 | Ingestion |
| 42 | B | 4 | Security |
| 43 | B | 3 | Operations |
| 44 | B | 2 | Data Lake |
| 45 | B | 1 | Streaming |
| 46 | B | 4 | Governance |
| 47 | B | 2 | Query |
| 48 | A | 3 | Monitoring |
| 49 | A | 1 | ETL |
| 50 | A, B | 4 | Security |
| 51 | B | 2 | Storage |
| 52 | A | 1 | Ingestion |
| 53 | A | 3 | Operations |
| 54 | A | 2 | Redshift |
| 55 | C | 1 | Streaming |
| 56 | C | 4 | Compliance |
| 57 | C | 2 | Data Lake |
| 58 | A, D | 3 | Troubleshooting |
| 59 | B | 1 | ETL |
| 60 | A | 4 | Security |
| 61 | A | 2 | Performance |
| 62 | A | 3 | Operations |
| 63 | B | 1 | Transformation |
| 64 | B | 4 | Governance |
| 65 | C | 2 | Architecture |


---

## Detailed Explanations

### Q1: A — Kinesis Data Firehose with Format Conversion
Firehose supports automatic format conversion from JSON to Parquet using the Glue Data Catalog schema. It's fully managed and serverless. **B** works but requires scheduling and isn't real-time. **C** Lambda has size/time limits. **D** EMR is overkill.

### Q2: B — S3 Intelligent-Tiering
Intelligent-Tiering automatically moves objects between access tiers based on actual access patterns. No manual management needed. **A** Fixed schedules may not match actual access patterns. **C** Glacier makes frequently accessed data unavailable. **D** Standard is the most expensive.

### Q3: B — Increase Batch Size and Parallelization Factor
Lambda's parallelization factor (up to 10) allows multiple Lambda invocations per shard, increasing throughput. Larger batch sizes reduce invocation overhead. **A** On-demand mode already auto-scales shards. **C** Firehose doesn't help Lambda processing. **D** Memory helps compute-bound functions, not throughput-bound.

### Q4: C — IAM Role with Trust Policy
An IAM role with a trust policy for the auditor's account provides temporary, scoped access. Session duration limits the access window. **A** IAM users with access keys are long-term credentials (security risk). **B** Pre-signed URLs work but are impractical for many objects. **D** Public access is never acceptable for sensitive data.

### Q5: B — Parallel State + Task State
The Parallel state runs all three ETL jobs concurrently. When all complete, the subsequent Task state runs the aggregation. **A** Sequential is slower. **C** Map state is for processing arrays of items, not fixed parallel tasks. **D** Choice is for conditional branching.

### Q6: B — Hashfield/Hashexpression
Glue supports partitioning JDBC reads using hashfield or hashexpression, which splits the read across multiple Spark partitions for parallel extraction. **A** Bookmarks help incremental processing, not parallelism. **C** Timeout doesn't improve speed. **D** Python Shell is slower.

### Q7: C — 16 Files (Multiple of Node Count)
COPY performs best when the number of files is a multiple of the number of slices (nodes × slices per node). 16 files for 4 nodes allows even distribution. **A** Single file can't be parallelized. **B** 4 files may not utilize all slices. **D** 100 small files add overhead.

### Q8: B — Data Filters with Row-Level Security
Lake Formation data filters support row-level security, allowing you to restrict rows based on column values (e.g., region = 'US'). **A** Column-level permissions hide columns, not rows. **C** LF-TBAC is for tag-based access, not row filtering. **D** Blueprints are for data ingestion.

### Q9: A — Kinesis Data Firehose to Redshift
Firehose natively supports Redshift as a destination. It stages data in S3 and uses COPY to load into Redshift. **B** Lambda + JDBC is slow and doesn't scale. **C** KDA doesn't write directly to Redshift. **D** Glue Streaming to Redshift adds complexity.

### Q10: C — CloudWatch Logs Insights
Logs Insights provides a SQL-like query language to search and analyze log data across multiple log groups. Perfect for finding error patterns. **A** Metrics are numerical, not log analysis. **B** Alarms trigger on thresholds. **D** Dashboards visualize metrics.

### Q11: B — Scheduled Glue Crawler
A daily crawler automatically discovers new partitions and updates the Data Catalog. **A** Manual partition management doesn't scale. **C** Partition projection works but requires knowing the partition scheme upfront. **D** MSCK REPAIR TABLE works but is manual and can be slow with many partitions.

### Q12: B — Broadcast Join
Broadcasting the small 50 MB table sends it to all executors, eliminating the shuffle of the large 1 TB dataset. This is a standard Spark optimization. **A** More DPUs help but don't eliminate the shuffle. **C** Repartitioning adds another shuffle. **D** Format change doesn't affect join performance.

### Q13: C — KMS with Customer Managed Key
Customer managed keys provide full control over key rotation, key policies, and audit logging. **A** Default encryption doesn't allow key management. **B** AWS managed keys don't allow custom rotation schedules. **D** CloudHSM is more complex and expensive than needed.

### Q14: B — S3 → EventBridge → Step Functions
EventBridge natively integrates with S3 events and can directly target Step Functions. This is the simplest and most reliable approach. **A** Lambda as a middleman adds unnecessary complexity. **C** CloudWatch alarm on object count is not event-driven. **D** Polling is inefficient and can miss events.

### Q15: B — Sorted Data with Row Group Statistics
Parquet stores min/max statistics per row group. If data is sorted by the filter column, Athena can skip entire row groups that don't match the filter (predicate pushdown). **A** Adding as a partition column may not be practical. **C** JSON is worse for column pruning. **D** Timeout doesn't improve performance.

### Q16: A — DMS with CDC
DMS with Change Data Capture captures inserts, updates, and deletes in near real-time. **B** Automated backups are point-in-time, not real-time. **C** DataSync is for file transfers. **D** Native replication to EC2 requires managing infrastructure.

### Q17: B — Custom IAM Policy with Least Privilege
A custom policy specifying exact permissions for each resource follows least privilege. **A** AdministratorAccess violates least privilege. **C** Overly permissive bucket policies. **D** Glue jobs use a single IAM role, not multiple.

### Q18: C — DynamoDB + Redshift
DynamoDB provides millisecond latency for real-time lookups. Redshift provides complex aggregate analytics. Using both optimizes for each access pattern. **A** DynamoDB is poor for aggregations. **B** Redshift has high latency for point lookups. **D** Athena has query startup latency.

### Q19: B — Shuffle Space Exhausted
Glue jobs use local disk for shuffle operations. If a join or aggregation produces a large shuffle, the local disk can fill up. Solutions: increase DPUs (more disk per worker) or optimize the job to reduce shuffle. **A** S3 has no practical storage limit. **C** Catalog limits don't cause disk errors. **D** Permission errors show different messages.

### Q20: B — Parquet Partitioned by Date
Parquet enables column pruning (only read 5 of 200 columns). Date partitioning enables partition pruning (skip irrelevant dates). Together, they minimize data scanned. **A** JSON doesn't support column pruning. **C** CSV is inefficient. **D** Avro is row-based.

### Q21: A — CloudTrail + Integrity Validation + S3 Object Lock
CloudTrail logs all API calls. Log file integrity validation detects tampering. S3 Object Lock (compliance mode) prevents deletion for the retention period. **B** CloudWatch Logs don't capture all API calls. **C** VPC Flow Logs capture network traffic, not API calls. **D** Config tracks resource changes, not API calls.

### Q22: B — Dynamic Partitioning
Dynamic partitioning allows Firehose to parse fields from the data payload (using JQ expressions) and use them as S3 partition keys. **A** Buffer configuration controls timing, not partitioning. **C** Lambda can transform data but dynamic partitioning is simpler for this use case. **D** Timestamp expressions use delivery time, not event time.

### Q23: B — Concurrency Scaling
Concurrency scaling automatically adds temporary clusters to handle burst read queries. **A** Elastic resize changes cluster size permanently. **C** WLM prioritizes queries but doesn't add capacity. **D** Spectrum queries S3, doesn't add compute.

### Q24: B — Step Functions Execution History
The Step Functions console shows detailed execution history including which state failed, input/output for each state, and error messages. **A** CloudWatch Logs has the logs but execution history is more structured. **C** CloudTrail shows API calls, not execution details. **D** S3 logs are irrelevant.

### Q25: A — Separate Crawlers and ETL Jobs
Different file formats need different classifiers and potentially different transformation logic. Separate crawlers ensure correct schema detection for each format. **B** A single crawler may misclassify mixed formats. **C** Pre-conversion adds an extra step. **D** Athena can query mixed formats but doesn't transform.

### Q26: B — VPC Connection + Glue VPC Endpoints
The Glue job needs a VPC connection for RDS access. VPC interface endpoints for Glue allow the job to reach the Glue Data Catalog without internet access. **A** NAT gateway provides internet access, which violates the security policy. **C** Moving RDS outside VPC is a security anti-pattern. **D** PrivateLink for RDS alone doesn't solve Glue Catalog access.

### Q27: B — KEY on product_id for sales, ALL for dimensions, Compound sort key
Sales table uses KEY distribution on product_id for co-located joins. Small dimension tables (50K products, 3.6K time entries) use ALL distribution. Compound sort key (time_id, product_id) optimizes the most common filter/group-by pattern. **A** KEY for time dimension wastes resources. **C** EVEN causes redistribution. **D** ALL on 10B row fact table is impossible.

### Q28: B — Idempotent Writes with Conditional Expressions
DynamoDB conditional expressions (e.g., attribute_not_exists or version checking) ensure that duplicate writes are safely ignored. **A** Kinesis doesn't have built-in deduplication. **C** Firehose doesn't guarantee exactly-once. **D** Retention doesn't prevent duplicates.

### Q29: A — Glue Data Quality with Stop-on-Failure
Glue Data Quality rules can be embedded in ETL jobs and configured to stop the job if quality checks fail, preventing bad data from reaching the target. **B** Post-job validation means bad data is already written. **C** Athena checks are after the fact. **D** Custom validation works but Glue DQ is purpose-built.

### Q30: B — Glue Data Catalog
The Glue Data Catalog is the central metadata repository for AWS data services. Athena, Redshift Spectrum, and EMR all use it as their metastore. **A** DynamoDB is a database, not a metadata catalog. **C** RDS is a database. **D** Parameter Store is for configuration.

### Q31: B — EC2 WebSocket → Kinesis → Firehose → S3
WebSocket connections require a persistent connection, which EC2 handles well. The data flows to Kinesis for buffering and Firehose for S3 delivery. **A** API Gateway WebSocket has connection limits. **C** REST API doesn't support WebSocket push. **D** AppFlow doesn't support WebSocket.

### Q32: B — IAM Condition Keys with ResourceTag
IAM policies support condition keys like `aws:ResourceTag/environment` to restrict actions based on resource tags. **A** Permission boundaries limit maximum permissions, not tag-based filtering. **C** SCPs are organization-level, not resource-tag-level. **D** Access advisor shows used permissions, not enforcement.

### Q33: B — Large Row Group Sizes
Parquet reads data in row groups. If row groups are very large, Athena must read more data even when only a few columns are needed, because it reads the entire column chunk within a row group. Optimal row group size is 128-256 MB. **A** File size alone isn't the issue. **C** Athena does support column pruning on Parquet. **D** Compression doesn't cause excess scanning.

### Q34: B — EventBridge for DynamoDB Export Events
EventBridge captures DynamoDB export completion events natively. **A** Polling is inefficient. **C** DynamoDB Streams capture item-level changes, not export events. **D** CloudWatch Alarms on metrics don't capture export completion.

### Q35: B — Reset Job Bookmark to Specific Run ID
Glue allows resetting job bookmarks to a specific previous run, enabling reprocessing from that point. **A** Deleting the bookmark reprocesses everything. **C** New job loses bookmark history. **D** Deleting target files doesn't reset the bookmark.

### Q36: B — LF-TBAC
Lake Formation Tag-Based Access Control allows assigning tags to both resources (tables) and principals (users/roles), then creating policies based on tag matches. **A** Data filters are for row/column filtering, not tag-based access. **C** IAM resource tags don't integrate with Lake Formation permissions. **D** Catalog resource policies are for cross-account access.

### Q37: B — DynamoDB
DynamoDB provides single-digit millisecond reads, handles small reference data well, and is accessible from both Lambda and Glue. **A** S3 has higher latency for small reads. **C** Parameter Store has lower throughput limits. **D** ElastiCache is overkill for < 1 MB of rarely changing data.

### Q38: A — Relationalize Transform
Glue's Relationalize transform flattens nested structures and arrays into relational tables. It's purpose-built for converting nested JSON to flat rows. **B** Map applies a function to each record. **C** Filter selects records. **D** ResolveChoice handles type ambiguity.

### Q39: B — Reduce DPUs + Enable Auto-Scaling
Right-sizing DPUs to match actual utilization and enabling auto-scaling (Glue 2.0+) optimizes cost. **A** Python Shell may not handle all workloads. **C** EMR migration is a large effort. **D** Glue doesn't have off-peak pricing.

### Q40: B — UNLOAD
UNLOAD exports query results from Redshift to S3 in various formats including Parquet. **A** COPY loads data INTO Redshift. **C** External tables define S3 data for querying, not exporting. **D** INSERT INTO writes to Redshift tables.

### Q41: B — Snowball Edge
At 100 Mbps, transferring 100 TB would take ~93 days over the network. Snowball Edge devices can transfer this in days via physical shipping. **A** DataSync over 100 Mbps is too slow. **C** Transfer Acceleration doesn't help with limited bandwidth. **D** Direct Connect takes weeks to provision.

### Q42: B — SSE-KMS with Automatic Key Rotation
KMS automatic key rotation creates new key material annually while keeping the old material for decrypting existing objects. No re-encryption needed. **A** SSE-S3 doesn't expose key rotation controls. **C** SSE-C requires you to manage rotation and re-encryption. **D** Client-side requires re-encryption.

### Q43: B — Map State with Error Tolerance
Map state processes an array of items (50 tables) with configurable maxConcurrency and toleratedFailurePercentage, allowing the pipeline to continue despite individual failures. **A** Sequential with Catch works but is slow. **C** 50 parallel branches is unwieldy. **D** Choice state can't dynamically handle failures.

### Q44: B — Lake Formation Governed Tables (Iceberg)
Iceberg supports ACID transactions, schema evolution, and time travel — all needed for SCD Type 2. **A** Overwriting loses history. **C** Separate objects are hard to manage. **D** S3 versioning is object-level, not record-level.

### Q45: B — Dynamic Partitioning
Dynamic partitioning extracts fields from the data payload and uses them as S3 partition keys. **A** Timestamp expressions use delivery time. **C** Lambda can help but dynamic partitioning is simpler. **D** Buffer configuration controls timing.

### Q46: B — Lake Formation Cross-Account Sharing
Lake Formation provides native cross-account sharing with fine-grained permissions. Analysts in Account B can query shared tables using Athena. **A** Copying data duplicates storage. **C** IAM roles are more complex to manage. **D** Public access is never acceptable.

### Q47: B — Per-Query and Per-Workgroup Scan Limits
Athena workgroups support data scan limits that cancel queries exceeding the threshold. **A** Result caching doesn't exist as a native feature. **C** Reserved capacity doesn't limit scans. **D** Query queuing doesn't limit cost.

### Q48: A — CloudWatch Alarm on IteratorAgeMilliseconds
This metric directly measures how far behind the consumer is. An alarm triggers when it exceeds the threshold. **B** Manual checking doesn't scale. **C** Lambda polling is unnecessary when CloudWatch metrics exist. **D** Enhanced monitoring provides shard-level metrics but you still need an alarm.

### Q49: A — DynamicFrames
Glue DynamicFrames handle schema variability natively — they don't require a fixed schema upfront. **B** DataBrew is for data preparation. **C** Crawlers discover schemas but don't handle variability during ETL. **D** Classifiers help crawlers, not ETL jobs.

### Q50: A, B — IAM Role Permissions + S3 Access Logging
The IAM role limits which buckets EMR can access (least privilege). S3 access logging records all access for audit. **C** Block Public Access is good practice but doesn't limit EMR access. **D** Consistent view is for S3 consistency. **E** VPC endpoint policies can restrict access but IAM is the primary control.

### Q51: B — Workgroup Query Result Reuse
Athena workgroups can be configured to reuse query results for a specified period, avoiding re-scanning. **A** Results are stored in S3 but not automatically reused without configuration. **C** Athena doesn't have materialized views in the traditional sense. **D** CTAS creates new tables, not cached results.

### Q52: A — Organization Trail
An organization trail in CloudTrail delivers logs from all accounts to a central S3 bucket. **B** Lambda in each account is complex. **C** DataSync is for file transfers. **D** CloudTrail Lake works but organization trail + S3 is more flexible for analytics.

### Q53: A — Glue Job Maximum Retry Count
Glue jobs have a built-in retry configuration (NumberOfRetries parameter). Simplest approach. **B** Step Functions works but adds complexity. **C** CloudWatch alarm + Lambda is over-engineered. **D** Script-level retry doesn't handle job-level failures.

### Q54: A — VACUUM
Frequent small INSERTs in Redshift create unsorted regions and deleted row markers. VACUUM reclaims space and re-sorts data. **B** Distribution keys can't be added after creation. **C** More nodes don't fix unsorted data. **D** External tables don't help with internal table performance.

### Q55: C — Firehose for S3 + Lambda for DynamoDB
Firehose handles S3 delivery with zero code. Lambda consumer handles DynamoDB writes with custom logic. This splits concerns cleanly. **A** Two Lambda consumers duplicate stream reading. **B** Flink is overkill for simple filtering. **D** Glue Streaming adds complexity.

### Q56: C — S3 Lifecycle Rules with Prefix-Based Expiration
With Hive-style partitioning (e.g., year=2024/month=01/), lifecycle rules can target specific prefixes to expire old data. **A** Object creation date may not match the data date. **B** Glue job for deletion is more complex. **D** Manual deletion doesn't scale.

### Q57: C — Apache Iceberg
Lake Formation governed tables are built on Apache Iceberg. While Hudi and Delta Lake work on AWS, Iceberg has the deepest native integration with Lake Formation. **A** Delta Lake works on EMR but isn't native to Lake Formation. **B** Hudi works on EMR but less integrated. **D** Not equally supported.

### Q58: A, D — Wrong S3 Location + Wrong Schema/SerDe
The most common causes of zero results from a crawler-created table are: (1) the crawler pointed to the wrong S3 path, or (2) the crawler inferred the wrong schema or SerDe (e.g., treating Parquet as CSV). **B** KMS errors would show access denied, not zero results. **C** No such setting. **E** Cross-region works with Athena.

### Q59: B — Lake Formation Governed Tables (Iceberg)
Iceberg supports MERGE INTO operations for upserts on S3 data. **A** Full overwrite is wasteful and risky. **C** Union views don't update existing records. **D** S3 versioning is object-level, not record-level.

### Q60: A — Kinesis Server-Side Encryption
Kinesis supports server-side encryption using KMS to encrypt data at rest in the stream. **B** TLS protects data in transit, not at rest. **C** Client-side encryption works but the question asks about the stream itself. **D** VPC endpoints don't encrypt data.

### Q61: A — Partition Projection with Date Range
Partition projection with a date range allows Athena to efficiently calculate which partitions to scan without querying the Glue Catalog for all 1,800+ partitions. **B** Separate table adds maintenance. **C** CTAS creates a snapshot, not a live view. **D** Athena doesn't have DPU allocation.

### Q62: A — EventBridge → SNS → Email
EventBridge captures Glue crawler state changes natively. SNS delivers email notifications. **B** Duration alarm doesn't capture completion events. **C** Lambda polling is over-engineered. **D** Glue workflows don't have built-in email notifications.

### Q63: B — Lambda Transformation
Firehose supports Lambda functions for data transformation, which can call external APIs for enrichment. **A** Format conversion changes format, not content. **C** Dynamic partitioning changes S3 organization. **D** Buffer configuration controls timing.

### Q64: B — LF-TBAC with Sensitivity Tags
LF-TBAC scales well for classification-based access control. Assign sensitivity tags to tables and matching tags to principals. **A** Separate databases don't scale. **C** IAM policies per level are hard to maintain. **D** Prefix-based policies don't work for table-level classification.

### Q65: C — Kinesis Streams → KDA → OpenSearch + Firehose → S3
This architecture handles all requirements: Kinesis ingests 1M events/sec, KDA (Flink) processes for real-time analytics, OpenSearch provides sub-second dashboard queries, and Firehose delivers raw data to S3 for batch. **A** DynamoDB isn't ideal for dashboard queries. **B** MSK adds operational overhead. **D** Redshift doesn't provide sub-second latency for real-time dashboards.

---

## Score Interpretation

| Score | Interpretation | Action |
|---|---|---|
| 80-100% (52-65 correct) | Excellent — likely ready to pass | Light review, focus on any missed topics |
| 70-79% (46-51 correct) | Good — on track but review weak areas | Targeted study on missed domains |
| 60-69% (39-45 correct) | Borderline — need more preparation | Focus on high-weight domains (1 and 2) |
| Below 60% (< 39 correct) | Not ready — need significant study | Review service primer, retake after more study |
