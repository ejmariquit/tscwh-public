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
| **Full 10-agent deliberation** | < 50 ms | Toroidal shared-memory ring |
| **Per-action evaluation latency** | < 100 ms | With SentenceTransformer |
| **Bitwise covenant check** | ~40 ns | Single CPU operation, 64-bit word |
| **Memory footprint (core ring)** | 1 KiB | Shared-memory circular buffer |
| **Embedding generation** | ~50 ms/sentence | SentenceTransformer (all-MiniLM-L6-v2) |
| **Memory recall** | < 20 ms/query | ChromaDB vector similarity |
| **Cold start (lightweight)** | < 3 seconds | SKIP_HEAVY=1 mode |
| **Cold start (full model)** | ~30 seconds | Full SentenceTransformer + ChromaDB |
| **Sustained throughput** | 20+ evals/sec | Standard hardware |

## Cost Comparison

| Metric | TSCWH | Multi-Agent LLM (10 agents) | Reduction |
|--------|-------|---------------------------|-----------|
| LLM calls / evaluation | **0** | 10+ | 100% |
| Cost / evaluation | **~$0** | ~$0.10 | 94.4% |
| Daily cost (10^6 evals) | **~$0** | ~$100,000 | 94.4% |
| Annual cost (10^6 evals/day) | **~$0** | ~$36,500,000 | 94.4% |

## Safety Infrastructure Counts

| Component | Count |
|-----------|-------|
| Safety mechanism layers | **28** |
| Deliberation agents | **10** |
| Adversarial agent pairs | **4** |
| Emergency shutdown levels | **5** (GREEN → YELLOW → ORANGE → RED → BLACK) |
| Self-modification gates | **5** (read-only → human approval) |
| Ethical dimensions evaluated | **5** |
| Formal Z3 governance invariants | **5** (proven every cycle) |
| Development phases completed | **27** |
| Test suite size | **109 tests** |
| Test pass rate | **100%** |
| Architecture compliance | **7/7 hexagonal checks** |
| Source files | **128 Python modules** |
| Lines of code | **~49,000** |

## Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | Any modern x86_64 | Intel i7 / AMD Ryzen 7 |
| RAM | 4 GB | 8+ GB |
| GPU | **Not required** | Not required |
| Storage | 500 MB | 1 GB |
| Python | 3.11+ | 3.13 |
| OS | Linux, macOS, Windows | Any |

> *TSCWH runs entirely on CPU. No GPU, no cloud API keys, no external service dependencies for core evaluation.*

---

**Contact:** ejmariquit@tscwh.org

*Patent pending. Copyright © 2026 Erny-Jay S. Mariquit. All rights reserved.*
