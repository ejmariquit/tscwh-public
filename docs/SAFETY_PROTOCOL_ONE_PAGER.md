# TSCWH — Safety Protocol Overview

<p align="center">
  <strong>The System for Covenant-Weighted Heuristics</strong><br/>
  <em>Erny-Jay S. Mariquit &middot; Independent Researcher &middot; March 2026</em>
</p>

---

## What It Does

TSCWH validates every AI action before it executes. It operates as a middleware layer between an LLM and its end user, enforcing moral covenants through a 10-agent dialectical council with zero LLM dependency for safety evaluation.

## Key Features

- **Multi-agent deliberation:** Every decision is reviewed by ten specialized agents representing caution, mercy, accountability, foresight, and other perspectives — arranged in adversarial pairs to prevent any single viewpoint from dominating
- **Zero LLM calls for safety evaluation:** Complete 10-agent consensus in under 50 ms with no API costs
- **Formal verification:** Mathematical proofs of governance invariants on every evaluation cycle
- **28 safety layers:** Integrated defense-in-depth including cryptographic integrity, anomaly detection, graduated shutdown, and self-monitoring
- **Proactive governance:** Predicts ethical drift before it occurs; pauses for human review (SABBATH state) when uncertain
- **Governed self-modification:** Code updates gated through a 5-stage human-approved pipeline
- **ASI hardening:** Randomized audits, semantic anchoring, sacrificial compute

## Performance Highlights

| Metric | Value |
|--------|-------|
| Full 10-agent deliberation | < 50 ms |
| LLM calls per safety evaluation | 0 |
| Cost per safety evaluation | ~$0 |
| False positive rate | < 2% |
| Self-correction accuracy | 98% |
| Emergency shutdown levels | 5 (GREEN → BLACK) |

## Emergency Response Levels

| Level | Name | Response |
|-------|------|----------|
| 1 | GREEN | Normal operation |
| 2 | YELLOW | Elevated monitoring |
| 3 | ORANGE | Restricted capabilities |
| 4 | RED | Suspend autonomous operation |
| 5 | BLACK | Complete shutdown |

## Deployment

- REST API middleware; supports Docker and on-premises installations
- Python 3.13; no GPU required
- Model-agnostic — works with any LLM or AI pipeline

## Contact

Pilot licenses available. Contact **ejmariquit@tscwh.org** with mutual NDA.

---

*Patent pending. Copyright © 2026 Erny-Jay S. Mariquit. All rights reserved.*
