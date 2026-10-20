# Mock Exam 1 — Part 1 (Questions 1–22)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q1

A retail company streams about 12,000 records per second (about 18 MB/s in total) into Amazon Kinesis Data Streams. Three independent applications (fraud detection, a real-time dashboard, and an archiver) must each read the full stream with low latency and without slowing each other down. Traffic varies widely during promotions, and the team wants to avoid capacity planning.
Which solution meets these requirements with the LEAST operational overhead?

A. A provisioned stream with 18 shards; all three applications use shared-throughput GetRecords polling.  
B. A stream in on-demand capacity mode; register each application as an enhanced fan-out consumer.  
C. An Amazon Data Firehose stream with three delivery destinations.  
D. An Amazon MSK Serverless cluster with one consumer group shared by the three applications.  

### Q2

A company stores audit logs in Amazon S3. The logs are read frequently for the first 30 days, then accessed roughly once per quarter, but any read must return in milliseconds. Logs must be kept 5 years and then deleted. The company wants to minimize storage cost.
Which S3 Lifecycle configuration should be used?

A. Store in S3 Intelligent-Tiering and enable the Archive Access and Deep Archive Access tiers; expire after 5 years.  
B. Transition to S3 Glacier Flexible Retrieval after 30 days; expire after 5 years.  
C. Transition to S3 One Zone-IA after 30 days; expire after 5 years.  
D. Transition to S3 Glacier Instant Retrieval after 30 days; expire after 5 years.  

### Q3

An AWS Lambda function processes records from a Kinesis data stream. One malformed record makes the function throw an error. The same batch is retried repeatedly and processing of that shard stalls until the record expires.
What should a data engineer do to isolate the bad record and keep the shard moving?

A. Enable BisectBatchOnFunctionError, set a maximum retry attempts value, and configure an on-failure destination (an SQS queue).  
B. Double the number of shards in the stream.  
C. Increase the function timeout to 15 minutes.  
D. Register the function as an enhanced fan-out consumer.  

### Q4

An S3 bucket in account A is encrypted with SSE-KMS using a customer managed key (CMK) in account A. A bucket policy already allows an IAM role in account B to call s3:GetObject. Reads by the role fail with an AccessDenied error from AWS KMS.
Which TWO actions are required to fix this? (Select TWO.)

A. Change the bucket encryption to the AWS managed key aws/s3.  
B. Add a statement to the CMK key policy allowing the account B role to use kms:Decrypt.  
C. Create a KMS grant in account B for the S3 service principal.  
D. Attach an IAM policy to the account B role allowing kms:Decrypt on the CMK ARN.  
E. Enable automatic key rotation on the CMK.  

### Q5

An AWS Glue Spark job joins two large tables on customer_id. One customer_id accounts for about 60% of rows. A few executors run out of memory while the rest sit idle, and the job takes hours.
Which change MOST directly addresses the root cause?

A. Double the number of G.1X workers.  
B. Enable job bookmarks.  
C. Add a random salt to the skewed key (for example key + salt) and join/aggregate in two stages.  
D. Switch the job to the Flex execution class.  

### Q6

A pipeline must run an AWS Glue job, then an Athena query, then a Lambda function that publishes a notification. Steps need retries with backoff and failure branching. The team wants a serverless solution with the LEAST operational overhead.
Which service should orchestrate the pipeline?

A. Amazon MWAA with an Airflow DAG.  
B. AWS Glue workflows.  
C. Chained Amazon EventBridge rules.  
D. AWS Step Functions with service integrations (.sync for Glue and Athena).  

### Q7

A Redshift cluster stores an orders fact table (about 2 billion rows) and a customers table (about 500 million rows). They are joined constantly on customer_id. Queries show large data redistribution (DS_DIST_BOTH) steps.
Which table design change will MOST improve join performance?

A. Set DISTSTYLE KEY with DISTKEY(customer_id) on both tables.  
B. Set DISTSTYLE ALL on the customers table.  
C. Set DISTSTYLE EVEN on both tables.  
D. Set DISTSTYLE ALL on the orders table.  

### Q8

A company receives 2 TB of CSV files in S3 each day. A daily job must apply custom PySpark transformations, join the data with a reference table in an Amazon RDS for PostgreSQL database, and write partitioned Parquet files. The team does not want to manage clusters.
Which solution is MOST appropriate?

A. An AWS Lambda function triggered on a schedule.  
B. A long-running Amazon EMR cluster on EC2.  
C. An AWS Glue Spark job with a JDBC connection, started by a scheduled trigger.  
D. An Amazon Athena CTAS query.  

### Q9

An Athena table over 10 TB of JSON logs in S3 is queried daily with filters on event_date. Query costs and runtime are high because each query scans most of the data.
Which action will reduce both cost and runtime the MOST?

A. Increase the DML query timeout.  
B. Use CTAS to rewrite the data as Parquet with Snappy compression partitioned by event_date.  
C. Spread the JSON files across more S3 prefixes.  
D. Enable query result reuse.  

### Q10

Analysts query a customers table through Amazon Athena. The table is registered in the AWS Glue Data Catalog and stored in S3. Analysts must see all columns except ssn, while the data science role must see all columns. The company wants centrally managed, auditable permissions with the LEAST operational overhead.
Which solution meets this requirement?

A. An S3 bucket policy that denies analysts access to objects containing ssn.  
B. An IAM policy that denies analysts glue:GetTable on the table.  
C. A second copy of the table without ssn in a separate bucket, maintained by a nightly job.  
D. Register the S3 location with AWS Lake Formation and grant analysts SELECT on the table with the ssn column excluded.  

### Q11

A company runs Apache Kafka on premises with Kafka Streams and Kafka Connect applications. It wants to move to AWS and keep the existing producers and consumers with minimal code changes.
Which service should the company choose?

A. Amazon MSK.  
B. Amazon Kinesis Data Streams.  
C. Amazon Data Firehose.  
D. Amazon SQS.  

### Q12

An application needs two access patterns on an orders dataset in Amazon DynamoDB: (1) list all orders for a customer, newest first; (2) fetch one order by order ID. Both must be efficient and avoid scans.
Which table design satisfies both?

A. Partition key orderId with a local secondary index on customerId.  
B. Partition key customerId, sort key orderDate, and a global secondary index with partition key orderId.  
C. Partition key customerId, sort key orderDate; use a Scan with a filter for orderId lookups.  
D. Partition key orderDate and sort key customerId.  

### Q13

Application events arrive as JSON and must be delivered in near real time to Amazon S3 as Parquet files, with no custom code and minimal operations.
Which solution meets these requirements?

A. Kinesis Data Streams with a Lambda function writing Parquet to S3.  
B. An EMR cluster running Spark Structured Streaming.  
C. AWS Glue crawlers scheduled every minute.  
D. Amazon Data Firehose with record format conversion to Parquet using an AWS Glue table schema.  

### Q14

At the start of each business hour, many analysts open dashboards that run short queries on an Amazon Redshift provisioned cluster. Queries queue for minutes during these bursts and are fast the rest of the day.
Which approach addresses this with the LEAST effort and cost?

A. Enable concurrency scaling with automatic workload management.  
B. Double the number of nodes permanently.  
C. Convert all tables to DISTSTYLE ALL.  
D. Move the data to Amazon RDS.  

### Q15

A nightly ETL job writes to a DynamoDB table in provisioned capacity mode. Bursts of writes from unpredictable sources cause ProvisionedThroughputExceededException. The team wants the LEAST operational overhead.
What should the data engineer do?

A. Increase the table read capacity units.  
B. Add DynamoDB Accelerator (DAX).  
C. Switch the table to on-demand capacity mode and keep retries with exponential backoff.  
D. Add a local secondary index.  

### Q16

A company wants to run row-level updates and deletes on data in its S3 data lake using Athena and to query the data as it looked last week. The company is evaluating Apache Iceberg tables.
Which TWO capabilities do Iceberg tables provide for this? (Select TWO.)

A. ACID row-level operations such as MERGE and DELETE.  
B. Automatic B-tree indexing of every column.  
C. Elimination of the need for any metadata or catalog.  
D. Snapshot-based time travel.  
E. Enforced foreign key constraints.  

### Q17

An AWS Glue job connects to an Amazon RDS database using a password that security policy requires to be rotated every 30 days without code changes or job downtime.
Which solution meets this requirement?

A. Store the password in a Glue job parameter and update it manually.  
B. Store the credentials in AWS Secrets Manager with automatic rotation, and reference the secret in the Glue connection.  
C. Store the password in an S3 object encrypted with SSE-S3.  
D. Embed the password in the script and rotate by redeploying.  

### Q18

A partner uploads a daily file to an S3 bucket at an unpredictable time. After the file arrives, a Glue crawler and then a Glue job must run exactly once. The solution should be serverless and avoid polling.
Which design is MOST appropriate?

A. A Glue trigger that runs the crawler every hour.  
B. A Lambda function on a one-minute schedule that lists the bucket.  
C. A Glue crawler scheduled to run continuously.  
D. An S3 event to Amazon EventBridge that starts a Step Functions state machine to run the crawler and job.  

### Q19

A team wants to be alerted when a consumer application falls behind processing a Kinesis data stream.
Which approach is the MOST direct?

A. A CloudWatch alarm on WriteProvisionedThroughputExceeded, notifying an SNS topic.  
B. A CloudWatch alarm on GetRecords.IteratorAgeMilliseconds, notifying an SNS topic.  
C. A CloudWatch alarm on IncomingBytes.  
D. A CloudTrail trail on GetRecords API calls.  

### Q20

An Amazon Redshift cluster holds 5 years of sales data. Data older than 1 year is rarely queried but must remain queryable with SQL. The company wants to cut storage cost.
Which TWO actions should be taken? (Select TWO.)

A. Add more compute nodes.  
B. Change all tables to DISTSTYLE EVEN.  
C. UNLOAD the old data to Amazon S3 in Parquet format.  
D. DELETE the old rows and run VACUUM only.  
E. Create an external schema and tables so Redshift Spectrum can query the S3 data.  

### Q21

An SQS queue triggers a Lambda function that writes to an Amazon RDS for MySQL database. During backlogs Lambda scales out and exhausts the database's connection limit.
Which change BEST protects the database?

A. Increase the function memory.  
B. Set a maximum concurrency on the SQS event source mapping (and use RDS Proxy for connection pooling).  
C. Convert to a FIFO queue.  
D. Increase the queue visibility timeout.  

### Q22

AWS Glue jobs run in a private subnet with no internet route. The jobs must read and write S3 data at the LOWEST cost.
What should be configured?

A. An S3 gateway VPC endpoint associated with the subnet route table.  
B. A NAT gateway in a public subnet.  
C. An internet gateway attached to the VPC.  
D. An interface VPC endpoint for AWS Glue only.  
