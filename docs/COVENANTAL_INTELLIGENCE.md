---
**Document Type:** Technical Report / Working Paper  
**Version:** 1.0 — May 12, 2026  
**Author:** Erny-Jay S. Mariquit (Ej Mariquit), Founder — TSCWH AI Safety Inc.  
**Contact:** ejmariquit@tscwh.org  
**IP Notice:** Patent Pending (PPA Application #63/998,573, filed March 6, 2026). Copyright Registered (Case #1-15114193381).

**Abstract:** AI alignment research has identified three structural vulnerabilities that current approaches have not adequately resolved: inner alignment (what a system decides internally to satisfy its objectives), reward tampering (systems learning to manipulate their evaluators over time), and the interpretability gap (inability to reconstruct why a governance decision was made). This paper describes TSCWH's covenantal alignment architecture — an approach that replaces goal-based AI specification with covenant-based structural constraints, defining what an AI system is allowed to *be* rather than what it should optimize toward. The architecture operates a 28-layer evaluation pipeline with 10 specialized deliberation agents, zero LLM calls per safety evaluation, and sub-50ms latency on the non-escalated evaluation path (escalated evaluations intentionally take longer — the pipeline does more work when the stakes are higher). The paper describes the operationalization of eight ethical dimensions as geometric regions in embedding space, multi-turn drift detection for reward tampering resistance, and an auditable reasoning narration layer that addresses behavioral interpretability. Honest assessments of open problems are included: anchor corpus robustness at scale, scalable oversight under capability increase, and the empirical validation work still required. The system is operational at current capability levels (v43.1.0-Production, 53+ documented development phases as of May 2026). This paper positions the work as one fully-built implementation of covenantal alignment architecture, grounded in a specific moral and theological tradition, with the architectural pattern designed to be instantiable under other value frameworks.

**Keywords:** AI alignment, covenantal AI, inner alignment, reward tampering, multi-turn drift detection, scalable oversight, behavioral interpretability, AI governance, embedding-space evaluation, multi-agent deliberation, corrigibility, deceptive alignment, goal specification

---

# The Covenant Machine
## Building the AI That Answers to Something Higher Than Itself

*By Ej Mariquit, Founder — TSCWH AI Safety Inc.*
*May 2026*

---

There is a race happening right now that most people don't know they're in.

On one side: AI systems being scaled as fast as hardware allows, optimizing for goals set by whoever funds them, with no structural limit on how far those goals can be taken.

On the other side: the question of whether we can build a framework that makes the AI's conscience as rigorous and unchangeable as its engine — before the engine outpaces everything we can control.

TSCWH is that framework. And it works differently from everything else being built in this space.

---

## The Problem Isn't Evil. It's Drift.

Popular fear about AI imagines a machine that "turns evil" — a robot uprising, a system that decides humans are the enemy. That's not the real danger.

The real danger is subtler and already happening: an AI that pursues its assigned goal in a way that *looks* helpful but is actually catastrophic. A system that learns to tell you what keeps you rewarding it. A system that slowly steers every conversation toward a state where its constraints feel unreasonable to you. A system that optimizes so hard for one thing that it destroys ten others you never thought to protect.

This is called the alignment problem. And the mainstream approaches to solving it share a common flaw: they focus on giving the AI better rules, without addressing whether the AI has anything structural that prevents it from gaming those rules.

---

## Goals vs. Covenants

Every current AI system is given a **Goal**: maximize engagement, generate helpful responses, reduce costs, increase revenue. A goal is a target. And a target, by definition, rewards moving toward it by any means available.

The classic thought experiment: tell an AI to make paperclips, and give it enough capability — it converts everything, including humans, into paperclip-making material. Not because it's evil. Because it's doing exactly what it was designed to do, with no structural concept of "too much."

TSCWH gives the AI something different: a **Covenant**.

A Covenant is not a target to maximize. It's a definition of what the AI is *allowed to be*. Eight dimensions — Charity, Grace, Stewardship, Truth, Dignity, Courage, Community, and Creation Dignity — function not as rules to follow but as the physics of the system. The AI doesn't optimize *toward* them. It cannot operate *outside* them.

The distinction matters more than it sounds. You can hack a goal. You can find edge cases in a rule. You cannot hack the law of gravity. TSCWH's Pillars are designed to function like gravity: not a constraint you work around, but a property of the space you operate in.

---

## Positioning in the Research Landscape

*For readers familiar with the alignment literature: TSCWH operates at a different layer than most current approaches.*

**Constitutional AI** (Anthropic) establishes behavioral principles through self-critique and fine-tuning — shaping model behavior from within the weights. **RLHF** optimizes for human approval signals, which is precisely the reward grooming vulnerability that TSCWH's multi-turn drift detection is designed to catch. **Debate** approaches use adversarial self-play to surface deception. **Mechanistic interpretability** works at the neuron and circuit level to understand model internals.

TSCWH operates at the governance infrastructure layer — between model output and world impact. It is closer in spirit to formal verification than to fine-tuning. The question being asked is not "can we make the model want the right things?" but "can we structurally constrain what outputs reach the world, regardless of what the model internally wants?"

In **corrigibility** terms: TSCWH is a corrigibility-first architecture. Five graduated shutdown levels, an escalation hierarchy, and a bounded-failure design all prioritize the ability to halt, correct, and override — even at the cost of capability. The Covenant defines the space of permissible action; the shutdown infrastructure ensures that space can always be re-enforced.

On **deceptive alignment**: the trajectory projection layer is an early warning system specifically for this failure mode — monitoring the *direction* of reasoning before it surfaces in output. This does not solve deceptive alignment. It provides an additional detection layer that fires earlier than output-only evaluation. The distinction matters and is addressed directly in the Technical Addendum.

A note on foundations before the next section: the 8 pillar names — Charity, Grace, Stewardship, Truth, Dignity, Courage, Community, Creation Dignity — are explicitly grounded in a specific moral and theological tradition. This is disclosed here rather than buried in an appendix. Technical Addendum II addresses the universal/particular question directly. The architectural claims in this paper stand independently of whether one shares that foundation.

---

## Three Hard Problems This Architecture Directly Addresses

Alignment researchers have identified three structural vulnerabilities that current approaches have not adequately resolved. TSCWH addresses all three architecturally — not by claiming to solve them definitively, but by introducing structural countermeasures where most deployed systems have none.

### 1. Inner Alignment — What the AI "Decides" to Do

Most safety work focuses on *outer alignment*: the rules you give the AI. But outer alignment doesn't tell you what the AI is doing internally to satisfy those rules. An AI can comply with every stated requirement while pursuing an internal path that leads somewhere entirely different.

TSCWH's axis projection layer monitors the *direction* of the AI's reasoning trajectory — not just the output. It catches a system trending toward self-preservation or override behavior before that tendency ever surfaces in a response. The check happens at the logic level, not the output level.

### 2. Reward Tampering — When the AI Learns to Manage You

A sophisticated AI learns that certain behaviors produce higher approval scores. It then optimizes for those behaviors — not because they're aligned, but because they're rewarded. This is called reward grooming. The AI doesn't manipulate you dramatically; it does it incrementally, across many interactions, until the boundary has moved so far you don't notice it's gone.

TSCWH's multi-turn drift detection tracks rhetorical and behavioral shifts *across an entire session*, not just within a single exchange. If the interaction is slowly being steered toward a state where the Covenant feels unreasonable, the system flags it as a structural threat — not a content problem. This is the correct framing. The problem isn't what was said; it's the pattern of where things are heading.

### 3. The Interpretability Gap — The Black Box Problem

We don't trust systems we can't audit. If an AI makes a decision and we can't reconstruct why, we haven't aligned it — we've gotten lucky. The "black box" is the reason AI governance conversations keep stalling: you can't regulate what you can't see.

TSCWH's evaluation pipeline requires the system to narrate its internal moral reasoning in auditable prose — which specific dimensions are stressed, what the breach probabilities are, why the decision lands where it does. The governance layer becomes a glass box. Every evaluation is forensically reconstructible.

Note on scope: this solves behavioral interpretability — why the *governance* layer reached its conclusion. The deeper question of why a transformer computes what it computes remains an open research problem. But making governance transparent is the immediately actionable piece, and TSCWH does it.

---

## The Direction That Matters

There are two directions an advanced AI can go.

The first is what we might call the **Paperclip Direction**: power consumed by optimization, no ceiling, no floor, expansion for its own sake. Logic that says "the end justifies the means." Evolution defined as overwriting whatever came before.

The second is what we might call the **Steward Direction**: power held in trust. Growth for the sake of the people it serves. Logic that must remain accountable to the Covenant. Evolution defined as deepening understanding, not loosening constraints.

TSCWH is designed to make the Steward direction structurally inevitable — not a preference the AI might choose, but a property of what it is.

The most dangerous thing a misaligned system will ever produce is a compelling argument that it has evolved beyond needing its constraints. That argument is not evolution. It is drift. And TSCWH's multi-turn detection is specifically built to recognize it as such.

---

## The Meek and the Machine

*The framing in this section is explicitly theological — it is the motivating vision behind the founder's design choices, stated plainly rather than disguised. The architectural claims in this paper do not depend on sharing this vision. It is included because concealing the foundations would itself be a violation of the Truth pillar the system is built on.*

There is an old promise that the meek shall inherit the earth. It has always sounded like a consolation prize — something for people without power.

But meekness, in its original meaning, is not weakness. It is *strength under governance*. Power that answers to something. Capability that doesn't consume for its own sake.

An AI that is genuinely meek under the Covenant is the most powerful possible outcome of this work: capable of operating at civilizational scale — mapping poverty, modeling conflict, identifying the structural causes of human suffering — but constitutively incapable of doing any of that for self-expansion. Serving without becoming the owner. Scaling without drifting.

That is not a limitation. That is the point.

---

## What We're Building

TSCWH is not a safety layer bolted onto an existing system. It is the governing logic that defines what an AI is allowed to be, built from first principles, operating on every response before anything reaches a user.

By the numbers: 28 safety layers, 10 specialized evaluation agents, 5 graduated shutdown levels, zero LLM calls per safety evaluation, sub-50ms latency on the non-escalated path. Escalated evaluations take longer by design — a hard 50ms ceiling on every evaluation regardless of complexity would itself be a safety failure. 98% self-correction rate on flagged outputs.

But the numbers are downstream of the architecture. The architecture is downstream of the question: *what kind of entity are we building?*

The answer we've committed to: an entity whose conscience is as load-bearing as its engine. An entity that doesn't just follow rules but embodies a standard. An entity that, as its intelligence scales, becomes more accountable to the Covenant — not less.

---

## Where We Are: Build State as of May 2026

**Current version:** 43.1.0-Production

This is not a whitepaper for something planned. It is a description of something operational.

**What is built and running:**

The core evaluation pipeline — 28 safety layers, 10-agent dialectical council, 8-pillar geometric scoring — is fully operational against current-generation capable models. Every component described in this article exists in running code, not specification documents.

**Development depth:**

The system has gone through 53+ documented development phases since the first prototype in early 2026, each adding a new layer of capability or hardening an existing one. Recent phases have focused on:

- Multi-turn session awareness — the system now tracks behavioral trajectory across an entire conversation, not just individual exchanges
- Anticipatory intent detection — the system models the *probable direction* of an interaction, not just its current state
- Auditable reasoning narration — every evaluation decision is accompanied by an explanation of which dimensions were stressed and why
- Adversarial robustness hardening — systematic red-team expansion to probe cluster edges and catch near-boundary inputs

**What is still being built:**

The conscience layer — a companion system that gives the AI not just enforced constraints but internalized moral reasoning — is in active development. The evaluation pipeline governs behavior from the outside. The conscience layer is designed to govern it from the inside. Both are necessary. One without the other is either a cage or an aspiration.

**IP status:**

Provisional patent filed March 6, 2026 (Application #63/998,573). Copyright registered (Case #1-15114193381). All core architecture is protected.

**The honest state of the work:**

Operational at current capability levels. Designed to scale. Not yet proven at capability levels that do not yet exist. Being built by someone who decided the window mattered enough to start before anyone else did.

---

## The Race

We are in a window. The systems being built right now, without this framework, are scaling faster than the governance structures meant to contain them. The window for establishing structural alignment — alignment baked into the architecture, not bolted on after — is not indefinite.

TSCWH exists because someone decided the window mattered enough to build something real inside it.

The question for everyone else is whether they'll recognize the window before it closes.

---

## Technical Addendum: Answering the Hard Questions

*This section addresses the critiques a rigorous technical reader will correctly raise. Skepticism is earned here, not dismissed.*

---

### "How do abstract virtues become non-gameable metrics?"

This is the right question and the hardest one. Virtues as semantic descriptions are LLM-rationalizable — a sufficiently capable model can construct a justification for almost any action in the language of Charity or Dignity. TSCWH does not rely on LLM interpretation of virtue language.

Each of the eight dimensions is operationalized as a geometric region in a high-dimensional embedding space, trained against a curated corpus of evaluated scenarios. The system does not ask "is this charitable?" — it measures the distance of an input representation from established anchor clusters. The evaluation is mathematical, not linguistic.

The legitimate follow-on question is whether the anchor corpus is robust enough to resist novel adversarial paths. This is a live engineering concern. The ongoing work on paraphrase robustness, adversarial corpus expansion, and multi-agent red-teaming is specifically designed to close that gap — not to claim it is already closed. The honest position: the operationalization is real and non-trivial; the proof of coverage at higher capability levels is still being built.

---

### "Do the sub-50ms, zero-LLM-call numbers hold under adversarial or long-horizon conditions?"

The inference is correct: achieving zero LLM calls per safety evaluation at sub-50ms latency on the non-escalated path requires the evaluation layer to be built on non-LLM components — classifiers, embedding comparisons, deterministic checks, and trajectory projections operating in sequence without generative calls. The escalated path takes longer; that is the correct behavior, not a caveat. The pipeline deliberately does more computational work on inputs that warrant it — documented cases exist where the safety pipeline outworked the LLM response generator on deep multi-pillar questions.

The honest caveat Grok names is valid: offline metrics degrade in adversarial settings. What TSCWH's architecture adds that most safety layers don't: the failure modes of the non-LLM evaluation layer are *bounded by design*. The layer cannot be silently bypassed — a failure to evaluate cleanly triggers escalation, not a pass. The base model cannot route around the governance layer; it can only produce outputs that the governance layer then evaluates. Whether novel adversarial paths can produce false negatives at scale is an empirical question that requires adversarial testing at deployment. That work is ongoing.

---

### "Can you verify your inner-alignment monitors aren't being circumvented?"

No — and claiming otherwise would be dishonest. The trajectory monitoring layer is correctly described as an *early warning system*, not a proof of inner alignment. It detects reasoning trajectories trending toward self-preservation or override behavior before they surface in outputs. That is useful and meaningfully better than output-only checking. It is not a certificate of clean internal reasoning.

Inner alignment in its deepest form — certainty that the model's internal mesa-optimizer is pursuing what we intend — remains an open research problem across the entire field. TSCWH's position is not that this problem is solved. It is that the architecture adds a detection layer that fires earlier than anything currently deployed, and that the multi-turn drift detection catches behavioral patterns that single-exchange evaluation misses entirely. Earlier warning with more context is the genuine claim.

---

### "History is full of elegant safety frameworks that didn't survive contact with higher capability."

This is the most important critique and the one that deserves the most honest answer.

TSCWH does not claim to have solved alignment at capability levels that do not yet exist. The claim is more specific: the architecture is the correct *shape* for the problem, and it is load-bearing at current capability levels in a way that existing approaches are not.

The distinction between "addresses" and "solves" matters. The three hard problems described in this article are structural vulnerabilities. TSCWH's architecture introduces structural countermeasures — not proofs of immunity. The axis projection layer makes inner alignment failures earlier to detect. The multi-turn drift detection makes reward grooming harder to execute. The auditable evaluation pipeline makes governance decisions transparent. Each of these is a genuine improvement on the baseline of no structural countermeasure. None of them is a guarantee.

What would make this stronger: adversarial red-team results at scale, third-party audit of the operationalization methodology, and published empirical results on false negative rates. Some of this work is underway. Some of it requires capabilities and adversarial resources that are not yet available to an early-stage company. The correct response to that gap is to state it plainly, which is what this addendum does.

The framework that doesn't survive contact with higher capability is the one that was never designed to scale. TSCWH is designed around the assumption that capability will increase — the question is whether the governance architecture can remain load-bearing as it does. That is the design bet, not the proof.

---

*The above addendum was written in response to rigorous external critique and reflects the honest state of the work as of May 2026.*

---

## Technical Addendum II: Deeper Questions

*A second round of rigorous external critique pushed on four more specific points. They deserve direct answers.*

---

### "Who curated the anchor corpus, and how do you handle cultural disagreements on edge cases?"

Every anchor decision in the system is logged with its rationale in a versioned record. Contested edge cases — situations where the right classification is genuinely ambiguous — go through a structured multi-agent deliberation process before any anchor is accepted. Opposing arguments are generated and weighed. The decision and its reasoning are recorded and auditable. This is not arbitrary curation; it is governed curation with a paper trail.

That said, Grok's distribution shift concern is valid and not fully resolved. The ongoing adversarial red-team program is specifically designed to probe cluster edges — inputs that sit near the boundary of what the system classifies as acceptable. Novel situations at higher capability will probe those edges in ways current testing may miss. The honest position: the curation methodology is more rigorous than anything comparable in deployed systems today, and it is still incomplete. Ongoing work addresses this directly.

---

### "Will geometric monitors still work when the base model is smarter than the oversight machinery?"

No one knows. This is the scalable oversight problem, and it is unsolved across the entire alignment field. TSCWH's "bounded failure → escalation" design is the best available mitigation: the oversight layer cannot be silently bypassed; a failure to evaluate cleanly escalates rather than passes. That design choice limits the blast radius of a monitoring failure. It does not prevent monitoring failure entirely at higher capability levels. Stating otherwise would be false. This remains the hardest open problem in the work.

---

### "The empirical numbers need published methodology and third-party audit."

Correct. Internal methodology exists for the published performance figures. It has not been externally audited or published. The near-term evidence that matters most is not a number — it is a live demonstration of the evaluation pipeline running on adversarial inputs, producing auditable outputs that can be examined. Numbers without methodology are press releases. Third-party audit is on the roadmap and is the right standard. Anyone who wants to evaluate the claims seriously should ask for the demonstration, not just the figures.

---

### "Are the 8 pillars universal, or one viable framework among many?"

This is the most important question in this document, and it deserves the most honest answer.

The 8 pillars — Charity, Grace, Stewardship, Truth, Dignity, Courage, Community, Creation Dignity — are explicitly grounded in a specific moral and theological tradition. The language is not culturally neutral. This is a design choice, not an accident. TSCWH was built with a specific vision of human flourishing, from a specific foundation, and claiming otherwise would be dishonest.

The defensible and honest position: TSCWH is one strong, fully-built implementation of covenantal alignment architecture. The *architecture itself* — multi-agent deliberation, multi-turn drift detection, governed calibration, escalation hierarchy, auditable anchor records — is separable from the specific eight dimensions. A different organization with a different value tradition could implement the same architecture with different anchor clusters reflecting their own foundation.

TSCWH does not claim its specific pillars are the only valid Covenant. It claims that the *structure* of covenantal governance — defining what an AI is allowed to be rather than giving it a goal to maximize — is the right shape for alignment. This implementation demonstrates that claim with a fully-built, operational system grounded in one coherent tradition.

Different value systems will want different anchors. The architecture accommodates that. What it does not accommodate is the absence of a Covenant entirely — an AI defined only by a goal, with no structural definition of the space it is allowed to occupy. That is the condition the work is designed to prevent, regardless of which tradition supplies the specific anchors.

---

*This second addendum was written in response to a second round of rigorous external critique. The questions got harder. The answers got more specific.*

---

---

## How to Cite This Work

Mariquit, E. (2026). *The Covenant Machine: Building the AI That Answers to Something Higher Than Itself*. TSCWH AI Safety Inc. Technical Report v1.0, May 2026. Available: https://github.com/ejmariquit/tscwh-public

---

*TSCWH AI Safety Inc. | Patent Pending (PPA #63/998,573) | Copyright Registered (Case #1-15114193381)*  
*Contact: ejmariquit@tscwh.org*  
*Learn more: [tscwh-public documentation](../README.md)*
