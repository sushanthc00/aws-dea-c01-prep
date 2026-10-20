# Exam-day playbook — DEA-C01 (Sun 1 Nov 2026, IST)
✓ = from official AWS pages read 2026-10-20 · advice = my recommendation (not official).

## 1. Logistics checklist
**Week before**
- ✓ Name on your AWS Certification account must **exactly match** your ID; a mismatch means you can be refused and the fee is forfeited. ✓ A **secondary ID** is always required; online and in-person ID rules differ — read them on the Pearson VUE confirmation.
- ✓ Request **ESL +30 min** in your AWS Certification account (once; applies to future registrations) if English isn't your first language — do it *before* scheduling; if already booked, verify it shows on the appointment [UNVERIFIED for existing bookings].
- ✓ Reschedule/cancel only up to **24 h before**; each booking can be rescheduled twice; within 24 h or no-show = fee forfeited (documented medical/emergency exceptions via Pearson VUE).
- Decide centre vs online. Sunday centre slots in India [UNVERIFIED — check scheduler]. ✓ English-language online proctors are available 24x7.
**Night before (Sat 31 Oct)**
- No new topics. Skim `cheatsheets/12-commonly-confused-pairs.md`, `05-limits-and-numbers.md`, your error log. Sleep ≥ 7 h; set two alarms; confirm the appointment time in IST on the confirmation email.
**Online proctoring checklist (OnVUE)** — ✓ system test must pass or the fee is forfeited; arriving > 15 min late forfeits the fee; **no breaks, you may not stand up or leave camera view**; you must communicate with the proctor throughout.
- Run the Pearson system test on the exact machine/network you'll use, a day early and again 1 h before.
- Private room, door closed, nobody enters; clear desk (no notes, phones away, no second monitor/headphones unless permitted); stable power + wired network if possible; ID + secondary ID ready; webcam sees you and room (expect a room scan). Toilet, water before check-in.
- Close all apps/VPN/corporate agents that could interfere; disable notifications.
**Test centre** — ✓ unscheduled breaks allowed but the **timer keeps running**, you can't leave the building, must check in again; arrive early; don't ask staff about exam content.
**You must agree to the Candidate Code of Conduct** before starting; failing to agree or timing out ends the exam without refund ✓.

## 2. Time management (130 min, 65 Q ≈ 2 min each)
| Phase | Budget | Rule |
|---|---|---|
| Pass 1 | ≈ 80–90 min | answer everything you can in ≤ 90 s; **flag** anything needing > 2 min and move on; never leave blanks |
| Pass 2 | ≈ 30–35 min | return to flagged items; eliminate; decide |
| Pass 3 | last 10 min | check unanswered (✓ no penalty for guessing → fill every one); re-read multi-select counts |
Checkpoints: Q20 by ~35 min, Q40 by ~70 min, Q65 by ~110 min. 15 questions are unscored and indistinguishable ✓ — don't agonise over a strange one.

## 3. Reading a stem (qualifier first)
1. Read the **last sentence** (the ask) and underline the qualifier: **LEAST operational overhead · MOST cost-effective · MOST secure · FASTEST/lowest latency · MOST scalable · near real time vs real time · without moving data**.
2. Extract constraints: volume/throughput, latency, access pattern, existing tech (Kafka, Airflow), compliance/residency, team skills, "no code".
3. Predict the answer *before* reading options; then eliminate options that violate a hard constraint.
Qualifier → default:
| Qualifier | Lean to |
|---|---|
| least ops | serverless/managed (Glue, Athena, Firehose, Step Functions, Lake Formation, EMR Serverless, S3 Tables, zero-ETL) |
| most cost-effective | right tier/engine, columnar+partitioned, Spot/Flex, on-demand for spiky, provisioned+commitment for steady |
| most secure | least privilege + Lake Formation + CMK + VPC endpoints + TLS enforced + audit |
| fastest | in-memory/cache, EFO, co-located joins, Express One Zone, provisioned capacity |
| real time | KDS/MSK + Flink/Lambda; near real time → Firehose (≥ 60 s ✓) |
| without copying data | Spectrum, federated query, data sharing, LF sharing, zero-ETL |

## 4. Multiple-response questions
Count how many answers are required ("Select TWO"). Evaluate each option **independently** as true/false for the scenario, then pick the best N. Both must be right; a correct+wrong pair is wrong. Typical pairings: "A and its prerequisite" (e.g., key policy + IAM policy ✓, UNLOAD + Spectrum, Macie + LF-tags).

## 5. Elimination patterns
- Wrong **scope/service**: option names a service that can't do the job (Firehose to private Redshift ✓, Lambda for > 15 min ✓, Athena for custom PySpark ETL, GSI vs LSI misuse).
- **Over-engineered**: extra services when a native feature exists (custom Lambda for lifecycle, TTL, partition projection, zero-ETL).
- **Violates qualifier**: EMR on EC2 in a "least ops" stem; provisioned for "unpredictable".
- **Hard limit** violated (record size, payload, timeout, history events ✓).
- **Manual/unauditable** steps; **public** exposure; **long-term keys**.
- Two plausible options → pick the one with **less ops, more native, narrower scope, cheaper tier**.

## 6. Unfamiliar services or features
Don't panic (15 unscored items exist ✓; compensatory scoring ✓). Map to a known category: *catalog/governance → SageMaker Catalog/LF; delivery → Firehose; orchestration → SFN/MWAA; streaming log → KDS/MSK*. Use the verb in the stem (ingest/transform/store/query/govern). Eliminate options you *know* are wrong; if two remain, choose the managed/serverless native one. Flag and return.

## 7. Traps seen in AWS-style stems
Near-synonyms (KDS vs Firehose; Spectrum vs federated query; GSI vs LSI; Standard-IA vs One Zone-IA vs Glacier IR); "cross-account" (needs both sides ✓); "encrypt" (SSE-S3/KMS/C/client-side); "real time" vs "near real time"; stale names (Kinesis Data Analytics → Managed Service for Apache Flink; Firehose rename; Quick); "data lake permissions" → Lake Formation not S3 policy; "replay" → KDS/MSK not Firehose/SQS; "orchestrate with retries" → Step Functions; old limits (Kinesis record now up to 10 MiB ✓).

## 8. Last 10 minutes
1. Fill every unanswered item (no penalty ✓). 2. Re-check flagged MR items for the required count. 3. Don't change answers without a concrete reason (a recalled fact), not a feeling. 4. Submit with ≥ 1 min spare; complete the survey if prompted. Result: pass/fail then scaled score + domain table later ✓; fail → 14-day wait ✓ (earliest retake Sun 15 Nov).

## 9. Mental routine
Breathe on flag; skip and return beats burning 5 minutes; hydrate; eat 60–90 min before; stretch before check-in (no breaks online ✓).
