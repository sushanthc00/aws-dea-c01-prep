# Domain 2 — Data Store Management (26 %) — one-pager
Task map: 2.1 choose store · 2.2 catalog · 2.3 lifecycle · 2.4 modeling/schema evolution. Numbers: `05-limits`.

## Store selection by access pattern
| Access pattern | Store |
|---|---|
| Analytics on huge columnar data, SQL, joins | Redshift (hot) / S3+Athena (cold) |
| Key lookup, known patterns, ms latency, variable scale | DynamoDB |
| Relational OLTP / transactions / joins | RDS / Aurora (Aurora PostgreSQL + pgvector for vectors) |
| Wide-column Cassandra API | Keyspaces |
| Document/Mongo | DocumentDB |
| Graph | Neptune |
| In-memory durable, Redis API, µs | MemoryDB |
| Full-text/log search | OpenSearch |
| Streams | KDS/MSK (store as log, retention ✓) |
| Lake files | S3 (classes below), Iceberg tables (S3 Tables managed ✓) |

## S3 storage classes (cost vs access) ✓ numbers in 05-limits
Standard (hot) · Intelligent-Tiering (unknown/changing access; no retrieval fee ~; small objects <128 KB not monitored/charged ~) · Standard-IA (multi-AZ, 30-day min ~) · One Zone-IA (single AZ, re-creatable data) · Glacier Instant Retrieval (ms, 90 d min ✓) · Glacier Flexible (min 90 d ✓; minutes-hours) · Deep Archive (180 d ✓, 12–48 h ~). Lifecycle: transition + expiration + noncurrent versions + abort incomplete multipart; <128 KB don't transition by default ✓; **Express One Zone** = single-digit-ms, directory buckets, ML/analytics hot data ~.
Versioning + MFA delete ; Object Lock (WORM; retention modes governance/compliance) ~; CRR/SRR replication (needs versioning) ; DynamoDB **TTL** (free expiry, ~48 h lag ~) → pair with Streams to archive to S3.

## Open table formats (2.1.7, new v1.1)
| | Iceberg | Delta Lake | Hudi |
|---|---|---|---|
| Strength | hidden partitioning, schema/partition evolution, snapshot/time travel, ACID, engine-neutral (Athena, Redshift, EMR, Glue, Snowflake…) | Databricks heritage, ACID, time travel | upserts/incremental/CDC, COW vs MOR |
Glue 5.1 supports all three ✓. **S3 Tables** = S3 bucket type for Iceberg with auto compaction/snapshot mgmt ✓ (in scope); Lake Formation/IAM governed ✓; Glue crawlers & catalog; Athena `MERGE`, `OPTIMIZE`, `VACUUM` ~. Lake Formation “Governed tables” → gone; use Iceberg.

## Catalog (2.2)
Glue Data Catalog (technical): crawlers (infer schema, partitions), manual DDL, Athena DDL, `MSCK REPAIR TABLE` / `ALTER TABLE ADD PARTITION` / **partition projection** (no catalog partitions; best for predictable time/ID partitions), connections (2.2.5), Hive metastore compatibility (EMR external metastore). Consume via catalog from Athena/EMR/Redshift Spectrum/Glue (2.2.1). Business catalog (2.2.6): **SageMaker Catalog** (built on DataZone): business glossary, metadata forms, data products, projects, subscribe/approve workflows, lineage ✓ (skills 2.4.4, 4.5.6). Athena reads max 1M partitions per scan ✓ → partition design.

## Lifecycle (2.3)
Load/unload: COPY/UNLOAD (see 07-redshift). Deletion for legal (2.3.5): S3 lifecycle expiration, delete markers/noncurrent expiry, DynamoDB TTL, Iceberg `expire_snapshots`/row-level deletes (+ deletion vectors v3 ~), Redshift DELETE+VACUUM, GDPR-style erase = identify (Macie/catalog) + delete + also backups/replicas. Resiliency (2.3.6): multi-AZ, S3 11 9s durability ~, CRR, AWS Backup (cross-Region/account copies, vault lock ~), Redshift snapshots (cross-Region), DynamoDB PITR (35 d ~) + global tables, RDS Multi-AZ/read replicas, Aurora Global DB.

## Modeling & evolution (2.4)
- Redshift: dist/sort (07-redshift); star schema; SUPER for semi-structured.
- DynamoDB: design from queries; PK high-cardinality for even partitions; SK for range; single-table design; GSI (eventual, own capacity) vs LSI (same PK, 10 GB limit, create at table creation ~); sparse indexes; adjacency list; write sharding for hot keys.
- Lake: partition by query filter (date), avoid over-partitioning (small files; Athena limit ✓), columnar + compression (06-formats), Lake Formation tables/LF-tags (2.4.1).
- Schema evolution (2.4.2): Iceberg ADD/DROP/RENAME columns; Parquet/Avro schema merge (`mergeSchema`) ; Glue Schema Registry compatibility; Glue crawler “update in database” behaviour; DMS CDC with DDL changes ~; DynamoDB schemaless.
- Schema conversion (2.4.3): **DMS Schema Conversion** (SCT dropped from in-scope list ✓ but still named in skill) for heterogeneous (Oracle→PostgreSQL); DMS for data (full load / CDC / both).
- Lineage (2.4.4): SageMaker Catalog lineage (OpenLineage-compatible ~), SageMaker ML Lineage Tracking, Glue job lineage via catalog ~. 
- Locks (2.1.6): Redshift table locks/long transactions; RDS row/table locks, deadlocks, `SHOW PROCESSLIST`/`pg_locks` ~; DynamoDB conditional writes/optimistic locking with version attribute ~.
- Remote access (2.1.5): Redshift federated queries, Spectrum, materialized views; Athena federated query (Lambda connectors; “managed connectors” 12 sources 2026 ~); Aurora zero-ETL.
- **Vectors (2.1.3, 2.1.8, 2.4.6)**: embedding = numeric vector from model (Bedrock Titan/Cohere ~) ; similarity search types: exact (kNN) vs approximate (ANN). **HNSW** = graph-based ANN: high recall/speed, more memory, slower build. **IVF** (IVFFlat) = cluster-based ANN: partitions vectors into lists, probes nearest lists; smaller memory/faster build, lower recall, needs data first to train ~. Stores: Aurora PostgreSQL (pgvector, HNSW/IVFFlat), OpenSearch (k-NN), MemoryDB (vector search), DynamoDB vector indexes ✓ (quotas page lists up to 4,096 dims, TopK ≤100), S3 Vectors, Bedrock Knowledge Bases (managed chunk→embed→store→retrieve; RAG). Pick: existing SQL app → pgvector; managed RAG → Knowledge Bases; ultra-low-latency → MemoryDB; low-cost large-scale cold vectors → S3 Vectors ~.

## Trap list
- Redshift PK/FK not enforced. KEY dist on skewed col = hot node. Too many partitions = small files.
- Standard-IA for tiny/short-lived objects wastes (min size/duration charges).
- Glacier needs restore; Expedited costs more.
- DynamoDB scans for analytics → export to S3 / zero-ETL / Athena.
