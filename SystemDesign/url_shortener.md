# URL Shortener — Interview Prep (Day 2: Classic Warm-up)

Full Socratic walkthrough of the classic "Design a URL Shortener" problem,
used as a template for the standard system-design interview framework:
(1) requirements clarification, (2) capacity estimation, (3) API design,
(4) high-level architecture, (5) deep-dive on the hardest sub-problem,
(6) scale/bottleneck follow-ups.

---

## 1. Requirements Clarification

- **Scope**: public URL shortening service (not tied to a specific org/user
  base).
- **Optional TTL**: links can optionally expire.
- **MVP scope**: no click analytics in the initial version (explicitly
  descoped to keep the core design focused).

---

## 2. Capacity Estimation

**QPS (queries per second)**:
- 1,000 writes/sec (new short URLs created)
- 100,000 reads/sec (redirects)
- Derived using the standard interview rounding trick: 1 day ≈ 100,000
  seconds (vs. the real 86,400), making back-of-envelope daily→per-second
  conversions simpler.

**Storage**:
- ~500 bytes per row (short code + long URL + metadata).
- At 1,000 writes/sec → ~50GB/day.
- Over 5 years → ~91TB total.
- **Key distinction reinforced**: per-row byte-size estimate is separate
  from replication overhead — replication is a multiplier applied to
  *total* storage, not something that inflates the *per-row* estimate.
  Table/DB partitioning (sharding) is also a distinct concept from both of
  these, and distinct from the CAP-theorem sense of "network partition."

**Short-code length (base62: `[a-zA-Z0-9]`)**:
- Target capacity: ~180 billion unique codes.
- `62^6 ≈ 56.8B` — insufficient.
- `62^7 ≈ 3.5T` — sufficient.
- Settled on **8 characters** as a round-number safety margin.

**Bandwidth**:
- Reads: ~50MB/s
- Writes: ~0.25MB/s
- (Initial pass miscalculated by 10x — corrected during the session.)

**Cache sizing (80/20 rule)**:
- Standard interview convention: treat ~20% of daily *read request volume*
  as a proxy for the count of unique "hot" cache entries. This is a widely
  accepted simplification (confirmed via external check against common
  system-design prep material) — don't confuse "unique keys that exist"
  with "unique keys actively being read," the latter is the relevant
  number for cache sizing.

---

## 3. API Design

- `POST /shorten` → returns `201 Created` + the generated short URL (not a
  redirect — this is a resource-creation endpoint).
- `GET /{shortCode}` → returns `302 Found` (temporary redirect), **not**
  `301 Moved Permanently`.
  - **Why 302, not 301**: a `301` gets cached by the browser, so repeat
    visits bypass the server entirely on subsequent requests. That would
    make it impossible to enforce expiry/revocation later (the server
    never gets asked again). `302` keeps every redirect request flowing
    through the server, preserving control. (Not a "browser warning"
    issue — that's a common but incorrect justification.)

---

## 4. High-Level Architecture

Load balancer → app servers → cache (hot short-code → long-URL lookups) →
primary DB + read replicas.

---

## 5. Deep Dive: Short-Code Generation

Two main approaches discussed:

1. **Random generation + collision check**: generate a random base62 string,
   check the DB for collision, retry if taken. Simple, but adds unbounded
   retries under high collision rates as the keyspace fills up.

2. **Counter + base62 encoding**: maintain a global monotonically
   increasing counter, encode each new value to base62. Guarantees no
   collisions, but introduces two follow-on problems:
   - **Predictability/enumeration vulnerability**: sequential codes let
     anyone enumerate all shortened URLs by incrementing the counter.
     Raised independently during the session. Mitigations: hash the
     counter value (with a fallback collision check), or use a
     bijective/Feistel-cipher-style reversible transform to make codes
     look random while remaining collision-free. Scoped as
     **awareness-level only** at this interview altitude — knowing the
     mitigation exists and why, not full implementation depth.
   - **Counter persistence/contention**: a single shared counter under
     heavy concurrent writes creates the same kind of hot-row lock
     contention seen in FinSync's ledger (see `finsync_deep_dive.md`).
     Resolved the same way: a **batch/range-allocation pattern** (a
     dedicated Key Generation Service hands out blocks of IDs, e.g.
     1,000 at a time, to each app server instance), accepting some small
     ID waste on a server crash (unused IDs in a claimed-but-unused
     block) rather than building compaction/reclamation logic.

---

## Follow-Up / Open Items (deferred, not yet explored in depth)

- [ ] Custom alias collision handling (user-supplied short codes, not just
  system-generated ones).
- [ ] Lazy vs. active expiry for TTL'd links.
- [ ] SQL vs. NoSQL choice for the main lookup table.
- [ ] Is eventual consistency acceptable for this system (e.g. read
  replicas lagging slightly behind writes)?
- [ ] Abuse/malware URL scanning before allowing a shortened link to go
  live.
- [ ] Multi-region / geo-DNS considerations for global low-latency reads.

**Date**: 2026-10-08 (session), logged 2026-10-12.
