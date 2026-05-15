# SL2 — Decision Trees

**Paired reading:** Mitchell Ch 3 · **Unit:** Supervised Learning

## The representation

A decision tree classifies an instance by routing it from the root to a leaf:
each internal node tests one attribute, each branch is an outcome of that test,
each leaf assigns a label. The tree is equivalent to a disjunction of
conjunctions — each root-to-leaf path is an AND of attribute tests, and the
whole tree ORs the paths for a given class. This makes trees readable, which is
a real advantage when a report has to *explain* model behavior.

The hypothesis space is the set of all trees over the attributes — effectively
complete for discrete-valued functions. That completeness is exactly why trees
overfit without help: H is rich enough to memorize.

## ID3 and the greedy top-down algorithm

ID3 builds the tree recursively and greedily: at each node, pick the attribute
that best splits the examples reaching that node, partition by its values,
recurse. Stop when examples at a node are pure (one class), attributes are
exhausted, or examples run out (then take a majority vote).

"Best" is defined by **information gain**, which rests on **entropy**:

```
Entropy(S) = − Σ_c p_c log2 p_c
```

Entropy is the expected number of bits to encode the class of a random example
from S. It is 0 when S is pure and maximal (1 bit for binary) when classes are
balanced. **Information gain** of attribute A is the reduction in entropy from
splitting on A:

```
Gain(S, A) = Entropy(S) − Σ_v (|S_v| / |S|) · Entropy(S_v)
```

ID3 picks the attribute with the highest gain. This is the first place
information theory shows up in the course and it is *not* incidental — OL3 is the
formal version of exactly this machinery, so understand entropy here.

**Gain's bias and the fix.** Information gain is biased toward
many-valued attributes (an attribute with a unique value per example gives
perfectly pure children and maximal gain, but generalizes terribly — think a
"date" or "ID" attribute). **Gain ratio** normalizes gain by the *split
information* (the entropy of the partition sizes themselves) to penalize that.
CART uses **Gini impurity** `1 − Σ p_c²` instead of entropy; in practice the two
criteria give very similar trees.

## Inductive bias of decision trees

ID3's bias is a **preference bias** (a.k.a. search bias), not a restriction
bias: it can in principle express any tree, but it *prefers* shorter trees, and
among short trees, those with high-information-gain attributes near the root.
This is an Occam's-razor bias — "the simplest hypothesis consistent with the
data is most likely to generalize." Contrast with candidate-elimination's
restriction bias, which limits H itself. Knowing the difference is a classic
exam question.

## Overfitting and pruning

A fully grown tree fits the training set perfectly, including its noise — pure
overfitting. Two remedies:

- **Pre-pruning (early stopping):** stop splitting when a node is too small, gain
  is below a threshold, or depth is capped. Cheap, but short-sighted — it can
  miss a good split that only pays off two levels down (the "horizon effect").
- **Post-pruning:** grow the full tree, then remove subtrees that don't help on a
  validation set. **Reduced-error pruning** replaces a subtree with a leaf if
  doing so doesn't hurt validation accuracy. **Rule post-pruning** converts the
  tree to rules and prunes preconditions independently — more flexible, used by
  C4.5. Post-pruning generally beats pre-pruning because it sees the whole tree
  before deciding.

## Practical extensions

- **Continuous attributes:** sort the values and consider thresholds at the
  midpoints between adjacent values with different labels; pick the best
  threshold by gain. A continuous attribute can be reused down the tree.
- **Missing values:** assign the most common value at that node, or distribute
  the example fractionally across branches by the observed value proportions.
- **Attribute costs:** weight gain by cost (e.g. divide by cost) when tests are
  expensive to acquire.
- **Regression trees:** leaves hold a numeric value (mean of the examples);
  splits minimize variance / squared error instead of entropy.

## Strengths, weaknesses, and where trees sit

Trees are fast to train and predict, handle mixed attribute types, need little
preprocessing (no scaling), and are interpretable. Their weakness is **high
variance** — small changes in the data can flip an early split and reshape the
whole tree — and they make **axis-parallel** cuts, so a diagonal boundary
becomes a noisy staircase. Both weaknesses are precisely what ensembles (SL5)
exist to fix: bagging averages away the variance, boosting composes shallow
trees into a flexible boundary.

On the bias–variance picture: a deep unpruned tree is low-bias / high-variance;
a shallow or heavily pruned tree (a "stump" at the extreme) is high-bias /
low-variance. Depth is the knob.

---

## Review Questions

**Conceptual checks**

1. Express a simple decision tree as a disjunction of conjunctions. Why does this
   equivalence make trees "interpretable" in a way SVMs and neural nets aren't?
2. Is ID3's inductive bias a restriction bias or a preference bias? Define both
   and justify your answer.
3. Why does ID3 stop and take a majority vote when attributes are exhausted but
   examples at the node still disagree?

**Derivation / math**

4. Compute the entropy of a set with 9 positive and 5 negative examples. Then
   compute information gain for an attribute that splits it into (6+, 2−) and
   (3+, 3−). Show the steps.
5. Show formally why information gain favors high-arity attributes, and write the
   gain-ratio correction. What quantity is in the denominator and what does it
   measure?
6. For a regression tree, what splitting criterion replaces entropy, and what do
   the leaves predict?

**Analysis — "why does it behave this way"**

7. You include a near-unique ID column as a feature. Describe exactly what ID3
   does with it, what the resulting tree looks like, and how it performs on test
   data. Which splitting criterion mitigates this?
8. Decision trees are described as high-variance. Trace *why* through the greedy
   algorithm: what happens downstream if noise flips the best attribute at the
   root?
9. Pre-pruning can suffer the "horizon effect." Explain it and explain why
   post-pruning avoids it.

**Exam-style**

10. Compare reduced-error pruning and rule post-pruning: mechanism, what data
    each needs, and one advantage of rule post-pruning.
11. A fully grown tree has 0% training error. Your classmate concludes it's the
    best model. Rebut this using the SL1 definition of overfitting.
12. In the SL report you're comparing a decision tree against boosted trees on
    two datasets. Predict, with reasons, on what kind of dataset a single pruned
    tree would be competitive — and where it would clearly lose.
