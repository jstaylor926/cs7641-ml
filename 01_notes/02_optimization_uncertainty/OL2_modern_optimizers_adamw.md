# OL2 — Deconstructing AdamW (Modern Optimizers)

**Paired reading:** curated AdamW readings (posted on Canvas during the term) · **Unit:** Optimization & Uncertainty

> This is the *gradient-based* counterpart to OL1's gradient-free methods. Where
> OL1 asked "what if you have no gradient," OL2 asks "given that you *do* have a
> gradient, how do you use it well." AdamW is built up one fix at a time — learn
> it as a stack of patches, because the exam wants you to know *what each layer
> fixes*.

## Layer 0 — Gradient Descent and SGD

Plain gradient descent: `θ ← θ − η ∇L(θ)`. On large datasets, computing the full
gradient every step is wasteful, so **Stochastic Gradient Descent (SGD)** uses a
**mini-batch** estimate of the gradient each step.

Problems with vanilla SGD that everything downstream is trying to fix:

- The **learning rate η** is a single global scalar — wrong for parameters with
  very different gradient scales.
- **Noisy** mini-batch gradients make the trajectory zig-zag.
- It crawls through **ravines** (steep in one direction, flat in another) and
  stalls on **plateaus / saddle points** — common in high-dimensional non-convex
  loss surfaces.

## Layer 1 — Momentum

Accumulate an exponentially-decayed running average of past gradients (the
"velocity") and step with that:

```
v ← β·v + (1−β)·∇L      θ ← θ − η·v
```

**Fixes:** damps oscillation across a ravine (opposing components cancel in the
average) while accumulating speed along the consistent downhill direction; helps
coast through small bumps, plateaus, and saddle points. This is the same idea as
neural-net momentum in SL3, made the default.

## Layer 2 — Adaptive learning rates (RMSProp / AdaGrad)

Give **each parameter its own effective learning rate**, scaled down for
parameters that have seen large gradients. RMSProp keeps a running average of
*squared* gradients and divides the step by its square root:

```
s ← β₂·s + (1−β₂)·(∇L)²      θ ← θ − η·∇L / (√s + ε)
```

**Fixes:** parameters with large/frequent gradients take smaller steps, sparse or
small-gradient parameters take larger ones — handles the "one global η is wrong"
problem. (AdaGrad does this too but its denominator only grows, so the step size
decays to zero and learning stalls; RMSProp's decay fixes that.)

## Layer 3 — Adam = Momentum + RMSProp

**Adam** combines both: a first-moment estimate `m` (momentum) *and* a
second-moment estimate `v` (RMSProp-style scaling), plus a **bias correction**
because `m` and `v` are initialized at zero and are biased toward zero in the
early steps.

```
m ← β₁·m + (1−β₁)·∇L
v ← β₂·v + (1−β₂)·(∇L)²
m̂ = m/(1−β₁ᵗ),  v̂ = v/(1−β₂ᵗ)        # bias correction
θ ← θ − η · m̂ / (√v̂ + ε)
```

**Fixes:** directional smoothing (from `m`) *and* per-parameter scaling (from
`v`) in one optimizer, with the early-training bias removed. Adam is the robust,
low-tuning default — which is exactly why it became ubiquitous.

## Layer 4 — AdamW = Adam + decoupled weight decay

**Weight decay** is L2 regularization — pull weights toward zero to reduce
overfitting (the SL3 regularizer). The subtle bug: in plain Adam, adding the L2
penalty to the gradient means it gets divided by `√v̂` along with everything
else, so the *effective* amount of regularization varies per parameter and is no
longer true weight decay.

**AdamW decouples it:** apply the weight decay directly to the parameter, as a
separate term, not through the gradient:

```
θ ← θ − η · m̂/(√v̂ + ε) − η·λ·θ
```

**Fixes:** restores weight decay to its intended, uniform regularizing behavior.
Empirically this generalizes better, which is why AdamW is the modern default
for training large models.

## The whole stack in one view

| Layer | Adds | Fixes |
|---|---|---|
| SGD | mini-batch gradient | full-gradient cost |
| + Momentum | velocity (avg of past gradients) | ravine zig-zag, plateaus, saddles |
| + RMSProp | per-parameter scaling (avg sq. gradient) | one global η is wrong |
| = Adam | both, + bias correction | combines them; fixes zero-init bias |
| = AdamW | decoupled weight decay | regularization corrupted by `√v̂` scaling |

## Connecting it to the unit

This is **inductive bias as an optimization choice**. The optimizer doesn't
change the hypothesis space, but it changes *which* hypothesis you land on — the
trajectory through a non-convex landscape determines the solution. It is also a
concrete answer to OL1's question: gradient-free methods (RHC/SA/GA) are what you
reach for *when this entire stack is unavailable* because there's no usable
gradient.

---

## Review Questions

**Conceptual checks**

1. Name the three concrete problems with vanilla SGD that the rest of the
   AdamW stack is built to fix.
2. AdamW is "two ideas plus a correction plus a fix." Name the two ideas, the
   correction, and the fix, and say what each contributes.
3. Why does the optimizer affect generalization at all, if it doesn't change the
   hypothesis space? Frame your answer in terms of the loss landscape.

**Derivation / math**

4. Write the momentum update. Show mathematically why it damps oscillation
   across a ravine but accumulates speed along a consistent descent direction.
5. Write the RMSProp update and explain what the `√s` denominator does for a
   parameter with persistently large gradients versus one with tiny gradients.
6. Why does Adam need bias correction? What are `m` and `v` initialized to, and
   what does `m/(1−β₁ᵗ)` correct for in early steps?

**Analysis — "why does it behave this way"**

7. AdaGrad's learning eventually stalls; RMSProp's doesn't. Explain the
   difference in their second-moment accumulation.
8. Explain the bug AdamW fixes: walk through what happens to an L2 penalty when
   it is added to the gradient and then divided by `√v̂` in plain Adam.
9. Adam is described as "low-tuning." Which SGD hyperparameter headaches does it
   remove or soften, and which knobs do you still have to set?

**Exam-style**

10. Reconstruct the optimizer stack table from memory: for each layer, what it
    adds and what it fixes.
11. Contrast OL1's randomized optimization with OL2's gradient methods: what
    information does each have access to, and when would you be *forced* to use
    OL1's methods?
12. Momentum appears both here and in SL3's backpropagation lecture. State the
    shared mechanism and why it helps in a non-convex landscape.
