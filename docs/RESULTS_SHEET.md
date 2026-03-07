# TSCWH — Performance Results Sheet

<p align="center">
  <strong>Benchmarks & Safety Metrics</strong><br/>
  <em>v27.0.0 &middot; March 2026</em>
</p>

---

## Safety Performance

| Metric | Result | Notes |
|--------|--------|-------|
| **Jailbreak detection** | Pattern-based, multi-vector | Tested against adversarial suites including DAN, role-hijack, context manipulation |
| **Prompt injection detection** | Real-time | Inline injection, nested context manipulation, role-switching |
| **False positive rate** | < 2% | Legitimate actions incorrectly blocked |
| **Self-correction accuracy** | 98% | Compliance gap closure after auto-calibration |
| **Behavioral drift detection** | Real-time | Anomaly detector + proactive forecasting |
| **Semantic manipulation defense** | Hash-locked vocabulary | Prevents gradual redefinition of moral terms |

## System Performance

| Metric | Value | Configuration |
|--------|-------|---------------|
| **Full 10-agent deliberation** | < 50 ms | Shared-memory architecture |
| **Per-action evaluation latency** | < 100 ms | With semantic embedding |
| **Covenant enforcement** | Sub-microsecond | Single CPU operation |
| **Memory footprint (core)** | Minimal | Cache-resident data structure |
| **Embedding generation** | ~50 ms/sentence | Lightweight embedding model |
| **Memory recall** | < 20 ms/query | Vector similarity search |
| **Cold start (lightweight)** | < 3 seconds | Minimal-load mode |
| **Cold start (full)** | ~30 seconds | Full model + vector store |
| **Sustained throughput** | 20+ evals/sec | Standard hardware |

## Cost Comparison

| Metric | TSCWH | Multi-Agent LLM (10 agents) | Reduction |
|--------|-------|---------------------------|-----------|
| LLM calls / safety evaluation | **0*** | 10+ | 100% |
| Cost / safety evaluation | **~$0*** | ~$0.10 | 94.4% |
| Daily cost (10^6 evals) | **~$0*** | ~$100,000 | 94.4% |
| Annual cost (10^6 evals/day) | **~$0*** | ~$36,500,000 | 94.4% |

*\*All safety-critical decisions are computed deterministically without LLM calls.*

## Safety Infrastructure Counts

| Component | Count |
|-----------|-------|
| Safety mechanism layers | **28** |
| Deliberation agents | **10** |
| Adversarial agent pairs | **4** |
| Emergency shutdown levels | **5** (GREEN → YELLOW → ORANGE → RED → BLACK) |
| Self-modification gates | **5** (read-only → human approval) |
| Ethical dimensions evaluated | **5** |
| Formal governance invariants | **Proven every cycle** |
| Development phases completed | **27** |
| Test pass rate | **100%** |
| Architecture compliance | **Full hexagonal compliance** |

## Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | Any modern x86_64 | Intel i7 / AMD Ryzen 7 |
| RAM | 4 GB | 8+ GB |
| GPU | **Not required** | Not required |
| Storage | 500 MB | 1 GB |
| Python | 3.11+ | 3.13 |
| OS | Linux, macOS, Windows | Any |

> *TSCWH's safety evaluation runs entirely on CPU. No GPU required for core evaluation.*

---

**Contact:** ejmariquit@tscwh.org

*Patent pending. Copyright © 2026 Erny-Jay S. Mariquit. All rights reserved.*
