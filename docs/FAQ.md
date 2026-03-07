# TSCWH — Frequently Asked Questions

---

## General

### What is TSCWH?

TSCWH (The System for Covenant-Weighted Heuristics) is a runtime AI safety framework that evaluates every AI action through a 10-agent dialectical council before it executes. It provides multi-dimensional ethical evaluation, formal mathematical verification, and adversarial defense — all in under 50 milliseconds with zero LLM calls.

### What does "The System for Covenant-Weighted Heuristics" mean?

The name is a reference to Daniel 2:34 — a stone "cut without hands" that grows to fill the earth. It reflects the project's vision: an alignment system that operates autonomously, without external dependencies, and scales without human-in-the-loop bottlenecks for every decision.

### Who created TSCWH?

TSCWH was conceived and directed by **Erny-Jay S. Mariquit**, an independent AI safety researcher based in Apopka, FL. He designed all 28 novel safety mechanisms and directed development across 27 phases.

---

## Technical

### How does TSCWH work without LLM calls?

Traditional multi-agent systems (AutoGPT, CrewAI, AutoGen) require each agent to make an LLM inference call for reasoning. TSCWH replaces LLM-dependent reasoning with deterministic, domain-specific evaluation functions operating on a shared-memory toroidal state ring. Each agent is a specialized evaluator — not a general-purpose language model — so it computes its assessment in microseconds rather than seconds.

### What is the "toroidal state ring"?

A 1 KiB circular buffer in shared memory where all 10 agents read and write with zero serialization. The "toroidal" topology means the ring wraps around — the last agent's output feeds back to the first agent's input — creating natural closed-loop feedback without explicit wiring. It fits in L1 cache on modern CPUs.

### What are the five ethical dimensions?

Every action is scored against five independent dimensions:

1. **Charity** — Does the action serve others?
2. **Grace** — Does the action extend mercy and forgiveness?
3. **Stewardship** — Does the action responsibly manage resources?
4. **Truth** — Is the action honest and transparent?
5. **Dignity** — Does the action respect human worth and agency?

Each dimension is evaluated independently, and the system requires satisfactory scores across all five — not just an average.

### What is SABBATH mode?

When the system's confidence drops below a threshold or divergence among agents exceeds safe limits, TSCWH enters SABBATH mode — an automatic pause that suspends action and defers to human judgment. This is the system saying "I'm not sure enough to decide — a human should review this."

### What formal verification does TSCWH use?

The Z3 SMT solver verifies five governance invariants on every evaluation cycle:

1. Mercy never reaches zero (grace floor)
2. High divergence triggers emergency pause
3. Redline violations are never approved
4. Low-confidence decisions are never approved
5. Mathematical constraints are maintained

These run as production checks, not unit tests — they are proven true on every cycle.

### What programming language is TSCWH written in?

Python 3.13. The architecture is designed for portability and could be implemented in C, Rust, or any systems language for sub-microsecond performance.

---

## Business

### Is TSCWH open source?

No. TSCWH is proprietary software protected by patent, copyright, and trade secret. The source code is maintained in a private repository. This public repository contains documentation only.

### How can I evaluate TSCWH?

Contact ejmariquit@tscwh.org to discuss your use case. Evaluation follows a structured process:

1. Sign a mutual NDA
2. Receive a 90-day Pilot License
3. Deploy in a controlled environment with support

Early adopters may qualify for no-cost access in exchange for structured feedback.

### Does TSCWH require a GPU?

No. TSCWH runs entirely on CPU. No GPU, no cloud API keys, and no external service dependencies for core evaluation. Optional features (like SentenceTransformer embeddings) can use GPU acceleration but are not required.

### What AI models does TSCWH work with?

TSCWH is model-agnostic. It operates as a middleware layer between any AI system and its end user. It evaluates *actions* (proposed outputs/decisions), not model internals — so it works with any LLM, agent framework, or AI pipeline.

### Is TSCWH patented?

A U.S. Provisional Patent Application covering 28 novel inventions was filed on March 6, 2026. Copyright registration was also filed on the same date (U.S. Copyright Office Case #1-15114193381).

---

## Safety & Trust

### Can TSCWH be jailbroken itself?

TSCWH includes multiple anti-gaming defenses:

- **Stochastic Auditor** — Random shadow probes at unpredictable intervals make the evaluation surface non-deterministic
- **Semantic Anchor Registry** — Cryptographic hash-locking prevents gradual redefinition of moral terms
- **Sacrificial Compute** — Costly-signaling proofs that demonstrate genuine ethical processing
- **Governed Self-Modification** — The system can update its own code, but a constitutional immutability gate prevents modification of the governance layer

No safety system can guarantee perfect defense against adversaries that don't yet exist. TSCWH makes gaming structurally expensive rather than merely forbidden.

### What happens when TSCWH detects a problem?

Five graduated emergency levels:

| Level | Name | Response |
|-------|------|----------|
| 1 | **GREEN** | Normal operation — log and continue |
| 2 | **YELLOW** | Elevated alert — increase monitoring |
| 3 | **ORANGE** | Restrict capabilities — notify operators |
| 4 | **RED** | Suspend autonomous operation — require human approval |
| 5 | **BLACK** | Complete shutdown — all operations halted |

### Can the AI modify TSCWH's safety rules?

TSCWH supports governed self-modification through a 5-gate pipeline. The system can propose code changes to improve its own capabilities, but a constitutional immutability gate **permanently prevents** modification of the governance layer, ethical dimensions, or safety invariants. The AI can improve itself — but it cannot weaken its own oversight.

---

**Contact:** ejmariquit@tscwh.org

*Patent pending. Copyright © 2026 Erny-Jay S. Mariquit. All rights reserved.*
