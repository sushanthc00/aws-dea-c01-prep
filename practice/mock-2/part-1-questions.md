# Mock Exam 2 — Part 1 (Questions 1–22)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q1

Application events arrive in Amazon Data Firehose as JSON, each containing a customer_id. Delivery to S3 must be organized under prefixes such as customer_id=123/, with the LEAST custom infrastructure.
What should the data engineer configure?

A. A Lambda function that writes each record to its own S3 object under a customer prefix.  
B. An AWS Glue job that repartitions the delivered data by customer_id every hour.  
C. Firehose dynamic partitioning, extracting customer_id from each record to build the S3 prefix.  
D. A separate Firehose delivery stream for each customer, each with its own S3 prefix.  

### Q2

A producer sends 6,000 records per second to a provisioned Kinesis data stream. Each record is 500 bytes (about 3 MB/s total). How many shards are required for the write side?

A. 6  
B. 3  
C. 12  
D. 2  

### Q3

A data lake holds millions of objects (each larger than 128 KB) in S3 Standard. Access patterns are unknown and change unpredictably. The company wants lower storage cost with no retrieval fees and no lifecycle tuning.
Which option is BEST?

A. Transition everything to S3 Glacier Flexible Retrieval.  
B. Transition everything to S3 One Zone-IA.  
C. Transition to S3 Standard-IA after 30 days.  
D. Use S3 Intelligent-Tiering.  

### Q4

An AWS Glue job in account A must read from an S3 bucket in account B. The job's role in account A already has an IAM policy allowing s3:GetObject on the bucket.
What additional step is required?

A. Add the Glue service principal glue.amazonaws.com to the bucket policy in account B.  
B. Add a bucket policy in account B that allows the Glue job role in account A to read the bucket.  
C. Create IAM users in account B and give their access keys to the Glue job in account A.  
D. Enable S3 Transfer Acceleration on the bucket so the cross-account request is accepted.  

### Q5

A critical Lambda function is intermittently throttled (HTTP 429) because another function in the same account consumes most of the Region's 1,000 concurrent executions. The critical function must always be able to run.
What should the engineer do?

A. Configure reserved concurrency for the critical function.  
B. Increase the critical function's memory so that it finishes sooner and frees concurrency.  
C. Increase the other function's timeout so that it releases environments more gradually.  
D. Place the critical function in a VPC so that it has its own pool of concurrency.  

### Q6

A workflow processes 100,000 short events per second. Each execution takes under 30 seconds and the steps are idempotent. The company wants the lowest cost per execution with Step Functions.
Which workflow type should be used?

A. Standard workflows.  
B. A Standard workflow with Distributed Map.  
C. Glue workflows.  
D. Express workflows.  

### Q7

A large Redshift fact table is frequently filtered by a date range. The same aggregation query is run repeatedly by dashboards.
Which TWO actions improve performance? (Select TWO.)

A. Set DISTSTYLE ALL on the fact table.  
B. Define the date column as the sort key.  
C. Create an interleaved sort key on every column.  
D. Reduce the cluster to a single node.  
E. Create a materialized view for the repeated aggregation.  

### Q8

Changes in an Amazon RDS for MySQL database must be replicated continuously into an S3 data lake as Parquet, with minimal operations and no custom code.
Which solution is BEST?

A. A scheduled Lambda function that exports the changed tables to S3 every few minutes.  
B. AWS DMS with full load plus CDC, using S3 as the target with Parquet format.  
C. An EMR cluster that runs Sqoop imports into S3 on a schedule.  
D. An AWS DataSync task that copies the database files to the S3 bucket.  

### Q9

A nightly EMR Spark job can tolerate node loss but must not lose data. The company wants the lowest cost.
Which cluster configuration is BEST?

A. All Spot Instances, including the primary and core nodes, to maximize savings.  
B. All On-Demand Instances, with a Savings Plan covering the whole cluster.  
C. On-Demand primary and core nodes, with Spot Instances for the task nodes.  
D. A single large node that runs the primary, core and task roles together.  

### Q10

A company wants to crawl and catalog tables in an on-premises PostgreSQL database reachable over AWS Direct Connect from a VPC.
What should the data engineer create?

A. A Glue JDBC connection configured with VPC, subnet and security group, used by a crawler.  
B. An S3 event notification that starts a crawler when the database changes.  
C. A Kinesis data stream that carries the database schema to the Glue Data Catalog.  
D. A Lake Formation LF-tag on the database that lets the crawler reach the source.  

### Q11

A Lambda function consumes a Kinesis stream with 4 shards. The function is fast but the GetRecords.IteratorAgeMilliseconds metric keeps rising during peaks. The team wants more throughput without resharding.
What should be changed?

A. Increase the function's memory only, because its code already runs fast enough.  
B. Increase the event source mapping's ParallelizationFactor (up to 10 batches per shard).  
C. Disable batching so that each record is processed by its own invocation.  
D. Reduce the batch size to 1 so that each invocation finishes sooner.  

### Q12

Analysts must read only tables in the sales schema of a Redshift cluster. Permissions should be managed for groups of users, not individually.
What should the administrator do?

A. Grant the analysts the Redshift superuser privilege so that they can read every schema.  
B. Make the sales schema public so that all database users can query it.  
C. Create a Redshift role, grant schema USAGE and table SELECT to it, and assign the users.  
D. Create one shared database user for the analysts and distribute its password.  

### Q13

A data transformation is a custom Python container that runs for about 6 hours per batch. The team wants a serverless way to run it as part of a Step Functions workflow.
Which solution is BEST?

A. An Amazon ECS task on AWS Fargate, started through the Step Functions .sync integration.  
B. An AWS Lambda function with the maximum memory and timeout settings.  
C. An EC2 instance that is left running and polls a queue for new batches.  
D. An API Gateway endpoint that triggers the container on each request.  

### Q14

Application logs must be searchable within seconds with dashboards, and the team accepts managing index retention.
Which pipeline is BEST?

A. Logs written to S3 and queried with Athena whenever someone needs to search.  
B. Logs loaded into Redshift through a nightly COPY job and queried there.  
C. Logs written to a DynamoDB table indexed by timestamp.  
D. Logs streamed through Amazon Data Firehose into Amazon OpenSearch Service.  

### Q15

A DynamoDB table must be restorable to any second within the last 35 days after accidental deletes.
Which feature should be enabled?

A. DynamoDB Streams.  
B. Point-in-time recovery (PITR).  
C. DynamoDB Accelerator (DAX).  
D. Global tables.  

### Q16

Multiple producers publish Avro events to Kinesis Data Streams. The schema changes over time, and consumers must not break. The team wants schema versioning and compatibility checks.
Which service should be used?

A. AWS Glue crawlers.  
B. Amazon Macie.  
C. AWS Glue Schema Registry.  
D. AWS Config.  

### Q17

A company must share Glue Data Catalog tables governed by Lake Formation with a different AWS account.
Which TWO steps are required? (Select TWO.)

A. Make the S3 bucket public.  
B. Email the table files to the other team.  
C. In the owner account, grant Lake Formation permissions on the tables to the other account.  
D. In the recipient account, create resource links to the shared tables and grant Lake Formation permissions to its principals.  
E. Replicate the S3 bucket to the recipient account.  

### Q18

An analyst wants to join data in S3 with a table in Amazon RDS for MySQL using Athena, without copying the RDS data.
What should be used?

A. A Glue crawler that catalogs the RDS tables so they appear next to the S3 data.  
B. A Redshift UNLOAD of the RDS table into S3 before each query.  
C. An S3 Select query over the exported RDS table.  
D. Athena federated query with a data source connector (Lambda).  

### Q19

Each salesperson viewing an Amazon Quick (QuickSight) dashboard must see only the rows for their own region.
Which feature is BEST?

A. Row-level security with a permissions dataset that maps users to regions.  
B. A separate dashboard for each salesperson with its own filter.  
C. Share the dashboard publicly and rely on a region filter control.  
D. Column-level security that hides the other regions' columns.  

### Q20

A non-urgent nightly Glue job can start up to several hours late. The company wants to reduce its cost.
Which option should be used?

A. Increase the number of workers.  
B. The Flex execution class.  
C. Provisioned capacity.  
D. Switch the job to Python shell.  

### Q21

Streaming writes create thousands of small files in an Apache Iceberg table queried with Athena, and queries are slowing.
What should the engineer do?

A. Convert the table to CSV so the many small files are easier to read.  
B. Drop and recreate the table every day from the raw data.  
C. Schedule table compaction (for example Athena OPTIMIZE ... BIN_PACK or S3 Tables maintenance).  
D. Add more partitions by minute so each query reads fewer files.  

### Q22

Security analysts want to run SQL queries on CloudTrail events across the whole organization without building any infrastructure.
Which feature should be used?

A. AWS CloudTrail Lake event data stores.  
B. A custom Hadoop cluster reading log files.  
C. CloudWatch dashboards.  
D. Amazon Macie.  
