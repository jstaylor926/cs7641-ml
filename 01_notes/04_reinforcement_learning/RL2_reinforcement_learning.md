# RL2 — Reinforcement Learning

**Paired reading:** Sutton & Barto chs. 2/4/6 (`bookdraft2017nov5.pdf`), `kaelbling96reinforcement.pdf` · **Unit:** Reinforcement Learning

## The shift: from planning to learning

RL1 *planned* — it assumed the agent **knows** the transition model `T` and
reward function `R`, and computed the optimal policy with value/policy
iteration. RL2 drops that assumption. The agent **does not know `T` or `R`** — it
must **learn the optimal policy from experience alone**, by acting and observing
the rewards and transitions that result.

This is the genuine reinforcement-learning problem. The same MDP framework (RL1)
still describes the world; the agent just can't see it directly.

## Model-based vs. model-free

Two strategies for not knowing the MDP:

- **Model-based RL** — *learn* `T` and `R` from experience (estimate transition
  frequencies and average rewards), then run RL1's planning on the learned
  model. Sample-efficient (every experience improves the model) but you have to
  build and maintain the model.
- **Model-free RL** — skip the model entirely; learn the value function or
  policy *directly* from experience. **Q-learning is the model-free method to
  know cold.**

## Q-learning

Learn the **action-value function `Q(s,a)`** — the expected return of taking
action `a` in state `s` and acting optimally thereafter — directly, with no model
of `T`. The update, applied after each observed transition `(s, a, r, s')`:

```
Q(s,a) ← Q(s,a) + α · [ r + γ·max_{a'} Q(s',a') − Q(s,a) ]
```

Read the pieces:

- **`r + γ·max_{a'} Q(s',a')`** — the **TD target**: a one-step estimate of the
  true value, "what I just got plus my best guess of the rest." This is a
  *sampled* version of the Bellman optimality equation — the model `T` is
  replaced by the single transition the agent actually experienced.
- **`[ TD target − Q(s,a) ]`** — the **temporal-difference error**: how wrong the
  current estimate was.
- **`α`** — the **learning rate**: how much to move toward the target.
- This is **bootstrapping** — updating an estimate using another estimate
  (`Q(s',a')`), not waiting for the final return.

**The key theoretical result:** Q-learning **converges to the optimal `Q*`**
(and hence `π*`) *regardless of how the agent behaves while learning*, provided
every state-action pair is visited infinitely often and the learning rate decays
appropriately. That property — learning the optimal policy while following a
different (exploratory) policy — makes Q-learning an **off-policy** method.

## Exploration vs. exploitation

The agent faces a dilemma absent from supervised learning: to learn `Q` it must
**explore** (try actions that look suboptimal, to discover their value), but to
earn reward it must **exploit** (take the action that currently looks best).
Pure exploitation gets stuck on the first decent policy it finds; pure
exploration never cashes in.

- **ε-greedy** — the standard scheme: with probability `ε` act randomly
  (explore), otherwise take `argmax_a Q(s,a)` (exploit). Decay `ε` over time:
  explore early, exploit late.
- **Optimistic initialization** — start `Q` high everywhere, so untried actions
  look attractive and get tried.
- **Softmax / Boltzmann** — choose actions probabilistically weighted by their
  `Q`-values, so near-best actions still get some play.

This is the *same* tension as simulated annealing's temperature in OL1 — high T /
high ε = explore, low T / low ε = exploit. Recognizing that connection is a
likely exam point.

## TD learning and the spectrum

Q-learning is one point on the **temporal-difference** family:

- **Monte Carlo** — wait until the episode ends, update toward the *actual*
  observed return. Unbiased but high-variance, and needs episodes to terminate.
- **TD(0)** — update after *one* step using a bootstrapped estimate. Lower
  variance, biased, works on continuing tasks. Q-learning is a TD(0) method.
- **TD(λ)** — interpolates between them with **eligibility traces**, blending
  many-step returns.

On-policy vs. off-policy: **SARSA** is the on-policy sibling of Q-learning — its
target uses the action *actually taken next* (`Q(s',a')`) rather than the greedy
`max`. SARSA learns the value of the policy it's *following* (including its
exploration); Q-learning learns the value of the *optimal* policy. The classic
illustration: on a cliff-walking task SARSA learns a safer path because it
accounts for its own exploratory mistakes.

## Function approximation (the scaling problem)

A `Q`-table has one entry per state-action pair — impossible for large or
continuous state spaces. The fix: **approximate `Q(s,a)` with a function** (a
linear model over features, or a neural net — that's Deep Q-Networks).
Generalization across states is now possible, but the convergence guarantees
weaken — combining bootstrapping, off-policy learning, and function
approximation (the "deadly triad") can diverge. This is the edge of the unit and
the doorway to RL5's variants.

## Where it sits

RL2 is the heart of the unit: model-free learning, Q-learning's update and
convergence property, exploration/exploitation, and the TD family. The RL report
typically pairs RL1's value/policy iteration (which *know* the MDP) against a
model-free learner like Q-learning (which doesn't) on the same MDPs — the
analysis is precisely about that contrast: convergence speed, policy quality,
and how each scales with problem size.

---

## Review Questions

**Conceptual checks**

1. What exactly does RL2 assume the agent does *not* know, and how does that
   change the problem from RL1's planning?
2. Distinguish model-based and model-free RL. What does each learn, and what is
   the sample-efficiency tradeoff?
3. Why does the exploration/exploitation dilemma exist in RL but not in
   supervised learning?

**Derivation / math**

4. Write the Q-learning update and label every term: TD target, TD error,
   learning rate. Explain in what sense the TD target is a *sampled* Bellman
   equation.
5. State the conditions under which Q-learning is guaranteed to converge to
   `Q*`. Why is the "infinitely often" visitation condition necessary?
6. What does "bootstrapping" mean here, and how does it distinguish TD(0) from
   Monte Carlo updates in terms of bias and variance?

**Analysis — "why does it behave this way"**

7. Q-learning is off-policy: it learns `π*` while following an exploratory
   policy. Explain which part of the update makes this work (be specific about
   the `max`).
8. On cliff-walking, SARSA learns a safer route than Q-learning. Explain why,
   using the difference in their TD targets.
9. Connect ε in ε-greedy to temperature `T` in simulated annealing (OL1). What
   is the shared tradeoff, and why do you decay both over time?

**Exam-style**

10. Contrast Q-learning and SARSA: on-policy vs. off-policy, the form of the TD
    target, and what each one's learned values actually represent.
11. Why can't tabular Q-learning scale to large or continuous state spaces, and
    what is the fix? Name one risk that fix introduces.
12. For the RL report, you compare value iteration (RL1) against Q-learning on
    the same MDP. State three concrete axes of comparison and predict how each
    method behaves on each.
