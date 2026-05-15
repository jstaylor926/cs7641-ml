# UL2 — Feature Selection

**Paired reading:** Mitchell Ch 7 · **Unit:** Unsupervised Learning

## Why select features at all

Given `n` features, feature selection picks a subset that matters and discards
the rest. Reasons it pays off:

- **The curse of dimensionality** (SL4) — more features means a sparser space
  and exponentially more data needed; distance-based learners (kNN, k-means,
  SVM) degrade directly.
- **Overfitting** — irrelevant features give a model extra ways to fit noise.
- **Interpretability and cost** — fewer features means a model you can explain
  and cheaper data to collect.
- **Computation** — training and prediction get faster.

The hard truth: finding the *optimal* subset is **`2ⁿ` subsets** — exponential,
NP-hard in general. Every practical method is a heuristic shortcut.

## Relevance vs. usefulness — the key distinction

A subtle, exam-worthy point:

- **Relevance** is about *information*. A feature is **strongly relevant** if
  removing it changes the Bayes-optimal classifier; **weakly relevant** if it
  helps only in the presence (or absence) of certain other features; otherwise
  **irrelevant**. Relevance is a property of the data and the true target — it is
  measured against the Bayes optimal classifier.
- **Usefulness** is about a *particular learner*. A feature is useful if it
  improves *that algorithm's* performance.

They are not the same. A relevant feature can be useless to a given learner
(e.g. perfectly collinear with one it already uses), and a strictly irrelevant
feature could appear useful by chance on a finite sample. Filters chase
relevance; wrappers chase usefulness.

## Filter methods

Score and rank features **before** and **independently of** any learner, using a
statistic of the feature-vs-label relationship.

- **Mechanism:** rank by a criterion — information gain / mutual information (the
  OL3 quantity, and the SL2 decision-tree criterion repurposed as a filter),
  correlation, chi-squared, variance — then keep the top features.
- **Pros:** fast, scales to many features, learner-agnostic, no overfitting *to
  the selector*.
- **Cons:** ignores the learner entirely (selects for *relevance*, not
  *usefulness*), and typically scores features **individually**, so it misses
  features that are useless alone but informative together (the classic example:
  two features whose XOR predicts the label — each has zero individual mutual
  information with the label) and it happily keeps **redundant** correlated
  features.

A decision tree used purely to *rank* features (by where/whether it splits on
them) is itself a filter — note that filtering and learning use the same
information-theoretic machinery.

## Wrapper methods

Use the **actual learner** as the scoring function: pick a subset, train and
cross-validate the model, use that score to guide the search.

- **Search strategies:** **forward selection** (start empty, greedily add the
  feature that most improves CV score), **backward elimination** (start full,
  greedily drop the least useful), or randomized/GA search (ties back to OL1 —
  this *is* a randomized optimization problem).
- **Pros:** selects for **usefulness** to the specific model; naturally accounts
  for feature *interactions* and *redundancy* because it evaluates whole subsets.
- **Cons:** **expensive** — every candidate subset requires training the model;
  and it can **overfit the selection** to the validation folds, so the chosen
  subset must be validated on truly held-out data.

## Filter vs. wrapper — the summary

| | Filter | Wrapper |
|---|---|---|
| Scoring | Statistic of feature↔label | The learner's CV performance |
| Selects for | Relevance | Usefulness to *this* learner |
| Speed | Fast | Slow (retrains per subset) |
| Interactions | Usually missed | Captured |
| Redundancy | Often kept | Handled |
| Overfitting risk | Low | Can overfit the selection |

A common practical pattern: filter down to a manageable candidate set, then run
a wrapper on what remains.

## Feature selection vs. feature transformation

Important framing for the UL report: **selection** keeps a *subset of the
original* features — the result is still interpretable in the original units.
**Transformation** (UL3 — PCA, ICA) creates *new* features as combinations of
all originals — more powerful at compressing information, but the new axes are
harder to interpret. The UL report asks you to run both and compare what each
reveals.

---

## Review Questions

**Conceptual checks**

1. Give three distinct reasons feature selection improves a model, and name
   which type of learner suffers most from having many irrelevant features.
2. Why is finding the optimal feature subset NP-hard? What is the size of the
   search space?
3. Distinguish strong relevance, weak relevance, and irrelevance. Against what
   reference is relevance defined?

**Analysis — "why does it behave this way"**

4. Explain how a feature can be *relevant* but *useless* to a particular learner,
   and how a feature can be *irrelevant* but appear *useful* on a finite sample.
5. Filter methods that score features individually miss the XOR case. Walk
   through why: what is the individual mutual information of each XOR input with
   the label, and what is their joint information?
6. Why do wrapper methods naturally handle feature redundancy and interactions
   while individual-scoring filters do not?

**Derivation / math**

7. A filter ranks by mutual information `I(feature; label)`. Connect this
   explicitly to OL3 and to SL2's decision-tree splitting criterion — what is the
   same quantity doing in all three places?
8. Forward selection on `n` features: how many model trainings does it require in
   the worst case, and how does that compare to exhaustive search?

**Exam-style**

9. Build the filter-vs-wrapper comparison table from memory: scoring function,
   what it selects for, speed, interaction handling, overfitting risk.
10. A wrapper can overfit the feature selection itself. Explain the mechanism and
    the protocol that guards against it.
11. Contrast feature *selection* with feature *transformation* on
    interpretability and on compressive power. Which would you reach for first
    if a stakeholder needs to understand the model?
12. For the UL report, describe how you'd combine a filter and a wrapper into one
    pipeline and justify the ordering.
