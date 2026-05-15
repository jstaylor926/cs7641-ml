# Math Foundations — Probability & Statistics

**Paired reading:** Wasserman, *All of Statistics*, Part 1 (errata: `02_readings/00_prerequisites/errata2.pdf`) · **Focus area A** (flagged weak area)

> This underlies OL4–OL5 (Bayesian learning), UL1's EM, and — crucially — the
> **experimental analysis in every single report**. You cannot claim a result is
> "real" without the vocabulary here. Log gaps in `math_gaps_log.md`.

## Random variables and distributions

A **random variable** maps outcomes to numbers. Its **distribution** says how
probability is spread:

- **Discrete:** a probability mass function `P(X = x)`, summing to 1.
- **Continuous:** a probability density function `p(x)`, integrating to 1.

Distributions you must recognize on sight:

- **Bernoulli / Binomial** — a coin flip / count of successes in `n` flips.
  Models any binary outcome (a single classification being right or wrong).
- **Gaussian (Normal)** `N(μ, σ²)` — the bell curve. Ubiquitous because of the
  Central Limit Theorem; it is the noise model behind least-squares regression
  (OL4) and the component model in GMM/EM (UL1).
- **Uniform** — all outcomes equally likely; the maximum-entropy distribution
  (OL3) and the "no prior knowledge" prior (OL4).

## Expectation and variance

- **Expectation** `E[X] = Σ x·P(x)` (or `∫ x·p(x) dx`) — the long-run average,
  the "center of mass." **Linear:** `E[aX + bY] = aE[X] + bE[Y]` *always*, even
  if `X, Y` are dependent. This linearity is used constantly.
- **Variance** `Var(X) = E[(X − E[X])²] = E[X²] − E[X]²` — the spread.
  `Var(aX) = a²Var(X)`. For *independent* variables, `Var(X + Y) = Var(X) +
  Var(Y)` — this additivity is exactly why bagging (SL5) reduces variance by
  averaging, and why you average independent runs.
- **Covariance** `Cov(X,Y) = E[(X−E[X])(Y−E[Y])]` — linear co-movement; zero ⇔
  *uncorrelated* (but **not** necessarily independent — see below). The
  covariance *matrix* is what PCA decomposes (UL3, linear algebra notes).

## Independence vs. uncorrelated — the distinction that matters

- **Independent:** `P(X, Y) = P(X)·P(Y)` — the joint factorizes; knowing one
  tells you *nothing* about the other.
- **Uncorrelated:** `Cov(X, Y) = 0` — no *linear* relationship.

Independence ⇒ uncorrelated, but **not the reverse**: variables can be
uncorrelated yet strongly dependent (e.g. `Y = X²` with `X` symmetric around 0).
This is precisely why **PCA ≠ ICA** (UL3): PCA only de-correlates; ICA seeks true
independence. It is also why Naive Bayes' "conditional independence" assumption
(OL5) is a strong one.

## Conditional probability and Bayes' rule

```
P(A | B) = P(A, B) / P(B)            P(A, B) = P(A | B)·P(B)
```

**Bayes' rule** — the engine of OL4–OL5 — rearranges this:

```
P(H | D) = P(D | H)·P(H) / P(D)
posterior = likelihood × prior / evidence
```

The **law of total probability** gives the evidence: `P(D) = Σ_h P(D|h)P(h)`.
Be fluent moving between joint, conditional, and marginal — EM (UL1) and
Bayesian networks (OL5) are nothing but this algebra applied repeatedly.

## MLE and MAP

Two ways to estimate a parameter `θ` from data `D`:

- **Maximum Likelihood (MLE):** `θ_MLE = argmax_θ P(D | θ)` — the parameter that
  makes the observed data most probable. Uses no prior.
- **Maximum A Posteriori (MAP):** `θ_MAP = argmax_θ P(D | θ)·P(θ)` — weights the
  likelihood by a prior. **MLE = MAP with a uniform prior.**

Practical fact: you almost always maximize the **log-likelihood** — `log` turns
products into sums (easier derivatives, no numerical underflow) and is monotonic
so the argmax is unchanged. This is the OL4 story; the foundations point is just
being able to *do* the maximization (set derivative to zero — see calculus
notes).

## Sampling, estimators, and the report-critical part

Your training set is one **sample** from a population. Any statistic you compute
(an accuracy, a mean) is an **estimate** with its own uncertainty:

- **Bias of an estimator** — does it systematically miss? **Variance of an
  estimator** — how much does it jump around across samples? (Same bias/variance
  language as SL1, applied to *estimates* rather than *models*.)
- **Standard error** — the standard deviation of an estimate; shrinks like
  `1/√n`. More data ⇒ tighter estimate, with diminishing returns.
- **Confidence interval** — a range that would contain the true value a stated
  fraction of the time under repeated sampling. *Report intervals, not point
  estimates*, for any experimental result.
- **Hypothesis testing / p-values** — is an observed difference larger than
  sampling noise would explain? A p-value is `P(data this extreme | null
  hypothesis true)` — **not** the probability the null is true (a notorious
  misreading).
- **Cross-validation** (SL1) is how you turn one dataset into many samples to
  estimate this variance.

This is what makes a report's analysis credible: "Model A scored 0.84, Model B
0.83" is meaningless without knowing whether that gap survives the noise. Always
report variance across seeded runs — the study plan grades this.

## Where it shows up in CS7641

| Concept | Where |
|---|---|
| Bayes' rule, priors/posteriors | OL4, OL5, UL1 (EM) |
| MLE / MAP, log-likelihood | OL4 (least-squares, regularization) |
| Gaussian noise model | OL4 squared-error; UL1 GMM |
| Independence vs. uncorrelated | OL5 Naive Bayes; UL3 PCA vs. ICA |
| Variance additivity | SL5 bagging; averaging seeded runs |
| Confidence intervals, CV, significance | **Every report's experimental analysis** |

---

## Review Questions

**Conceptual checks**

1. State the difference between independent and uncorrelated, and give a concrete
   pair of variables that are uncorrelated but dependent. Which CS7641 topic pair
   hinges on this distinction?
2. Write Bayes' rule and name all four terms in learning vocabulary. Which term
   is just a normalizer, and why can it be dropped when comparing hypotheses?
3. What is the precise relationship between MLE and MAP?

**Derivation / math**

4. Show `Var(X) = E[X²] − E[X]²` from the definition `Var(X) = E[(X−E[X])²]`.
5. Why is `Var(X + Y) = Var(X) + Var(Y)` only for *independent* `X, Y`, while
   `E[X + Y] = E[X] + E[Y]` always holds? Tie the variance fact to why bagging
   reduces variance.
6. Why do we maximize the *log*-likelihood instead of the likelihood directly?
   Give two distinct reasons and explain why the argmax is unaffected.

**Analysis — "why does it matter"**

7. A standard error shrinks like `1/√n`. Explain what that implies about the
   value of collecting 4× more data, and connect it to the shape of a learning
   curve (SL1).
8. A classmate reports "p = 0.03, so there's a 97% chance our model is better."
   Identify the error and state what a p-value actually measures.
9. Why is reporting a single run of a stochastic algorithm (e.g. a GA in OL, or
   k-means in UL) statistically indefensible? What should you report instead?

**Exam-style**

10. Given a uniform prior over hypotheses, show that `h_MAP` reduces to `h_MLE`.
    What does the uniform prior represent?
11. Define the bias and variance *of an estimator* and relate them to the bias
    and variance *of a model* from SL1 — same idea, different object.
12. For a report comparing two classifiers, describe the statistical procedure
    you'd use to decide whether the accuracy difference is real, and what you'd
    actually put in the figure/table.
