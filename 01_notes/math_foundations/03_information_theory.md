# Math Foundations — Information Theory (Quick Reference)

**Paired reading:** `02_readings/optimization_uncertainty/` (3 PDFs) · **Focus area A** (flagged weak area)

> Information theory is unusual: it is both a **Week-0 math prerequisite** *and* a
> full lecture (**OL3**). This file is the compact refresher / formula sheet — the
> minimum you need so SL2's decision trees don't ambush you before OL3 arrives.
> For the conceptual depth, the No Free Lunch theorem, and the full treatment,
> see **`../02_optimization_uncertainty/OL3_information_theory.md`** — don't
> duplicate the effort, cross-read.

## The four quantities — definitions

**Entropy** — uncertainty / expected surprise in a single variable, in bits:

```
H(X) = − Σ_x p(x) log₂ p(x)
```

`0` when certain; maximal (`log₂ n`) when uniform over `n` outcomes. The
`−log₂ p(x)` term is the **surprisal** of one outcome; entropy is its expectation.

**Conditional entropy** — uncertainty left in `Y` after observing `X`:

```
H(Y | X) = H(X, Y) − H(X)            and always   H(Y | X) ≤ H(Y)
```

**Mutual information** — information shared by `X` and `Y` (symmetric,
non-negative, zero ⇔ independent):

```
I(X; Y) = H(Y) − H(Y | X) = H(X) + H(Y) − H(X, Y)
```

**KL divergence** — extra bits to encode `p` using a code built for `q`
(non-negative, **asymmetric**, zero ⇔ `p = q`):

```
D_KL(p ‖ q) = Σ_x p(x) log₂( p(x) / q(x) )
```

Useful identities: `I(X;Y) = D_KL( p(x,y) ‖ p(x)p(y) )` and cross-entropy
`H(p,q) = H(p) + D_KL(p ‖ q)`.

## The one thing to internalize before SL2

**Information gain is mutual information.** ID3's decision-tree splitting
criterion —

```
Gain(S, A) = H(S) − Σ_v (|S_v|/|S|) · H(S_v) = H(S) − H(S | A)
```

— is literally `I(label; attribute)`. SL2 is the first appearance of this
machinery; OL3 is the formal version. If you understand entropy and mutual
information here, SL2's "why split on the highest-gain attribute" is obvious.

## Where each quantity resurfaces

| Quantity | Appears in |
|---|---|
| Entropy / information gain | SL2 decision-tree splits; UL2 filter feature selection |
| Mutual information | OL1 MIMIC's dependency tree; UL2 filters; UL3 ICA |
| KL divergence | OL4 (MLE = minimize KL to data); UL4 t-SNE objective |
| Cross-entropy | OL4 classification loss; standard NN loss (SL3) |
| Max-entropy = uniform | OL3 maximum-entropy principle; OL4 uninformative prior |

## Worked sanity checks

- Fair coin: `H = −(½log½ + ½log½) = 1` bit.
- Biased coin `p = 0.9`: `H ≈ 0.47` bits — more predictable, less information.
- Certain event: `H = 0`.
- `n` equally likely outcomes: `H = log₂ n` (e.g. fair 8-sided die → 3 bits).

If you can reproduce these four in your head, the SL2 entropy/gain computations
will not slow you down.

---

## Review Questions

**Conceptual checks**

1. In one sentence each: what do entropy, conditional entropy, mutual
   information, and KL divergence measure?
2. Which distribution maximizes entropy for a fixed number of outcomes, and why
   is that intuitive?
3. KL divergence is *not* symmetric and *not* a distance metric. Why does the
   asymmetry matter when `q` is a model and `p` is the data?

**Derivation / math**

4. Compute `H(X)` for a biased coin with `p = 0.25`. Compare to a fair coin and
   explain the difference.
5. Show that ID3's information gain `H(S) − H(S|A)` is exactly the mutual
   information `I(label; attribute)`.
6. Using an identity from this sheet, show that minimizing cross-entropy is the
   same as minimizing KL divergence to the data distribution.

**Analysis — "why does it matter"**

7. A feature has zero *individual* mutual information with the label, yet a pair
   of features jointly predicts it perfectly (the XOR case). Explain why an
   individual-scoring filter (UL2) misses this.
8. Why does ICA (UL3) phrase its objective as "minimize mutual information among
   components" — what would zero mutual information mean about those components?

**Exam-style**

9. Trace entropy, mutual information, and KL divergence across the course: name
   one place each appears in SL, OL, and UL.
10. Fill in from memory: the formulas for `H(X)`, `I(X;Y)` (any one form), and
    `D_KL(p‖q)`.
11. (Pointer) The No Free Lunch theorem is part of the OL3 lecture, not this
    refresher. State it in one sentence and say which file develops it fully.
