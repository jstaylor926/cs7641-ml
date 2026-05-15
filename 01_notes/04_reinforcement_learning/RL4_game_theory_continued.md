# RL4 — Game Theory, Continued

**Paired reading:** curated readings (posted on Canvas during the term) · **Unit:** Reinforcement Learning

> RL3 established the static picture — payoff matrices, Nash equilibria,
> Prisoner's Dilemma. RL4 makes games **repeated** and **learned**: what happens
> when the same game is played over and over, and when the players are *RL
> agents* adapting to each other?

## Repeated games change everything

A one-shot Prisoner's Dilemma has a grim, unavoidable answer: defect. But play
the **same game repeatedly** and the strategic landscape opens up, because
players can **condition this move on past behavior** — they can reward and punish
history.

- **Iterated Prisoner's Dilemma (IPD):** with repetition, **cooperation can
  emerge and be stable**, because a player can retaliate against defection in
  future rounds. The threat of future punishment makes present cooperation
  rational.
- **The role of the horizon:** if the number of rounds is **finite and known**,
  *backward induction* unravels cooperation — the last round is a one-shot game
  (defect), so the second-to-last is too, all the way back. Cooperation needs an
  **infinite or unknown horizon** (or discounting, so "the future" always has
  weight). This unraveling argument is a favorite exam question.
- **Tit-for-Tat:** the famously effective IPD strategy — cooperate first, then
  copy the opponent's last move. It is *nice* (never defects first),
  *retaliatory* (punishes defection immediately), *forgiving* (returns to
  cooperation at once), and *clear* (easy for the opponent to read). Not
  unbeatable, but remarkably robust.

## The Folk Theorem

The formal statement of "repetition enables cooperation":

> In an infinitely repeated game, **essentially any outcome that gives every
> player at least their minimax (security) payoff can be sustained as an
> equilibrium** — provided players are patient enough (discount factor close
> enough to 1).

What it means and how to read it:

- Repetition makes a **huge set** of outcomes equilibria — including the
  cooperative, Pareto-efficient ones that were impossible in the one-shot game.
- It is sustained by **credible threats**: "if you deviate, I punish you down to
  your minimax payoff forever." The threat only works if players care enough
  about the future (high `γ`).
- The double edge: it also means equilibrium is **not predictive** — *so many*
  outcomes are now possible that the concept stops telling you which one will
  happen. Cooperation is *possible*, not *guaranteed*.

## Multi-agent reinforcement learning

Now make the players **learning agents**. RL3 noted the core problem: when
everyone learns simultaneously, each agent's environment is **non-stationary** —
the transition/reward structure it faces shifts as the others adapt. This breaks
the stationarity assumption behind Q-learning's convergence guarantee. Approaches:

- **Independent learners** — each agent just runs its own Q-learning and treats
  the others as part of the environment. Simple, sometimes works, but has *no
  convergence guarantee* — the agents can chase each other forever.
- **Minimax-Q** — for two-player **zero-sum** stochastic games: replace
  Q-learning's `max` with a **minimax** over the opponent's actions. It
  provably converges to the game's value (the zero-sum structure is what makes
  this tractable).
- **Nash-Q** — generalizes to **general-sum** games by computing a Nash
  equilibrium of the stage game at each update. Converges only under restrictive
  conditions — general-sum multi-agent learning is genuinely hard, and there's no
  clean universal guarantee.

The honest summary: single-agent RL has clean convergence theory; multi-agent RL
mostly doesn't, and *why* it doesn't (non-stationarity, equilibrium
multiplicity) is the conceptual content RL4 wants you to carry.

## Mechanism design — the inverse problem

A brief but exam-worthy flip of perspective. Game theory **analyzes** a given
game. **Mechanism design** *constructs* the game: design the rules and payoffs so
that when self-interested agents each play their best response, the **collective
outcome is the one you wanted**. It is "game theory in reverse" — engineering the
incentives. Auctions are the canonical example.

## Where it sits

RL4 closes the game-theory arc and the multi-agent generalization of the unit.
The throughline of RL3→RL4: a single agent (RL1–RL2) → multiple static agents
(RL3) → multiple agents in repeated, learned interaction (RL4), with the optimism
("cooperation is possible," Folk Theorem) tempered by the hard part
("convergence is not guaranteed," non-stationarity). RL5 then surveys where the
whole field extends from here.

---

## Review Questions

**Conceptual checks**

1. Why does repeating the Prisoner's Dilemma change the strategic outcome, when
   the one-shot game has a unique grim equilibrium? What new capability do
   players gain?
2. State the four properties of Tit-for-Tat and explain why each contributes to
   its robustness.
3. What is mechanism design, and in what sense is it "game theory in reverse"?

**Derivation / analysis**

4. Walk through the backward-induction argument that unravels cooperation in a
   *finitely* repeated Prisoner's Dilemma. Why does an infinite or unknown
   horizon break the argument?
5. State the Folk Theorem. What outcomes does it make sustainable, what sustains
   them, and what condition on the players is required?
6. The Folk Theorem is described as a "double-edged" result. Explain both
   edges — the optimistic one and the one that weakens the predictive power of
   equilibrium.

**Analysis — "why does it behave this way"**

7. Why is multi-agent RL fundamentally harder than single-agent RL? Name the
   specific property of the learning setting that breaks Q-learning's
   convergence guarantee.
8. Minimax-Q converges but Nash-Q generally doesn't. What structural feature of
   zero-sum games makes Minimax-Q tractable, and why is general-sum harder?
9. "Independent learners" each run plain Q-learning in a multi-agent setting.
   Describe a concrete way this can fail to converge.

**Exam-style**

10. Contrast the one-shot and infinitely-repeated Prisoner's Dilemma: the
    equilibrium outcome, what makes cooperation rational (or not), and the role
    of the discount factor.
11. Compare independent learners, Minimax-Q, and Nash-Q on: the game class each
    targets, the convergence guarantee, and the cost per update.
12. Trace the RL1 → RL2 → RL3 → RL4 progression in one paragraph: how the agent
    setting generalizes at each step and what guarantee is lost along the way.
