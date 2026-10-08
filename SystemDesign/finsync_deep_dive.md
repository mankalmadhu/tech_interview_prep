# FinSync Deep Dive — Interview Prep

Curated Q&A for defending FinSync (core banking ledger) under interview-level
scrutiny: architecture, code organization/SOLID, HTTP framework, rate
limiter, circuit breaker, RDS sizing, cache IOPS, Grafana/Prometheus, Kafka
provisioning/choke points, Redis, retries, and more.

No proprietary source code is stored here — only abstracted talking points.

---

## Open Items To Verify (before interviews)

- [ ] **RDS Multi-AZ failover behavior during an actual network partition**:
  does FinSync's primary accept writes and let the standby/replica catch up
  (favor Availability), or does it block/fail writes until the replica is
  reachable (favor Consistency)? Current guess: accepts writes on primary,
  tolerates replica lag — **needs confirmation** against actual AWS RDS
  Multi-AZ configuration/behavior used in production.

---

## Q&A Log

### Q1: Why single-writer serialization instead of distributed locking?

**A (refined)**: A ledger has zero tolerance for balance corruption or race
conditions. Distributed locking (e.g., a global lock) introduces its own
failure modes (lock-holder crashes, can't guarantee strong correctness) and
doesn't eliminate contention — it just moves it. Database transactions
alone, under heavy concurrent writes to the same account, cause lock
contention that degrades throughput. The single-writer pattern — partitioned
by account ID via Kafka — ensures serialized writes *per account* (not
globally), so ~98% of accounts get real-time balance updates, with only a
small number of very high-transaction-volume ("hot") accounts experiencing
higher lag under load.

**Framing distinction (important)**: This is better described via **PACELC**,
not CAP — there's no network partition in play during normal hot-account
contention, so it's a **Latency vs Consistency** trade-off (favoring
Consistency), not an Availability vs Consistency trade-off. CAP's
partition-tolerance trade-off (Availability vs Consistency) would apply
specifically during an actual network partition event, e.g., AWS RDS
Multi-AZ losing connectivity between primary and standby — see Open Items
above.

**Mechanism nuance**: Kafka topic is partitioned by account ID, so writes to
different accounts are processed in parallel by different partition
consumers, while writes to the *same* account are strictly serialized
within that partition — giving per-account single-writer semantics at
global scale, not a single global bottleneck writer.

**Rating**: 3/5 (solid core answer, needed refinement on CAP vs PACELC
framing; RDS Multi-AZ behavior still unverified)
**Date**: 2026-10-08

---

### Q2: What problem does the outbox pattern solve in FinSync, and why not just publish to Kafka directly after the DB commit?

**A (refined)**: Two distinct problems solved together:

1. **Why defer balance updates at all** (not inline with the PIB write):
   updating balance in the same transaction as the posting instruction batch
   (PIB) causes DB lock contention on hot accounts under heavy concurrent
   traffic. So the PIB transaction only appends an event to an outbox table
   (same local transaction, cheap append-only insert) instead of touching
   the balance directly.

2. **The dual-write problem**: if you publish directly to Kafka right after
   the DB commit (two separate systems, two separate operations), the DB
   commit can succeed while the Kafka publish fails — silently losing a
   balance update forever. Unacceptable on a ledger. The outbox pattern
   avoids this by making "record the event" part of the same atomic
   transaction as the business write; a separate poller/scheduler later
   reads unprocessed outbox rows and publishes them to Kafka asynchronously,
   batched by account ID.

**Follow-up: duplicate delivery / idempotency.** The outbox poller can crash
after publishing to Kafka but before marking the row processed, causing a
duplicate publish (also possible via lost producer acks, consumer group
rebalances, etc.). FinSync's consumers are idempotent by design:
- The balance `UPDATE` (`balance = balance + delta`) and an append-only
  insert into a balance time-series table happen in **one DB transaction**.
- The time-series table has a **unique constraint on (account_id, txn_id)**.
- On a duplicate event, the unique constraint violation causes the **entire
  transaction to roll back** — including the balance increment — so the
  balance is never double-applied. This works because both writes share one
  transaction boundary, not because the constraint alone protects balance.

**Follow-up: error classification.** All consumers propagate **typed
errors** from the repository/storage/Kafka/S3 layers (e.g., a specific
constraint-violation error type) up to the business/use-case layer, which
owns the retryable-vs-non-retryable decision. A constraint-violation error
is treated as an **expected, non-retryable** condition (a benign duplicate)
— the use case acks the Kafka message and moves on, rather than retrying or
escalating. Retry policy is deliberately a business-layer concern, not
baked into the storage layer.

**Rating**: 4/5 (strong, coherent multi-layer answer: outbox rationale,
idempotency mechanism, and error-classification architecture all connected
correctly)
**Date**: 2026-10-08
