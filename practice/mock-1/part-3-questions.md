# Mock Exam 1 — Part 3 (Questions 45–65)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q45

A Java-based Lambda function that enriches records suffers cold-start latency every weekday morning at 08:00 when traffic jumps. The traffic pattern is predictable. The team wants consistent low latency.
What should the data engineer do?

A. Increase the function timeout so initialization has more time.  
B. Set reserved concurrency to 1 so the same environment is reused.  
C. Provisioned concurrency with scheduled scaling just before 08:00.  
D. Move the function code into a Lambda layer to shrink the package.  

### Q46

A company runs Apache Cassandra on premises and uses CQL. It wants a serverless managed database on AWS with minimal application changes.
Which service should it use?

A. Amazon Keyspaces (for Apache Cassandra).  
B. Amazon DocumentDB (with MongoDB compatibility).  
C. Amazon Neptune, a graph database service.  
D. Amazon MemoryDB, a durable Redis-compatible database.  

### Q47

An AWS Glue ETL job loads customer data into a curated zone. The team wants the job to stop and alert when more than 5% of order_id values are null, so bad data is never published.
What should the data engineer do?

A. Run a Glue crawler after the job to check the schema of the curated data.  
B. Enable job bookmarks so the job tracks which records were already loaded.  
C. An Evaluate Data Quality step with Completeness "order_id" > 0.95 that fails the job on failure.  
D. Increase the worker type so the job finishes before bad data is published.  

### Q48

A company has dozens of existing Apache Airflow DAGs that run on premises. It wants to move them to AWS with minimal rewriting and without managing Airflow servers.
Which service should it choose?

A. AWS Step Functions with state machines translated from each DAG.  
B. AWS Glue workflows built from the existing task definitions.  
C. Amazon EventBridge Scheduler invoking each task on a cron schedule.  
D. Amazon Managed Workflows for Apache Airflow (MWAA).  

### Q49

A Lambda function runs in a private subnet with no NAT gateway and must write records to Kinesis Data Streams without traversing the internet.
What should be created?

A. A gateway VPC endpoint for Kinesis added to the subnet route table.  
B. An interface VPC endpoint (AWS PrivateLink) for Kinesis Data Streams.  
C. An internet gateway with a route from the private subnet.  
D. A site-to-site VPN connection between the VPC and the Kinesis service.  

### Q50

A team wants analytics tables in Apache Iceberg format on S3 with automatic compaction and snapshot management, and wants the LEAST operational overhead.
Which option is BEST?

A. Self-managed Iceberg tables with a scheduled Glue compaction job.  
B. Parquet files in S3 Standard with a crawler.  
C. Amazon S3 Tables (table buckets).  
D. Amazon DynamoDB with exports.  

### Q51

A Spark job reads one 50 GB gzip-compressed CSV file and runs for hours using only one executor.
What is the BEST fix?

A. Have the source deliver multiple smaller files, or convert to Parquet, so Spark can parallelize.  
B. Add more workers so that the single file is split across more executors.  
C. Switch from gzip to a different gzip compression level that can be split.  
D. Increase the driver memory so the file can be read by the driver faster.  

### Q52

A Redshift COPY of a single 50 GB uncompressed file from S3 into a 16-slice cluster is very slow and uses one slice.
How should the load be improved?

A. Move to a larger node type so the single file loads faster on one slice.  
B. Split the data into multiple compressed files (a multiple of the slice count) and COPY from the prefix.  
C. Load the rows with INSERT statements, which run in parallel across slices.  
D. Disable compression encodings on the table to speed up the load.  

### Q53

An S3 bucket encrypted with SSE-KMS receives very high request volumes. The company sees KMS request throttling and rising KMS costs.
What should be done?

A. Switch to SSE-C.  
B. Create more KMS keys with the same alias.  
C. Disable encryption.  
D. Enable S3 Bucket Keys for SSE-KMS.  

### Q54

An S3 bucket has versioning enabled. Storage costs keep growing because of overwritten object versions that are never needed after 30 days.
What should be configured?

A. Disable versioning on the bucket so old versions are removed.  
B. A lifecycle rule that expires noncurrent versions after 30 days.  
C. Enable S3 Object Lock in compliance mode on the bucket.  
D. Enable Cross-Region Replication to keep the old versions elsewhere.  

### Q55

A Glue job must run every day at 02:00 India Standard Time without manually converting for daylight changes.
Which scheduling option is BEST?

A. EventBridge Scheduler with the Asia/Kolkata time zone, starting the job or a state machine.  
B. An EventBridge rule with a cron expression written in local India time.  
C. A Lambda function that computes the offset from UTC before starting the job.  
D. A cron job on an EC2 instance configured with the IST time zone.  

### Q56

During business hours, many concurrent Athena queries return TooManyRequestsException because active DML query quotas (including queued queries) are exceeded. The workload is predictable and heavy.
What is the BEST solution?

A. Increase the DML query timeout so queued queries are not cancelled.  
B. Add more S3 prefixes so Athena can read the tables with more parallelism.  
C. Create an Athena capacity reservation and assign the workgroup to it.  
D. Convert the tables to CSV so the queries need fewer resources.  

### Q57

A Glue job must read objects under s3://lake/raw/ and write objects under s3://lake/curated/ only.
Which IAM policy design follows least privilege?

A. s3:GetObject on lake/raw/*, s3:PutObject on lake/curated/*, and s3:ListBucket scoped by prefix.  
B. s3:* on all resources, so the job never fails with AccessDenied.  
C. The AmazonS3FullAccess managed policy attached to the job role.  
D. The AdministratorAccess managed policy attached to the job role.  

### Q58

A company wants to ingest Salesforce objects into S3 daily with no custom code.
Which service is MOST suitable?

A. AWS DataSync.  
B. AWS Snowball Edge.  
C. AWS Transfer Family.  
D. Amazon AppFlow.  

### Q59

A DynamoDB table has a hot partition because most writes target a few partition key values.
Which TWO changes reduce the hot partition? (Select TWO.)

A. Choose a partition key with high cardinality that spreads requests evenly.  
B. Place DAX in front of the table to absorb writes.  
C. Add a random or calculated suffix to hot keys (write sharding).  
D. Add a local secondary index.  
E. Increase only the read capacity units.  

### Q60

Analysts need a 7-day rolling average of daily_sales for each store in Athena.
Which query pattern is correct?

A. SELECT store, day, AVG(daily_sales) FROM t GROUP BY store, day ORDER BY day  
B. SELECT store, day, RANK() OVER (PARTITION BY store ORDER BY daily_sales) FROM t  
C. SELECT store, day, SUM(daily_sales) OVER (PARTITION BY store ORDER BY day) / 7 FROM t  
D. SELECT store, day, AVG(daily_sales) OVER (PARTITION BY store ORDER BY day ROWS 6 PRECEDING) FROM t  

### Q61

A company must ensure all data written to an S3 bucket is encrypted in transit and at rest.
Which TWO actions should be implemented? (Select TWO.)

A. A bucket policy that denies requests when aws:SecureTransport is false.  
B. Enable S3 Transfer Acceleration.  
C. Enable default bucket encryption with SSE-KMS.  
D. Enable MFA delete.  
E. Enable Requester Pays.  

### Q62

Events flow continuously through Kinesis Data Streams. The team needs micro-batch transformations with Spark and writes into an Apache Iceberg table in S3, without managing clusters.
What should be used?

A. A Glue batch job scheduled every minute.  
B. An AWS Glue streaming ETL job.  
C. An Athena query run on a schedule.  
D. A Lambda function per record.  

### Q63

A company wants a business data catalog with a glossary, published data products, subscription approval workflows, and lineage across project teams.
Which AWS capability fits BEST?

A. Amazon SageMaker Catalog in SageMaker Unified Studio.  
B. The AWS Glue Data Catalog with Lake Formation permissions.  
C. AWS CloudTrail with an organization trail.  
D. AWS Config with conformance packs.  

### Q64

The team wants an email whenever a production Glue job fails or times out.
What is the MOST direct way?

A. A daily Athena query over the job logs that emails the failed runs.  
B. A Glue console check each morning by the on-call engineer.  
C. An EventBridge rule on Glue Job State Change events (FAILED, TIMEOUT) that publishes to SNS.  
D. A CloudTrail Insights event that notifies the team on unusual Glue API calls.  

### Q65

A financial company wants to detect fraud rings by traversing relationships among accounts, devices, and addresses.
Which database is the BEST fit?

A. Amazon DynamoDB.  
B. Amazon Redshift.  
C. Amazon DocumentDB.  
D. Amazon Neptune.  
