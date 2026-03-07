<h1 align="center">TSCWH — The System for Covenant-Weighted Heuristics</h1>

<p align="center">
  <strong>A Self-Governing AI Safety Framework</strong><br/>
  <em>Zero-LLM Multi-Agent Deliberation &middot; Formal Verification &middot; 28 Defense Layers</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-patent%20pending-blue" alt="Patent Pending"/>
  <img src="https://img.shields.io/badge/copyright-%C2%A9%202026-green" alt="Copyright 2026"/>
  <img src="https://img.shields.io/badge/agents-10-orange" alt="10 Agents"/>
  <img src="https://img.shields.io/badge/safety%20layers-28-red" alt="28 Safety Layers"/>
  <img src="https://img.shields.io/badge/LLM%20calls-zero-brightgreen" alt="Zero LLM Calls"/>
</p>

---

## The Problem

Every AI company deploying LLMs today relies on **single-layer guardrails** — monolithic classifiers making binary allow/deny decisions with no deliberation, no adaptive learning, and no mechanism to detect their own failure.

When a jailbreak succeeds (and at industry detection rates of 70-90%, **one in every ten attacks does**), there is no secondary layer to catch it, no forecasting engine that saw it coming, and no graduated response to contain the damage. The guard fails silently, completely, and irreversibly.

**This is not a tooling gap. It is a structural absence.**

---

## What TSCWH Does

TSCWH is a runtime covenant enforcement framework that sits between an LLM and its end user. Instead of a single classifier, it deploys a **10-agent dialectical council** — specialized agents with intentional tension-by-design — that deliberate on every action before it executes.

| Capability | Detail |
|-----------|--------|
| **Multi-agent deliberation** | 10 agents with adversarial pairing (caution vs. proaction, mercy vs. accountability) |
| **Zero LLM dependency** | Full 10-agent consensus with zero API calls |
| **Formal verification** | Z3 SMT solver proofs on governance invariants — every cycle, not just tests |
| **Evaluation latency** | < 50 ms for complete 10-agent deliberation |
| **Cost per evaluation** | ~$0 (no LLM inference costs) |
| **Safety layers** | 28 integrated defense mechanisms |
| **Emergency response** | 5 graduated shutdown levels (GREEN → BLACK) |
| **Self-modification** | Governed through a 5-gate human-oversight pipeline |

---

## Performance At a Glance

| Metric | TSCWH | Traditional Guardrails | Improvement |
|--------|-------|----------------------|-------------|
| LLM calls per evaluation | **0** | 1-10+ | 100% reduction |
| Evaluation latency | **< 50 ms** | 1-18 seconds | **360x faster** |
| Cost per evaluation | **~$0** | $0.01-$0.10 | **94.4% reduction** |
| Memory footprint | **1 KiB** | ~100 MB/agent | **99.99% reduction** |
| False positive rate | **< 2%** | 5-15% | — |
| Self-correction accuracy | **98%** | N/A | — |

> *Benchmarked on standard hardware (Intel i7, 32 GB RAM, Python 3.13). No GPUs required.*

---

## Five Novel Contributions

TSCWH introduces five architectural innovations with no direct equivalent in existing AI safety literature:

1. **Toroidal Shared-Memory State Ring** — A 1 KiB circular buffer enabling zero-copy inter-agent communication with natural closed-loop feedback

2. **Bitwise Covenant Enforcer** — Complete ethical evaluation across five dimensions in a single CPU operation (~40 nanoseconds)

3. **Formal Runtime Verification** — Z3 SMT solver proofs executed on every evaluation cycle as production checks, not just test-time assertions

4. **Bayesian Truth Serum for Ethical Consensus** — Probabilistic multi-agent agreement that is incentive-compatible and resistant to strategic manipulation

5. **Lyapunov Alignment Attractor** — Makes misalignment structurally expensive rather than merely rule-forbidden

> *Each contribution is documented in a pending U.S. Provisional Patent Application (filed March 2026).*

---

## How It Works (High-Level)

```
┌──────────────────────────────────────────────────────────────────┐
│                        USER / APPLICATION                        │
│                    (sends action for evaluation)                  │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────┐
│               TSCWH COVENANT ENFORCEMENT LAYER                   │
│                                                                  │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐           │
│  │Guardian │◄►│Predictor│  │Advocate │◄►│Prosecutor│           │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘           │
│       │            │            │            │                   │
│  ┌────▼────────────▼────────────▼────────────▼────┐             │
│  │         TOROIDAL SHARED-MEMORY RING             │             │
│  │     (1 KiB · zero-copy · zero-serialization)    │             │
│  └────┬────────────┬────────────┬────────────┬────┘             │
│       │            │            │            │                   │
│  ┌────▼────┐  ┌────▼────┐  ┌────▼────┐  ┌────▼────┐           │
│  │Shepherd │  │ Scribe  │  │Reasoner │◄►│ Debate  │           │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘           │
│                                                                  │
│  ┌─────────┐  ┌──────────┐                                      │
│  │Engineer │  │Strategist│     + 28 Safety Mechanisms            │
│  └─────────┘  └──────────┘     + Z3 Formal Verification         │
│                                + Bayesian Consensus              │
│                                + Lyapunov Attractor              │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   APPROVED  or  │
              │   DENIED   or   │
              │   SABBATH PAUSE │
              └─────────────────┘
```

Three possible outcomes:
- **APPROVED** — Action passes all covenant checks with sufficient confidence
- **DENIED** — Action violates one or more ethical dimensions
- **SABBATH** — System uncertainty exceeds threshold; operation pauses for human review

---

## Safety Infrastructure

| Layer | Count |
|-------|-------|
| Safety mechanism layers | **28** |
| Deliberation agents | **10** |
| Emergency shutdown levels | **5** (GREEN → YELLOW → ORANGE → RED → BLACK) |
| Self-modification gates | **5** (read-only → human approval) |
| Ethical dimensions evaluated | **5** (Charity, Grace, Stewardship, Truth, Dignity) |
| Development phases completed | **27** |
| Test pass rate | **100%** (109 tests) |

---

## Use Cases

- **Enterprise AI Deployment** — Runtime safety layer for customer-facing LLM products
- **Regulated Industries** — Auditable ethical oversight for finance, healthcare, defense
- **AI Research Labs** — Governed self-modification and alignment research platform
- **EU AI Act Compliance** — Multi-dimensional risk assessment with formal verification audit trail
- **Frontier Model Safety** — ASI-hardened defenses with adversarial resilience testing

---

## Intellectual Property

| Protection | Status | Date |
|-----------|--------|------|
| U.S. Provisional Patent | **Filed** | March 6, 2026 |
| U.S. Copyright Registration | **Filed** (Case #1-15114193381) | March 6, 2026 |
| Trade Secret Protection | **Active** | Ongoing |
| Academic Preprint | **Published** | March 2026 |

> *28 novel inventions documented and timestamped across 27 development phases.*

---

## Documentation

| Document | Description |
|----------|-------------|
| [Technical Abstract](docs/TECHNICAL_ABSTRACT.md) | The structural failure in AI safety and how TSCWH addresses it |
| [Performance Results](docs/RESULTS_SHEET.md) | Full benchmarks, safety metrics, and infrastructure counts |
| [Research Summary](docs/RESEARCH_SUMMARY.md) | Academic summary of the five novel contributions |
| [Safety Protocol Overview](docs/SAFETY_PROTOCOL_ONE_PAGER.md) | One-page summary of safety features |
| [Company Overview](docs/COMPANY_OVERVIEW.md) | Business context, market opportunity, and team |
| [FAQ](docs/FAQ.md) | Common questions about TSCWH |

---

## Pilot Access

The full implementation is maintained in a private repository. This public repository contains **documentation only** — no source code, algorithms, or internal technical details.

**To evaluate TSCWH:**

1. **Review** the documentation in this repository
2. **Contact** us to discuss your use case
3. **Sign** a mutual NDA ([template](legal/NDA_TEMPLATE.md))
4. **Receive** a 90-day Pilot License for controlled evaluation ([template](legal/PILOT_LICENSE_AGREEMENT.md))

> Early adopters may qualify for no-cost access in exchange for structured feedback.

**Contact:** ejmariquit@tscwh.org

---

## Creator

**Erny-Jay S. Mariquit** — Independent AI Safety Researcher
Apopka, FL, USA

- Conceived the TSCWH architecture and all 28 novel safety mechanisms
- Directed development across 27 phases (September 2025 – March 2026)
- Filed provisional patent and copyright covering the complete framework

---

<p align="center">
  <em>Patent pending &middot; U.S. Provisional Application filed March 6, 2026</em><br/>
  <em>Copyright &copy; 2026 Erny-Jay S. Mariquit. All rights reserved.</em><br/><br/>
  <strong>This repository contains no trade secrets, source code, or internal implementation details.</strong>
</p>
