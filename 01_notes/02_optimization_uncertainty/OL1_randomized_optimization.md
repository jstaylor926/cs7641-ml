# OL1 — Randomized Optimization

**Paired reading:** Mitchell Ch 9 · **Unit:** Optimization & Uncertainty

## The problem setting

Given a **fitness function** `f(x)` over some input space, find the `x` that
maximizes (or minimizes) it. The catch: you have **no gradient** — `f` may be
discontinuous, non-differentiable, or a black box you can only *query*. This is
exactly the situation backprop can't touch, and it's pervasive: hyperparameter
tuning, combinatorial problems, training neural-net weights when the loss
landscape is hostile.

Randomized optimization algorithms only **sample and evaluate**. They differ in
how they use past evaluations to decide where to sample next. The OL report
compares four of them, so know each one's mechanism, its single key knob, and
its failure mode.

## Randomized Hill Climbing (RHC)

From the current point, sample a neighbor; move if it's better, else stay.
**Random restarts** run this from many random starting points and keep the best
result.

- **Mechanism:** pure greedy local search.
- **Strength:** dead simple, cheap per step, fast on smooth/unimodal landscapes.
- **Failure mode:** gets trapped in **local optima** and plateaus — it can never
  go downhill. Random restarts are the only escape, and they only help if good
  basins are reasonably probable.
- **Knob:** number of restarts.

## Simulated Annealing (SA)

Hill climbing that *sometimes accepts worse moves*, with the willingness to do so
shrinking over time. Accept a worse neighbor with probability
`P = exp(−ΔE / T)` (the **Metropolis criterion**), where `ΔE` is the fitness
drop and `T` is the **temperature**.

- **High T:** almost any move is accepted → behaves like a random walk →
  **explores**.
- **Low T:** only improving moves accepted → behaves like hill climbing →
  **exploits**.
- The **cooling/annealing schedule** lowers `T` gradually, shifting from
  exploration to exploitation. Cool too fast and you freeze in a local optimum;
  cool too slow and you waste evaluations.
- **Theory:** with a sufficiently slow (logarithmic) schedule, SA converges to
  the global optimum in the limit — a guarantee RHC cannot make.
- **Knob:** the cooling schedule (initial T, decay rate).
- This is the cleanest illustration of the **exploration vs. exploitation**
  tradeoff in the course — it recurs in RL.

## Genetic Algorithms (GA)

Maintain a **population** of candidate solutions and evolve it:

- **Selection:** pick parents biased toward high fitness (roulette, tournament).
- **Crossover:** combine two parents into offspring — recombining "good pieces"
  of solutions. This is the operator that distinguishes GAs.
- **Mutation:** randomly perturb offspring to maintain diversity and reach new
  regions.
- Repeat for many generations.

- **Strength:** population-based, so it explores many basins at once; crossover
  exploits *structure* — when the problem decomposes into sub-parts, recombining
  good sub-solutions is powerful.
- **Failure mode:** **premature convergence** (the population collapses to one
  mediocre solution and diversity is lost); crossover is wasted or harmful when
  the representation has no exploitable building-block structure.
- **Knobs:** population size, mutation rate, crossover scheme, selection
  pressure.

## MIMIC

The others throw away everything they learn about the *structure* of the search
space between iterations. **MIMIC** keeps it: it builds a **probabilistic model**
of "what good solutions look like."

- Each iteration: sample from the current model, keep the top fraction (those
  above a fitness threshold), **re-estimate the probability distribution** from
  those survivors, raise the threshold, repeat.
- It models **dependencies between variables** (via a dependency tree / chain
  that maximizes mutual information), so it captures *structure*, not just
  marginal statistics.
- **Strength:** far more **sample-efficient** when evaluating `f` is expensive —
  it conveys information *across* iterations instead of rediscovering it. It also
  *reveals* structure as a by-product.
- **Cost:** each iteration is computationally much heavier (model-building);
  worth it only when `f`-evaluations dominate the cost.
- **Knobs:** population size, the keep-threshold percentile.

## How to compare them (the OL report's actual question)

| Algorithm | Uses a population? | Models structure? | Key knob | Main weakness |
|---|---|---|---|---|
| RHC | No | No | # restarts | Local optima |
| SA | No | No | Cooling schedule | Schedule tuning; slow if cooled slowly |
| GA | Yes | Implicitly (via crossover) | Pop size, mutation rate | Premature convergence |
| MIMIC | Yes (samples) | Yes (explicitly) | Pop size, threshold | Expensive per iteration |

The report wants you to argue *which problem favors which algorithm and why*: a
problem with strong inter-variable structure favors MIMIC and (if there are
building blocks) GA; a smooth landscape favors RHC/SA; a problem where
`f`-evaluations are cheap favors RHC/SA on wall-clock even if MIMIC needs fewer
iterations. Always report **variance across seeded runs**, not single runs —
these are stochastic algorithms.

This is also where No Free Lunch (OL3) bites: no one of these dominates across
all problems — the report is an exercise in *matching algorithm to landscape*.

## RO for training neural-net weights

The second half of the OL report: replace backprop with RHC/SA/GA to optimize a
neural net's weights. Backprop is a gradient method that can stall in local
minima or on bad curvature; RO is gradient-free. Expect RO to be **slower** and
often **less accurate** than backprop on a well-behaved net — the comparison is
the point. It demonstrates *when* gradient information is worth having and *when*
a gradient-free method is the only option.

---

## Review Questions

**Conceptual checks**

1. What defines a "randomized optimization" problem, and why can't backprop be
   used on it? Give two real examples.
2. Define exploration and exploitation. Explain precisely how temperature `T`
   controls the balance in simulated annealing.
3. Which of the four algorithms keeps information *about the structure of the
   search space* between iterations, and how?

**Derivation / math**

4. Write the Metropolis acceptance probability. Evaluate its behavior as
   `T → ∞`, `T → 0`, and for `ΔE = 0`. What does each limit mean operationally?
5. RHC with random restarts: if a good basin is hit with probability `p` per
   restart, how many restarts give you ≥ 95% chance of hitting it at least once?
6. In MIMIC, what quantity does the dependency tree maximize, and why does
   capturing variable dependencies make it more sample-efficient than GA?

**Analysis — "why does it behave this way"**

7. Cooling too fast vs. too slow in SA — describe the failure in each case.
8. Premature convergence in a GA: what is it, what causes it, and which knob(s)
   counteract it?
9. MIMIC needs the fewest *iterations* but is often beaten on *wall-clock time*.
   Explain the tradeoff and state the condition under which MIMIC is genuinely
   the right choice.

**Exam-style**

10. Fill in the comparison table from memory: for RHC, SA, GA, MIMIC give
    population (Y/N), models structure (Y/N), key knob, main weakness.
11. You replace backprop with a GA to train a neural net's weights. Predict the
    relative speed and accuracy versus backprop and explain why — what does
    backprop have that the GA doesn't?
12. Connect this lecture to the No Free Lunch theorem: why does the OL report
    not have a single "winner," and what *is* the report actually demonstrating?
