# SL8 — VC Dimension

**Paired reading:** VC-dimension reading (hosted on Canvas) · **Unit:** Supervised Learning

## Why we need it

SL7's sample-complexity bound used `ln|H|` — useless when `|H|` is infinite,
which is the case for every interesting learner (linear separators, neural nets,
SVMs). **VC dimension** is the replacement: a measure of the *effective*
capacity of a hypothesis space that works even when `|H| = ∞`. It is the formal
peak of the unit and a near-certain final-exam topic.

## Shattering

A hypothesis space `H` **shatters** a set of points if, for **every possible
labeling** of those points (all `2^n` of them, for `n` points), some hypothesis
in `H` classifies them exactly that way. Shattering means H is rich enough to
realize *any* dichotomy of that particular set.

Important subtlety: you need *one* set of `n` points that can be shattered — not
*all* sets of `n` points. You get to choose the most favorable configuration.

## The definition

> **The VC dimension of H is the size of the largest set of points that H can
> shatter.** If H can shatter arbitrarily large sets, `VC(H) = ∞`.

To prove `VC(H) = d` you must show **both**:

1. **Lower bound (≥ d):** *exhibit* one specific set of `d` points and show H
   shatters it (handles all `2^d` labelings).
2. **Upper bound (< d+1):** show that **no** set of `d+1` points can be shattered
   by H — i.e. for *every* arrangement of `d+1` points, some labeling is
   impossible.

The upper bound is the harder, more commonly botched half. Both directions are
required; an exam answer with only one is incomplete.

## Canonical results — memorize these

- **Interval on the real line** (`a ≤ x ≤ b`): VC = **2**. Two points can be
  labeled all 4 ways; three points labeled `+ − +` cannot be captured by a single
  interval.
- **Linear separators / perceptrons in `d` dimensions:** VC = **d + 1**. In 2-D
  a line has VC = 3: three non-collinear points can be shattered; no 4 points can
  (a labeling like XOR's diagonal pattern is impossible).
- **Axis-aligned rectangles in the plane:** VC = **4**.
- **A single threshold** (`x > θ`) on the line: VC = **1**.
- **Finite H:** `VC(H) ≤ log₂|H|` — VC dimension generalizes the finite-H story.
- **An infinite H can still have finite VC** — linear separators are the prime
  example. Conversely, some infinite H (e.g. `sin(αx)` with free `α`) have VC = ∞
  despite a single real parameter — VC dimension is *not* the number of
  parameters.

## The sample-complexity bound

VC dimension slots into a PAC-style bound, replacing `ln|H|`:

```
m ≥ (1/ε) · ( 8·VC(H)·log₂(13/ε) + 4·log₂(2/δ) )
```

The exact constants are not the point — the **structure** is: required sample
size grows (roughly) **linearly with VC(H)**. Higher capacity ⇒ more data needed
to guarantee generalization. There is also a lower bound showing you *cannot* PAC-
learn with fewer than `Ω(VC(H)/ε)` examples, so VC dimension characterizes sample
complexity from both sides.

**The punchline:** a hypothesis class is PAC-learnable **if and only if its VC
dimension is finite.** Finite VC ⇔ learnable. This is the central theorem.

## How it ties the unit together

- **Bias–variance, formalized:** VC dimension *is* the capacity axis. Low VC =
  high bias, can't fit complex targets, but generalizes from little data. High VC
  = low bias, fits anything, but needs lots of data to not overfit. The
  bias–variance tradeoff from SL1 is the VC dimension dial.
- **Occam's razor, formalized:** prefer the hypothesis from the lowest-VC class
  that still fits — it carries the strongest generalization guarantee.
- **SVMs (SL6):** the margin argument is a capacity-control story. A large-margin
  classifier has *effective* VC dimension bounded by the margin (and the data
  radius) — **independent of the input dimensionality**. That is the rigorous
  reason an infinite-dimensional RBF SVM doesn't automatically overfit.
- **Structural risk minimization:** instead of minimizing training error alone,
  minimize training error *plus* a capacity penalty that grows with VC dimension —
  pick the model that best balances fit against capacity.

## The catch (same as SL7)

The VC bounds are **loose** — correct but pessimistic, often demanding orders of
magnitude more data than works in practice. Their value is the *qualitative*
law: capacity must be controlled, and finite VC is exactly what makes learning
possible at all.

---

## Review Questions

**Conceptual checks**

1. Define "shatter." Why does proving a class shatters *some* set of `n` points
   require only one favorable configuration, not all configurations?
2. State the VC-dimension definition precisely. What are the *two* things you
   must prove to establish `VC(H) = d`, and which is usually harder?
3. Why was VC dimension needed at all — what specific shortcoming of the SL7
   `ln|H|` bound does it repair?

**Derivation / proof**

4. Prove that the VC dimension of intervals `[a,b]` on the real line is exactly
   2: shatter 2 points, then show 3 cannot be shattered.
5. Linear separators in 2-D have VC = 3. Exhibit a shatterable 3-point set, then
   argue no 4-point set can be shattered (use the XOR-style labeling).
6. Show `VC(H) ≤ log₂|H|` for finite H. Why does this mean VC dimension
   *generalizes* the finite-hypothesis-space analysis?

**Analysis — "why does it behave this way"**

7. Give an example of an infinite hypothesis space with *finite* VC dimension,
   and one with a single parameter but *infinite* VC dimension. What does this
   prove about the relationship between VC dimension and parameter count?
8. Explain how VC dimension is the formal version of the bias–variance tradeoff.
   What is high-VC, what is low-VC, in bias/variance terms?
9. An RBF SVM lives in an infinite-dimensional feature space. Explain, via
   margin-based effective VC dimension, why it can still generalize.

**Exam-style**

10. State the central theorem connecting VC dimension and PAC-learnability (the
    "if and only if").
11. Write the VC sample-complexity bound and explain how required sample size
    scales with VC(H), ε, and δ. Which dependence is linear, which is
    logarithmic?
12. Define structural risk minimization and contrast it with plain empirical
    risk (training-error) minimization. What does the extra term penalize?
