# Topic Set — Part 2 Answers & Explanations (Q25–47)

### Q25 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.1.1 · Difficulty: Medium · Type: MC
- Correct B: S3 storage is cheap and Athena charges only per data scanned when queries run.
- A: Pays for compute continuously for rare queries.
- C: Expensive for 50 TB analytics.
- D: Not an ad hoc SQL analytics store.

### Q26 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.1.2 · Difficulty: Medium · Type: MC
- Correct C: Aurora Replicas scale reads, and the reader endpoint load-balances connections across them.
- A: Keeps reads on the writer.
- B: A rewrite of the application.
- D: Removes read scaling.

### Q27 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.1.6 · Difficulty: Hard · Type: MC
- Correct D: Consistent lock ordering and retry logic are the standard remedies.
- A: Loses atomicity.
- B: Does not affect lock cycles.
- C: Does not help.

### Q28 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.1.5 · Difficulty: Hard · Type: MC
- Correct A: Materialized views precompute and store results, including over external tables.
- B: Distribution styles apply to local tables.
- C: VACUUM applies to local tables.
- D: Athena is not involved.

### Q29 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.2.1 · Difficulty: Medium · Type: MC
- Correct B: The Glue Data Catalog is a Hive-compatible metastore shared across services.
- A: Drifts apart.
- C: Manual and error-prone.
- D: No central governance.

### Q30 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.2.3 · Difficulty: Medium · Type: MC
- Correct C: The "Log" option records changes without modifying the table.
- A: More frequent changes.
- B: Destructive.
- D: Would break everything.

### Q31 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.3.1 · Difficulty: Medium · Type: MC
- Correct D: UNLOAD writes query results to S3 in parallel and supports Parquet and partitioning.
- A: COPY loads data into Redshift.
- B: Not valid.
- C: Reclaims space.

### Q32 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.3.5 · Difficulty: Hard · Type: MC
- Correct A: Deleting rows creates a new snapshot; old snapshots still reference the data until they are expired and files removed.
- B: Leaves data files and breaks the table.
- C: Does not target the customer.
- D: Does not delete.

### Q33 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.3.3 · Difficulty: Medium · Type: MC
- Correct B: Lifecycle rules can expire objects and clean up incomplete uploads.
- A: Policies do not delete data.
- C: Transfer speed feature.
- D: Reporting only.

### Q34 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.4.1 · Difficulty: Hard · Type: MC
- Correct C: A GSI re-keys the data for a new access pattern across partitions.
- A: Inefficient.
- B: An LSI keeps the same partition key (customerId), so it cannot query across customers.
- D: Manual duplication.

### Q35 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.4.4 · Difficulty: Medium · Type: MC
- Correct D: Lineage shows data movement and transformations for governed assets.
- A: Tracks spend.
- B: Delivery logs.
- C: Unrelated.

### Q36 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.4.5 · Difficulty: Medium · Type: MC
- Correct A: Snappy is fast and is the widely used Parquet default.
- B: High ratio but slow.
- C: Larger files and more I/O.
- D: Breaks columnar block layout and splitting.

### Q37 — A, C

- Domain: D2 (Data Store Management) · Task/skill: 2.1.8 · Difficulty: Hard · Type: MR
- Correct A and C: IVF is a cluster-based approximate index with lower build cost and memory than HNSW.
- B: Cluster centroids should be built from representative data.
- D: Reversed: HNSW is graph-based.
- E: IVF is approximate.

### Q38 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.1.7 · Difficulty: Medium · Type: MC
- Correct B: Iceberg keeps snapshots of table state so earlier versions can be queried or restored.
- A: Iceberg does not enforce primary key constraints.
- C: Iceberg uses metadata and file statistics, not B-tree indexes.
- D: Foreign keys are not enforced.

### Q39 — A

- Domain: D2 (Data Store Management) · Task/skill: 2.2.4 · Difficulty: Hard · Type: MC
- Correct A: Partition indexes speed partition lookup; projection avoids catalog lookups.
- B: Planning time is not about timeout.
- C: Unrelated.
- D: Small files worsen performance.

### Q40 — B

- Domain: D2 (Data Store Management) · Task/skill: 2.1.3 · Difficulty: Medium · Type: MC
- Correct B: MemoryDB provides Redis data structures such as sorted sets with durability.
- A: Object storage.
- C: Warehouse.
- D: ETL service.

### Q41 — C

- Domain: D2 (Data Store Management) · Task/skill: 2.4.2 · Difficulty: Hard · Type: MC
- Correct C: DynamicFrames represent mixed types as choices that can be resolved explicitly.
- A: Loses data quality.
- B: Loses data.
- D: Stops the pipeline.

### Q42 — D

- Domain: D2 (Data Store Management) · Task/skill: 2.3.6 · Difficulty: Medium · Type: MC
- Correct D: Global tables replicate across Regions and accept writes in each Region.
- A: A change log, not replication.
- B: Point-in-time copies.
- C: Restore within one Region.

### Q43 — A

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.3 · Difficulty: Medium · Type: MC
- Correct A: List calls return up to 1,000 keys per page; paginators iterate over all pages.
- B: Returns only the first page.
- C: 1,000 is the maximum per response.
- D: Does not change paging.

### Q44 — C

- Domain: D3 (Data Operations and Support) · Task/skill: 3.1.6 · Difficulty: Medium · Type: MC
- Correct C: DataBrew offers visual transformations saved as reusable recipes.
- A: Needs engineers.
- B: Requires code.
- D: Streaming.

### Q45 — D

- Domain: D3 (Data Operations and Support) · Task/skill: 3.2.5 · Difficulty: Medium · Type: MC
- Correct D: Serverless scales with demand and bills for usage.
- A: A 24/7 provisioned cluster bills for idle time.
- B: Reserved instances commit to capacity regardless of use.
- C: An always-on single node still bills while idle and lacks elasticity.

### Q46 — A

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.1 · Difficulty: Medium · Type: MC
- Correct A: Exporting to S3 gives cheap retention and SQL access through Athena.
- B: Not auditable.
- C: Loses evidence.
- D: Loses evidence.

### Q47 — B

- Domain: D3 (Data Operations and Support) · Task/skill: 3.3.2 · Difficulty: Medium · Type: MC
- Correct B: Audit logs capture connections, user activity, and queries.
- A: Performance feature.
- C: Resizing.
- D: Queries S3.
