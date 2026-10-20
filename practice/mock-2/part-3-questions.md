# Mock Exam 2 — Part 3 (Questions 45–65)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q45

A nightly job calls a paginated third-party REST API, takes about 40 minutes, and writes JSON to S3. The team wants the simplest serverless scheduled solution.
Which option is BEST?

A. A single Lambda function that runs for 40 minutes.  
B. An EC2 instance with cron.  
C. An EMR cluster.  
D. An AWS Glue Python shell job started by a schedule.  

### Q46

A Spark job in AWS Glue reads a very large table from Amazon RDS for PostgreSQL over JDBC and is slow because a single connection reads all rows.
How can read performance be improved?

A. Configure a partitioned JDBC read (partition column with lower and upper bounds, or Glue hashfield/hashpartitions) for parallel reads.  
B. Add more workers without changing the read.  
C. Convert the job to a Python shell job.  
D. Disable the JDBC connection.  

### Q47

A team wants to build a retrieval-augmented generation (RAG) application where documents in S3 are chunked, embedded, stored in a vector store, and retrieved for prompts, with minimal custom code.
Which service is BEST?

A. Amazon Redshift.  
B. Amazon Bedrock Knowledge Bases.  
C. AWS Glue DataBrew.  
D. Amazon Kinesis Data Firehose.  

### Q48

An EMR Spark step failed, and the cluster was terminated before engineers could inspect the YARN and Spark logs.
What should be configured to prevent this problem?

A. A larger instance type.  
B. EMR managed scaling.  
C. A cluster log URI (log archiving) to an S3 bucket.  
D. A smaller block size.  

### Q49

Jobs in a VPC use an S3 gateway endpoint. Security wants to ensure traffic through the endpoint can reach only the company's data lake buckets.
What should be configured?

A. A security group on the S3 endpoint.  
B. A VPC endpoint policy that allows only the company's buckets.  
C. An S3 lifecycle rule.  
D. A Route 53 private hosted zone.  

### Q50

A company must classify 10 million support tickets nightly with a foundation model and store the results in S3. Results are not needed in real time, and cost efficiency matters.
Which approach is BEST?

A. Call the model synchronously per ticket from a Lambda function with unlimited concurrency.  
B. Train a custom model on SageMaker daily.  
C. Run an Amazon Bedrock batch inference job that reads prompts from S3 and writes results to S3.  
D. Use Amazon Rekognition.  

### Q51

An existing application on Amazon Aurora PostgreSQL needs semantic search over product descriptions and must join results with relational tables in the same database, without adding a new service.
What should the data engineer use?

A. Amazon DynamoDB.  
B. Amazon S3 Select.  
C. Amazon Athena.  
D. The pgvector extension with vector columns and an approximate nearest-neighbor index.  

### Q52

A new Airflow DAG file uploaded to the MWAA environment's S3 dags folder does not appear in the Airflow UI.
What should the engineer check first?

A. The scheduler/DAG processing logs in CloudWatch Logs for import or syntax errors, and that the file is in the configured dags path.  
B. The VPC route tables for the S3 bucket.  
C. The Glue Data Catalog.  
D. Kinesis shard count.  

### Q53

Business partners need to upload files to S3 using SFTP with their existing SFTP clients, and the company does not want to run servers.
Which service should be used?

A. AWS DataSync.  
B. AWS Transfer Family.  
C. AWS Snowball Edge.  
D. Amazon AppFlow.  

### Q54

Which TWO actions protect S3 objects from accidental deletion or overwrite? (Select TWO.)

A. Enable Transfer Acceleration.  
B. Enable Requester Pays.  
C. Enable bucket versioning.  
D. Enable server access logging only.  
E. Enable MFA delete or S3 Object Lock.  

### Q55

A data scientist wants to explore S3 data interactively with PySpark without provisioning or managing clusters.
Which option is BEST?

A. A self-managed Jupyter server on EC2.  
B. A long-running EMR cluster.  
C. Amazon Redshift query editor.  
D. Amazon Athena notebooks that use Apache Spark.  

### Q56

A data lake is currently governed only by IAM and S3 policies, and many jobs depend on that. The company wants to adopt Lake Formation permissions gradually without breaking existing jobs.
Which feature supports this?

A. Lake Formation hybrid access mode.  
B. Deleting all IAM policies immediately.  
C. Making buckets public.  
D. Disabling Glue.  

### Q57

A team runs occasional open-source Spark jobs with custom libraries and wants no cluster management and pay-per-use pricing.
Which service is BEST?

A. EMR on EC2 with a persistent cluster.  
B. Amazon Athena.  
C. Amazon EMR Serverless.  
D. AWS Batch with EC2.  

### Q58

A team wants every change to a Glue ETL script and its infrastructure to be tested and deployed automatically.
Which approach is BEST?

A. AWS CodePipeline with CodeBuild running unit tests and deploying the infrastructure through CloudFormation or CDK.  
B. Editing scripts directly in the console.  
C. Emailing scripts to operations.  
D. A cron job copying files.  

### Q59

A developer wants to define a Lambda function, a Step Functions state machine, and a DynamoDB table in one template, test locally, and deploy.
Which tool is MOST appropriate?

A. AWS CLI scripts only.  
B. Manual console configuration.  
C. AWS Batch.  
D. AWS Serverless Application Model (AWS SAM).  

### Q60

A company must keep a copy of critical S3 data in another Region for disaster recovery with minimal effort.
What should be enabled?

A. S3 Transfer Acceleration.  
B. S3 Select.  
C. S3 Cross-Region Replication (with versioning enabled).  
D. A VPC peering connection.  

### Q61

Which TWO statements about Amazon S3 Express One Zone are correct? (Select TWO.)

A. It uses directory buckets.  
B. It stores data redundantly across at least three Availability Zones.  
C. It is designed for single-digit millisecond request latency in a single Availability Zone.  
D. It is intended for archival data.  
E. It requires restores before reads.  

### Q62

A Glue Spark job reading thousands of tiny JSON files from S3 spends most of its time listing and opening files.
What is the BEST tuning step?

A. Reduce the number of workers.  
B. Use file grouping (groupFiles and groupSize) or compact the inputs into larger files.  
C. Disable the Data Catalog.  
D. Increase the job timeout.  

### Q63

A data engineer must profile a 5 TB dataset cheaply while keeping the sample representative of each customer segment.
Which TWO sampling approaches are appropriate? (Select TWO.)

A. Stratified sampling by customer segment.  
B. Reading only the first 1,000 rows.  
C. Random sampling with a fixed seed.  
D. Choosing only the largest customers.  
E. Skipping profiling entirely.  

### Q64

A Glue ETL job writes to S3 and CloudWatch Logs and uses bookmarks. Policy requires all three to be encrypted with a customer managed KMS key.
What should be used?

A. S3 Select.  
B. A Glue crawler.  
C. Data Catalog resource policy only.  
D. A Glue security configuration that specifies KMS keys for S3, CloudWatch Logs, and job bookmarks.  

### Q65

The security team wants to prevent anyone in the account from making S3 buckets or objects public.
Which control is MOST effective?

A. Educate developers.  
B. Use bucket tags.  
C. Enable S3 Block Public Access at the account level.  
D. Enable CloudWatch Logs.  
