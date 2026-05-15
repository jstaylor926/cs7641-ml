# SL5 — Ensemble Learning & Boosting

**Paired reading:** Matas & Šochman AdaBoost slides (`adaboost_matas.pdf`) · **Unit:** Supervised Learning

## The core idea

An **ensemble** combines many simple models ("weak learners") into one strong
predictor. The premise: a learner that is only slightly better than chance
("weak"), if you can produce many *diverse* ones, can be combined into an
arbitrarily accurate ("strong") learner. Diversity is the whole game — averaging
copies of the same model buys nothing.

Two families differ in *what error they attack*:

- **Bagging** attacks **variance** — average many low-bias, high-variance models.
- **Boosting** attacks **bias** — sequentially compose many high-bias weak
  models into a flexible one.

## Bagging (Bootstrap Aggregating)

Train each model on a **bootstrap sample** — draw N examples *with replacement*
from the training set, so each model sees a slightly different dataset (~63% of
unique examples). Predict by **vote/average** across models.

Why it works: if the models' errors are partially independent, averaging cancels
the variance component while leaving bias roughly unchanged. So bagging helps a
*lot* for high-variance learners (deep decision trees) and **barely at all** for
stable, high-bias learners (linear models) — there's no variance to average
away. **Random forests** push diversity further by also sampling a random subset
of features at each split, decorrelating the trees. The **out-of-bag** examples
(the ~37% not in a given bootstrap) give a free validation estimate.

Bagging is **parallel** — models are independent — and it does not overfit as
you add more trees (it converges).

## Boosting

Boosting is **sequential and adaptive**: each new weak learner is trained to fix
the mistakes of the ensemble so far.

**AdaBoost** (the algorithm to know cold):

1. Initialize a uniform weight `D₁(i) = 1/N` over training examples.
2. For `t = 1..T`:
   - Train weak learner `h_t` on the data weighted by `D_t`.
   - Compute its weighted error `ε_t = Σ D_t(i) · [h_t(x_i) ≠ y_i]`.
   - Compute its vote weight `α_t = ½ ln((1 − ε_t)/ε_t)`.
   - Reweight: **increase** the weight of misclassified examples, **decrease**
     correctly classified ones, then renormalize so `D_{t+1}` sums to 1.
3. Final hypothesis: `H(x) = sign(Σ α_t h_t(x))` — a weighted vote.

Read the pieces: `α_t` is large when `ε_t` is small (a good learner gets a big
vote) and goes to 0 as `ε_t → ½` (a coin-flip learner is ignored). The
reweighting forces successive learners to concentrate on the **hard, repeatedly
missed examples**. As long as every weak learner is even slightly better than
chance (`ε_t < ½`), the **training error of the ensemble drops exponentially**
in T.

The typical weak learner is a **decision stump** (depth-1 tree). Stumps are
high-bias / low-variance — exactly what boosting wants, since boosting *adds*
capacity by composition.

## Why AdaBoost resists overfitting (the famous result)

Empirically, AdaBoost often keeps improving **test** error even after **training**
error has hit zero — it appears to defy the overfitting story. The accepted
explanation is the **margin**: AdaBoost keeps increasing the *confidence* of
correct classifications (pushing examples further from the boundary) even after
they're all correct, and larger margins generalize better. This is a favorite
exam discussion — be ready to state both the observation and the margin
explanation.

But AdaBoost is **not immune**: it overfits with **noisy data / mislabeled
examples**, because the reweighting will relentlessly chase a mislabeled point
it can never get right, pouring weight into noise. This is its key weakness — and
a good caveat for the OL report.

## Bias–variance summary

| | Bagging | Boosting |
|---|---|---|
| Attacks | Variance | Bias |
| Base learner | Low-bias, high-variance (deep trees) | High-bias, low-variance (stumps) |
| Training | Parallel, independent | Sequential, adaptive |
| Overfitting | Resistant; converges | Resistant to a point; sensitive to **noise** |
| Diversity from | Bootstrap samples (+ feature subsets) | Reweighting toward hard examples |

## Strengths, weaknesses, where it sits

Ensembles are among the strongest off-the-shelf learners — boosted trees and
random forests routinely top tabular-data benchmarks. The cost: you lose the
interpretability of a single tree, training (boosting) is sequential and slower,
and boosting needs clean data. Conceptually, ensembles are the *answer* to SL2's
complaint that single trees are high-variance and make axis-parallel cuts.

---

## Review Questions

**Conceptual checks**

1. Why is *diversity* among base learners essential? What does an ensemble of
   identical models achieve?
2. Bagging targets variance; boosting targets bias. Match each to the kind of
   base learner it should use and explain why the pairing makes sense.
3. What is a decision stump, and why is it the canonical weak learner for
   boosting rather than a deep tree?

**Derivation / math**

4. Write AdaBoost's `α_t` formula. Evaluate its behavior as `ε_t → 0`, `ε_t = ½`,
   and `ε_t → 1`. Why does the `ε_t = ½` case make sense?
5. Describe exactly how `D_{t+1}` is computed from `D_t` and `h_t`'s predictions.
   Which examples gain weight and which lose it?
6. State the guarantee: under what condition on each weak learner does AdaBoost's
   *training* error decrease, and how fast?

**Analysis — "why does it behave this way"**

7. AdaBoost often improves test error *after* training error reaches zero.
   State the observation precisely and give the margin-based explanation.
8. Bagging helps deep decision trees enormously but does almost nothing for a
   linear regression model. Explain via the bias–variance decomposition.
9. You have a dataset with ~5% mislabeled examples. Predict AdaBoost's behavior
   over many rounds and explain the mechanism that causes the problem.

**Exam-style**

10. Contrast bagging and boosting on: parallel vs. sequential training, the bias
    or variance each reduces, source of diversity, and noise robustness.
11. Random forests add a second randomization on top of bagging. What is it, and
    what problem with plain bagged trees does it fix?
12. For the SL report, you compare a single pruned tree, a random forest, and a
    boosted tree on two datasets — one clean, one noisy. Predict the ranking on
    each dataset and justify each prediction with this lecture's mechanisms.
