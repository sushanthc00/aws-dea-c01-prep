# Mock Exam 2 — Part 3 (Questions 45–65)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q45

A nightly job calls a paginated third-party REST API, takes about 40 minutes, and writes JSON to S3. The team wants the simplest serverless scheduled solution.
Which option is BEST?

A. A single Lambda function that is allowed to run for 40 minutes.  
B. An EC2 instance that runs a cron job calling the API.  
C. An EMR cluster that is started for the nightly run.  
D. An AWS Glue Python shell job started by a schedule.  

### Q46

A Spark job in AWS Glue reads a very large table from Amazon RDS for PostgreSQL over JDBC and is slow because a single connection reads all rows.
How can read performance be improved?

A. Configure a partitioned JDBC read (a partition column with bounds, or hashfield/hashpartitions).  
B. Add more workers without changing how the JDBC source is read.  
C. Convert the job to a Python shell job to avoid Spark overhead.  
D. Disable the JDBC connection and export the table to CSV by hand.  

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

A. A larger instance type for the primary node.  
B. EMR managed scaling for the core and task node groups.  
C. A cluster log URI that archives the logs to an S3 bucket.  
D. A smaller HDFS block size for the Spark input data.  

### Q49

Jobs in a VPC use an S3 gateway endpoint. Security wants to ensure traffic through the endpoint can reach only the company's data lake buckets.
What should be configured?

A. A security group attached to the S3 gateway endpoint.  
B. A VPC endpoint policy that allows only the company's buckets.  
C. An S3 lifecycle rule on the shared buckets.  
D. A Route 53 private hosted zone that resolves only the company's buckets.  

### Q50

A company must classify 10 million support tickets nightly with a foundation model and store the results in S3. Results are not needed in real time, and cost efficiency matters.
Which approach is BEST?

A. Call the model synchronously for every ticket from a Lambda function with unlimited concurrency.  
B. Train a custom classification model on SageMaker every day.  
C. Run an Amazon Bedrock batch inference job that reads prompts from S3 and writes results to S3.  
D. Send every ticket to Amazon Rekognition for classification.  

### Q51

An existing application on Amazon Aurora PostgreSQL needs semantic search over product descriptions and must join results with relational tables in the same database, without adding a new service.
What should the data engineer use?

A. Amazon DynamoDB with a separate similarity-search service.  
B. Amazon S3 Select over exported embeddings.  
C. Amazon Athena over the embeddings stored in S3.  
D. The pgvector extension with an approximate nearest-neighbor index.  

### Q52

A new Airflow DAG file uploaded to the MWAA environment's S3 dags folder does not appear in the Airflow UI.
What should the engineer check first?

A. The DAG processing logs in CloudWatch Logs, and the file's path under dags/.  
B. The VPC route tables for the S3 bucket that holds the DAG files.  
C. The Glue Data Catalog entries that the DAG reads at parse time.  
D. The Kinesis shard count of the stream that triggers the DAG.  

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

A. AWS CodePipeline with CodeBuild unit tests, deploying through CloudFormation or CDK.  
B. Editing the Glue scripts directly in the console and saving the new version.  
C. Emailing updated scripts to operations, who upload them to S3 after review.  
D. A cron job on an EC2 instance that copies the scripts to S3 every night.  

### Q59

A developer wants to define a Lambda function, a Step Functions state machine, and a DynamoDB table in one template, test locally, and deploy.
Which tool is MOST appropriate?

A. AWS CLI scripts that create each resource one by one.  
B. Manual console configuration that is documented in a runbook.  
C. AWS Batch jobs that deploy each resource on demand.  
D. AWS Serverless Application Model (AWS SAM).  

### Q60

A company must keep a copy of critical S3 data in another Region for disaster recovery with minimal effort.
What should be enabled?

A. S3 Transfer Acceleration on the source bucket.  
B. S3 Select queries that copy the critical objects.  
C. S3 Cross-Region Replication (with versioning enabled).  
D. A VPC peering connection between two Regions.  

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

A. Reduce the number of workers to lower the per-file overhead.  
B. Use file grouping (groupFiles and groupSize) or compact the inputs into larger files.  
C. Disable the Data Catalog so that the job lists the files itself.  
D. Increase the job timeout so that the listing can finish.  

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

A. S3 Select on the job's output location to read the encrypted files.  
B. A Glue crawler that scans the encrypted output location.  
C. A Data Catalog resource policy that restricts who can read the output.  
D. A Glue security configuration that specifies KMS keys for S3, CloudWatch Logs and bookmarks.  

### Q65

The security team wants to prevent anyone in the account from making S3 buckets or objects public.
Which control is MOST effective?

A. Educate developers about the risks of public buckets.  
B. Use bucket tags to mark which buckets may be public.  
C. Enable S3 Block Public Access at the account level.  
D. Enable CloudWatch Logs for the S3 buckets.  
