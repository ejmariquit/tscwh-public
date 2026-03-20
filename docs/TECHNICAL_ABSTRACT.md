# TSCWH — Technical Abstract

<p align="center">
  <strong>The System for Covenant-Weighted Heuristics</strong><br/>
  <em>Ethical AI Alignment & Covenant Safety Framework</em><br/><br/>
  Erny-Jay S. Mariquit &middot; Independent Researcher &middot; March 2026
</p>

---

## The Structural Failure in AI Safety

Large Language Models are deployed today behind guardrail systems that share a single, fatal architectural flaw: **they are monolithic classifiers making binary allow/deny decisions with no deliberation, no adaptive learning, and no mechanism to detect their own failure.**

When a jailbreak succeeds — and at current industry detection rates of 70-90%, one in every ten attacks does — there is no secondary layer to catch it, no forecasting engine that saw it coming, and no graduated response to contain the damage. The guard fails silently, completely, and often irreversibly.

This is not a tooling gap. It is a **structural absence** — the AI safety stack has no defense-in-depth.

## Why Depth Cannot Be Bolted On

Traditional guardrails (keyword filters, single-model classifiers, static rule engines) cannot be layered to create real depth because they lack three critical properties:

1. **Tension** — A single decision-maker has no internal disagreement. Without competing perspectives (caution vs. compassion, enforcement vs. grace), ethical edge cases collapse into rigid rules or silent failures.

2. **Memory** — Static classifiers have no episodic awareness. They cannot detect patterns across interactions, recognize escalation, or adapt to novel threats they haven't been explicitly trained on.

3. **Self-Awareness** — Current guardrails cannot inspect their own state. When detection degrades, confidence erodes, or adversarial conditions shift the evaluation surface, no alarm fires — the system does not know what it does not know.

## The TSCWH Architecture

TSCWH addresses all three deficits through a novel architecture:

- **Tension by Design:** Ten specialized agents arranged in adversarial pairs — each balancing caution against proaction, mercy against accountability, and analysis against advocacy — ensure that every decision is contested from multiple ethical and strategic perspectives before reaching consensus.

- **Persistent Memory:** A proprietary shared-memory architecture provides zero-copy inter-agent communication with full episodic awareness. The system remembers context, detects patterns, and recognizes escalation.

- **Structural Self-Awareness:** Formal verification proves governance invariants on every evaluation cycle. The system mathematically verifies its own correctness in real-time — not through tests, but through runtime proofs.

## Key Differentiators

| Feature | Traditional Guardrails | TSCWH |
|---------|----------------------|-------|
| Architecture | Single classifier | 10-agent dialectical council |
| Decision type | Binary (allow/deny) | Probabilistic consensus with confidence |
| LLM dependency | 1-10+ calls per eval | Zero LLM calls for safety evaluation* |
| Latency | 1-18 seconds | < 50 ms |
| Self-monitoring | None | Formal verification every cycle |
| Adversarial defense | Static patterns | Randomized audits, non-deterministic boundaries |
| Uncertainty handling | Silent failure | SABBATH pause for human review |
| Cost at scale | $100K+/day at 10^6 evals | ~$0 per safety evaluation* |

*\*TSCWH's 10-agent deliberative council, formal verification, and all governance layers operate entirely without LLM calls. Safety-critical decisions are computed deterministically.*

## Why Now

The convergence of three forces makes TSCWH urgent:

1. **EU AI Act** (enforcement begins 2027) — Requires risk assessment, human oversight, and audit trails for high-risk AI systems. TSCWH provides all three natively.

2. **Enterprise LLM Adoption** — Every Fortune 500 company is deploying LLMs into customer-facing products. Each deployment needs runtime safety that doesn't destroy latency or break the budget.

3. **Adversarial Sophistication** — Jailbreak techniques are advancing faster than single-layer defenses can adapt. Defense-in-depth is no longer optional.

## Intellectual Property

- **U.S. Provisional Patent Application** — Filed March 6, 2026 (28 novel inventions)
- **U.S. Copyright Registration** — Filed March 6, 2026 (Case #1-15114193381)
- **Trade Secret Protection** — Active (source code, algorithms, parameters)

---

**Contact:** ejmariquit@tscwh.org

*Patent pending. Copyright © 2026 Erny-Jay S. Mariquit. All rights reserved.*
