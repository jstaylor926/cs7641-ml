# Math Foundations — Linear Algebra & Eigenproblems

**Paired reading:** `02_readings/00_prerequisites/Eigenproblems.fm.pdf` · **Focus area A** (flagged weak area)

> This is the math that UL3 (PCA/ICA) and SL6 (SVMs) are *built on*. Close these
> gaps in Week 0, not when the unit exposes them. Where a derivation stalls you,
> log it in `math_gaps_log.md` and close it the same week.

## Vectors and the inner product

A **vector** is a point/direction in `ℝⁿ`. The two operations everything else
rests on:

- **Norm** `‖x‖ = √(x·x)` — the length of `x`. The L2 norm; `‖x − y‖` is
  Euclidean distance, which is what kNN (SL4) and k-means (UL1) measure.
- **Inner (dot) product** `x·y = Σ xᵢyᵢ = ‖x‖‖y‖cos θ`. It measures **alignment**:
  zero ⇔ orthogonal (perpendicular). This is *the* operation SVMs depend on — the
  kernel trick (SL6) works precisely because the SVM decision function uses data
  only through inner products.

**Projection** of `x` onto a unit vector `u` is `(x·u)u` — the component of `x`
in the `u` direction. PCA is, at its core, choosing the `u`s to project onto.

## Matrices as linear transformations

A matrix `A` is a **linear map**: `x ↦ Ax`. Read every matrix as "a thing that
rotates, scales, shears, and projects space." Key objects:

- **Rank** — the dimension of the output space; the number of linearly
  independent columns. A rank-deficient matrix collapses dimensions (loses
  information).
- **Transpose `Aᵀ`**, and **symmetric** matrices `A = Aᵀ` — covariance matrices
  (the heart of PCA) are always symmetric.
- **Inverse `A⁻¹`** — undoes the map; exists only if `A` is square and full-rank.
- **Orthogonal matrix** `QᵀQ = I` — a pure rotation/reflection; preserves lengths
  and angles. Eigenvector matrices of symmetric matrices are orthogonal.
- **Positive semi-definite (PSD)** — `xᵀAx ≥ 0` for all `x`. Covariance matrices
  and valid kernel (Gram) matrices are PSD — this is exactly **Mercer's
  condition** from SL6.

## Eigenvectors and eigenvalues — the core idea

For a square matrix `A`, an **eigenvector** `v` is a direction that `A` only
**stretches**, without rotating:

```
A v = λ v
```

`λ` is the **eigenvalue** — the stretch factor along `v`. Found by solving the
characteristic equation `det(A − λI) = 0`.

Why this is the load-bearing concept for the course:

- Eigenvectors are the **natural axes** of the transformation `A`. In those
  coordinates, `A` is just independent scaling — no mixing.
- For a **symmetric** matrix (e.g. any covariance matrix), the eigenvectors are
  **orthogonal** and the eigenvalues are **real**. This is the *spectral
  theorem*, and it is what makes PCA work.

## PCA in one paragraph (the payoff)

Center the data, form the **covariance matrix** `C` (symmetric, PSD). Its
**eigenvectors are the principal components** — orthogonal directions; its
**eigenvalues are the variance captured along each**. Sort by eigenvalue, keep
the top `k`. That's it: PCA is the eigen-decomposition of the covariance matrix.
"Maximize variance" ⇔ "pick the largest-eigenvalue directions." (See UL3.)

## Singular Value Decomposition (SVD)

Eigen-decomposition needs a *square* matrix; **SVD generalizes it to any matrix**:

```
A = U Σ Vᵀ
```

`U` and `V` are orthogonal (rotations), `Σ` is diagonal with non-negative
**singular values**. Interpretation: *any* linear map is a rotation, then an
axis-aligned scaling, then another rotation.

- SVD applied to the (centered) data matrix gives PCA directly — the right
  singular vectors `V` are the principal components, the singular values are
  `√(eigenvalues)` of the covariance matrix. In practice PCA is computed via SVD
  because it is numerically more stable.
- **Low-rank approximation:** keeping the top-`k` singular values gives the best
  rank-`k` approximation of `A` (Eckart–Young) — this *is* dimensionality
  reduction and the formal version of "minimize reconstruction error" from UL3.

## Where it shows up in CS7641

| Concept | Where |
|---|---|
| Inner products, projections | SL6 kernels/SVMs; kNN/k-means distances |
| PSD matrices | SL6 Mercer's condition; covariance matrices |
| Eigen-decomposition of covariance | UL3 PCA |
| SVD / low-rank approximation | UL3 PCA, reconstruction error |
| Orthogonality vs. independence | UL3 PCA (uncorrelated) vs. ICA (independent) |
| Linear maps, rank | UL3/UL4 dimensionality reduction generally |

---

## Review Questions

**Conceptual checks**

1. Geometrically, what does the dot product `x·y` measure? What does `x·y = 0`
   mean, and why does that matter for SVMs?
2. What is special about the eigenvectors of a *symmetric* matrix, and why is
   "symmetric" the case that actually matters for PCA?
3. State the difference between eigen-decomposition and SVD. Why can't you always
   eigen-decompose a data matrix directly?

**Derivation / math**

4. Write the eigenvector equation and the characteristic equation used to find
   eigenvalues. For `A = [[2,0],[0,3]]`, find the eigenvectors and eigenvalues by
   inspection and explain why they're obvious.
5. Show that projecting `x` onto a unit vector `u` gives `(x·u)u`. What is the
   length of that projection?
6. Explain, step by step, why PCA reduces to the eigen-decomposition of the
   covariance matrix — what do the eigenvectors and eigenvalues each become?

**Analysis — "why does it matter"**

7. PCA's components are *orthogonal*; ICA's are *independent*. Connect each to a
   linear-algebra (vs. statistical) property and explain why orthogonal is the
   weaker condition.
8. A covariance matrix and a valid SVM kernel matrix are both PSD. Explain what
   PSD guarantees and why each application needs it.
9. Why is keeping the top-`k` singular values "the best rank-`k` approximation"?
   Tie this to UL3's "minimize reconstruction error" framing.

**Exam-style**

10. Given the eigenvalues of a covariance matrix are `[8, 5, 1, 0.5, 0.1]`, how
    many principal components would you keep to retain ~93% of the variance, and
    how did you compute that?
11. Explain how SVD expresses *any* linear transformation as three simpler
    operations. Name them in order.
12. Where does the inner product appear in SL6, and why does that single fact
    make the kernel trick possible?
