# UL3 — Feature Transformation

**Paired reading:** `ica-algorithms-and-applications.pdf`, `isbell-ica-nips-1999.pdf` · **Unit:** Unsupervised Learning

## Selection vs. transformation

UL2 *kept a subset* of original features. **Feature transformation** builds
**new** features as combinations of all the originals — projecting the data into
a new, usually lower-dimensional space. More compressive power, at the cost of
interpretability: the new axes are mixtures, not original measurements. This
lecture is the payoff for Week 0's linear algebra (eigen-decomposition, SVD).

## PCA — Principal Components Analysis

**Goal:** find the orthogonal directions of **maximum variance** in the data and
re-express the data along them.

- **Mechanism:** center the data, compute the covariance matrix, take its
  **eigenvectors** (the principal components) and **eigenvalues** (the variance
  captured along each). Equivalent to the **SVD** of the data matrix. Keep the
  top `k` components.
- **The criterion is variance.** PC1 is the direction of greatest variance; PC2
  is the greatest-variance direction orthogonal to PC1; and so on. Equivalently,
  PCA finds the linear projection that **minimizes reconstruction error** (mean
  squared error of reprojecting back) — maximize-variance and
  minimize-reconstruction-error are the same optimization.
- **Components are orthogonal and uncorrelated.** PCA *de-correlates* the data.
- **Assumptions / limitations:** it is **linear**; it assumes **large variance =
  important signal**, which fails when the signal is low-variance or the noise is
  high-variance; it is **not scale-invariant** (standardize first, or a
  large-unit feature dominates every component); and the components are
  mathematical constructs, often not physically meaningful.
- **Choosing `k`:** the cumulative **explained-variance** curve — keep enough
  components to retain, say, 90–95% of variance — or the scree-plot elbow.

## ICA — Independent Components Analysis

**Goal:** different from PCA. ICA seeks a linear transformation whose components
are **statistically independent**, not merely uncorrelated. It solves the
**blind source separation** problem — the "cocktail party": given microphones
each recording a *mixture* of several speakers, recover the original
**independent source signals**.

- **Independence is strictly stronger than uncorrelatedness.** Uncorrelated means
  no *linear* relationship (zero covariance); independent means the joint
  distribution factorizes — *no* statistical relationship of any kind. PCA
  delivers the former; ICA targets the latter.
- **The engine is non-Gaussianity.** By the Central Limit Theorem, a sum
  (mixture) of independent signals is *more Gaussian* than the individual
  sources. So ICA *un-mixes* by finding the projection directions that are
  **maximally non-Gaussian** — measured by kurtosis or negentropy. Maximizing
  non-Gaussianity ⇔ minimizing mutual information among the components, which is
  the OL3 quantity doing the work here.
- **Crucial caveat:** ICA **fails if the sources are actually Gaussian** — a
  mixture of Gaussians is Gaussian and there's no non-Gaussianity to exploit, so
  the sources are unrecoverable. It also can't recover the **scale** or
  **ordering** of the components.
- Isbell & Viola (`isbell-ica-nips-1999.pdf`): ICA applied to restructuring
  high-dimensional data — it tends to find **localized, meaningful** features
  (e.g. edges in images, individual words/topics in documents), where PCA finds
  global, variance-driven mixtures.

## PCA vs. ICA — the comparison to know cold

| | PCA | ICA |
|---|---|---|
| Criterion | Maximize variance / minimize reconstruction error | Maximize statistical independence (non-Gaussianity) |
| Output components are | Orthogonal, **uncorrelated**, ordered by variance | **Independent**, not orthogonal, unordered, unscaled |
| Assumes | Signal lives in high-variance directions | Sources are non-Gaussian |
| Fails when | Signal is low-variance | Sources are Gaussian |
| Tends to find | Global structure | Local, often interpretable structure |
| Classic use | Compression, de-correlation, denoising, visualization | Blind source separation (cocktail party) |

## Random Projection

**Mechanism:** project the data onto a randomly-generated lower-dimensional
subspace — no fitting, no optimization, no eigen-decomposition.

- **Why it works at all:** the **Johnson–Lindenstrauss lemma** — a random
  projection into a surprisingly low dimension approximately preserves pairwise
  distances with high probability.
- **Trade-off:** much **cheaper** and faster than PCA, and it doesn't assume the
  signal is high-variance — but each run gives a *different* result (it's
  stochastic, so report variance across runs in the UL report) and it captures
  *less* information per dimension than PCA. It is a strong baseline precisely
  *because* it makes no assumptions — surprisingly competitive.

## Why this lecture matters

Feature transformation is half the UL report: run PCA, ICA, randomized
projections (and typically one more, e.g. a random-forest importance projection
or a manifold method from UL4) on your datasets, then **re-cluster the
transformed data and re-train a supervised learner on it.** The analysis is
about *what each transformation reveals* — PCA's variance story, ICA's
independent-sources story, RP's assumption-free story — not just downstream
accuracy. Linear algebra (eigenvectors, SVD) and OL3's information theory
(mutual information, non-Gaussianity) are both directly load-bearing here.

---

## Review Questions

**Conceptual checks**

1. How does feature transformation differ from feature selection (UL2), and what
   do you trade away to get the extra compressive power?
2. State PCA's optimization criterion two equivalent ways. Why are
   "maximize variance" and "minimize reconstruction error" the same problem?
3. What problem does ICA solve that PCA does not? State the cocktail-party setup.

**Derivation / math**

4. Walk through the PCA pipeline from raw data to top-`k` projection. Where do
   eigenvectors and eigenvalues enter, and what does each represent?
5. Explain why ICA relies on non-Gaussianity. Invoke the Central Limit Theorem
   and connect "maximize non-Gaussianity" to "minimize mutual information."
6. State the Johnson–Lindenstrauss lemma in words. What does it guarantee about
   a random projection, and why is that enough to make random projection useful?

**Analysis — "why does it behave this way"**

7. PCA can discard the signal entirely. Construct a scenario where the
   discriminative information lies in a low-variance direction, and explain what
   PCA does to it.
8. Why does ICA fail when the sources are Gaussian? Be precise about what
   property disappears.
9. Random projection makes no assumptions yet is competitive with PCA. Explain
   why "no assumptions" is a *strength* here, and name the cost you pay for it.

**Exam-style**

10. Reproduce the PCA-vs-ICA table from memory: criterion, properties of the
    output components, key assumption, failure mode, typical use.
11. "PCA components are uncorrelated; ICA components are independent." Explain
    the difference between uncorrelated and independent and why ICA's is the
    stronger condition.
12. For the UL report you transform a dataset with PCA, ICA, and RP, then
    re-cluster each. Predict, with reasons, how the cluster structure might
    differ across the three transformations.
