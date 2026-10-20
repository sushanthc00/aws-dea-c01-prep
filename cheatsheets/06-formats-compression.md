# File formats & compression (1.2.6, 2.4.5)
~ established; not re-fetched.

| Format | Layout | Splittable | Schema | Best for | Notes |
|---|---|---|---|---|---|
| **Parquet** | columnar | yes (row groups) | embedded | Athena/Redshift Spectrum/EMR analytics; column pruning + predicate pushdown | default analytics format; Snappy default; nested types |
| **ORC** | columnar | yes | embedded | Hive/Presto/Athena; ACID in Hive | similar to Parquet; strong compression |
| **Avro** | row | yes | embedded (JSON schema) | streaming/Kafka, write-heavy, schema evolution, Schema Registry | good for whole-record reads |
| **JSON** | row, text | line-delimited yes | none | APIs, semi-structured, logs | large, slow; convert to Parquet |
| **CSV/TSV** | row, text | yes (uncompressed or splittable codecs) | none | interchange, small | no types; headers; avoid for analytics |
| Iceberg/Delta/Hudi | table format over Parquet/ORC/Avro | — | catalog + metadata | ACID, upserts, time travel, evolution | see 02-d2 |

| Compression | Splittable | Ratio | Speed | Use |
|---|---|---|---|---|
| Snappy | no (OK inside Parquet/ORC) | low-med | very fast | default for Parquet |
| GZIP | no | high | slow | cold data, cost of storage; text files not parallel |
| LZO | yes (indexed) | med | fast | Hadoop legacy |
| BZIP2 | yes | high | slowest | rarely |
| ZSTD | no (inside columnar OK) | high | fast | modern balance (Parquet/ORC support) |
Redshift COPY: gzip/bzip2/lzop/zstd for text; split files ≈ multiple of slices.

## Rules of thumb
- Analytics scan cost (Athena $/TB scanned): **columnar + compression + partitioning** cut bytes scanned most.
- Target file size ≈ **128 MB–1 GB**; avoid thousands of tiny files (per-file overhead, S3 request limits ✓, Athena partition limits ✓). Compact via Glue/Athena CTAS/Iceberg compaction/Firehose buffering.
- Partition on columns used in filters with moderate cardinality (date, region); not user_id. Hive-style `s3://b/t/dt=2026-10-20/`. Partition projection avoids catalog calls.
- Bucketing for join/sampling ~. Sort within files (Parquet min/max stats) improves pruning.
- Row format for append/streaming, columnar for query. Convert at landing (Firehose conversion, Glue).
- Gzip-ed single CSV ⇒ one reader (non-splittable) ⇒ slow.
