# Math Foundations — Calculus & Optimization

**Focus area A** (flagged weak area)

> This is the math under SL3 (backpropagation), OL1–OL2 (randomized and
> gradient-based optimization), and SL6 (the SVM constrained optimization).
> Backprop *is* the chain rule; AdamW *is* gradient descent with patches; the SVM
> *is* a Lagrangian. Close these gaps in Week 0. Log what stalls you in
> `math_gaps_log.md`.

## Derivatives and gradients

A **derivative** `df/dx` is the instantaneous rate of change — the slope. For a
function of many variables (every loss function in ML), the generalization is
the **gradient**:

```
∇f(x) = [ ∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ ]
```

Two facts that drive everything:

- The gradient **points in the direction of steepest ascent**. So `−∇f` points
  downhill — that is the entire idea of gradient descent.
- At a **minimum, maximum, or saddle point, the gradient is zero**. Setting
  `∇f = 0` and solving is how you derive closed-form estimators (e.g. the MLE in
  the probability notes, or least-squares).

## The chain rule — and why it *is* backpropagation

The **chain rule** computes the derivative of a composition:

```
d/dx f(g(x)) = f'(g(x)) · g'(x)
```

A neural network is a deep composition of functions (layer ∘ layer ∘ ... ∘
loss). **Backpropagation is nothing more than the chain rule applied through
that composition**, organized so that intermediate results are reused rather
than recomputed:

- **Forward pass** evaluates the composition, caching each layer's output.
- **Backward pass** multiplies local derivatives from the loss back toward the
  inputs — each layer's gradient is the downstream gradient times its own local
  derivative. That product structure is the chain rule, layer by layer.

If the chain rule is solid, SL3 backprop is bookkeeping, not magic.

## Gradient descent

The update rule behind SL3 and all of OL2:

```
θ ← θ − η · ∇L(θ)
```

`η` is the **learning rate** — step size. Too large: overshoot, oscillate,
diverge. Too small: crawl, stall on plateaus. The behavior depends entirely on
the **shape of the loss surface**:

- **Convex** surface (one bowl) — gradient descent reaches the global minimum.
- **Non-convex** surface — it finds a *local* minimum, and *which* one depends on
  initialization and the trajectory. This is the SL3 caveat and the reason OL2's
  momentum/adaptive tricks exist (escape plateaus, ravines, saddles).

## Convexity — why it's the property everyone wants

A function is **convex** if the line segment between any two points on its graph
lies on or above the graph (equivalently, the second derivative / Hessian is
`≥ 0`). Why it matters:

- A convex function has **no local minima other than the global one** — so
  gradient descent is *guaranteed* to find the best solution.
- This is exactly the structural difference between **SVMs** (SL6 — convex
  quadratic program, one global optimum, reproducible) and **neural networks**
  (SL3 — non-convex, many local minima, init-dependent). When the exam asks "why
  is SVM optimization 'nicer' than NN training," the answer is *convexity*.

## Constrained optimization & Lagrange multipliers

Sometimes you minimize subject to constraints — the SVM minimizes `½‖w‖²`
**subject to** `y_i(w·x_i + b) ≥ 1`. **Lagrange multipliers** convert a
constrained problem into an unconstrained one by folding each constraint into the
objective with a multiplier `α_i`:

```
L(w, b, α) = ½‖w‖² − Σ α_i [ y_i(w·x_i + b) − 1 ]
```

Solving this is what produces the SVM **dual** form — the one expressed purely in
inner products `x_i · x_j`, which is what makes the **kernel trick** possible
(SL6). The multipliers `α_i` are non-zero only for the **support vectors**. You
don't need to derive the dual from scratch for the course, but you should know
*that* the SVM's nice properties (dual form, sparsity, kernelizability) come out
of this Lagrangian.

## Gradient-based vs. gradient-free — the OL1 connection

Everything above assumes you *have* a gradient. When you don't — `f` is
discontinuous, a black box, or combinatorial — you fall back to the
**gradient-free** methods of OL1 (hill climbing, simulated annealing, GA, MIMIC).
The calculus notes and OL1 are two halves of one picture: *use the gradient when
it exists and is informative; reach for randomized optimization when it doesn't.*

## Where it shows up in CS7641

| Concept | Where |
|---|---|
| Chain rule | SL3 backpropagation |
| Gradient descent, learning rate | SL3, OL2 (SGD → AdamW) |
| Convex vs. non-convex | SL6 (SVM, convex) vs. SL3 (NN, non-convex) |
| `∇f = 0` to find optima | MLE/MAP derivations (OL4, prob notes) |
| Lagrange multipliers / duality | SL6 SVM dual, support vectors, kernel trick |
| When no gradient exists | OL1 randomized optimization |

---

## Review Questions

**Conceptual checks**

1. What does the gradient `∇f` represent geometrically, and why does the update
   rule subtract it rather than add it?
2. State, in one sentence, why "backpropagation is just the chain rule." What do
   the forward and backward passes each compute?
3. What does it mean for a function to be convex, and what is the single most
   important consequence for optimization?

**Derivation / math**

4. Apply the chain rule to `f(g(x))` where `f(u) = u²` and `g(x) = 3x + 1`.
   Then explain how this scales up to a multi-layer network.
5. Write the gradient-descent update and describe what happens to the trajectory
   when `η` is far too large, and when it is far too small.
6. Set up the SVM as a constrained optimization problem and write its Lagrangian.
   What role do the multipliers `α_i` play, and which ones end up non-zero?

**Analysis — "why does it behave this way"**

7. Why is SVM training guaranteed to find the global optimum while neural-network
   training is not? Name the property and connect it to reproducibility of
   results.
8. Gradient descent on a non-convex loss can land in different solutions on
   different runs. Name the two things that determine which solution, and name
   one OL2 technique that mitigates the problem.
9. Explain why the existence of a usable gradient is the dividing line between
   OL2's methods and OL1's methods. Give an example problem on each side of the
   line.

**Exam-style**

10. "Setting the gradient to zero" is how several closed-form results in this
    course are derived. Name one (from the probability notes or OL4) and sketch
    the step.
11. Trace the chain: SVM constrained problem → Lagrangian → dual form → kernel
    trick. What does each step enable?
12. Convexity, the chain rule, and gradient descent each map to a specific
    CS7641 lecture. Name the lecture for each and the one-line reason.
