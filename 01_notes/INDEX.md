# CS 7641 — Course Notes

Concept and lecture notes for Georgia Tech OMSCS **CS 7641: Machine Learning**,
organized by the four course units. Each unit folder holds one file per lecture
topic. Every topic ends with a **Review Questions** block — a mix of conceptual
checks, derivation prompts, "why does this algorithm behave this way" analysis
questions, and exam-style questions — so each note doubles as a self-quiz.

These notes are paired with the readings in `../02_readings/` and follow the
week-by-week structure in `../../CS7641_Summer2026_Study_Plan.md`.

Before the units, there is also a **`math_foundations/`** folder — the Week-0
refreshers for the course's assumed math (the study plan's flagged weak area).

## How to use these notes

Read the lecture and the paired reading first, then use the matching note to
consolidate. Do not just re-read the answers — cover the Review Questions and
answer them cold. If a question stalls you, that is a gap; log it (math gaps go
in `math_foundations/`, per the study plan) and close it the same week.

## Math Foundations (`math_foundations/`)

Week-0 refreshers for the assumed math — read these first.

| Topic | File | Feeds into |
|-------|------|------------|
| Linear Algebra & Eigenproblems | `01_linear_algebra.md` | UL3 (PCA/ICA), SL6 (SVMs) |
| Probability & Statistics | `02_probability_statistics.md` | OL4–OL5, UL1, every report |
| Information Theory (quick reference) | `03_information_theory.md` | SL2, OL3, UL2/UL3 |
| Calculus & Optimization | `04_calculus_optimization.md` | SL3, OL1–OL2, SL6 |
| Math Gaps Log (running) | `math_gaps_log.md` | — |

## Unit 1 — Supervised Learning (`01_supervised_learning/`)

| Topic | File | Paired reading |
|-------|------|----------------|
| SL1 — ML Overview & Problem Setup | `SL1_ml_overview.md` | Mitchell Ch 1 |
| SL2 — Decision Trees | `SL2_decision_trees.md` | Mitchell Ch 3 |
| SL3 — Neural Networks | `SL3_neural_networks.md` | Mitchell Ch 4 |
| SL4 — Instance-Based Learning | `SL4_instance_based_learning.md` | Mitchell Ch 8 |
| SL5 — Ensemble Learning & Boosting | `SL5_ensembles_boosting.md` | `adaboost_matas.pdf` |
| SL6 — Kernel Methods & SVMs | `SL6_kernels_svms.md` | `yor12-introsvm.pdf`, `svmtutorial.pdf` |
| SL7 — Computational Learning Theory | `SL7_computational_learning_theory.md` | Mitchell Ch 7 |
| SL8 — VC Dimension | `SL8_vc_dimension.md` | VC reading (Canvas) |

## Unit 2 — Optimization & Uncertainty in Learning (`02_optimization_uncertainty/`)

| Topic | File | Paired reading |
|-------|------|----------------|
| OL1 — Randomized Optimization | `OL1_randomized_optimization.md` | Mitchell Ch 9 |
| OL2 — Deconstructing AdamW (Modern Optimizers) | `OL2_modern_optimizers_adamw.md` | AdamW readings (Canvas) |
| OL3 — Information Theory | `OL3_information_theory.md` | `InfoTheory.fm.pdf`, `gentle_intro_to_information_theory.pdf`, `nfl-optimization-explanation.pdf` |
| OL4 — Bayesian Learning | `OL4_bayesian_learning.md` | Mitchell Ch 6 |
| OL5 — Bayesian Inference | `OL5_bayesian_inference.md` | Mitchell Ch 6 |

## Unit 3 — Unsupervised Learning (`03_unsupervised_learning/`)

| Topic | File | Paired reading |
|-------|------|----------------|
| UL1 — Clustering | `UL1_clustering.md` | `em-intuitive-explanation.pdf`, `em.pdf`, `nips15.pdf` |
| UL2 — Feature Selection | `UL2_feature_selection.md` | Mitchell Ch 7 |
| UL3 — Feature Transformation | `UL3_feature_transformation.md` | `ica-algorithms-and-applications.pdf`, `isbell-ica-nips-1999.pdf` |
| UL4 — Manifold Learning | `UL4_manifold_learning.md` | Bishop Ch 12, t-SNE paper |

## Unit 4 — Reinforcement Learning (`04_reinforcement_learning/`)

| Topic | File | Paired reading |
|-------|------|----------------|
| RL1 — Markov Decision Processes | `RL1_markov_decision_processes.md` | Mitchell Ch 13 |
| RL2 — Reinforcement Learning | `RL2_reinforcement_learning.md` | Sutton & Barto chs. 2/4/6, `kaelbling96reinforcement.pdf` |
| RL3 — Game Theory | `RL3_game_theory.md` | A. Moore slides |
| RL4 — Game Theory, Continued | `RL4_game_theory_continued.md` | Curated readings (Canvas) |
| RL5 — Horizon of Variants | `RL5_horizon_of_variants.md` | Curated readings (Canvas) |

## The theory spine (shows up on the cumulative final)

The study plan flags these as the backbone of the final exam — they recur across
units, so the notes cross-reference each other:

- **Information theory** — entropy/IG in SL2, the formal treatment in OL3, ICA in UL3.
- **Bias–variance & generalization** — SL1 framing, SL7/SL8 formalization, ensembles in SL5.
- **Optimization** — gradient-based in SL3/OL2, gradient-free in OL1, the Bellman fixed point in RL1.
- **Bayesian reasoning** — OL4/OL5, EM in UL1, MAP vs MLE everywhere.
- **No Free Lunch** — OL3, and the conceptual reason cross-validation and inductive bias matter at all.
