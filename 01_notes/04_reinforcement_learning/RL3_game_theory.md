# RL3 — Game Theory

**Paired reading:** Andrew Moore's slides · **Unit:** Reinforcement Learning

## Why game theory enters an ML course

RL1–RL2 had **one agent** in a fixed environment. Game theory is what happens
when there are **multiple agents**, each optimizing its own reward, and the
environment for any one agent *includes the others*. The "environment" is now
strategic — it reacts to you. This is the natural generalization of single-agent
RL and the setup for multi-agent learning in RL4.

## The basic vocabulary

- **Players** — the decision-makers.
- **Strategies** — what each player can do. A **pure strategy** is a definite
  choice; a **mixed strategy** is a probability distribution over pure
  strategies.
- **Payoff matrix** — the reward to each player for every combination of
  strategies.
- **Zero-sum game** — one player's gain is exactly the other's loss (payoffs sum
  to a constant). Strictly competitive.
- **Non-zero-sum game** — payoffs need not trade off; cooperation can make
  *both* players better off (or both worse off).

## Solving zero-sum games: minimax

In a **two-player, zero-sum, deterministic, perfect-information** game, each
player assumes the opponent plays optimally against them. The **minimax**
strategy: maximize your payoff under the assumption the opponent minimizes it.

**Von Neumann's minimax theorem:** in any two-player zero-sum game, there is a
well-defined **value of the game**, and `max-min = min-max` — it doesn't matter
who "moves first" in the analysis. The catch: this clean result requires
**mixed strategies** for games without a pure-strategy solution (e.g.
rock-paper-scissors has no pure equilibrium, but "1/3 each" is the minimax
solution).

## Nash equilibrium — the general solution concept

Minimax is specific to zero-sum. The general concept, covering non-zero-sum
games too:

> A **Nash equilibrium** is a strategy profile in which **no player can improve
> their payoff by unilaterally changing strategy** — given what everyone else is
> doing, every player is already playing a best response.

Key facts to know cold:

- **Existence (Nash's theorem):** *every* finite game has at least one Nash
  equilibrium, **possibly in mixed strategies.** This is the famous result.
- **Not necessarily unique** — a game can have many equilibria.
- **Not necessarily optimal** — a Nash equilibrium can be bad for everyone. It is
  *stable*, not *efficient*. This is the crucial distinction and the point of the
  Prisoner's Dilemma.

## The Prisoner's Dilemma

Two players each choose **cooperate** or **defect**. The payoffs are set so that
**defect dominates** — whatever the other player does, you personally do better
by defecting. So the unique Nash equilibrium is **(defect, defect)** — yet
**(cooperate, cooperate)** would have been better for *both*.

The lesson: **individually rational behavior can produce a collectively
irrational outcome.** The Nash equilibrium is stable (neither player will
unilaterally deviate) but Pareto-inefficient (both could be better off). "Defect"
here is a **dominant strategy** — best regardless of the opponent — which is why
the equilibrium is so robust and so bad.

## Pareto optimality vs. Nash equilibrium

- **Nash equilibrium** — *stability*. No one wants to deviate alone.
- **Pareto optimal** — *efficiency*. No outcome makes someone better off without
  making someone else worse off.

The Prisoner's Dilemma shows these are different: (defect, defect) is the Nash
equilibrium but is *not* Pareto optimal; (cooperate, cooperate) is Pareto optimal
but is *not* a Nash equilibrium. Conflating the two is a classic exam mistake.

## Connecting to RL

A game can be modeled as a **stochastic game / Markov game** — an MDP with
multiple agents, where transitions and rewards depend on the *joint* action.
Single-agent RL is the one-player special case. The complication RL4 has to face:
when every agent is *simultaneously learning*, each agent's environment is
**non-stationary** — it's changing underneath them as the others adapt — which
breaks the stationarity assumption that made Q-learning's convergence guarantee
work.

---

## Review Questions

**Conceptual checks**

1. Why does game theory belong in a reinforcement learning unit? What does it
   generalize about the RL1/RL2 setting?
2. Distinguish pure and mixed strategies. Give a game that has no pure-strategy
   solution but does have a mixed one.
3. Distinguish zero-sum and non-zero-sum games. Which solution concept is
   specific to zero-sum, and which is general?

**Derivation / analysis**

4. State von Neumann's minimax theorem. What does "the value of the game" mean,
   and why is mixed-strategy reasoning sometimes required to achieve it?
5. Define Nash equilibrium precisely (the "no profitable unilateral deviation"
   form). State Nash's existence theorem and the important qualifier in it.
6. In the Prisoner's Dilemma, show that "defect" is a dominant strategy by
   checking both of the opponent's possible choices.

**Analysis — "why does it behave this way"**

7. Explain how the Prisoner's Dilemma demonstrates that individually rational
   choices can yield a collectively irrational outcome. Which equilibrium
   property causes this, and which property is violated?
8. A Nash equilibrium can be bad for every player. Reconcile this with the claim
   that players are behaving "rationally."
9. Why does a Nash equilibrium being *stable* not imply it is *efficient*? Use
   Nash vs. Pareto vocabulary.

**Exam-style**

10. Contrast Nash equilibrium and Pareto optimality. For the Prisoner's Dilemma,
    state which outcome satisfies which, and which satisfies neither/both.
11. Explain how a multi-agent game can be cast as a Markov (stochastic) game and
    how single-agent RL is a special case.
12. When multiple agents learn at the same time, each agent's environment becomes
    non-stationary. Explain why, and which RL2 convergence assumption this
    breaks.
