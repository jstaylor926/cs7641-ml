# OL4 — Bayesian Learning

**Paired reading:** Mitchell Ch 6 · **Unit:** Optimization & Uncertainty

## The Bayesian frame

Bayesian learning treats learning as **updating beliefs about hypotheses in
light of data**. Instead of searching for one hypothesis, you maintain a
probability distribution over all of them.

**Bayes' theorem** is the engine:

```
P(h | D) = P(D | h) · P(h) / P(D)
```

- **`P(h)`** — the **prior**: belief in hypothesis `h` before seeing data.
  Encodes inductive bias *explicitly and quantitatively*.
- **`P(D | h)`** — the **likelihood**: how probable the observed data is if `h`
  were true.
- **`P(h | D)`** — the **posterior**: updated belief after seeing `D`.
- **`P(D)`** — the **evidence / marginal likelihood**: a normalizing constant,
  `Σ_h P(D|h)P(h)`. Independent of `h`, so it drops out when *comparing*
  hypotheses.

The key reframe: the prior is where inductive bias goes. SL1 said every learner
needs a bias; OL4 says state it as a probability distribution and let Bayes'
rule do the rest.

## MAP and ML hypotheses

Picking the single most probable hypothesis given the data:

```
h_MAP = argmax_h P(h | D) = argmax_h P(D | h) · P(h)
```

(`P(D)` dropped — constant in `h`.) The **Maximum A Posteriori** hypothesis
balances fit (`P(D|h)`) against prior plausibility (`P(h)`).

If the prior is **uniform** (all hypotheses equally likely a priori), the `P(h)`
term is constant and:

```
h_ML = argmax_h P(D | h)
```

the **Maximum Likelihood** hypothesis. So **ML is MAP with a flat prior** — and
this is exactly why ML can overfit: with no prior, nothing penalizes a complex
hypothesis that fits the noise.

## Three results from Mitchell Ch 6 worth knowing cold

**1. ML and least-squares regression.** Under the assumption that observations
are the true target plus i.i.d. Gaussian noise, the maximum-likelihood
hypothesis is *exactly* the one that **minimizes sum of squared errors**. This is
why squared-error loss is the default — it is the ML estimate under Gaussian
noise, not an arbitrary choice.

**2. MAP and regularization.** Adding a prior that prefers "simple" hypotheses
(e.g. a Gaussian prior on weights → small weights are more probable) makes the
MAP objective equal to **squared error plus an L2 penalty**. Regularization *is*
a prior. Weight decay (SL3, OL2) is the MAP correction to ML's overfitting.

**3. ML and cross-entropy.** For classification with probabilistic outputs, the
ML hypothesis minimizes **cross-entropy** — closing the loop with OL3 (minimizing
cross-entropy = minimizing KL to the data = maximum likelihood).

So three "loss functions" you might have thought were design choices —
squared error, L2-regularized error, cross-entropy — are all just maximum
likelihood (or MAP) under different noise/prior assumptions.

## The Minimum Description Length principle

Take `log` of the MAP objective and negate:

```
h_MAP = argmin_h [ −log₂ P(D | h) − log₂ P(h) ]
```

By Shannon (OL3), `−log₂ P(h)` is the optimal code length for `h`, and
`−log₂ P(D|h)` is the code length for the data given `h`. So **MAP = minimize
(description length of the hypothesis + description length of the data given the
hypothesis)**. This is **MDL**: the best hypothesis is the one that compresses
the data best. It is **Occam's razor derived from probability theory** — and it
ties OL3, OL4, and SL7's Occam discussion into one statement.

## The Bayes Optimal Classifier

`h_MAP` is the best *single* hypothesis. But to classify a *new instance*
optimally you should not commit to one hypothesis — you should let **every**
hypothesis vote, weighted by its posterior:

```
P(class | x, D) = Σ_h P(class | x, h) · P(h | D)
```

This **Bayes Optimal Classifier** has the lowest possible error of any
classifier — *no* method can do better on average. The catch: it requires
summing over the entire hypothesis space, which is computationally infeasible in
general. It is the theoretical gold standard, not a practical algorithm — its
value is as a *benchmark* and as the justification for ensembles (SL5 averaging
is a cheap approximation to it).

## Why this lecture matters

OL4 makes inductive bias explicit (it's the prior), explains *why* the standard
loss functions are what they are (ML/MAP under noise/prior assumptions),
re-derives regularization and Occam's razor from probability, and defines the
optimal-but-intractable classifier everything else approximates. OL5 turns this
into usable algorithms.

---

## Review Questions

**Conceptual checks**

1. Name the four terms in Bayes' theorem and say what each represents in
   learning. Which one can be ignored when *comparing* hypotheses, and why?
2. In what precise sense is "the prior" the home of inductive bias? Contrast with
   how a decision tree or SVM encodes its bias.
3. State the relationship between `h_ML` and `h_MAP`. Under what condition do
   they coincide?

**Derivation / math**

4. Show that under i.i.d. Gaussian noise, the ML hypothesis minimizes sum of
   squared errors. Where exactly does the squared term come from?
5. Show that a Gaussian prior on weights turns the MAP objective into
   squared-error-plus-L2. What does the prior's variance correspond to in the
   regularized objective?
6. Derive the MDL form of `h_MAP` by taking `−log` of the MAP objective.
   Interpret each of the two resulting terms as a code length.

**Analysis — "why does it behave this way"**

7. ML estimation is prone to overfitting; MAP with a sensible prior is less so.
   Explain the mechanism — what does the prior term *do* to a complex,
   noise-fitting hypothesis?
8. Explain why MDL is "Occam's razor derived from probability theory" rather than
   assumed as a heuristic.
9. The Bayes Optimal Classifier has provably minimal error but is never used
   directly. Why? And what practical method is a cheap approximation to it?

**Exam-style**

10. Three common loss functions — squared error, L2-regularized error,
    cross-entropy — are all ML or MAP under some assumption. State the assumption
    behind each.
11. Write the Bayes Optimal Classifier's prediction rule and explain how it
    differs from "use `h_MAP` to classify." Why is the difference important?
12. Connect OL3 and OL4: show the chain minimize-cross-entropy =
    minimize-KL-to-data = maximum-likelihood, and say where the prior would enter
    to make it MAP instead.
