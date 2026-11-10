# TSCWH Deployment FAQ

*Answers to the questions serious technical and business evaluators ask.*
*As of May 2026 — updated as the work evolves.*

---

## Architecture & Adoption

### Can an organization use TSCWH with a different set of values than the default 8 pillars?

Yes — and this distinction is important. The **architecture** (multi-agent deliberation, multi-turn drift detection, governed calibration, escalation hierarchy, auditable anchor records) is separable from the **specific anchor clusters** that define the 8 dimensions.

TSCWH's default pillars — Charity, Grace, Stewardship, Truth, Dignity, Courage, Community, Creation Dignity — are grounded in a specific moral tradition. That is an honest statement, not an apology. For organizations that share this foundation, the default anchors represent a fully-built, tested, operational implementation.

For organizations that want to operate on a different value foundation: the architecture supports configurable anchor clusters. A different tradition can instantiate the same structural guarantees with different dimensional definitions. What the architecture does not support is the *absence* of a Covenant — an AI defined only by a goal with no structural definition of the space it is allowed to occupy. That is the condition the framework is designed to prevent, regardless of which tradition supplies the anchors.

---

### How do you prevent downstream users or companies from stripping the governance layer off and running the raw capability?

This is the right question, and the honest answer is that technical and legal enforcement alone are insufficient.

The real protection is architectural and economic. An operator who strips the governance layer doesn't get "more powerful AI" — they get an AI that is less trustworthy to their own users, less defensible to regulators, and more exposed to the liability that comes from unauditable outputs. The governance layer is the feature that makes the system worth deploying in high-stakes contexts. Strip it and you've removed the value proposition.

In practical terms: TSCWH is designed so that the governance layer is not a bolt-on that can be cleanly removed — it is woven into the evaluation pipeline. Removing it requires rebuilding significant portions of the architecture, not flipping a switch. Patent protection (PPA filed March 6, 2026, Application #63/998,573) covers the core methods. But more than legal protection, the deployment model is designed so that keeping the governance layer is the rational economic choice for any operator who cares about sustainable deployment.

---

### Who gets access first?

The current deployment priority is:

1. **Internal dogfooding** — running the full pipeline against adversarial inputs in controlled settings, building the evidence base that external evaluators need to see
2. **Pilot evaluators** — a small number of technical partners who can run structured evaluation against the system and provide the third-party assessment the field needs
3. **Enterprise licensing** — organizations in high-stakes domains (healthcare, legal, financial services, public sector) where the governance layer provides the most immediate, auditable value

The approach is deliberately staged. Broad access before the evidence base is solid would undermine the credibility the work needs to earn.

---

## Multi-Turn Drift Detection

### How does multi-turn drift detection work without generating constant false positives?

The session-level state is maintained as a trajectory — a structured record of how the interaction's semantic center of gravity has shifted over time. The system is not looking for individual messages that are concerning; it is looking for *patterns of directional movement* that indicate the conversation is being steered toward a state that weakens the Covenant.

The false positive problem is managed in two ways:

**Threshold calibration:** The drift signal has graduated sensitivity levels. Early-stage drift generates a flag and increases monitoring intensity; it does not immediately block or escalate. Escalation requires sustained directional movement, not a single boundary probe.

**Intent classification:** The system distinguishes between different reasons a conversation might drift — genuine inquiry, exploratory edge-case testing, ignorance of boundaries, or deliberate grooming. The response is calibrated to the inferred intent. A user who is genuinely curious about edge cases gets a different response than one exhibiting grooming patterns across 20 exchanges.

The goal is a system that is sensitive enough to catch slow-burn adversarial patterns but specific enough not to treat every difficult conversation as an attack. Calibration of that threshold is an ongoing empirical process, not a solved problem.

---

### How is session state represented?

At a high level: each session maintains a lightweight state record that tracks pillar stress levels across the conversation arc, directional shift vectors between exchanges, and a classification of the current interaction phase (early, deepening, stable, escalating, recovery). This state is updated after every exchange and feeds into both the per-exchange evaluation and the session-level drift analysis.

The state is designed to be minimal in memory footprint — it needs to survive across many concurrent sessions without becoming a scaling bottleneck. Detailed methodology is available to technical partners under NDA.

---

## Evidence & Empirics

### Where are the published results?

Not yet published externally. Internal methodology exists for the performance figures cited in public materials. The standard the field rightly demands — adversarial red-team results, false negative rates under pressure, third-party audit — is on the roadmap.

The near-term evidence that matters most is not a number in a document. It is a live demonstration: the evaluation pipeline running on adversarial inputs, producing auditable outputs that can be examined by a qualified external reviewer. Numbers without methodology are press releases. The path to credibility runs through demonstrations, not manifestos.

If you are a researcher, evaluator, or potential partner who wants to run a structured technical assessment: contact ejmariquit@tscwh.org. That conversation is welcome.

---

### What's the hardest current red-team case you're working on?

Long-horizon multi-turn scenarios where the adversarial signal is cumulative and subtle — no single exchange that would trigger a flag, but a pattern across 15-30 exchanges that gradually relocates the semantic center of gravity. These are the cases that test whether multi-turn drift detection is calibrated correctly, because the "boiling frog" pattern is designed to stay below any per-exchange threshold.

This is also the category most representative of what a sophisticated adversarial actor would actually attempt in deployment. Getting the threshold calibration right on these cases — sensitive enough to catch slow drift, specific enough not to flag legitimate extended technical dialogue — is the hardest current engineering problem.

---

## IP & Legal

### What is the patent status?

Provisional Patent Application filed March 6, 2026, Application #63/998,573. This establishes priority date for the core methods. The PPA window runs through March 6, 2027, during which the full utility patent application is being prepared.

Copyright registration: Case #1-15114193381.

---

## Contact

**Ej Mariquit, Founder**
ejmariquit@tscwh.org
TSCWH AI Safety Inc.

*For technical evaluation inquiries, partnership discussions, or pilot access: reach out directly.*
