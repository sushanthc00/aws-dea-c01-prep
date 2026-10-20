# F. Mock Exam 1 — AWS Certified Data Engineer Associate (DEA-C01)

> 65 questions (50 scored + 15 unscored) | 130 minutes | Passing: 720/1000
> Original questions — not copied from any source.
> Mix of single-answer and multiple-answer questions across all 4 domains.

## Instructions
- Single-answer questions: Choose 1 correct answer (A, B, C, or D)
- Multiple-answer questions: Choose 2 or 3 correct answers (marked as "Select TWO" or "Select THREE")
- Answer all questions — no penalty for guessing
- Target time: ~2.5 minutes per question

---

## Questions

### Q1 | Domain 1 | Streaming Ingestion | Difficulty: Medium
**Type: Single Answer**

A company collects clickstream data from its website at a rate of 50,000 events per second. The data must be delivered to Amazon S3 in near real-time for batch analytics. The solution should require minimal operational overhead.

Which service should the data engineer use?

A. Amazon Kinesis Data Streams with a custom consumer writing to S3
B. Amazon Kinesis Data Firehose with S3 as the destination
C. Amazon MSK with a Kafka Connect S3 sink connector
D. AWS Lambda triggered by API Gateway writing directly to S3

### Q2 | Domain 2 | Storage Selection | Difficulty: Easy
**Type: Single Answer**

A data engineer needs to store 10 TB of historical log data that will be queried approximately once per month using Amazon Athena. The data must be retained for 7 years for compliance. Which S3 storage class is most cost-effective?

A. S3 Standard
B. S3 Standard-Infrequent Access
C. S3 Glacier Flexible Retrieval
D. S3 Intelligent-Tiering

### Q3 | Domain 1 | ETL | Difficulty: Medium
**Type: Single Answer**

A data engineer runs a daily AWS Glue ETL job that processes new files from an S3 bucket. The job currently reprocesses all files every run, causing increased costs and processing time. What should the engineer enable to process only new files?

A. Glue crawlers with a daily schedule
B. Glue job bookmarks
C. S3 event notifications with Lambda
D. Glue DataBrew profiling jobs

### Q4 | Domain 4 | Security | Difficulty: Medium
**Type: Single Answer**

A company requires that all data stored in Amazon S3 be encrypted at rest using keys that the company can audit and rotate. The solution must log every time a key is used to decrypt data. Which encryption option meets these requirements?

A. SSE-S3
B. SSE-KMS with an AWS managed key
C. SSE-KMS with a customer managed key
D. SSE-C

### Q5 | Domain 3 | Orchestration | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to orchestrate a pipeline that runs a Glue crawler, then a Glue ETL job, then a data quality check, and finally sends a notification. If any step fails, the pipeline should retry twice before sending an alert. Which service is best suited?

A. Amazon EventBridge with scheduled rules
B. AWS Step Functions with retry and catch blocks
C. AWS Lambda with recursive invocations
D. Amazon MWAA (Managed Airflow)


### Q6 | Domain 1 | Data Transformation | Difficulty: Easy
**Type: Single Answer**

A data engineer needs to convert a large collection of JSON files in S3 to Parquet format for improved query performance in Athena. The transformation should be repeatable and serverless. Which approach is most appropriate?

A. Use Athena CTAS (CREATE TABLE AS SELECT) to create a new Parquet table
B. Use Amazon Redshift COPY to load JSON and UNLOAD as Parquet
C. Write a custom EC2 application to convert files
D. Use S3 Batch Operations to convert file formats

### Q7 | Domain 2 | Data Warehouse | Difficulty: Hard
**Type: Single Answer**

A data engineer is designing a star schema in Amazon Redshift. The fact table has 5 billion rows and is frequently joined with a dimension table containing 500 rows. Which distribution strategy should be used for the dimension table?

A. KEY distribution on the join column
B. EVEN distribution
C. ALL distribution
D. AUTO distribution

### Q8 | Domain 4 | Governance | Difficulty: Medium
**Type: Single Answer**

A company has a data lake on S3 with hundreds of tables in the Glue Data Catalog. Different teams need access to different columns based on their role. Some columns contain PII that only the compliance team should see. Which service provides the most efficient solution?

A. S3 bucket policies with prefix-based access
B. IAM policies with condition keys for specific columns
C. AWS Lake Formation with data filters
D. Amazon Macie for PII detection and access control

### Q9 | Domain 1 | Streaming | Difficulty: Hard
**Type: Single Answer**

A data engineer has a Kinesis Data Stream with 10 shards. Three different consumer applications need to read from the stream simultaneously. Each consumer is experiencing ReadProvisionedThroughputExceeded errors. What should the engineer do?

A. Increase the number of shards to 30
B. Enable enhanced fan-out for each consumer
C. Switch to Kinesis Data Firehose
D. Increase the data retention period

### Q10 | Domain 3 | Monitoring | Difficulty: Medium
**Type: Single Answer**

A data engineer wants to be notified when an AWS Glue ETL job fails. The notification should include the job name and error message. Which approach requires the least operational overhead?

A. Configure CloudWatch Logs and create a metric filter for errors
B. Create an EventBridge rule that matches Glue job state change events and targets an SNS topic
C. Add error handling code in the Glue job script to send SNS notifications
D. Create a CloudWatch alarm on the Glue job duration metric

### Q11 | Domain 1 | Ingestion | Difficulty: Medium
**Type: Single Answer**

A company needs to migrate 50 TB of data from an on-premises Oracle database to Amazon S3 as Parquet files. The migration must capture ongoing changes after the initial load. Which service should be used?

A. AWS DataSync
B. AWS Database Migration Service (DMS) with CDC
C. AWS Transfer Family
D. AWS Snow Family

### Q12 | Domain 2 | Query Optimization | Difficulty: Medium
**Type: Single Answer**

A data engineer notices that Athena queries on a large S3 dataset are slow and expensive. The data is stored as CSV files without partitioning. Which combination of changes will most improve performance and reduce cost? (Select TWO)

A. Convert data from CSV to Parquet format
B. Implement Hive-style partitioning by date
C. Enable S3 Transfer Acceleration
D. Switch to S3 Glacier storage class
E. Increase Athena query timeout

### Q13 | Domain 4 | Security | Difficulty: Hard
**Type: Single Answer**

A data engineer needs to allow an AWS Glue ETL job in Account A to read data from an S3 bucket in Account B. Which combination of configurations is required? (Select TWO)

A. Create an IAM role in Account A with S3 read permissions and a trust policy allowing Glue
B. Add a bucket policy on Account B's S3 bucket allowing the role from Account A
C. Create a VPC peering connection between the two accounts
D. Enable S3 cross-region replication from Account B to Account A
E. Create an IAM user in Account B and share the access keys with Account A

### Q14 | Domain 1 | Streaming | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to perform real-time aggregations (tumbling windows of 5 minutes) on streaming data from Kinesis Data Streams. The results should be written to a DynamoDB table. Which service should process the stream?

A. Kinesis Data Firehose with Lambda transformation
B. Amazon Kinesis Data Analytics (Apache Flink)
C. AWS Glue Streaming ETL
D. Amazon EMR with Spark Structured Streaming

### Q15 | Domain 2 | Data Catalog | Difficulty: Easy
**Type: Single Answer**

A data engineer has new data files arriving daily in S3 in an unknown schema. The schemas need to be automatically discovered and registered in the Glue Data Catalog so Athena can query them. Which Glue feature should be used?

A. Glue ETL job
B. Glue crawler
C. Glue DataBrew
D. Glue workflow


### Q16 | Domain 3 | Operations | Difficulty: Medium
**Type: Single Answer**

A Glue ETL job processes data from S3 and writes to Redshift. The job has been running successfully for months but suddenly starts failing with out-of-memory errors. The input data volume has not changed significantly. What is the most likely cause?

A. The Redshift cluster is full
B. Data skew in the source data causing uneven partition processing
C. The Glue Data Catalog has too many tables
D. The S3 bucket has versioning enabled

### Q17 | Domain 1 | Data Formats | Difficulty: Easy
**Type: Single Answer**

A data engineer is designing a data pipeline where the schema is expected to evolve frequently. Downstream consumers need to handle schema changes gracefully. The data will be streamed through Amazon MSK. Which data format is most appropriate?

A. CSV
B. JSON
C. Avro
D. Parquet

### Q18 | Domain 4 | Compliance | Difficulty: Medium
**Type: Single Answer**

A company must demonstrate that no unauthorized user has accessed specific S3 objects containing financial data in the past 90 days. Which AWS service provides this audit capability?

A. Amazon Macie
B. AWS CloudTrail with data events enabled
C. Amazon GuardDuty
D. AWS Config

### Q19 | Domain 2 | Redshift | Difficulty: Hard
**Type: Single Answer**

A data engineer needs to query data that resides both in Amazon Redshift tables and in S3 (as Parquet files). The S3 data should be joined with Redshift tables without loading it into Redshift. Which feature should be used?

A. Redshift Federated Query
B. Redshift Spectrum
C. Redshift COPY command
D. Redshift materialized views

### Q20 | Domain 1 | ETL | Difficulty: Medium
**Type: Single Answer**

A data engineer has a Glue ETL job that processes 100 GB of data daily. The job takes 4 hours to complete. The team wants to reduce processing time to under 1 hour. Which approach is most effective?

A. Increase the number of DPUs allocated to the Glue job
B. Switch from Glue to Lambda for processing
C. Enable Glue job bookmarks
D. Change the Glue job to use Python Shell instead of Spark

### Q21 | Domain 3 | Event-Driven | Difficulty: Medium
**Type: Single Answer**

A data engineer wants to automatically start a Glue crawler every time new data files are uploaded to a specific S3 prefix. Which approach requires the least custom code?

A. S3 event notification → Lambda → Start Glue crawler
B. EventBridge rule matching S3 PutObject events → Step Functions → Start Glue crawler
C. CloudWatch alarm on S3 bucket size → SNS → Lambda → Start Glue crawler
D. S3 event notification → SQS → Glue crawler

### Q22 | Domain 4 | Encryption | Difficulty: Hard
**Type: Single Answer**

A data engineer is loading data from S3 into Redshift using the COPY command. The S3 data is encrypted with SSE-KMS using a customer managed key. What additional configuration is required for Redshift to read the data?

A. The Redshift cluster IAM role must have kms:Decrypt permission on the KMS key
B. The S3 bucket must have a bucket policy allowing Redshift access
C. The data must be decrypted before loading into Redshift
D. Redshift cannot read SSE-KMS encrypted data

### Q23 | Domain 1 | Batch Processing | Difficulty: Medium
**Type: Single Answer**

A company needs to run complex Apache Spark jobs that require custom libraries, specific Spark configurations, and access to both S3 and HDFS. The team needs full control over the cluster configuration. Which service is most appropriate?

A. AWS Glue ETL
B. Amazon EMR on EC2
C. Amazon Athena for Apache Spark
D. AWS Lambda

### Q24 | Domain 2 | Data Lake | Difficulty: Medium
**Type: Single Answer**

A data engineer is designing a data lake architecture with three zones: raw, processed, and curated. Data flows from raw to processed to curated with increasing levels of transformation and quality. Which S3 organizational approach is recommended?

A. Separate S3 buckets for each zone
B. Single S3 bucket with prefixes for each zone
C. Separate AWS accounts for each zone
D. Both A and C are valid approaches depending on requirements

### Q25 | Domain 3 | Troubleshooting | Difficulty: Hard
**Type: Single Answer**

A Kinesis Data Firehose delivery stream is configured to deliver data to S3. The data engineer notices that some records are being delivered to an S3 error prefix instead of the main prefix. What is the most likely cause?

A. The Firehose buffer size is too large
B. The Lambda transformation function is returning records with a "ProcessingFailed" status
C. The S3 bucket has reached its object limit
D. The Firehose IAM role does not have S3 write permissions

### Q26 | Domain 1 | Schema Management | Difficulty: Medium
**Type: Single Answer**

A data engineer uses AWS Glue Schema Registry to manage schemas for data flowing through Amazon MSK. A producer needs to publish messages with a new schema version that adds a required field. How should the engineer configure the schema registry to prevent breaking existing consumers?

A. Set compatibility mode to BACKWARD
B. Set compatibility mode to FORWARD
C. Set compatibility mode to FULL
D. Set compatibility mode to NONE

### Q27 | Domain 4 | Access Control | Difficulty: Hard
**Type: Single Answer**

A data engineer has configured AWS Lake Formation permissions to grant a data analyst SELECT access on a table. However, the analyst receives an "Access Denied" error when querying the table through Athena. The analyst's IAM policy allows Athena and Glue Data Catalog access. What is the most likely issue?

A. The analyst needs direct S3 read permissions on the underlying data
B. The S3 location is not registered with Lake Formation
C. The analyst needs a Lake Formation data lake administrator role
D. Athena workgroup permissions are blocking the query

### Q28 | Domain 2 | Performance | Difficulty: Medium
**Type: Single Answer**

A data engineer has a Redshift table with 2 billion rows. Queries that filter on a `transaction_date` column are slow. The table uses EVEN distribution. What should the engineer do to improve query performance for date-filtered queries?

A. Change the distribution style to KEY on transaction_date
B. Add transaction_date as a sort key
C. Create a materialized view filtered by recent dates
D. Enable concurrency scaling

### Q29 | Domain 1 | Ingestion | Difficulty: Easy
**Type: Single Answer**

A data engineer needs to load 500 GB of data from S3 into Amazon Redshift as quickly as possible. Which method should be used?

A. INSERT INTO statements using JDBC
B. Redshift COPY command from S3
C. AWS Glue ETL job writing to Redshift
D. Redshift Federated Query from S3

### Q30 | Domain 3 | Automation | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to run a data pipeline every day at 2:00 AM UTC. The pipeline consists of a single Glue ETL job. Which is the simplest approach?

A. AWS Step Functions with a CloudWatch Events schedule
B. Amazon EventBridge scheduled rule targeting the Glue job directly
C. Lambda function triggered by CloudWatch Events that starts the Glue job
D. Glue workflow with a time-based trigger


### Q31 | Domain 4 | Network Security | Difficulty: Medium
**Type: Single Answer**

A data engineer has a Glue ETL job that needs to read data from an RDS PostgreSQL database in a private subnet. The Glue job also needs to write output to S3. What networking configuration is required?

A. The Glue job needs a VPC connection with a NAT gateway for S3 access and security group allowing RDS access
B. The RDS database must be moved to a public subnet
C. A VPN connection between Glue and the VPC is required
D. The Glue job needs a VPC connection with an S3 VPC endpoint and security group allowing RDS access

### Q32 | Domain 1 | Transformation | Difficulty: Easy
**Type: Single Answer**

A data analyst (non-developer) needs to clean and normalize data in S3 without writing code. The tool should provide a visual interface for data preparation. Which AWS service is most appropriate?

A. AWS Glue Studio
B. AWS Glue DataBrew
C. Amazon SageMaker Data Wrangler
D. Amazon QuickSight

### Q33 | Domain 2 | Storage | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to store time-series IoT sensor data that will be queried by device ID and time range. The data volume is 1 TB per day with queries requiring single-digit millisecond latency. Which storage solution is most appropriate?

A. Amazon DynamoDB with device_id as partition key and timestamp as sort key
B. Amazon Redshift with KEY distribution on device_id
C. Amazon S3 with Athena queries
D. Amazon RDS PostgreSQL with partitioning

### Q34 | Domain 3 | Data Quality | Difficulty: Medium
**Type: Single Answer**

A data engineer wants to validate that incoming data meets quality standards before it is loaded into the curated zone of a data lake. The validation should check for null values, data type conformance, and value ranges. Which AWS service provides built-in data quality rules?

A. AWS Glue Data Quality (DQDL)
B. Amazon Macie
C. AWS Config Rules
D. Amazon Inspector

### Q35 | Domain 1 | Streaming | Difficulty: Hard
**Type: Single Answer**

A company processes financial transactions through Kinesis Data Streams. Each transaction must be processed exactly once, and transactions for the same account must be processed in order. How should the data engineer configure the stream?

A. Use the account ID as the partition key and enable enhanced fan-out
B. Use a random partition key for even distribution and use DynamoDB for deduplication
C. Use the account ID as the partition key and implement idempotent processing in the consumer
D. Use Kinesis Data Firehose instead for exactly-once delivery

### Q36 | Domain 2 | Catalog | Difficulty: Medium
**Type: Single Answer**

A data engineer has multiple AWS accounts, each with their own Glue Data Catalog. The company wants to create a centralized data catalog that all accounts can use for Athena queries. Which approach is recommended?

A. Use AWS RAM (Resource Access Manager) to share the Glue Data Catalog across accounts
B. Replicate the Glue Data Catalog to each account using Lambda
C. Use Lake Formation cross-account data sharing
D. Create a central S3 bucket accessible from all accounts

### Q37 | Domain 4 | Governance | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to automatically discover and classify PII (personally identifiable information) in S3 data lake buckets. Which AWS service is purpose-built for this?

A. AWS Glue Data Quality
B. Amazon Macie
C. AWS Lake Formation
D. Amazon Inspector

### Q38 | Domain 1 | ETL | Difficulty: Medium
**Type: Single Answer**

A Glue ETL job reads data from S3, applies transformations, and writes to another S3 location. The job runs daily and should only process files that arrived since the last successful run. The source files are not partitioned by date. Which feature handles this?

A. Glue job bookmarks
B. Glue crawlers with a schedule
C. S3 lifecycle policies
D. S3 Inventory reports

### Q39 | Domain 3 | Operations | Difficulty: Easy
**Type: Single Answer**

A data engineer wants to view the execution history and logs of a Glue ETL job to debug a transformation error. Where should they look?

A. AWS CloudTrail
B. Amazon CloudWatch Logs
C. AWS Glue Data Catalog
D. Amazon S3 server access logs

### Q40 | Domain 2 | Redshift | Difficulty: Hard
**Type: Single Answer**

A data engineer notices that queries joining two large tables in Redshift are slow due to data redistribution during the join. Both tables are frequently joined on the `customer_id` column. What should the engineer do?

A. Change both tables to use KEY distribution on customer_id
B. Change both tables to use ALL distribution
C. Add a sort key on customer_id to both tables
D. Enable concurrency scaling for the query queue

### Q41 | Domain 1 | Ingestion | Difficulty: Medium
**Type: Single Answer**

A company receives data files from external partners via SFTP. The files need to be automatically ingested into S3 for processing. Which AWS service provides managed SFTP capability with S3 integration?

A. AWS DataSync
B. AWS Transfer Family
C. Amazon AppFlow
D. AWS Direct Connect

### Q42 | Domain 4 | Security | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to ensure that a Redshift cluster can only be accessed from within the company's VPC and not from the public internet. Which configuration achieves this?

A. Deploy the Redshift cluster in a private subnet and disable the publicly accessible setting
B. Create an IAM policy that denies access from public IP addresses
C. Enable Redshift encryption with SSE-KMS
D. Configure Redshift enhanced VPC routing

### Q43 | Domain 1 | Streaming | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to deliver streaming data from Kinesis Data Streams to both S3 (for archival) and OpenSearch (for real-time dashboards). Which approach minimizes operational overhead?

A. Create two Kinesis Data Firehose delivery streams, each reading from the Kinesis Data Stream
B. Create a Lambda consumer that writes to both S3 and OpenSearch
C. Create a Kinesis Data Analytics application that writes to both destinations
D. Use Kinesis Data Firehose with S3 as the destination and a Lambda function for OpenSearch

### Q44 | Domain 2 | Data Lake | Difficulty: Hard
**Type: Single Answer**

A data engineer needs to implement ACID transactions on data stored in S3 as part of a data lakehouse architecture. The solution should support time travel and schema evolution. Which approach is recommended on AWS?

A. Use S3 versioning with Glue ETL jobs
B. Use Lake Formation governed tables (Apache Iceberg)
C. Use DynamoDB for transactional data and sync to S3
D. Use Redshift Spectrum with external tables

### Q45 | Domain 3 | Troubleshooting | Difficulty: Hard
**Type: Single Answer**

An AWS Glue ETL job that reads from a JDBC source in a VPC is failing with a connection timeout error. The Glue connection test succeeds. What is the most likely cause?

A. The Glue job's IAM role does not have VPC permissions
B. The security group's inbound rules allow the connection test but the Glue job uses different IP addresses from the subnet
C. The JDBC source database is not running
D. The Glue Data Catalog does not have the table definition

### Q46 | Domain 1 | Transformation | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to deduplicate records in a Glue ETL job. The source data contains duplicate records with the same primary key but different timestamps. The engineer wants to keep only the most recent record for each primary key. Which PySpark approach in Glue is correct?

A. Use the `DropDuplicates` transform on the primary key column
B. Use a Window function to rank by timestamp descending, then filter for rank = 1
C. Use the Glue `ResolveChoice` transform
D. Use the Glue `Filter` transform with a custom condition

### Q47 | Domain 4 | Encryption | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to encrypt data in transit between a Kinesis Data Firehose delivery stream and its S3 destination. Which mechanism provides this?

A. SSE-KMS on the S3 bucket
B. TLS encryption (enabled by default for Firehose to S3)
C. Client-side encryption in the Firehose producer
D. VPC endpoint for S3

### Q48 | Domain 2 | Query | Difficulty: Medium
**Type: Single Answer**

A data engineer has an Athena table partitioned by `year`, `month`, and `day`. The table has 3 years of data (over 1,000 partitions). Queries that filter by date are slow because Athena must look up partition metadata from the Glue Data Catalog. Which feature eliminates this overhead?

A. Athena CTAS
B. Athena partition projection
C. Athena workgroups
D. Athena federated query

### Q49 | Domain 3 | Cost | Difficulty: Medium
**Type: Single Answer**

A data engineer notices that Athena query costs have increased significantly. Investigation reveals that analysts are running full table scans on large datasets. Which TWO actions will reduce costs? (Select TWO)

A. Convert data to columnar format (Parquet or ORC)
B. Set data scan limits per workgroup
C. Enable S3 Intelligent-Tiering
D. Increase Athena query concurrency
E. Move data to Redshift

### Q50 | Domain 1 | ETL | Difficulty: Easy
**Type: Single Answer**

A data engineer needs to run a simple Python script that processes a small CSV file (50 MB) from S3 and writes results back to S3. The script uses pandas and takes about 2 minutes to run. Which is the most cost-effective compute option?

A. AWS Glue ETL job (Spark)
B. AWS Glue Python Shell job
C. Amazon EMR cluster
D. Amazon EC2 instance


### Q51 | Domain 4 | Governance | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to track data lineage across multiple Glue ETL jobs to understand how data flows from raw to curated zones. Which AWS feature provides this capability?

A. AWS CloudTrail
B. AWS Glue Data Catalog lineage
C. Amazon DataZone
D. AWS Lake Formation tag-based access control

### Q52 | Domain 2 | Storage | Difficulty: Medium
**Type: Single Answer**

A data engineer is designing a pipeline where data arrives as small files (1-5 MB each) every minute into S3. Downstream Athena queries are slow due to the large number of small files. What is the best solution?

A. Use S3 Transfer Acceleration to speed up uploads
B. Schedule a periodic Glue ETL job to compact small files into larger files
C. Increase the Athena query timeout
D. Switch from S3 to EBS for storage

### Q53 | Domain 1 | Streaming | Difficulty: Medium
**Type: Single Answer**

A data engineer is configuring Kinesis Data Firehose to deliver data to S3. The business requires that data be available in S3 within 1 minute of being produced. Which Firehose configuration achieves this?

A. Set the buffer interval to 60 seconds and buffer size to 1 MB
B. Set the buffer interval to 300 seconds and buffer size to 128 MB
C. Enable dynamic partitioning with inline parsing
D. Use Kinesis Data Streams instead of Firehose

### Q54 | Domain 3 | Operations | Difficulty: Hard
**Type: Single Answer**

A Step Functions state machine orchestrates a data pipeline. One of the states invokes a Glue ETL job that occasionally fails due to transient errors. The state machine should retry the Glue job up to 3 times with exponential backoff before moving to an error handling state. Which Step Functions feature implements this?

A. Choice state with error checking
B. Retry field with maxAttempts and backoffRate on the Task state
C. Parallel state with error branches
D. Map state with error tolerance

### Q55 | Domain 2 | Redshift | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to provide a team of analysts with a Redshift environment for ad-hoc queries. The workload is unpredictable — sometimes heavy, sometimes idle for days. Cost optimization is the primary concern. Which Redshift option is best?

A. Redshift provisioned cluster with reserved instances
B. Redshift provisioned cluster with on-demand pricing
C. Redshift Serverless
D. Redshift provisioned cluster with concurrency scaling

### Q56 | Domain 1 | Ingestion | Difficulty: Medium
**Type: Single Answer**

A company needs to ingest data from a SaaS application (Salesforce) into S3 on a scheduled basis. The solution should require no custom code. Which AWS service is designed for this?

A. AWS DataSync
B. Amazon AppFlow
C. AWS Transfer Family
D. Amazon Kinesis Data Firehose

### Q57 | Domain 4 | Security | Difficulty: Hard
**Type: Single Answer**

A data engineer has an EMR cluster processing sensitive data. The company's security policy requires that all data in transit between EMR nodes be encrypted. Which configuration achieves this?

A. Enable SSE-KMS on the S3 buckets used by EMR
B. Enable in-transit encryption in the EMR security configuration
C. Use a VPC with private subnets for the EMR cluster
D. Enable EMRFS consistent view

### Q58 | Domain 2 | Data Modeling | Difficulty: Medium
**Type: Single Answer**

A data engineer is designing a Redshift data warehouse for a retail company. The most common query pattern joins a large `orders` fact table with a small `products` dimension table (10,000 rows). What is the optimal distribution strategy?

A. KEY distribution on product_id for both tables
B. KEY distribution on product_id for orders, ALL distribution for products
C. EVEN distribution for both tables
D. ALL distribution for both tables

### Q59 | Domain 3 | Monitoring | Difficulty: Medium
**Type: Single Answer**

A data engineer wants to create a dashboard showing the number of records processed by each Glue ETL job over the past 30 days. Which service should be used to build this dashboard?

A. Amazon QuickSight connected to CloudWatch metrics
B. CloudWatch dashboards with Glue job metrics
C. AWS Glue Studio job monitoring
D. Amazon Managed Grafana

### Q60 | Domain 1 | ETL | Difficulty: Hard
**Type: Single Answer**

A data engineer has a Glue ETL job that processes data from multiple S3 partitions. The job needs to handle schema differences between partitions (some partitions have extra columns). Which Glue feature handles this?

A. Glue job bookmarks
B. Glue DynamicFrame with ResolveChoice
C. Glue crawlers with schema versioning
D. Glue DataBrew recipe

### Q61 | Domain 4 | Compliance | Difficulty: Medium
**Type: Single Answer**

A company must ensure that S3 buckets containing sensitive data are never made publicly accessible. Which AWS service can continuously monitor and automatically remediate public access settings?

A. Amazon Macie
B. AWS Config with auto-remediation rules
C. AWS CloudTrail
D. Amazon GuardDuty

### Q62 | Domain 2 | Lake Architecture | Difficulty: Medium
**Type: Single Answer**

A data engineer is implementing a medallion architecture (bronze/silver/gold) in a data lake. The bronze layer stores raw data, silver stores cleaned data, and gold stores aggregated business-level data. Which data format is most appropriate for the silver and gold layers?

A. JSON
B. CSV
C. Parquet
D. Avro

### Q63 | Domain 1 | Streaming | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to enrich streaming data from Kinesis Data Streams by looking up reference data in DynamoDB before writing to S3. Which approach is most efficient?

A. Kinesis Data Firehose with Lambda transformation that queries DynamoDB
B. Kinesis Data Analytics (Flink) with a DynamoDB lookup
C. Lambda consumer that reads from Kinesis, queries DynamoDB, and writes to S3
D. All of the above are valid; the choice depends on latency and throughput requirements

### Q64 | Domain 3 | Operations | Difficulty: Easy
**Type: Single Answer**

A data engineer wants to schedule a Glue crawler to run every 6 hours. Which is the simplest way to achieve this?

A. Create a Glue trigger with a schedule expression
B. Create an EventBridge rule with a rate expression targeting the crawler
C. Create a Lambda function on a CloudWatch Events schedule
D. Both A and B are equally simple and valid

### Q65 | Domain 4 | Security | Difficulty: Medium
**Type: Single Answer**

A data engineer needs to ensure that Redshift queries accessing S3 data through Spectrum do not traverse the public internet. Which configuration achieves this?

A. Enable Redshift enhanced VPC routing and create an S3 VPC endpoint
B. Enable SSE-KMS encryption on the S3 bucket
C. Create a NAT gateway in the VPC
D. Use S3 Transfer Acceleration

---

## Answer Key

| Q | Answer | Domain | Topic |
|---|---|---|---|
| 1 | B | 1 | Streaming Ingestion |
| 2 | B | 2 | Storage Selection |
| 3 | B | 1 | ETL |
| 4 | C | 4 | Security |
| 5 | B | 3 | Orchestration |
| 6 | A | 1 | Data Transformation |
| 7 | C | 2 | Data Warehouse |
| 8 | C | 4 | Governance |
| 9 | B | 1 | Streaming |
| 10 | B | 3 | Monitoring |
| 11 | B | 1 | Ingestion |
| 12 | A, B | 2 | Query Optimization |
| 13 | A, B | 4 | Security |
| 14 | B | 1 | Streaming |
| 15 | B | 2 | Data Catalog |
| 16 | B | 3 | Operations |
| 17 | C | 1 | Data Formats |
| 18 | B | 4 | Compliance |
| 19 | B | 2 | Redshift |
| 20 | A | 1 | ETL |
| 21 | A | 3 | Event-Driven |
| 22 | A | 4 | Encryption |
| 23 | B | 1 | Batch Processing |
| 24 | D | 2 | Data Lake |
| 25 | B | 3 | Troubleshooting |
| 26 | B | 1 | Schema Management |
| 27 | B | 4 | Access Control |
| 28 | B | 2 | Performance |
| 29 | B | 1 | Ingestion |
| 30 | D | 3 | Automation |
| 31 | D | 4 | Network Security |
| 32 | B | 1 | Transformation |
| 33 | A | 2 | Storage |
| 34 | A | 3 | Data Quality |
| 35 | C | 1 | Streaming |
| 36 | C | 2 | Catalog |
| 37 | B | 4 | Governance |
| 38 | A | 1 | ETL |
| 39 | B | 3 | Operations |
| 40 | A | 2 | Redshift |
| 41 | B | 1 | Ingestion |
| 42 | A | 4 | Security |
| 43 | A | 1 | Streaming |
| 44 | B | 2 | Data Lake |
| 45 | B | 3 | Troubleshooting |
| 46 | B | 1 | Transformation |
| 47 | B | 4 | Encryption |
| 48 | B | 2 | Query |
| 49 | A, B | 3 | Cost |
| 50 | B | 1 | ETL |
| 51 | C | 4 | Governance |
| 52 | B | 2 | Storage |
| 53 | A | 1 | Streaming |
| 54 | B | 3 | Operations |
| 55 | C | 2 | Redshift |
| 56 | B | 1 | Ingestion |
| 57 | B | 4 | Security |
| 58 | B | 2 | Data Modeling |
| 59 | B | 3 | Monitoring |
| 60 | B | 1 | ETL |
| 61 | B | 4 | Compliance |
| 62 | C | 2 | Lake Architecture |
| 63 | D | 1 | Streaming |
| 64 | D | 3 | Operations |
| 65 | A | 4 | Security |


---

## Detailed Explanations

### Q1: B — Kinesis Data Firehose
Firehose is the managed delivery service for streaming data to S3. It requires zero administration and handles buffering, batching, compression, and encryption automatically. **A** works but requires managing a custom consumer (more overhead). **C** works but MSK + Kafka Connect is more complex. **D** Lambda + API Gateway has concurrency limits and isn't designed for 50K events/sec.

### Q2: B — S3 Standard-IA
The data is queried monthly (infrequent access) but needs to be immediately available when queried. Standard-IA is cheaper than Standard for infrequent access. **C** Glacier requires retrieval time (minutes to hours) which doesn't work for Athena queries. **D** Intelligent-Tiering adds monitoring costs that aren't justified for a known access pattern.

### Q3: B — Glue Job Bookmarks
Job bookmarks track which data has been processed, enabling incremental processing. On each run, the job only processes new files. **A** Crawlers discover schemas, they don't control what data is processed. **C** Lambda + S3 events would work but adds complexity. **D** DataBrew is for data preparation, not incremental processing.

### Q4: C — SSE-KMS with Customer Managed Key
Customer managed KMS keys give you full control over key rotation and key policies. CloudTrail automatically logs every KMS API call (Decrypt, Encrypt), providing the audit trail. **A** SSE-S3 doesn't provide audit logging of key usage. **B** AWS managed keys don't allow custom key policies. **D** SSE-C requires managing keys yourself and doesn't integrate with CloudTrail.

### Q5: B — Step Functions
Step Functions provides built-in retry with configurable attempts, backoff, and catch blocks for error handling. It's purpose-built for orchestrating multi-step workflows. **A** EventBridge can trigger jobs but doesn't orchestrate sequential steps with retry logic. **C** Recursive Lambda is an anti-pattern. **D** MWAA works but is overkill for this simple pipeline.

### Q6: A — Athena CTAS
CTAS creates a new table from a SELECT query, allowing format conversion (JSON → Parquet) with partitioning in a single serverless operation. **B** Loading into Redshift just to convert format is wasteful. **C** Custom EC2 is unnecessary overhead. **D** S3 Batch Operations doesn't convert formats.

### Q7: C — ALL Distribution
A 500-row dimension table should use ALL distribution, which copies the entire table to every node. This eliminates data redistribution during joins with the large fact table. **A** KEY distribution on a small table wastes resources. **B** EVEN distribution would require redistribution during joins.

### Q8: C — Lake Formation with Data Filters
Lake Formation data filters provide column-level and row-level security on Glue Data Catalog tables. This is exactly what's needed for hiding PII columns from non-compliance teams. **A** S3 bucket policies can't control column-level access. **B** IAM doesn't support column-level access to data. **D** Macie detects PII but doesn't control access.

### Q9: B — Enhanced Fan-Out
With 3 consumers sharing 10 shards, each shard's 2 MB/s read throughput is split among consumers. Enhanced fan-out provides dedicated 2 MB/s per consumer per shard, eliminating throttling. **A** Adding shards increases cost and doesn't solve the per-shard consumer contention. **C** Firehose is for delivery, not custom processing. **D** Retention doesn't affect throughput.

### Q10: B — EventBridge Rule
EventBridge natively captures Glue job state change events (including failures) and can route them to SNS with the job name and error details. Zero custom code needed. **A** Metric filters require more setup. **C** Adding code to the Glue job is more maintenance. **D** Duration metric doesn't capture failures.

### Q11: B — DMS with CDC
AWS DMS supports full load + Change Data Capture (CDC) for ongoing replication from Oracle to S3. It can output Parquet format. **A** DataSync is for file transfers, not database migration. **C** Transfer Family is for SFTP/FTP. **D** Snow Family is for offline bulk transfer without CDC.

### Q12: A, B — Parquet + Partitioning
Converting to Parquet reduces data scanned (columnar = only read needed columns). Partitioning by date allows Athena to skip irrelevant partitions. Together, these can reduce costs by 90%+. **C** Transfer Acceleration is for uploads, not queries. **D** Glacier can't be queried by Athena. **E** Timeout doesn't reduce cost.

### Q13: A, B — IAM Role + Bucket Policy
Cross-account S3 access requires: (1) an IAM role in the source account with S3 permissions, and (2) a bucket policy on the target bucket allowing that role. **C** VPC peering is for network connectivity, not S3 access. **D** Replication is for copying data, not access. **E** Sharing access keys is a security anti-pattern.

### Q14: B — Kinesis Data Analytics (Flink)
Flink natively supports tumbling windows and can write to DynamoDB. It's designed for real-time stream processing with windowed aggregations. **A** Firehose doesn't support windowed aggregations. **C** Glue Streaming is micro-batch, not true real-time windowing. **D** EMR Spark Streaming works but has more operational overhead.

### Q15: B — Glue Crawler
Crawlers automatically discover schemas from data in S3 and register them in the Glue Data Catalog. This is their primary purpose. **A** ETL jobs transform data, not discover schemas. **C** DataBrew is for data preparation. **D** Workflows orchestrate multiple Glue components.

### Q16: B — Data Skew
Data skew causes some Spark executors to process much more data than others, leading to OOM on the overloaded executors. This can happen when data distribution changes even if total volume doesn't. **A** Redshift being full would cause write errors, not Glue OOM. **C** Catalog size doesn't affect job memory. **D** Versioning doesn't cause OOM.

### Q17: C — Avro
Avro supports schema evolution (adding/removing fields) and embeds the schema with the data. It's the standard format for Kafka/MSK streaming. **A** CSV has no schema. **B** JSON supports schema evolution but is less efficient. **D** Parquet is columnar and better for analytics, not streaming.

### Q18: B — CloudTrail with Data Events
CloudTrail data events log S3 object-level operations (GetObject, PutObject). This provides a complete audit trail of who accessed which objects. **A** Macie detects sensitive data, not access patterns. **C** GuardDuty detects threats, not specific object access. **D** Config tracks resource configuration changes.

### Q19: B — Redshift Spectrum
Spectrum allows Redshift to query external tables in S3 and join them with local Redshift tables. **A** Federated Query is for querying RDS/Aurora from Redshift, not S3. **C** COPY loads data INTO Redshift. **D** Materialized views work on data already in Redshift.

### Q20: A — Increase DPUs
More DPUs = more Spark executors = faster processing. This is the most direct way to reduce Glue job duration. **B** Lambda has a 15-min timeout and 10 GB memory limit — can't handle 100 GB. **C** Bookmarks help with incremental processing, not speed. **D** Python Shell is slower than Spark for large data.

### Q21: A — S3 Event → Lambda → Crawler
S3 event notifications can trigger a Lambda function that starts the Glue crawler. This is the most straightforward event-driven approach. **B** Works but more complex (EventBridge + Step Functions). **C** CloudWatch alarm on bucket size is not event-driven. **D** Glue crawlers can't be directly triggered by SQS.

### Q22: A — kms:Decrypt Permission
When S3 data is encrypted with SSE-KMS, any service reading the data needs kms:Decrypt permission on the KMS key. The Redshift cluster's IAM role must include this. **B** Bucket policy is for S3 access, not KMS. **C** You don't need to manually decrypt. **D** Redshift can read SSE-KMS data with proper permissions.

### Q23: B — EMR on EC2
EMR provides full control over cluster configuration, custom libraries, Spark settings, and access to both S3 (via EMRFS) and HDFS. **A** Glue doesn't provide the same level of customization. **C** Athena Spark is for interactive notebooks, not complex production jobs. **D** Lambda can't run Spark.

### Q24: D — Both Separate Buckets and Separate Accounts
Both approaches are valid. Separate buckets provide logical isolation. Separate accounts provide stronger security boundaries. The choice depends on security requirements, team structure, and governance needs. The exam recognizes both as valid patterns.

### Q25: B — Lambda Processing Failed
When Firehose uses Lambda for transformation, records that the Lambda function marks as "ProcessingFailed" are delivered to the error prefix. This is the most common cause of records in the error prefix. **A** Buffer size doesn't cause errors. **C** S3 has no practical object limit. **D** Missing permissions would fail the entire delivery, not individual records.

### Q26: B — FORWARD Compatibility
FORWARD compatibility means new schemas can be read by old consumers. Adding a required field breaks old consumers (they don't know about the new field). FORWARD compatibility would actually prevent this — the correct answer ensures new schemas are forward-compatible. Note: In practice, adding a required field is a breaking change in most compatibility modes. The exam tests understanding of compatibility directions.

### Q27: B — S3 Location Not Registered
Lake Formation can only manage access to S3 locations that are registered with it. If the underlying S3 location isn't registered, Lake Formation permissions don't apply, and the default IAM-based S3 access is used (which the analyst may not have). **A** With Lake Formation, direct S3 permissions should NOT be needed. **C** Admin role is for managing Lake Formation, not querying. **D** Workgroup permissions are separate.

### Q28: B — Sort Key on transaction_date
A sort key on transaction_date allows Redshift to skip blocks that don't match the date filter (zone maps). This dramatically improves filter performance. **A** KEY distribution on a date column would cause data skew (recent dates get more data). **C** Materialized views help but don't solve the fundamental scan problem. **D** Concurrency scaling is for concurrent queries, not single query performance.

### Q29: B — COPY Command
COPY is the fastest way to load data into Redshift from S3. It parallelizes the load across all compute nodes. **A** INSERT via JDBC is orders of magnitude slower. **C** Glue writing to Redshift uses JDBC under the hood (slower). **D** Federated Query is for querying, not loading.

### Q30: D — Glue Workflow with Time-Based Trigger
Glue workflows support time-based triggers natively, making this the simplest approach for scheduling a single Glue job. **A** Step Functions + CloudWatch is more complex. **B** EventBridge can trigger Glue jobs but requires more configuration. **C** Lambda as a middleman adds unnecessary complexity.

### Q31: D — VPC Connection + S3 VPC Endpoint
Glue needs a VPC connection to access the RDS database. For S3 access from within the VPC, an S3 VPC Gateway endpoint is needed (free). **A** NAT gateway works but costs money — S3 VPC endpoint is free and preferred. **B** Moving RDS to public subnet is a security anti-pattern. **C** VPN is not needed for Glue.

### Q32: B — Glue DataBrew
DataBrew provides a visual, no-code interface for data cleaning and normalization. It's designed for data analysts. **A** Glue Studio is visual but still requires understanding of ETL concepts. **C** SageMaker Data Wrangler is for ML data preparation. **D** QuickSight is for BI, not data preparation.

### Q33: A — DynamoDB
DynamoDB with device_id as partition key and timestamp as sort key provides single-digit millisecond latency for point lookups and range queries. **B** Redshift is for analytics, not low-latency lookups. **C** Athena has query startup latency. **D** RDS can work but DynamoDB is better for this access pattern at scale.

### Q34: A — Glue Data Quality (DQDL)
Glue Data Quality uses DQDL (Data Quality Definition Language) to define rules for null checks, type validation, range checks, and more. It integrates directly with Glue ETL jobs. **B** Macie is for PII detection. **C** Config is for resource compliance. **D** Inspector is for vulnerability scanning.

### Q35: C — Account ID Partition Key + Idempotent Processing
Using account ID as partition key ensures ordering within an account (same partition key → same shard → ordered). Idempotent processing handles the "at-least-once" delivery of Kinesis. **A** Enhanced fan-out helps throughput but doesn't provide exactly-once. **B** Random keys break ordering. **D** Firehose doesn't guarantee exactly-once.

### Q36: C — Lake Formation Cross-Account Sharing
Lake Formation provides native cross-account data sharing with fine-grained permissions. It's the recommended approach for sharing Glue Data Catalog resources across accounts. **A** RAM can share some resources but Lake Formation is more appropriate for data catalog sharing. **B** Replication is complex and not recommended. **D** Central S3 doesn't solve catalog sharing.

### Q37: B — Amazon Macie
Macie uses ML to automatically discover and classify PII and sensitive data in S3. It's purpose-built for this use case. **A** Glue Data Quality validates data rules, not PII detection. **C** Lake Formation manages access, not discovery. **D** Inspector is for vulnerability scanning.

### Q38: A — Job Bookmarks
Job bookmarks track processed files and only process new ones on subsequent runs, regardless of partitioning. **B** Crawlers discover schemas, not track processed files. **C** Lifecycle policies manage storage, not processing. **D** Inventory reports list objects but don't track processing state.

### Q39: B — CloudWatch Logs
Glue ETL jobs write their logs (stdout, stderr, Apache Spark logs) to CloudWatch Logs. This is where you debug transformation errors. **A** CloudTrail logs API calls, not job execution details. **C** Data Catalog stores metadata, not logs. **D** S3 access logs show S3 API calls, not Glue job internals.

### Q40: A — KEY Distribution on customer_id for Both Tables
When two large tables are frequently joined on the same column, using KEY distribution on that column co-locates matching rows on the same node, eliminating data redistribution. **B** ALL distribution on large tables wastes storage. **C** Sort keys help filtering, not join redistribution. **D** Concurrency scaling doesn't improve single query performance.

### Q41: B — AWS Transfer Family
Transfer Family provides managed SFTP, FTPS, and FTP servers with direct S3 integration. Partners upload via SFTP, files land in S3. **A** DataSync is for transferring between storage systems, not SFTP. **C** AppFlow is for SaaS integrations. **D** Direct Connect is a network connection.

### Q42: A — Private Subnet + Disable Public Access
Deploying Redshift in a private subnet and disabling the publicly accessible setting ensures it's only reachable from within the VPC. **B** IAM policies don't control network access. **C** Encryption protects data, not network access. **D** Enhanced VPC routing controls data routing, not access.

### Q43: A — Two Firehose Delivery Streams
Kinesis Data Streams supports multiple consumers. Creating two Firehose delivery streams (one for S3, one for OpenSearch) is the simplest managed approach. **B** Custom Lambda is more code to maintain. **C** KDA is overkill for simple delivery. **D** Single Firehose can only have one primary destination.

### Q44: B — Lake Formation Governed Tables (Iceberg)
Lake Formation governed tables use Apache Iceberg to provide ACID transactions, time travel, and schema evolution on S3 data. **A** S3 versioning doesn't provide ACID transactions. **C** DynamoDB + S3 sync is complex and not a lakehouse pattern. **D** Spectrum doesn't provide ACID.

### Q45: B — Security Group IP Addresses
Glue jobs run on managed infrastructure within your VPC subnet. The connection test may use different IPs than the actual job. If the security group's inbound rules are too restrictive (e.g., allowing only specific IPs), the job may fail while the test succeeds. The fix is to allow the entire subnet CIDR range. **A** VPC permissions are part of the Glue connection, not IAM. **C** If the DB wasn't running, the connection test would also fail. **D** Table definition isn't needed for connectivity.

### Q46: B — Window Function
A Window function (ROW_NUMBER partitioned by primary key, ordered by timestamp DESC) lets you rank records and keep only the most recent. **A** DropDuplicates keeps an arbitrary record, not necessarily the most recent. **C** ResolveChoice handles schema ambiguity, not deduplication. **D** Filter can't implement this logic alone.

### Q47: B — TLS (Default)
Firehose encrypts data in transit to S3 using TLS by default. No additional configuration is needed. **A** SSE-KMS is encryption at rest, not in transit. **C** Client-side encryption is for the producer to Firehose, not Firehose to S3. **D** VPC endpoint is for network routing, not encryption.

### Q48: B — Partition Projection
Partition projection defines partition patterns in the table DDL, allowing Athena to calculate partition locations without querying the Glue Data Catalog. This eliminates metadata lookup overhead for well-structured partition schemes. **A** CTAS creates tables, doesn't optimize partition lookups. **C** Workgroups manage cost/access, not performance. **D** Federated query is for non-S3 sources.

### Q49: A, B — Columnar Format + Workgroup Scan Limits
Columnar formats (Parquet/ORC) reduce data scanned by only reading needed columns. Workgroup scan limits prevent runaway queries. **C** Intelligent-Tiering reduces storage cost, not query cost. **D** Concurrency doesn't reduce per-query cost. **E** Moving to Redshift changes the architecture entirely.

### Q50: B — Glue Python Shell
Python Shell jobs are designed for small-scale processing with pandas/Python libraries. They're much cheaper than Spark jobs for small datasets. **A** Spark job has overhead (DPU minimum) that's wasteful for 50 MB. **C** EMR cluster is massive overkill. **D** EC2 requires management.

### Q51: C — Amazon DataZone
Amazon DataZone provides data lineage tracking across AWS data services. It shows how data flows through pipelines and transformations. **A** CloudTrail logs API calls, not data lineage. **B** Glue Data Catalog stores metadata but limited lineage. **D** LF-TBAC is for access control, not lineage.

### Q52: B — Compact Small Files with Glue
A periodic Glue ETL job can read many small files and write them as fewer, larger files (128-512 MB). This dramatically improves Athena query performance. **A** Transfer Acceleration is for uploads. **C** Timeout doesn't fix the root cause. **D** EBS is block storage, not suitable for data lake.

### Q53: A — Buffer Interval 60s, Size 1 MB
Firehose delivers data when either the buffer interval OR buffer size threshold is reached (whichever comes first). Setting interval to 60 seconds ensures data arrives within 1 minute. **B** 300 seconds = 5 minutes, too slow. **C** Dynamic partitioning doesn't affect delivery timing. **D** Kinesis Streams doesn't deliver to S3 directly.

### Q54: B — Retry Field
Step Functions Task states support a Retry field with maxAttempts, intervalSeconds, and backoffRate for automatic retries with exponential backoff. A Catch field handles the final failure. **A** Choice state is for branching logic. **C** Parallel state runs branches concurrently. **D** Map state processes arrays.

### Q55: C — Redshift Serverless
Serverless automatically scales up/down and you only pay when queries are running. Perfect for unpredictable, bursty workloads. **A** Reserved instances require commitment and payment even when idle. **B** On-demand still requires a running cluster. **D** Concurrency scaling helps with burst queries but still needs a base cluster.

### Q56: B — Amazon AppFlow
AppFlow provides no-code integration with SaaS applications (Salesforce, SAP, Google Analytics, etc.) and can deliver data to S3 on a schedule. **A** DataSync is for storage-to-storage transfers. **C** Transfer Family is for SFTP. **D** Firehose is for streaming data.

### Q57: B — In-Transit Encryption in EMR Security Configuration
EMR security configurations allow enabling in-transit encryption (TLS) for data moving between EMR nodes. **A** SSE-KMS is encryption at rest on S3. **C** Private subnets provide network isolation, not encryption. **D** EMRFS consistent view is for S3 consistency, not encryption.

### Q58: B — KEY for Orders, ALL for Products
The large fact table (orders) should use KEY distribution on the join column (product_id) to distribute data evenly. The small dimension table (products, 10K rows) should use ALL distribution to copy it to every node, eliminating redistribution during joins. **A** KEY on both works but ALL for the small table is more efficient. **C** EVEN causes redistribution. **D** ALL on the large table wastes storage.

### Q59: B — CloudWatch Dashboards
Glue publishes job metrics to CloudWatch. CloudWatch dashboards can visualize these metrics over time. **A** QuickSight is overkill for operational metrics. **C** Glue Studio monitoring shows individual job runs, not historical dashboards. **D** Managed Grafana works but CloudWatch is simpler for AWS-native metrics.

### Q60: B — DynamicFrame with ResolveChoice
Glue DynamicFrames handle schema inconsistencies natively. ResolveChoice resolves ambiguous types when schemas differ across partitions. **A** Bookmarks track processed data, not schema differences. **C** Crawlers detect schemas but don't resolve conflicts during ETL. **D** DataBrew is for data preparation, not schema resolution.

### Q61: B — AWS Config with Auto-Remediation
AWS Config can monitor S3 bucket configurations and automatically remediate public access settings using Lambda or SSM Automation. **A** Macie detects sensitive data, not configuration compliance. **C** CloudTrail logs events but doesn't remediate. **D** GuardDuty detects threats but doesn't auto-remediate S3 settings.

### Q62: C — Parquet
Parquet is the standard columnar format for analytical workloads. It provides excellent compression, column pruning, and predicate pushdown — ideal for the silver and gold layers where data is queried frequently. **A** JSON is inefficient for analytics. **B** CSV lacks types and compression. **D** Avro is row-based, better for streaming/ingestion.

### Q63: D — All Valid
All three approaches work. The choice depends on requirements: Firehose+Lambda for simple enrichment with S3 delivery, Flink for complex real-time processing, Lambda consumer for custom logic. The exam sometimes has "all of the above" as the correct answer when multiple approaches are valid.

### Q64: D — Both A and B
Glue triggers with schedule expressions and EventBridge rules with rate expressions are both simple, native ways to schedule a crawler. Neither requires custom code. **C** Lambda as a middleman adds unnecessary complexity.

### Q65: A — Enhanced VPC Routing + S3 VPC Endpoint
Enhanced VPC routing forces all Redshift traffic (including Spectrum queries to S3) through the VPC. Combined with an S3 VPC Gateway endpoint, traffic stays within the AWS network and never traverses the public internet. **B** Encryption protects data content, not routing. **C** NAT gateway routes through the internet. **D** Transfer Acceleration is for uploads.

---

## Score Interpretation

| Score | Interpretation | Action |
|---|---|---|
| 80-100% (52-65 correct) | Excellent — likely ready to pass | Light review, focus on any missed topics |
| 70-79% (46-51 correct) | Good — on track but review weak areas | Targeted study on missed domains |
| 60-69% (39-45 correct) | Borderline — need more preparation | Focus on high-weight domains (1 and 2) |
| Below 60% (< 39 correct) | Not ready — need significant study | Review service primer, retake after more study |

### Domain Score Breakdown
Count your correct answers per domain:
- **Domain 1** (Ingestion & Transformation): Q1, 3, 6, 9, 11, 14, 17, 20, 23, 26, 29, 35, 38, 41, 43, 46, 50, 53, 56, 60, 63 = 21 questions
- **Domain 2** (Data Store Management): Q2, 7, 15, 19, 24, 28, 33, 36, 40, 44, 48, 52, 55, 58, 62 = 15 questions
- **Domain 3** (Operations & Support): Q5, 10, 16, 21, 25, 30, 34, 39, 45, 49, 54, 59, 64 = 13 questions
- **Domain 4** (Security & Governance): Q4, 8, 12, 13, 18, 22, 27, 31, 37, 42, 47, 51, 57, 61, 65 = 16 questions (note: Q12 and Q13 are multi-answer)
