# TSCWH — White Paper (Public Summary)

<p align="center">
  <strong>The System for Covenant-Weighted Heuristics</strong><br/>
  <em>A Self-Governing AI Safety Framework</em><br/><br/>
  Erny-Jay S. Mariquit &middot; Independent Researcher &middot; March 2026
</p>

---

## Executive Summary

TSCWH (The System for Covenant-Weighted Heuristics) is a covenant enforcement framework for AI systems. It evaluates and validates every proposed AI action against ethical covenants in real-time, ensuring that machine behavior aligns with human-defined moral principles — with zero LLM calls for safety evaluation, sub-50ms latency, and formal mathematical proofs of governance correctness.

The core innovation is the combination of multi-agent deliberation on a proprietary shared-memory architecture with formal verification. Rather than relying on static rule lists or post-hoc classifiers, TSCWH engages ten independent agents — arranged in adversarial pairs — to deliberate each action, then mathematically proves that the resulting decision satisfies all governance invariants.

## The Challenge

Existing AI safety solutions fall short:

- **Overly rigid filters** impede legitimate use and create false positives
- **Permissive classifiers** are easily bypassed by adversaries
- **Static rules** cannot adapt to evolving contexts or ethical norms
- **Multi-agent LLM systems** solve the deliberation problem but at O(N) cost and latency
- **No existing framework** provides formal mathematical guarantees on safety properties

The gap in the market is not "better guardrails" — it is **defense-in-depth with formal verification at production speed and zero marginal cost.**

## TSCWH Approach

- **Dialectical council:** Ten agents with intentional tension — each balancing caution against proaction, mercy against accountability, and analysis against advocacy — ensure balanced decisions through adversarial deliberation
- **Zero-LLM evaluation:** Deterministic evaluation functions replace LLM inference, eliminating API costs and latency
- **Proprietary shared memory:** A cache-resident data structure enables zero-overhead inter-agent communication
- **Formal verification:** Mathematical proofs of governance invariants on every evaluation cycle
- **Adaptive governance:** Probabilistic consensus and structural alignment attractors prevent drift and exploitation
- **Human-in-the-loop:** SABBATH pause suspends operation when uncertainty exceeds safe thresholds
- **ASI hardening:** Randomized audits, semantic anchoring, and sacrificial compute defend against advanced adversaries

## Performance

| Metric | TSCWH | Prior Art | Improvement |
|--------|-------|-----------|-------------|
| LLM calls / evaluation | 0* | 10+ | 100% reduction |
| Latency | < 50 ms | 1-18 seconds | 360x faster |
| Cost / evaluation | ~$0* | ~$0.10 | 94.4% reduction |
| Formal verification | Every cycle | None | New capability |
| Memory footprint | Minimal | ~100 MB/agent | Orders of magnitude reduction |

*\*Per safety evaluation. All safety-critical decisions computed deterministically.*

## Capabilities

- Evaluates every AI action in under 50 ms with zero API calls
- Detects jailbreaks and prompt injections using pattern-based multi-vector analysis
- Maintains < 2% false positive rate on legitimate actions
- Five graduated emergency shutdown levels with automatic escalation
- Governed self-modification with constitutional immutability
- 28 integrated safety mechanisms providing defense-in-depth

## Use Cases

- Enterprises integrating AI into customer-facing products requiring ethical oversight
- Regulated industries (finance, healthcare, defense) needing auditable AI governance
- Research organizations studying safe self-modifying systems
- Any deployment where AI actions must be constrained by explicit covenants
- EU AI Act compliance readiness (enforcement begins 2027)

## Licensing & Next Steps

Pilot licenses are available for qualified partners. To learn more or request an evaluation, contact **ejmariquit@tscwh.org**. All technical engagements are governed by a mutual non-disclosure agreement.

---

*This white paper contains public-facing descriptions only. Technical architectures, formulas, and source code remain confidential.*

*Patent pending. Copyright © 2026 Erny-Jay S. Mariquit. All rights reserved.*
