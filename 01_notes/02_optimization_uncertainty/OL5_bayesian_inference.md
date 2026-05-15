# OL5 — Bayesian Inference

**Paired reading:** Mitchell Ch 6 · **Unit:** Optimization & Uncertainty

> OL4 set up the Bayesian *framework* (priors, likelihoods, posteriors,
> MAP/ML, the Bayes Optimal Classifier). OL5 turns it into *usable algorithms* —
> chiefly the Naive Bayes classifier and the machinery of belief networks — and
> the practical reasoning tools that come with them.

## Naive Bayes — making Bayes tractable

To classify `x = (a₁, ..., aₙ)`, the Bayes-optimal choice is
`argmax_c P(c) · P(a₁,...,aₙ | c)`. The problem: estimating the full joint
`P(a₁,...,aₙ | c)` needs exponentially many parameters and far more data than you
have.

**The naive assumption:** attributes are **conditionally independent given the
class**:

```
P(a₁, ..., aₙ | c) = Π_i P(aᵢ | c)
```

This collapses an exponential estimation problem into estimating each
`P(aᵢ | c)` separately — linear in the number of attributes. The classifier:

```
c_NB = argmax_c  P(c) · Π_i P(aᵢ | c)
```

**Why it works despite the assumption usually being false.** Conditional
independence rarely holds exactly, yet Naive Bayes is a strong classifier. The
reason: you don't need accurate *probabilities*, only the *correct argmax*. Even
when the estimated probabilities are badly miscalibrated, the *ranking* of
classes is often still right. It is also low-variance (few parameters), so it
needs little data and resists overfitting — a great high-bias baseline.

**Practical detail — smoothing.** If a value `aᵢ` never co-occurs with class `c`
in training, `P(aᵢ | c) = 0` zeros out the entire product. **Laplace (add-one)
smoothing** adds a small pseudo-count so no probability is ever exactly zero.

## Belief networks (Bayesian networks)

Naive Bayes assumes *all* attributes are conditionally independent given the
class — a sledgehammer. **Bayesian networks** let you specify *which*
independence relations hold:

- A **directed acyclic graph** where nodes are random variables and edges denote
  direct probabilistic dependence.
- Each node carries a **conditional probability table** giving `P(node |
  parents)`.
- The graph encodes the factorization
  `P(X₁,...,Xₙ) = Π_i P(Xᵢ | parents(Xᵢ))` — the joint, compactly.
- A node is **conditionally independent of its non-descendants given its
  parents**. Naive Bayes is the special case: one class node, all attribute
  nodes as its children, no other edges.

Belief networks are the general representation; Naive Bayes is the most
restrictive useful point in that space. **Inference** (computing a posterior
over some variables given evidence on others) is exact for simple graphs but
NP-hard in general — approximate methods (sampling) are used for large networks.

## The reasoning tools OL5 gives you

- **Prior vs. posterior, made operational.** OL4 defined them; OL5 is where you
  *compute* them and update beliefs as evidence arrives. Sequential updating: the
  posterior after one batch of data is the prior for the next.
- **MAP vs. ML, revisited.** With small data the prior matters a lot (MAP and ML
  diverge); with abundant data the likelihood dominates and the posterior
  concentrates regardless of a reasonable prior — the data "washes out" the
  prior.
- **Generative vs. discriminative.** Naive Bayes is **generative** — it models
  `P(x | c)` and `P(c)`, i.e. how the data is *generated*, and can synthesize
  data. Logistic regression / SVMs are **discriminative** — they model the
  boundary `P(c | x)` directly. Generative models can be better with little data
  and handle missing features; discriminative models usually win with abundant
  data because they don't waste capacity modeling `P(x)`. This contrast is a
  frequent exam question.

## Where it sits in the course

OL5 is the practical payoff of the Bayesian unit and the bridge to UL1: the
**EM algorithm** for clustering (Gaussian mixture models) is Bayesian inference
applied to *latent* variables you can't observe — the cluster assignments. The
prior/posterior/likelihood vocabulary from OL4–OL5 is exactly the vocabulary
UL1's EM derivation uses.

---

## Review Questions

**Conceptual checks**

1. State the "naive" conditional-independence assumption precisely. What
   intractable quantity does it let you avoid estimating?
2. Why is Naive Bayes often an accurate classifier even when its independence
   assumption is clearly violated? (Hint: what does a classifier actually need
   to get right?)
3. What does an edge in a Bayesian network mean, and what does the *absence* of
   an edge assert?

**Derivation / math**

4. Write the Naive Bayes decision rule from Bayes' theorem and show where the
   independence assumption enters and what it simplifies.
5. Explain the zero-frequency problem and how Laplace smoothing fixes it. Why
   does a single zero factor wreck the whole prediction?
6. Write the joint-distribution factorization a Bayesian network encodes. Show
   that Naive Bayes is a special case and draw its graph.

**Analysis — "why does it behave this way"**

7. With very little training data, MAP and ML estimates differ noticeably; with
   lots of data they converge. Explain the mechanism.
8. Naive Bayes is low-variance and high-bias. Tie that to its parameter count
   and to why it's a good baseline but rarely a top performer.
9. When does a generative model (Naive Bayes) beat a discriminative model, and
   when does the discriminative model win? Give the reasoning, not just the
   answer.

**Exam-style**

10. Contrast Naive Bayes and a general Bayesian network: what independence
    structure does each assume, and what is the cost of the more general model?
11. Define generative vs. discriminative classifiers, give one example of each
    from this course, and state one practical advantage of each.
12. Explain how OL5's prior/likelihood/posterior machinery sets up UL1's EM
    algorithm — what is the "latent variable" that makes clustering a Bayesian
    inference problem?
