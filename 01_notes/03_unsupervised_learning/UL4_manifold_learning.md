# UL4 — Manifold Learning

**Paired reading:** Bishop Ch 12 (LLE & Isomap), t-SNE paper (source separately) · **Unit:** Unsupervised Learning

## The manifold hypothesis

PCA and ICA (UL3) are **linear** — they project onto flat subspaces. But
high-dimensional data often lies on or near a **low-dimensional curved surface
(a manifold)** embedded in the high-dimensional space. The canonical picture is
the **"Swiss roll"**: data in 3-D that is intrinsically a 2-D sheet, rolled up.

PCA fails on the Swiss roll: it sees the global 3-D variance and "flattens" the
roll, smashing together points that are far apart *along the sheet* but close in
straight-line 3-D distance. The fix is to respect **geodesic distance** —
distance measured *along the manifold* — not Euclidean distance through the
ambient space. Manifold learning = **nonlinear dimensionality reduction** that
unrolls the manifold.

## Isomap

Isomap = "isometric mapping." The idea: approximate geodesic distance with a
graph.

1. Build a **neighborhood graph** — connect each point to its `k` nearest
   neighbors, with Euclidean edge weights (valid *locally*, where the manifold is
   approximately flat).
2. Estimate the **geodesic distance** between every pair as the **shortest path**
   through that graph.
3. Apply **classical MDS (multi-dimensional scaling)** to that geodesic distance
   matrix to find a low-dimensional embedding that preserves those distances.

**Preserves global structure** — the overall shape of the manifold. Weaknesses:
sensitive to the neighborhood size `k` (too large "short-circuits" the manifold
by connecting points across a fold; too small fragments the graph), and the
all-pairs shortest path step is expensive.

## LLE — Locally Linear Embedding

A different bet: don't try to preserve global distances, preserve **local
geometry**.

1. For each point, find its `k` nearest neighbors and compute the **weights**
   that best **reconstruct the point as a linear combination of those
   neighbors**.
2. Find a low-dimensional embedding in which **each point is still reconstructed
   by the same weights from the same neighbors.**

The insight: a manifold is *locally* linear, so the local reconstruction weights
are an intrinsic, embedding-invariant description of local shape. **Preserves
local structure**; cheaper than Isomap (no all-pairs shortest paths); but it can
distort the global layout and is also sensitive to `k`.

## t-SNE

Built for **visualization** (embedding to 2-D or 3-D), and the one you'll most
likely use in the UL report.

- **Mechanism:** convert pairwise distances into **probabilities** that two
  points are neighbors — in the high-dimensional space (Gaussian kernel) and in
  the low-dimensional map (heavier-tailed Student-t kernel) — then move the
  low-D points to **minimize the KL divergence** between the two probability
  distributions. (KL divergence — straight from OL3.)
- The Student-t tail in the low-D space is the trick that **fixes the crowding
  problem**: it gives moderate-distance points room, so clusters separate
  cleanly instead of collapsing into a blob.
- **Excellent at revealing cluster structure**, which is why it's a go-to
  diagnostic plot.
- **Read t-SNE plots with discipline** — the standard caveats, and a likely exam
  question:
  - **Cluster sizes are not meaningful** — t-SNE expands dense clusters and
    contracts sparse ones.
  - **Distances *between* clusters are not meaningful** — only local neighborhood
    structure is preserved.
  - It is **stochastic** — different runs/seeds give different layouts.
  - The **perplexity** hyperparameter strongly changes the picture; try several.
  - It is for **visualization**, not as a preprocessing step for a downstream
    learner (it has no clean "transform new points" operation).
  - (UMAP is the newer alternative: similar visual quality, faster, and somewhat
    better at preserving global structure.)

## The comparison to carry

| Method | Linear? | Preserves | Main use | Key knob | Caveat |
|---|---|---|---|---|---|
| PCA (UL3) | Yes | Global variance | Compression, preprocessing | # components | Misses curved structure |
| Isomap | No | Global (geodesic) structure | Unrolling manifolds | neighborhood `k` | Short-circuiting; expensive |
| LLE | No | Local geometry | Unrolling manifolds | neighborhood `k` | Distorts global layout |
| t-SNE | No | Local neighborhoods | **Visualization only** | perplexity | Sizes/between-distances meaningless; stochastic |

## Where it sits

UL4 closes the unsupervised unit and the dimensionality-reduction arc that
started in UL3: **selection (UL2) → linear transformation (UL3) → nonlinear
manifold learning (UL4)**, a steady relaxation of assumptions. For the UL report,
t-SNE is the standard tool for *visualizing* whether your clusters and your
reduced representations actually have structure — but remember it shows you
neighborhoods, not geometry.

---

## Review Questions

**Conceptual checks**

1. State the manifold hypothesis. Why does PCA fail on the Swiss roll — what does
   it do to two points that are far apart along the sheet but close in 3-D?
2. Define geodesic distance and explain why respecting it (rather than Euclidean
   distance) is the central idea of manifold learning.
3. Isomap and LLE both unroll manifolds but bet on different things. State what
   each one preserves.

**Derivation / math**

4. Walk through Isomap's three steps. Where does the geodesic distance get
   approximated, and what does the final MDS step accomplish?
5. Explain LLE's two-stage procedure. Why are the local reconstruction weights an
   *embedding-invariant* description of local shape?
6. t-SNE minimizes a KL divergence. Between which two distributions, and why does
   using a Student-t kernel in the low-dimensional space fix the crowding
   problem?

**Analysis — "why does it behave this way"**

7. Isomap's neighborhood size `k` causes "short-circuiting" if set too large.
   Describe exactly what goes wrong in the neighborhood graph and downstream.
8. A classmate reads a t-SNE plot and concludes "cluster A is twice as big as
   cluster B, and A is far from C." Correct both claims and explain what t-SNE
   *does* faithfully represent.
9. Why is t-SNE a poor choice as a preprocessing step for a downstream
   classifier, even though it produces a great-looking low-dimensional map?

**Exam-style**

10. Reproduce the PCA / Isomap / LLE / t-SNE comparison table from memory.
11. Order PCA, ICA, Isomap/LLE, and t-SNE by how strong an assumption they make
    about the data's structure, and explain the progression.
12. For the UL report, you produce a t-SNE plot of a dataset before and after
    PCA. What can you legitimately conclude from comparing the two plots, and
    what would be an over-claim?
