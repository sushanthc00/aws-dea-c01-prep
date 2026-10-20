# Lake Formation + security deep sheet
✓ skill list from exam guide v1.1 · ~ established behaviour, re-check Phase 3/5.

## Lake Formation (LF) — 4.2.4, 4.5
- Central, fine-grained permissions on **Glue Data Catalog** resources (db/table/column/row/cell) enforced for **Athena, Redshift Spectrum, EMR, Glue** ✓ (guide names Redshift, EMR, Athena, S3); S3 locations must be **registered** with LF (role) ~. LF vends temporary credentials to integrated engines (credential vending). June 2026: table grants (SELECT=read, SUPER=read/write) can extend to underlying S3 file access with EMR 7.13+ ✓(WN, non-English).
- **Permission model**: LF grants (GRANT/REVOKE SELECT, DESCRIBE, ALTER, DROP, INSERT, DELETE, CREATE_TABLE…) **plus** IAM permission to call the service. Effective access = IAM allows ∧ LF allows (when LF-enforced). Default “Use only IAM access control” (IAMAllowedPrincipals group) bypasses LF → remove it to enforce LF; **hybrid access mode** lets you migrate per-table/location gradually ~.
- **Data filters**: column-level, row-level (filter expression), cell-level (both).
- **LF-tags (TBAC / LF-TBAC)**: tag databases/tables/columns (`classification=pii`), grant by tag expression → scales better than named resources; fits “tag-based/attribute-based” 4.2.5.
- **Cross-account**: grant to another account's principals or to that account (their admin re-grants); uses AWS RAM underneath for named-resource sharing; LF-tag sharing; recipient creates **resource link** (shared db/table) to query ~; encrypted S3 data → KMS key policy must allow the consumer/role.
- Roles: Data lake administrator, database creator; service-linked role for registration.
- Governs Redshift **datashares** via LF ~, and Iceberg/S3 Tables with IAM/LF ✓ (Athena IAM-based auth for S3 Tables ✓ WN).
- LF vs alternatives: IAM/bucket policy = coarse, per-object/prefix, hard to scale; S3 Access Points = per-app prefix policies, VPC-restricted ; **LF = column/row/cell, central, audited (CloudTrail)**.

## IAM essentials (4.1, 4.2)
- Identity-based vs resource-based (bucket, KMS key, SQS, Lambda, LF/Glue catalog resource policy) ; **cross-account**: needs allow in *both* identity (caller) and resource policy (target) unless role assumption (assume role in target account → only role perms apply).
- Roles for services (trust policy = who can assume; permission policy = what). Lambda execution role, Glue job role (`glue.amazonaws.com`), `iam:PassRole` needed to hand roles to Glue/EMR/Redshift/Step Functions.
- Permission boundaries (max perms), SCPs (org guardrail, don't grant), session policies. Conditions: `aws:SourceVpce`, `aws:PrincipalOrgID`, `s3:prefix`, tags (ABAC `aws:PrincipalTag/…`) — 4.2.5. Least privilege (4.2.6): resource ARNs, specific actions, IAM Access Analyzer policy generation/validation ~.
- Roles for: Lambda, API Gateway (execution/authorizers), CLI (profiles/SSO), CloudFormation (service role) — 4.1.4. Policies for **S3 Access Points** & **PrivateLink endpoints** (endpoint policy) — 4.1.5.
- Managed vs unmanaged services (4.1.6): managed (Glue, Athena, Redshift Serverless) → AWS handles patching/HA, shared responsibility shifts; unmanaged (EC2-hosted Kafka/Spark) → you patch/scale/secure.
- Redshift DB authN/authZ (4.2.3): IAM roles, database users/groups/roles, GRANT, RLS/DDM, IAM Identity Center ~.

## Credentials (4.1.3, 4.2.2)
| | Secrets Manager | Parameter Store |
|---|---|---|
| Rotation | **built-in rotation (Lambda)** for RDS/Redshift/DocumentDB etc. ~ | no native rotation |
| Cost | per secret + API ~ | Standard free; Advanced paid ~ |
| Cross-account | resource policy ✓ ~ | limited (Advanced shares via RAM ~) |
| Use | DB credentials needing rotation | config values, simple secrets (SecureString/KMS) |
Glue connections, DMS endpoints, MSK SASL/SCRAM, Redshift can reference Secrets Manager.

## KMS (4.3.2, 4.3.3)
- **Key policy is mandatory** (root of trust); IAM policy works only if the key policy enables IAM (default “Enable IAM User Permissions”) ; **grants** for temporary delegation (AWS services use them).
- Envelope encryption: data key (GenerateDataKey) encrypts data; KMS key encrypts data key. Direct Encrypt ≤ 4 KB ~.
- Types: AWS owned, AWS managed (`aws/s3`, can't edit policy, **can't share cross-account**), customer managed (full control, rotation: automatic yearly default, on-demand ~). Multi-Region keys for DR/cross-Region replication ~. Imported key material (own rotation) ~, CloudHSM-backed custom key store ~.
- **Cross-account encryption (4.3.3)**: use a **customer managed key**; key policy allows external account/role (`kms:Decrypt`, `kms:GenerateDataKey`, `kms:ReEncrypt*`, `kms:DescribeKey`), and caller's IAM policy also allows. S3 CRR with SSE-KMS: replication role needs kms perms on source+destination keys; set destination key in replication config ~. Cross-account Redshift snapshot copy / RDS snapshot share need CMK shared.
- S3 encryption: **SSE-S3 default for all new objects** ~ ; SSE-KMS (audit/CloudTrail, per-request KMS cost → **S3 Bucket Keys** reduce calls) ; DSSE-KMS ~ ; SSE-C (customer supplies key each request) ; client-side (encrypt before upload = “before transit”, 4.3.4). Enforce with bucket policy conditions (`s3:x-amz-server-side-encryption`, `aws:SecureTransport`).
- Per-service at rest: Redshift (cluster KMS/HSM; can't encrypt in place — migrate via snapshot ~ ), RDS (at creation; snapshot-copy to encrypt), DynamoDB (always encrypted; owned/managed/CMK), KDS (SSE-KMS), Firehose (CMK ≤500 streams ✓), Glue (catalog encryption, job security configuration: S3/CloudWatch/bookmarks encryption), EMR (security configuration: at-rest/in-transit; EBS), MSK (KMS), SQS (SSE), Athena (results encryption), EBS/EFS (KMS).
- In transit: TLS everywhere (`aws:SecureTransport`, Redshift `require_ssl`, MSK TLS, Kinesis HTTPS, Redshift TLS ≥1.2 (enforced from 2026-10-31) ✓), VPC endpoints keep traffic on AWS network.

## Network (4.1.1, 1.1.8)
Security groups (stateful, allow-only, reference other SGs; Glue/Redshift/EMR/RDS in VPC; self-referencing SG for Glue). **Gateway endpoints**: S3, DynamoDB (free, route table). **Interface endpoints (PrivateLink)**: most others (Kinesis, Glue, Athena, KMS, Secrets Manager, STS, Step Functions…), ENI with SG, hourly + per-GB cost; endpoint policies. Private subnets + NAT for outbound internet; Redshift enhanced VPC routing; S3 bucket policy `aws:SourceVpce` to force private path.

## Privacy, masking, governance (4.3.1, 4.5)
- **Macie**: finds PII/sensitive data in S3 (managed + custom identifiers, sampling) → findings to Security Hub/EventBridge; works with LF-tags to restrict ✓ (4.5.2). **Glue sensitive data detection** in jobs; **DataBrew** masking/hash/substitute; **Redshift DDM** + RLS; LF data filters; tokenization/pseudonymisation via Lambda; hashing, k-anonymity ~.
- Data sovereignty/residency (4.5.3/4.5.5): restrict Regions with **SCP** `aws:RequestedRegion`, disable replication/backup copies (S3 CRR rules, AWS Backup cross-Region copy, snapshots) to disallowed Regions, Config rules/Access Analyzer to detect, Control Tower region deny ~, KMS keys single-Region; EU sovereign cloud exists ✓ (Glue 5.1 available).
- Redshift data sharing permissions (4.5.1): producer authorizes consumer account/namespace; LF-governed sharing ~. Data Exchange for third-party data.
- Config (4.5.4) conformance packs & rules; CloudTrail (management/data/Insights events, log file validation, org trail → S3; **CloudTrail Lake** query) 4.4; CloudWatch Logs retention/export; log analysis via Athena (CloudTrail table), Logs Insights, OpenSearch.
- **SageMaker Unified Studio (4.1.7, 4.5.6, 4.5.7)**: a **domain** is the top-level boundary (identity: IAM Identity Center or IAM-based ~); **domain units** organise teams/BUs with delegated policy; **projects** = collaboration workspace with its own IAM role, members/roles, compute and data assets; **SageMaker Catalog** publishes data assets/products, consumers **subscribe** (owner approves) → access granted through LF/Redshift grants for managed assets ✓(secondary source); lineage. Governance framework: ownership/stewardship, classification (tags/glossary), policy-as-code, audit, quality; sharing patterns: Redshift datashares, LF cross-account, S3 Access Points, catalog subscription, Data Exchange, clean rooms ~.
- Backup/DR (2.3.6): AWS Backup (policies, vault lock, cross-account/Region); RPO/RTO tiers: backup-restore → pilot light → warm standby → active-active.

## Trap list
- “Least privilege + column restriction on S3 data lake” → **Lake Formation**, not bucket policy.
- Cross-account S3 + KMS needs **both** bucket/ACL (or role) access **and** key policy. AWS-managed key can't be used cross-account.
- Interface endpoint needed for Kinesis/Glue; gateway endpoint for S3/DynamoDB.
- Secrets Manager when “automatic rotation”; Parameter Store when “cheapest config”.
- SCP denies; it never grants.
- ⚠ CloudTrail Lake: not open to new customers from 2026-05-31 (existing customers fine) ✓ per AWS doc; skill 4.4.3 still in exam guide. See guide/D4/4.4.
