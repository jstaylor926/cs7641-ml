# SL1 — Machine Learning Overview & Problem Setup

**Paired reading:** Mitchell Ch 1 · **Unit:** Supervised Learning

## What machine learning is

Mitchell's working definition: a program *learns* from experience **E** with
respect to task **T** and performance measure **P** if its performance at T,
measured by P, improves with E. The definition matters because it forces you to
name all three before you start — a vague task or an unstated metric is the most
common reason a project produces a model nobody can evaluate.

Machine learning is the alternative to writing rules by hand. You use it when
the mapping from input to output is too complex, too variable, or too poorly
understood to specify directly, but examples of correct behavior are available.
The cost is that you trade an explicit, inspectable program for a model whose
behavior you can only characterize statistically.

## The three families

**Supervised learning** is the focus of this unit: you are given labeled pairs
`(x, y)` and learn a function `f: X → Y` that generalizes to unseen `x`. If `Y`
is categorical it is *classification*; if continuous, *regression*.

**Unsupervised learning** (Unit 3) has inputs but no labels — the goal is to
find structure: clusters, lower-dimensional representations, density.

**Reinforcement learning** (Unit 4) has no fixed dataset at all. An agent acts,
receives delayed scalar reward, and learns a policy. The supervision is the
reward signal, which is sparse and indirect.

A useful contrast Mitchell draws: supervised learning is *induction* — going
from specific observed examples to a general rule. Everything that makes
supervised learning hard is a consequence of that being fundamentally
under-determined.

## Concept learning and the hypothesis space

A **concept** is a boolean-valued function over instances; **concept learning**
is inferring it from labeled examples. Two ideas from this framing carry through
the entire course:

The **hypothesis space H** is the set of functions your learner is even capable
of expressing. A decision tree of depth 3, a linear separator, a degree-5
polynomial — each defines a different H. Learning is *search through H* for a
hypothesis consistent with the data.

**Inductive bias** is the set of assumptions a learner uses to generalize beyond
the training data. It is *not* optional and not a flaw — a learner with no bias
cannot generalize at all (it could justify any labeling of unseen points).
Examples: a decision tree's bias is "prefer shorter trees / splits with high
information gain"; kNN's bias is "nearby points have similar labels"; a linear
model's bias is "the boundary is a hyperplane." Choosing a learner *is* choosing
a bias. This is the conceptual seed of the No Free Lunch theorem in OL3.

## Generalization, overfitting, and the core tension

The only thing that matters is performance on **unseen** data. Training error is
a means, never the goal.

**Overfitting:** a hypothesis `h` overfits if some other hypothesis `h'` has
higher training error but lower true error — i.e. `h` has fit noise and
sampling artifacts as if they were signal. **Underfitting** is the opposite: H
is too restricted to capture the real pattern, so both training and test error
are high.

This is the **bias–variance tradeoff**, the single most important framing in the
unit:

- **Bias** — error from H being too simple to represent the true function.
  High-bias models underfit; their predictions are systematically off.
- **Variance** — error from sensitivity to the particular training sample.
  High-variance models overfit; retrain on a different sample and you get a
  very different model.

For squared-error regression the expected test error decomposes exactly into
`bias² + variance + irreducible noise`. You cannot drive both bias and variance
to zero with finite data; model selection is choosing where to sit on that
curve.

## Evaluation methodology

Because training error is misleading, you need a protocol:

- **Train/validation/test split** — train on one part, tune hyperparameters on
  validation, and touch test *once* at the end. The test set is spent the moment
  you make a decision based on it.
- **k-fold cross-validation** — partition into k folds, train on k−1 and
  validate on the held-out fold, rotate, average. Standard for model selection
  when data is limited. Stratify for imbalanced classes.
- **Learning curves** — performance vs. training-set size. They diagnose *which*
  problem you have: a high, converged-together pair of curves means high bias
  (more data won't help); a wide persistent gap means high variance (more data
  or regularization will help).
- **Validation curves** — performance vs. a single hyperparameter. They show the
  underfit→overfit sweep directly.

The cardinal sins: tuning on the test set, letting preprocessing (scaling,
feature selection) see the validation fold, and reporting a single run of a
stochastic algorithm without variance. Use `Pipeline` and fixed seeds — these
are graded in the SL report.

## Why this lecture anchors the unit

Every algorithm in SL2–SL8 is a different point in `(hypothesis space,
inductive bias, position on the bias–variance curve)` space. Decision trees,
neural nets, kNN, SVMs, ensembles — read each one as an answer to "what does H
look like, what is the bias, and which knob moves it along the bias–variance
curve."

---

## Review Questions

**Conceptual checks**

1. State Mitchell's E/T/P definition and apply it concretely to spam filtering —
   name the experience, task, and performance measure.
2. Why is a learner with *no* inductive bias unable to generalize? What does it
   have to do when it sees an unlabeled instance?
3. Distinguish hypothesis space from inductive bias. Can two learners share a
   hypothesis space but have different inductive biases? Give an example.

**Analysis — "why does it behave this way"**

4. You train a model and see ~2% training error but ~25% test error. Which side
   of the bias–variance tradeoff are you on, and name three concrete
   interventions. Now the reverse: 22% training and 24% test — same questions.
5. A learning curve shows training and validation error both high and nearly
   touching. Will collecting 10× more data help? Why or why not?
6. Explain precisely why evaluating on the test set more than once corrupts your
   estimate of true error.

**Derivation / formal**

7. Write the bias–variance–noise decomposition of expected squared error. What
   does each term depend on — the model, the data sample, or the world?
8. Argue that minimizing training error and minimizing true error are different
   objectives, and describe the assumption under which they coincide.

**Exam-style**

9. Define overfitting in Mitchell's exact terms (the "exists an h'" form), not
   just "fits noise." Why is the formal version more useful?
10. For the SL report you must compare several learners on two datasets. Using
    only the vocabulary of this lecture, what would a *good analysis* of the
    results talk about, beyond which model had the highest accuracy?
