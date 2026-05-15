# OL3 — Information Theory

**Paired reading:** `InfoTheory.fm.pdf` (Isbell), `gentle_intro_to_information_theory.pdf`, `nfl-optimization-explanation.pdf` · **Unit:** Optimization & Uncertainty

> The most math-dense lecture in the unit. You already met entropy informally in
> SL2 (decision-tree splitting); this is the formal treatment, and it reappears
> in UL3 (ICA) and on the final. Read the three PDFs twice, as the study plan
> says.

## Entropy — uncertainty measured in bits

The **entropy** of a discrete random variable `X` is the expected number of bits
needed to encode an outcome drawn from it:

```
H(X) = − Σ_x p(x) log₂ p(x)
```

Read it as a measure of **uncertainty / surprise / information content**:

- A fair coin: `H = 1` bit (maximum for 2 outcomes).
- A biased coin `p = 0.9`: `H ≈ 0.47` bits — more predictable, less information.
- A certain outcome (`p = 1`): `H = 0` — no surprise, no information.
- For `n` equally likely outcomes, `H = log₂ n` — entropy is **maximized by the
  uniform distribution**. This is a key fact and the basis of the maximum-entropy
  principle.

The `−log₂ p(x)` term is the **surprisal** of a single outcome: rare events carry
more information. Entropy is the *expected* surprisal. This is also exactly the
optimal code length — Shannon's source coding theorem says you cannot compress
below `H(X)` bits per symbol on average.

## Joint, conditional entropy, and information gain

- **Joint entropy** `H(X, Y)` — uncertainty in the pair.
- **Conditional entropy** `H(Y | X) = H(X, Y) − H(X)` — the uncertainty
  *remaining* in `Y` once you know `X`. It is `≤ H(Y)`: knowing something can
  never *increase* your uncertainty on average.
- **Information gain** `IG(Y, X) = H(Y) − H(Y | X)` — how much knowing `X`
  reduces uncertainty about `Y`. This is *exactly* the decision-tree splitting
  criterion from SL2; SL2 was a special case of this lecture.

## Mutual information

```
I(X; Y) = H(X) − H(X | Y) = H(Y) − H(Y | X) = H(X) + H(Y) − H(X, Y)
```

**Mutual information** is the amount of information `X` and `Y` share — the
reduction in uncertainty about one from knowing the other. It is **symmetric**,
**non-negative**, and **zero if and only if `X` and `Y` are independent**. Unlike
correlation, MI captures *any* statistical dependence, linear or not. This is the
core quantity behind ICA (UL3) and MIMIC's dependency tree (OL1).

## KL divergence

The **Kullback–Leibler divergence** measures how different one distribution `p`
is from another `q`:

```
D_KL(p ‖ q) = Σ_x p(x) log₂( p(x) / q(x) )
```

Interpretation: the *extra* bits per symbol you pay for encoding data that is
really distributed as `p` using a code optimized for `q`. Properties:

- `D_KL(p ‖ q) ≥ 0`, with equality **iff `p = q`** (Gibbs' inequality).
- It is **not symmetric**: `D_KL(p ‖ q) ≠ D_KL(q ‖ p)` — it is *not* a distance
  metric. Knowing which argument is "truth" and which is "model" matters.
- Mutual information is a KL divergence: `I(X; Y) = D_KL( p(x,y) ‖ p(x)p(y) )` —
  the divergence between the true joint and the independence assumption.

KL divergence is the bridge to OL4: maximum-likelihood estimation is equivalent
to minimizing the KL divergence between the data distribution and the model.

## Cross-entropy

`H(p, q) = H(p) + D_KL(p ‖ q)` — the average bits to encode `p` using `q`'s code.
Minimizing cross-entropy (the standard classification loss) over a fixed dataset
is exactly minimizing KL divergence to the data, which is exactly maximum
likelihood. Three things you may have thought were separate are the same thing.

## The No Free Lunch theorem

The conceptual climax of the lecture (`nfl-optimization-explanation.pdf`):

> **Averaged over *all possible problems* (all possible objective functions), no
> optimization or learning algorithm outperforms any other** — including random
> search.

Why it's true, intuitively: an algorithm performs well on problems whose
structure matches its assumptions, and *necessarily* pays for it on problems
where those assumptions are wrong. Superior performance on one class of problems
is borrowed from inferior performance on another. There is no universal learner.

What it does **not** say: it does *not* say all algorithms are equal on the
problems *we actually care about*. Real-world problems are a tiny, highly
structured subset of "all possible functions." NFL says performance comes
**entirely from inductive bias matching problem structure** — so the job is
choosing the right bias, not finding a magic algorithm. This is the formal
justification for everything in SL1 about inductive bias, for cross-validation,
and for why the OL report has no single winning optimizer.

## Why this lecture is load-bearing

Information theory is the connective tissue of the course: it *defined* SL2's
splitting rule, it *is* the OL4 likelihood story (via KL), it underlies UL3's
ICA (maximize non-Gaussianity / minimize mutual information) and UL2's
feature-selection filters, and NFL is the theoretical reason inductive bias is
the whole game. Expect it heavily on the final.

---

## Review Questions

**Conceptual checks**

1. Define entropy in words ("expected ...") and state which distribution
   maximizes it for a fixed number of outcomes. Why does that maximum make
   intuitive sense?
2. What is surprisal, and how does entropy relate to it?
3. State three properties of mutual information. How is it strictly more general
   than correlation as a dependence measure?

**Derivation / math**

4. Compute `H(X)` for a biased coin with `p = 0.25`. Then for a 4-sided fair die.
   Which is larger and why?
5. Show that `I(X; Y) = H(Y) − H(Y|X) = H(X) + H(Y) − H(X,Y)` are equivalent
   from the definitions.
6. Write `D_KL(p ‖ q)`. Prove (or argue) it is non-negative, and give a concrete
   2-outcome example where `D_KL(p ‖ q) ≠ D_KL(q ‖ p)`.

**Analysis — "why does it behave this way"**

7. Explain precisely how SL2's information-gain splitting criterion is a special
   case of this lecture's machinery. Map each piece.
8. Show that minimizing cross-entropy loss equals minimizing KL divergence to
   the data equals maximum likelihood. Why is it useful to see these as one
   thing?
9. KL divergence is not symmetric. Give a practical reason why the asymmetry
   matters when `q` is a model fit to data `p`.

**Exam-style**

10. State the No Free Lunch theorem precisely. State one thing it *does* imply
    about algorithm choice and one common misreading it does *not* imply.
11. Use NFL to explain why the OL randomized-optimization report cannot have a
    single "best" algorithm, and what the report is therefore really assessing.
12. Trace information theory through the whole course: name where entropy, mutual
    information, and KL divergence each resurface in SL, UL, and OL4.
