# SL6 — Kernel Methods & Support Vector Machines

**Paired reading:** `yor12-introsvm.pdf`, `svmtutorial.pdf` (Burges) · **Unit:** Supervised Learning

## The maximum-margin idea

When many hyperplanes separate the data, which one generalizes best? The SVM
answer: the one with the **largest margin** — the maximum distance to the
nearest training point on either side. Intuition: a fat separating band is the
most robust to perturbation, and (this connects to SL7/SL8) a large-margin
classifier has *lower effective capacity*, so it generalizes better.

For a hyperplane `w·x + b = 0` with labels `y ∈ {−1, +1}`, the (geometric)
margin is `1/‖w‖` to each side once you fix the scale so that the closest points
satisfy `y_i(w·x_i + b) = 1`. **Maximizing the margin = minimizing `½‖w‖²`**
subject to `y_i(w·x_i + b) ≥ 1` for all `i`. This is a **convex quadratic
program** — a single global optimum, no local minima (unlike neural nets).

## Support vectors and the dual

Solving via Lagrange multipliers yields the **dual** form. The decision function
depends on the data **only through inner products** `x_i · x_j`, and the
solution is **sparse**: only the training points lying *on* the margin have
nonzero multipliers. These are the **support vectors** — the only points that
matter. Move or delete a non-support-vector and the boundary doesn't change.
This sparsity is why SVMs are memory-efficient at prediction time and why they
resist overfitting: the model is pinned by a handful of critical points.

## Soft margin and C

Real data isn't cleanly separable, and a hard margin would be hostage to one
outlier. The **soft-margin SVM** adds slack variables `ξ_i` that allow margin
violations, penalized in the objective:

```
minimize  ½‖w‖² + C · Σ ξ_i
```

`C` is the **regularization knob and the bias–variance dial**:

- **Large C** — violations are expensive, the margin is narrow, the model fits
  the training data hard. Low bias, high variance.
- **Small C** — violations are cheap, the margin is wide and smooth, some points
  are sacrificed. High bias, low variance.

`C` is the single most important SVM hyperparameter to tune — a validation curve
over `C` is a standard SL-report figure.

## The kernel trick

The decision function uses inputs **only as inner products**. So replace every
`x_i · x_j` with a **kernel** `K(x_i, x_j)` that computes the inner product in
some higher-dimensional feature space `φ(x)` — **without ever computing `φ`
explicitly**. You get a nonlinear boundary in the original space for almost the
cost of a linear one. That is the kernel trick.

A valid kernel must be a genuine inner product in *some* space — formally,
**Mercer's condition**: the kernel (Gram) matrix must be symmetric positive
semi-definite. Common kernels:

- **Linear:** `K = x_i · x_j`. The plain SVM.
- **Polynomial:** `K = (x_i · x_j + c)^d`. Feature space = all monomials up to
  degree `d`. `d` controls capacity.
- **RBF / Gaussian:** `K = exp(−γ‖x_i − x_j‖²)`. Feature space is infinite-
  dimensional. `γ` is the second crucial knob: **large γ** → each point's
  influence is very local → wiggly boundary → high variance; **small γ** →
  influence is broad → smooth boundary → high bias. With RBF you tune **C and γ
  jointly** (a 2-D grid search).

The kernel encodes your **inductive bias** — your assumption about what
"similar" means. Choosing a kernel is choosing a hypothesis space.

## Why the margin connects to generalization

This lecture is the practical bridge to computational learning theory. The
margin gives a capacity bound that is **independent of the input dimension** —
it depends on the margin size, not on how many features you have. That's why an
RBF SVM, despite an infinite-dimensional feature space, doesn't automatically
overfit: the *effective* capacity is controlled by the margin (via C and γ), not
by the dimensionality. Keep this for SL7/SL8.

## Strengths, weaknesses, where it sits

Strengths: convex (global optimum, reproducible), strong generalization,
effective in high dimensions, flexible via kernels, sparse solution. Weaknesses:
training is roughly `O(N²)`–`O(N³)` so it scales poorly to huge datasets,
requires feature scaling (it's a distance-based method underneath), needs
careful C/γ tuning, gives no native probability estimates and no
interpretability, and is natively binary (multi-class needs one-vs-one or
one-vs-rest).

On the bias–variance picture: C and (for RBF) γ are the knobs. A high-C, high-γ
RBF SVM is the high-variance extreme; low-C, low-γ is high-bias.

---

## Review Questions

**Conceptual checks**

1. Among infinitely many separating hyperplanes, which does an SVM pick, and
   what is the generalization intuition for that choice?
2. What is a support vector? What happens to the decision boundary if you delete
   a training point that is *not* a support vector? If you delete one that is?
3. Why is the SVM optimization problem "nicer" than neural-network training?
   Name the property and its practical consequence.

**Derivation / math**

4. Show that maximizing the geometric margin is equivalent to minimizing `½‖w‖²`
   under the constraints `y_i(w·x_i + b) ≥ 1`. What fixes the scale?
5. Why does the kernel trick work — what specific structural feature of the SVM
   decision function makes it possible to never compute `φ(x)`?
6. State Mercer's condition. What property must the kernel/Gram matrix have for a
   kernel to be valid?

**Analysis — "why does it behave this way"**

7. Trace the effect of `C` from very small to very large on margin width,
   training error, and the bias–variance position.
8. For the RBF kernel, explain what large `γ` vs. small `γ` does to each training
   point's "region of influence" and hence to the boundary's shape.
9. An RBF SVM operates in an infinite-dimensional feature space yet often
   doesn't overfit. Resolve the apparent paradox using the margin/effective-
   capacity argument.

**Exam-style**

10. You must tune an RBF SVM. Which hyperparameters, why must they be tuned
    *jointly*, and what does the validation surface look like?
11. Contrast an SVM with a neural network on: optimization landscape,
    interpretability, scaling with dataset size, and what the main capacity knob
    is.
12. For the SL report, describe the figure you'd produce to show an SVM moving
    from underfitting to overfitting, and state which hyperparameter axis it
    sweeps and what each end looks like.
