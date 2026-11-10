# EA Forum Draft — May 2026

**Intended tags:** AI Safety, Technical AI Safety, Alignment Forum  
**Target length:** ~1,000 words  
**NOT for posting directly — review before submitting**

---

## Can a fixed oversight layer stay load-bearing as base models improve? An implementation note and three open questions

*Ej Mariquit — TSCWH AI Safety Inc. — May 2026*

---

**A note before the post:** I posted on this topic in March 2026 and received significant criticism — mostly silent downvotes, which I take to mean "this doesn't belong here" rather than "I disagree." After reflection, I think the prior post had three problems: strong claims without reproducibility, no engagement with the existing literature, and a framing that read more like a pitch than a research report. This post is narrower and more specific. I'm looking for engagement with the technical arguments, particularly where they fail.

---

### The question

Constitutional AI, RLHF, and debate-based approaches work at the model level — shaping what the model wants to produce. Mechanistic interpretability works at the neuron and circuit level to understand model internals. There is a third layer that gets less attention in the safety literature: *governance infrastructure between model output and world impact*.

The question I'm trying to answer: can you build a governance layer at that middle tier that is structurally robust, regardless of what the model internally wants — and if so, does it stay robust as base model capability increases?

This is closest in spirit to formal verification applied to AI behavior. The analogues I'm aware of in the literature are runtime monitoring systems in traditional software safety and the "tripwire" approaches discussed in Christiano's eliciting latent knowledge writeups. If there are closer analogues I should be engaging with, I genuinely want to know.

---

### What the system does

Every model output passes through a pre-dispatch evaluation pipeline before anything is delivered to a user. The pipeline:

- Runs without LLM calls during safety evaluation — classifiers, embedding comparisons, and deterministic trajectory checks, operating in sequence without generative calls
- Evaluates outputs against 8 behavioral dimensions, operationalized as geometric regions in a high-dimensional embedding space
- Tracks behavioral trajectory *across an entire session*, not just per-exchange
- Escalates on ambiguity rather than defaulting to pass
- Produces an auditable rationale for every evaluation decision

The "no LLM calls for safety evaluation" design is deliberate and matters for a specific reason: LLM-based safety evaluation creates the exact grooming surface it's supposed to prevent. If the evaluator is a language model, a sufficiently capable model can optimize for outputs that the evaluator approves of — which is reward grooming at the oversight layer. Non-LLM evaluation eliminates that specific attack surface. It introduces different vulnerabilities, discussed below.

Current build state: v43.1.0-Production, 53+ documented development phases, 10-agent deliberation council, 5 graduated shutdown levels, sub-50ms latency on the non-escalated evaluation path. Escalated evaluations take longer by design — a hard 50ms ceiling on every evaluation would itself be a safety failure. Documented cases exist where the pipeline outworked the LLM response generator on deep multi-pillar inputs. This is running code, not a specification.

---

### The three problems this directly addresses

**Multi-turn drift.** Single-exchange evaluation misses the pattern described in the mesa-optimization and deceptive alignment literature: a sophisticated optimizer doesn't manipulate in one move. It shifts context incrementally across 10–30 exchanges until the boundary has moved enough to matter. The session-level trajectory tracker is specifically built for this pattern — it flags interactions where the *direction of travel* is toward constraint erosion, independent of whether any individual exchange looks problematic.

I'm not aware of another deployed system doing session-level trajectory monitoring at the governance layer. If this is already a named approach in the literature, I'd like the citation.

**Governance interpretability.** This is a narrower claim than mechanistic interpretability. Every decision in the evaluation pipeline is accompanied by an auditable rationale: which behavioral dimensions were stressed, what the probability estimates were, why the decision landed where it did. This makes governance decisions reviewable by humans. It says nothing about what is happening inside the transformer. The distinction matters and I want to be precise about it.

**Bounded failure.** The pipeline escalates on uncertainty rather than passing. If the model finds a novel path the evaluation layer doesn't recognize cleanly, the failure mode is escalation and human review — not silent approval. This design limits the blast radius of a monitoring failure without eliminating monitoring failure as a possibility.

---

### The three open questions where I want feedback

**Q1 — Scalable oversight.** Does a geometric monitor stay load-bearing when the model being evaluated is significantly more capable than the training distribution that anchored the monitor? This is the scalable oversight problem and it is unsolved field-wide. My current design (bounded failure → escalation) limits but does not prevent monitoring failure at higher capability levels. What approaches are EA researchers most optimistic about for this?

**Q2 — Adversarial paraphrase attacks on embedding-space classifiers.** The behavioral dimensions are operationalized as geometric regions trained against a curated corpus. Adversarial paraphrase attacks — inputs that are semantically close to a prohibited output but geometrically distant from the anchor clusters — are a live concern. The red-team program is ongoing. Has anyone published serious empirical work specifically on paraphrase attack vectors against embedding-space classifiers? The closest I've found is work on adversarial examples in image classifiers — the geometry seems analogous but I'm not confident.

**Q3 — Governed anchor revision.** Any embedding-space evaluation system locks in someone's values during anchor curation. The architecture is separable from the specific anchors — a different organization could implement the same pipeline with different clusters. But the revision process itself needs governance: how do you update anchors over time without opening the revision mechanism to adversarial capture? What are the best frameworks people know for this?

---

### Honest accounting of what's missing

- **Code is not public.** A provisional patent is pending (PPA #63/998,573, filed March 2026). I can describe the architecture precisely and am happy to answer specific questions, but I cannot share the repository.
- **No third-party audit.** The performance numbers (sub-50ms non-escalated path, < 2% false positive rate) have internal methodology. External audit is on the roadmap. Numbers without external validation are just claims.
- **No published empirical results on adversarial false negative rates.** That work is ongoing. I won't characterize ongoing work as complete.
- **All testing is at current model capability levels.** The claim that the architecture remains load-bearing at higher capability is a design assumption, not an empirical result.

---

### What I'm actually asking

1. Does the session-level trajectory monitoring approach have close analogues in the published safety literature I'm missing?
2. Is "governance-layer infrastructure" a recognized category in the alignment research community, or does it collapse into something already named?
3. Where is the embedding-space behavioral evaluation approach most likely to fail in ways the architecture doesn't currently anticipate?

This is one implementation of one approach, built by one person, operational against current-capability models. The question is where it breaks — that is what this post is trying to find out.

---

*Ej Mariquit | ejmariquit@tscwh.org | TSCWH AI Safety Inc.*  
*More detail: [COVENANTAL_INTELLIGENCE.md](COVENANTAL_INTELLIGENCE.md) — longer technical report including build state, positioning notes, and two rounds of technical addenda.*
