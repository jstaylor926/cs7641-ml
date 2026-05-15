# SL4 — Instance-Based Learning

**Paired reading:** Mitchell Ch 8 · **Unit:** Supervised Learning

## The lazy-learning idea

Instance-based learners do **no work at training time** — they just store the
examples. All computation is deferred to query time, when the learner finds the
stored instances most similar to the query and combines their labels. This is
**lazy learning**, in contrast to the **eager** learners (trees, nets) that
build a global model up front and throw the data away.

The consequence: instance-based methods form a **different local approximation
for every query**. They never commit to one global hypothesis. That is their
power (they can fit very irregular boundaries) and their cost (no compact model,
slow queries, sensitive to the distance metric).

## k-Nearest Neighbors

Given a query `x_q`: find the `k` stored instances closest under a distance
metric, and predict by **majority vote** (classification) or **average**
(regression).

**The k knob is a pure bias–variance dial:**

- `k = 1` — the boundary follows every point, including noise. Low bias, high
  variance. Training error is 0 by construction (a point is its own nearest
  neighbor), which tells you nothing.
- Large `k` — predictions are smoothed over a big neighborhood. High bias, low
  variance. At `k = N` it just predicts the global majority — maximum bias.

**Distance-weighted kNN** weights each neighbor by `1/d²` so closer neighbors
count more. This lets you use a larger `k` (more noise robustness) without
distant, irrelevant points dominating — and at the extreme you can let *all*
points vote, weighted by distance.

## The distance metric is everything

kNN's inductive bias is "instances close in feature space have similar labels."
Whether that bias is *true* depends entirely on the metric:

- **Feature scaling is mandatory.** Euclidean distance is dominated by
  large-magnitude features. A feature in dollars (0–100000) will swamp one in
  fractions (0–1). Standardize or normalize first — this is the single most
  common kNN mistake and it is graded in the report.
- **Irrelevant features actively hurt.** Every junk feature adds noise to every
  distance computation. Unlike a decision tree, which simply never splits on a
  useless attribute, kNN cannot ignore one. This is a strong argument for
  feature selection (UL2) as a preprocessing step.
- **Metric choice:** Euclidean (L2), Manhattan (L1), Hamming for categorical,
  cosine for direction-not-magnitude data. The right metric encodes domain
  knowledge.

## The curse of dimensionality

In high dimensions, distances **concentrate** — the ratio of the farthest to the
nearest neighbor approaches 1, so "nearest" stops being meaningful. The volume
of the space grows exponentially, so any fixed sample becomes hopelessly sparse;
to keep the same neighbor density you need exponentially more data. This is
*the* fundamental limitation of instance-based learning and a recurring exam
topic. It is also the motivation for dimensionality reduction in Unit 3.

## Locally weighted regression

A generalization: instead of averaging neighbor labels, **fit a local model**
(often linear) to the neighborhood around the query, weighting each point by its
distance via a kernel. The prediction is that local model evaluated at `x_q`.
This produces smoother fits than plain kNN and handles local trends, at higher
query cost.

## Cost, and why it can be managed

Naive query cost is `O(N·d)` per prediction — linear in the dataset. **k-d
trees** and **ball trees** bring this down to roughly `O(log N)` in low-to-
moderate dimensions, but they degrade back toward linear as dimensionality rises
(the curse again). **Edited / condensed nearest neighbor** prunes the stored set
to the points near the decision boundary, shrinking both memory and query cost.

## Strengths, weaknesses, where it sits

Strengths: trivial training, naturally handles multi-class and complex nonlinear
boundaries, no model assumptions, easy to update (just add an instance), and a
strong baseline. Weaknesses: slow at query time, stores all data, demands
careful scaling, breaks under irrelevant features and high dimensionality, and
gives no interpretable model.

On the bias–variance picture: `k` is the knob, cleanly and monotonically. `k=1`
is the high-variance extreme; large `k` is the high-bias extreme. This makes kNN
a clean teaching example — and a clean validation-curve figure for the SL
report.

---

## Review Questions

**Conceptual checks**

1. Define lazy vs. eager learning. What does kNN do at training time, and what is
   the consequence at query time?
2. Why is 1-NN training error always 0, and why does that number tell you
   nothing about generalization?
3. State kNN's inductive bias in one sentence. Name a dataset where that bias is
   badly wrong.

**Analysis — "why does it behave this way"**

4. Trace how `k` moves kNN along the bias–variance curve. What does the decision
   boundary look like at `k=1`, at moderate `k`, and at `k=N`?
5. You forget to scale features and one feature is in the thousands while others
   are 0–1. Describe precisely what the distance metric does and which feature
   effectively decides every prediction.
6. A decision tree is largely unbothered by 20 irrelevant features; kNN is
   crippled by them. Explain the difference in terms of how each algorithm uses
   features.

**Derivation / math**

7. Explain the curse of dimensionality quantitatively: what happens to the ratio
   (distance to farthest neighbor)/(distance to nearest neighbor) as dimension
   grows, and why does that make "nearest neighbor" meaningless?
8. Write the distance-weighted kNN prediction for regression. How does weighting
   let you safely increase `k`?

**Exam-style**

9. Contrast kNN and locally weighted regression: what does each compute in the
   neighborhood of a query, and which gives smoother predictions?
10. Your kNN model is too slow at query time on a moderate-dimensional dataset.
    Give two structural fixes and state when each stops helping.
11. For the SL report, kNN gives a clean validation curve over `k`. Sketch what
    that curve looks like and mark the underfit region, the overfit region, and
    the selected `k`.
12. Why is kNN a natural argument *for* doing feature selection or dimensionality
    reduction (forward-referencing Unit 3)? Be specific about which kNN weakness
    each addresses.
