# Topic Set — Part 2 (Questions 25–47)

Timed: ~2 min per question. Do not open the answers file until the whole mock is finished.

### Q25

A company keeps 50 TB of historical data and runs ad hoc SQL queries on it only a few times a month. It wants the lowest cost and no infrastructure to manage.
Which solution is BEST?

A. A provisioned Redshift cluster running continuously.  
B. Data in S3 as Parquet, queried with Amazon Athena.  
C. Amazon Aurora with a large instance.  
D. A DynamoDB table with provisioned capacity.  

### Q26

A read-heavy reporting workload overloads the primary Amazon Aurora PostgreSQL writer. Reports tolerate seconds of replica lag.
What should the engineer configure?

A. A bigger writer instance, with the reports routed to it as well.  
B. Convert the database to DynamoDB so that reads scale automatically.  
C. Aurora Replicas and the reader endpoint for the reporting connections.  
D. Disable replication so that the writer has more capacity for reports.  

### Q27

Concurrent transactions in Amazon RDS for MySQL occasionally fail with deadlock errors.
What is the BEST approach?

A. Disable transactions so that rows are never locked while the statements run.  
B. Increase the storage size so that lock tables have more room.  
C. Move to a smaller instance class so that fewer sessions run concurrently.  
D. Access rows in a consistent order, keep transactions short, and retry on deadlock errors.  

### Q28

Dashboards repeatedly aggregate data in S3 queried through Redshift Spectrum external tables, and queries are slow.
Which feature can speed repeated queries?

A. A materialized view over the external table, refreshed on a schedule.  
B. DISTSTYLE ALL on the external table so that every node holds a copy.  
C. VACUUM on the external table to reclaim space and re-sort the data.  
D. A bigger Athena workgroup to speed up the Spectrum scans.  

### Q29

Spark jobs on Amazon EMR must use the same table definitions that Athena and Glue use.
What should be configured?

A. A separate Hive metastore for each cluster, synchronized with scripts.  
B. Configure EMR to use the AWS Glue Data Catalog as its Hive metastore.  
C. Copy the schemas manually into each Spark job at deployment time.  
D. Store the schemas in a text file in S3 that each job parses.  

### Q30

A Glue crawler runs nightly. After an upstream change, the crawler altered a production table's columns and broke downstream queries. The team wants schema changes reviewed first.
What should be configured?

A. Run the crawler hourly so that schema changes are picked up faster.  
B. Delete and recreate the table each night from the crawler results.  
C. Set the crawler's schema change policy to log changes, then apply approved changes manually.  
D. Disable the Glue Data Catalog and define the schemas in each query.  

### Q31

Query results from Redshift must be exported to S3 as Parquet, partitioned by sale_date, in parallel.
Which command should be used?

A. COPY with FORMAT AS PARQUET into a table, then export it with a SELECT statement.  
B. INSERT INTO an S3 path with a SELECT statement.  
C. VACUUM the table with a PARQUET option after the export.  
D. UNLOAD with FORMAT PARQUET and PARTITION BY (sale_date).  

### Q32

A customer requests erasure of personal data stored in an Apache Iceberg table in the S3 data lake queried by Athena.
What is the BEST approach?

A. Run a row-level DELETE for the customer, then expire old snapshots and remove orphaned files.  
B. Delete only the table's current metadata file so that the rows can no longer be found.  
C. Wait for the S3 lifecycle rule to remove the objects at the end of the retention period.  
D. Disable queries for the customer's identifier in the BI tool.  

### Q33

An S3 bucket accumulates abandoned incomplete multipart uploads that add storage cost, and logs older than 90 days must be removed.
What should be configured?

A. A bucket policy that denies uploads to the logs prefix after 90 days.  
B. A lifecycle configuration with a 90-day expiration rule and an AbortIncompleteMultipartUpload rule.  
C. S3 Transfer Acceleration on the bucket to finish uploads sooner.  
D. S3 Inventory reports that list the old objects for manual deletion.  

### Q34

A DynamoDB table has PK customerId and SK orderDate. A new requirement is to query orders by orderStatus across all customers, sorted by orderDate.
What should be added?

A. A scan with a filter expression on orderStatus, run on a schedule.  
B. A local secondary index on orderStatus, added to the existing table.  
C. A global secondary index with partition key orderStatus and sort key orderDate.  
D. A second table copy that is updated by hand whenever the status changes.  

### Q35

Governance wants to see which upstream datasets and transformations produced a published analytics asset, across projects.
Which capability should be used?

A. AWS Budgets.  
B. Amazon CloudFront logs.  
C. EC2 instance metadata.  
D. Data lineage in Amazon SageMaker Catalog.  

### Q36

A team writes Parquet and wants fast compression and decompression with a reasonable ratio, accepting the common default.
Which compression codec is MOST appropriate?

A. Snappy.  
B. BZIP2.  
C. None, to avoid CPU cost.  
D. A single gzip wrapper around the whole directory.  

### Q37

Which TWO statements about the IVF vector index type are correct? (Select TWO.)

A. It partitions vectors into clusters (lists) and searches only the nearest clusters at query time.  
B. It can be built effectively on an empty table before any data is loaded.  
C. It generally builds faster and uses less memory than HNSW, but typically has lower recall at similar speed.  
D. It is a graph-based index while HNSW is cluster-based.  
E. It always returns exact nearest neighbors.  

### Q38

A bad write corrupted an Iceberg table. The team needs to inspect and restore the table to its state from yesterday.
Which Iceberg capability applies?

A. Primary key constraints, which are enforced to prevent bad rows.  
B. Snapshots, which enable time travel and rollback to an earlier snapshot.  
C. B-tree indexes on each column, which are rebuilt after every write.  
D. Foreign keys, which reject writes that reference missing rows.  

### Q39

Athena query planning is slow because a Glue table has millions of partitions and queries filter on a few partition keys.
What can improve planning time?

A. Create partition indexes in the Glue Data Catalog (or use partition projection).  
B. Increase the Athena query timeout so that planning has more time to finish.  
C. Add an S3 lifecycle rule that moves old partitions to a cheaper class.  
D. Decrease the file size so that each partition holds fewer rows.  

### Q40

A gaming platform needs a durable store for leaderboards using sorted sets with microsecond reads and writes.
Which service is BEST?

A. Amazon S3.  
B. Amazon MemoryDB.  
C. Amazon Redshift.  
D. AWS Glue.  

### Q41

An upstream system changed a column from integer to string, and the Glue job now fails or produces mixed types.
What is the BEST way to handle the changing data characteristic?

A. Ignore the failures and rerun the job when the upstream team fixes the column.  
B. Delete the column from the target so that the type conflict disappears.  
C. Use ResolveChoice (for example cast to string) and manage schema versions in a schema registry.  
D. Disable the job until the upstream system returns to the previous type.  

### Q42

A DynamoDB-based application needs multi-Region active-active writes with replication measured in seconds and Regional failover.
Which feature should be used?

A. DynamoDB Streams alone.  
B. On-demand backups.  
C. PITR.  
D. DynamoDB global tables.  

### Q43

A script using the AWS SDK must list all objects in a bucket with more than 1,000 keys.
What should the developer do?

A. Use the SDK paginator, or loop on the continuation token.  
B. Call list_objects_v2 once and read the full result set.  
C. Increase MaxKeys above 1,000 so that one call returns every key.  
D. Use a larger instance so that the single call returns more results.  

### Q44

Analysts without coding skills must standardize date formats and remove duplicates in files in S3 and reuse the steps on new files.
Which service is BEST?

A. Amazon EMR.  
B. AWS Lambda.  
C. AWS Glue DataBrew with a recipe.  
D. Amazon Kinesis.  

### Q45

A development team runs unpredictable, intermittent Redshift queries and wants to avoid paying for idle capacity.
Which option is BEST?

A. A large provisioned cluster running 24/7.  
B. Reserved instances.  
C. A single node cluster always on.  
D. Amazon Redshift Serverless.  

### Q46

Auditors need application logs from CloudWatch Logs delivered to S3 for long-term, low-cost querying.
What should be done?

A. Export the logs to S3 (an export task, or a subscription filter through Firehose) and query with Athena.  
B. Take screenshots of the CloudWatch console each month and file them.  
C. Delete older log events so that only recent entries need review.  
D. Stop logging after the audit period to reduce the volume.  

### Q47

Security requires a record of connections, user changes, and queries run on a Redshift cluster.
What should be enabled?

A. Concurrency scaling, which records each query that the extra clusters run.  
B. Redshift audit logging to S3 or CloudWatch Logs, with enable_user_activity_logging.  
C. Elastic resize, which keeps a history of all connections and queries.  
D. Redshift Spectrum, which logs the queries that read external tables.  
