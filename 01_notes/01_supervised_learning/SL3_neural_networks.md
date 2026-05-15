# SL3 — Neural Networks

**Paired reading:** Mitchell Ch 4 · **Unit:** Supervised Learning

## From perceptron to network

The **perceptron** is a single linear threshold unit: it computes a weighted sum
`w·x + b` and fires `1` if the sum exceeds 0. Geometrically it is a hyperplane;
it can represent any **linearly separable** boolean function (AND, OR) but not
XOR. The **perceptron training rule** — `w ← w + η(y − ŷ)x` — provably converges
to a separating hyperplane *if one exists*, and does not converge otherwise.

The **delta rule / LMS** is the gradient-descent alternative on the
*un-thresholded* linear output, minimizing squared error. Unlike the perceptron
rule it converges (to the least-squares fit) even when the data is not
separable — it just converges to the best linear approximation. The distinction
matters: perceptron rule operates on the thresholded output and needs
separability; delta rule operates on the linear output and degrades gracefully.

XOR forces the move to **multilayer networks**. Stack linear units and the
network collapses to a single linear map — so you need a **nonlinear
activation** between layers. The classic choice is the **sigmoid**
`σ(z) = 1/(1+e^{−z})`, which is differentiable (essential for gradient methods)
and squashes to (0,1). Modern nets use **ReLU** `max(0, z)` because it avoids the
vanishing-gradient problem sigmoids suffer in deep stacks (this connects forward
to OL2).

## Backpropagation

Backprop is just the **chain rule** applied to compute the gradient of the loss
with respect to every weight, plus gradient descent to update them.

- **Forward pass:** feed the input through, layer by layer, caching each unit's
  activation.
- **Backward pass:** compute the error at the output, then propagate it
  backward — each layer's "delta" is the downstream delta times the local
  derivative of the activation. The weight gradient at each connection is
  `(upstream activation) × (downstream delta)`.
- **Update:** `w ← w − η · ∂Loss/∂w`.

Key properties to internalize:

- The loss surface is **non-convex** — backprop finds a *local* minimum, not the
  global one. In practice many local minima are "good enough," and this is
  empirical, not guaranteed.
- It is **sensitive to initialization** — start all weights equal and units
  learn identical things (the symmetry never breaks); start them too large and
  sigmoids saturate. Use small random weights.
- **Momentum** adds a fraction of the previous update to the current one,
  smoothing the trajectory and helping escape shallow local minima and plateaus.
  This is the conceptual ancestor of the modern optimizers in OL2.

## Representational power

A network with **one sufficiently wide hidden layer** of sigmoid units can
approximate any continuous function to arbitrary accuracy (universal
approximation). So the hypothesis space is, in the limit, almost unrestricted —
which means the inductive bias is *not* "what can it represent" but **how
backprop searches**: it favors smooth interpolation between training points and,
because it starts from small weights, favors near-linear functions early in
training, growing complexity as it trains. Early stopping exploits this.

## The bias–variance knobs

Neural nets are flexible, so they overfit readily. The levers:

- **Network size** (layers, units): more capacity → lower bias, higher variance.
- **Training time:** longer training fits the data more closely. **Early
  stopping** — halt when validation error starts rising — is a regularizer that
  works *because* of the small-weights-grow-complexity dynamic above.
- **Weight decay / L2 regularization:** penalize large weights, pulling toward
  simpler (smoother) functions.
- **Learning rate η:** too large → divergence or oscillation; too small →
  painfully slow, gets stuck. Not a bias–variance knob directly but it governs
  whether training works at all.

A learning curve and a validation curve over training epochs are the standard
diagnostics — and exactly the figures the SL report wants.

## Strengths, weaknesses, where nets sit

Strengths: highly expressive, handle high-dimensional and noisy input, learn
their own features, predict fast once trained. Weaknesses: slow to train,
non-convex (no convergence guarantee), many hyperparameters, sensitive to
feature scaling (**standardize inputs**), and a black box — the opposite of a
decision tree on interpretability. They want a lot of data to not overfit.

On the bias–variance picture: small net trained briefly = high bias; large net
trained to convergence with no regularization = high variance. Unlike a decision
tree, the dominant knob is often *training time*, not just architecture.

---

## Review Questions

**Conceptual checks**

1. Why can't a single perceptron represent XOR? What is the minimum architecture
   that can, and what makes it work?
2. State the difference between the perceptron training rule and the delta rule
   in terms of (a) what output they operate on and (b) their behavior when the
   data is not linearly separable.
3. Why must the activation function be nonlinear? What happens to a deep network
   of purely linear units?

**Derivation / math**

4. Backpropagation is "just the chain rule." For a 2-layer net, write the
   gradient of the loss w.r.t. a hidden-layer weight and identify which factor is
   the "upstream activation" and which is the "downstream delta."
5. Why is small *random* initialization required? Walk through what happens to
   the gradients if all weights start at exactly the same value.
6. Write the sigmoid and its derivative. Explain, using the derivative, why deep
   sigmoid stacks suffer vanishing gradients and why ReLU helps.

**Analysis — "why does it behave this way"**

7. Early stopping reduces overfitting. Explain the mechanism via the
   "weights start small and grow" view of backprop's inductive bias — why is
   stopping early equivalent to limiting model complexity?
8. You train two nets on the same data; one converges to a much worse solution.
   Give two distinct reasons rooted in the non-convexity and initialization
   properties of backprop.
9. Momentum helps training. What two specific failure modes of plain gradient
   descent does it address, and how?

**Exam-style**

10. Universal approximation says one hidden layer can fit anything. Why, then, do
    we still talk about neural networks having an inductive bias? Where does the
    bias actually live?
11. Contrast neural nets with decision trees on: training cost, interpretability,
    need for feature scaling, and the dominant bias–variance knob.
12. For the SL report, which plots would you produce to *demonstrate* a neural
    net overfitting, and what would each plot show at the point overfitting
    begins?
