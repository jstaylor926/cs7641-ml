# Math Foundations — Focus Area A

The course assumes linear algebra, probability/statistics, information theory,
and calculus/optimization. The Summer 2026 study plan flags math as a **weak
area** and says to close gaps in **Week 0** and continuously — not when a topic
exposes them.

These notes are the Week-0 refreshers, written so each connects forward to the
exact CS7641 lecture that depends on it. Same format as the unit notes:
comprehensive explanation, then a mixed **Review Questions** block.

| File | Covers | Feeds into |
|------|--------|------------|
| `01_linear_algebra.md` | Vectors, inner products, matrices, eigenvectors/eigenvalues, SVD, PSD | UL3 (PCA/ICA), SL6 (SVMs/kernels) |
| `02_probability_statistics.md` | Distributions, expectation/variance, Bayes' rule, MLE/MAP, confidence intervals, significance | OL4–OL5, UL1 (EM), **every report's analysis** |
| `03_information_theory.md` | Entropy, conditional entropy, mutual information, KL divergence (quick reference) | SL2, OL3 (full lecture), UL2, UL3 |
| `04_calculus_optimization.md` | Gradients, chain rule, gradient descent, convexity, Lagrange multipliers | SL3 (backprop), OL1–OL2, SL6 (SVM dual) |
| `math_gaps_log.md` | Running log of derivations that stalled you — close each within the week | — |

## How to use this folder

1. **Week 0:** read all four refreshers and `Eigenproblems.fm.pdf`; skim
   Wasserman Part 1.
2. **Every week of the term:** when a derivation in a lecture or reading stalls
   you, write the gap into `math_gaps_log.md` immediately and close it the same
   week. Compounding math gaps is the anti-pattern the study plan warns about.
3. Use the Review Questions as cold self-tests, not re-reading.

Note: `03_information_theory.md` is intentionally a compact refresher — the full
treatment (No Free Lunch theorem, the three info-theory PDFs, depth) is the
**OL3** lecture note in `../02_optimization_uncertainty/`.
