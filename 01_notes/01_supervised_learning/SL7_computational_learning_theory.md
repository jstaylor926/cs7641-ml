# SL7 — Computational Learning Theory

**Paired reading:** Mitchell Ch 7 · **Unit:** Supervised Learning

## The question

Earlier lectures gave *algorithms*. This one asks the *theory* questions:

- **How many examples** does a learner need to learn well?
- **How much computation** does it take?
- Can we *guarantee*, not just hope, that low training error implies low true
  error?

Computational learning theory answers these with probabilistic bounds. It is the
formal core of the unit and a guaranteed presence on the final.

## PAC learning

A concept class is **PAC-learnable** ("Probably Approximately Correct") if there
is a learner that, for any target concept in the class and any distribution over
inputs, with probability at least `1 − δ` outputs a hypothesis with true error at
most `ε`, using a number of examples and amount of computation polynomial in
`1/ε`, `1/δ`, and the problem size.

Unpack the two slack parameters — they are the heart of PAC:

- **ε (epsilon) — "approximately":** we don't demand a perfect hypothesis, just
  one with error ≤ ε.
- **δ (delta) — "probably":** we don't demand success every time, just with
  probability ≥ 1 − δ. The training sample could be unrepresentative by bad luck;
  δ is the budget for that bad luck.

Both are necessary. With finite data you can never guarantee zero error with
certainty — so you relax *both* the accuracy and the confidence.

## The sample-complexity bound (finite hypothesis space)

For a **finite** hypothesis space `H`, if the learner returns any hypothesis
**consistent** with the training data, the number of examples needed is:

```
m ≥ (1/ε) · ( ln|H| + ln(1/δ) )
```

Read every term:

- **`ln|H|`** — sample complexity grows with the (log of the) size of the
  hypothesis space. A richer H needs more data to pin down. This is *Occam's
  razor made quantitative*: smaller H ⇒ fewer examples needed ⇒ better
  generalization guarantee.
- **`1/ε`** — wanting lower error costs (linearly) more data.
- **`ln(1/δ)`** — wanting higher confidence costs more data, but only
  logarithmically — confidence is cheap.

The derivation is worth knowing: a single "bad" hypothesis (true error > ε) is
consistent with `m` independent examples with probability at most `(1−ε)^m`.
Union-bound over all `|H|` hypotheses, set `|H|(1−ε)^m ≤ δ`, use
`(1−ε) ≤ e^{−ε}`, and solve for `m`. Be able to reproduce this — it's a classic
exam derivation.

## Agnostic learning

The bound above assumes a consistent hypothesis *exists* (the target is in H).
**Agnostic learning** drops that assumption: the learner just returns the
hypothesis with lowest *training* error, which may still be nonzero. The bound
then uses a Hoeffding-style argument and becomes:

```
m ≥ (1/(2ε²)) · ( ln|H| + ln(1/δ) )
```

Note the `1/ε²` instead of `1/ε` — agnostic learning needs **more** data,
because it must estimate each hypothesis's error rather than rely on
consistency. This realistic-but-costlier setting is the bridge to VC dimension
in SL8.

## What the theory buys you

These bounds turn vague intuitions into statements:

- **"Simpler models generalize better"** becomes "smaller `ln|H|` ⇒ smaller
  required `m` for the same (ε, δ)." That is the formal content of Occam's razor
  and the inductive-bias discussion from SL1.
- **The bias–variance tradeoff** gets a theoretical home: a large H can fit
  anything (low bias) but needs enormous data to *guarantee* generalization (the
  manifestation of high variance).
- It connects directly to **SVMs** (SL6): the large-margin argument is a way of
  controlling effective capacity — and it's the limitation of the `|H|` bound
  (it's useless for infinite H) that forces the move to VC dimension.

## The catch

The `ln|H|` bound is **vacuous for infinite hypothesis spaces** — linear
separators, neural nets, SVMs all have `|H| = ∞`. It is also typically **loose**:
the bounds are correct but pessimistic, often demanding far more data than works
in practice. The point of the theory is the *shape* of the dependence (what
matters and how), not a tight engineering number. SL8 (VC dimension) is the fix
for the infinite-H problem.

---

## Review Questions

**Conceptual checks**

1. In "Probably Approximately Correct," which parameter is "probably" and which
   is "approximately"? Why can neither be dropped when learning from finite data?
2. What does it mean for a hypothesis to be *consistent* with the training data,
   and why does the basic PAC bound assume the learner returns a consistent one?
3. Define agnostic learning. What assumption does it remove, and why is that more
   realistic?

**Derivation / math**

4. Reproduce the derivation of `m ≥ (1/ε)(ln|H| + ln(1/δ))`: the probability a
   bad hypothesis survives `m` examples, the union bound, and the final solve.
   Where is `(1−ε) ≤ e^{−ε}` used?
5. The agnostic bound has `1/ε²` where the consistent bound has `1/ε`. Explain
   *why* agnostic learning requires more data.
6. If you double the hypothesis space size, how does the required sample size
   change? If you halve `δ`? If you halve `ε`? Answer each from the bound.

**Analysis — "why does it behave this way"**

7. Explain how the term `ln|H|` makes Occam's razor a quantitative statement
   rather than a slogan.
8. Map the PAC bound onto the bias–variance tradeoff: which part of the bound
   corresponds to the cost of a large, flexible hypothesis space?
9. Why is the `ln|H|` bound useless for an SVM or a neural network, and what
   does that failure motivate?

**Exam-style**

10. A learner has `|H| = 1000`. You want error ≤ 0.05 with confidence ≥ 0.95.
    Compute the minimum number of consistent training examples.
11. State two reasons the PAC bounds are described as "loose" or "pessimistic,"
    and explain what the theory is actually useful for despite that.
12. Give the precise definition of PAC-learnability, including the polynomial-
    resource requirement, and explain what each resource is polynomial *in*.
