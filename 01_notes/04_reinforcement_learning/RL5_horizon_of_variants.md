# RL5 — Horizon of Variants

**Paired reading:** curated readings (posted on Canvas during the term) · **Unit:** Reinforcement Learning

> The closing lecture of the course. RL1–RL4 built the core: MDPs, model-free
> learning, game theory. RL5 surveys the **frontier** — the assumptions the core
> made, and what happens when you relax each one. Treat this as a map of where
> the field goes, and as the place the final exam tests whether you understand
> the *limits* of what you learned.

## The core assumptions, and relaxing them

Everything in RL1–RL2 rested on a stack of simplifying assumptions. Each variant
below is "what if this one isn't true?"

**Assumption: the state is fully observable.**
Relax it → a **Partially Observable MDP (POMDP)**. The agent sees only noisy or
incomplete *observations*, not the true state. The fix is to act on a **belief
state** — a probability distribution over what the true state might be — which is
itself a (continuous) MDP. POMDPs are vastly harder to solve; this is the single
most important variant to know.

**Assumption: the reward function is given.**
Relax it → **Inverse Reinforcement Learning** — observe an expert's behavior and
*infer the reward function* they must be optimizing, then optimize it yourself.
Useful when "good behavior" is easy to demonstrate but hard to specify (the
reward-design problem). Related: **reward shaping** — adding intermediate rewards
to make a sparse-reward problem learnable, without changing the optimal policy.

**Assumption: the state space is small enough to enumerate.**
Relax it → **function approximation** (introduced in RL2) and **Deep RL** —
represent the value function or policy with a neural network so it generalizes
across states. This is what made RL work on games and robotics, but it forfeits
the tabular convergence guarantees (the "deadly triad" of bootstrapping +
off-policy + function approximation can diverge).

**Assumption: learn the value function, then act greedily.**
Relax it → **policy-gradient / actor-critic** methods, which optimize the policy
*directly* by gradient ascent on expected return, instead of going through a
value function. Better suited to continuous action spaces and stochastic optimal
policies; the "actor" picks actions, the "critic" estimates value to reduce the
gradient's variance.

**Assumption: every problem is learned from scratch.**
Relax it → **hierarchical RL** (learn reusable sub-policies / options for
temporally extended actions), **transfer learning** (reuse knowledge across
related tasks), and **multi-task / meta-RL** (learn to learn). All attack RL's
notorious **sample inefficiency**.

## The themes that recur across every variant

RL5 is easier to hold onto if you track the *recurring tensions* rather than
memorizing a list:

- **Exploration vs. exploitation** — RL2's dilemma never goes away; it gets
  *harder* in large/partially-observed spaces, where naive ε-greedy is hopeless
  and you need directed/curiosity-driven exploration.
- **Sample efficiency** — real RL needs an enormous amount of experience. Almost
  every variant (model-based, hierarchical, transfer, reward shaping) is, in
  part, an attack on this.
- **The generalization vs. guarantees tradeoff** — tabular methods have clean
  convergence proofs but can't scale; function approximation scales but loses the
  guarantees. This is the RL echo of the bias–variance / capacity story from the
  SL unit.
- **Credit assignment** — harder with long horizons, partial observability, and
  sparse rewards. Eligibility traces, reward shaping, and hierarchy are all
  partial answers.
- **Specification** — *getting the reward function right* is itself a hard,
  error-prone problem (reward hacking, unintended optima); IRL and reward shaping
  exist because of it.

## Connecting back to the whole course

RL5 is a natural place for the final-exam concept map to converge:

- **No Free Lunch (OL3)** — no single RL algorithm dominates; each variant
  encodes a bias matched to a class of problems.
- **Bias–variance / capacity (SL unit)** — reappears as tabular-vs-approximation,
  and as the bias/variance of Monte Carlo vs. TD targets.
- **Optimization (OL1–OL2)** — policy-gradient methods *are* gradient ascent;
  RL's non-convex, noisy landscapes are exactly the OL terrain.
- **Bayesian reasoning (OL4–OL5)** — POMDP belief states are posterior
  distributions updated by Bayes' rule; model-based RL learns a model the way
  OL5 learns distributions.

## Where it sits

This lecture is deliberately a **survey** — breadth, not depth. For the final,
you don't need to *solve* a POMDP; you need to know **which assumption each
variant relaxes, why that makes the problem harder, and what general strategy
addresses it.** That mapping — assumption → relaxation → consequence → approach —
is the whole point of RL5.

---

## Review Questions

**Conceptual checks**

1. RL5 is organized around "relaxing assumptions." List four assumptions the
   RL1–RL2 core made, and name the variant that drops each one.
2. What is a belief state, and why does acting on it turn a POMDP back into
   (a much harder) MDP?
3. What problem does Inverse Reinforcement Learning solve, and when would you
   reach for it instead of just writing down a reward function?

**Analysis — "why does it behave this way"**

4. Why does function approximation forfeit the convergence guarantees that
   tabular Q-learning enjoys? Name the "deadly triad."
5. Policy-gradient methods optimize the policy directly instead of going through
   a value function. Give two situations where that is the better choice and
   explain why.
6. Why is exploration *harder* in large or partially observable state spaces than
   in a small tabular MDP? Why does naive ε-greedy break down?

**Synthesis — across the course**

7. Explain how the "generalization vs. guarantees" tradeoff in RL is the same
   underlying tension as the bias–variance tradeoff from the supervised-learning
   unit.
8. Connect POMDP belief states to OL4/OL5: in what precise sense is maintaining a
   belief state an application of Bayesian inference?
9. Use the No Free Lunch theorem to explain why RL5 is a *catalog of variants*
   rather than a search for the one best RL algorithm.

**Exam-style**

10. For POMDPs, IRL, and Deep RL: state the assumption each relaxes, why that
    makes the problem harder, and the general strategy used to cope.
11. Name three distinct techniques that attack RL's sample-inefficiency problem
    and explain the mechanism of each.
12. Sketch how RL5's themes would sit on a course-wide concept map — name one
    explicit link from RL back to each of the SL, OL, and UL units.
