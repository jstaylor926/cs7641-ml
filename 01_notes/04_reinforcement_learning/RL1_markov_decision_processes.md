# RL1 — Markov Decision Processes

**Paired reading:** Mitchell Ch 13 · **Unit:** Reinforcement Learning

## The setting

A new kind of learning. No labeled dataset (supervised) and no static pile of
unlabeled data (unsupervised). Instead an **agent** acts in an **environment**,
receives a scalar **reward**, and must learn to act so as to maximize reward
**over time**. The supervision is sparse, delayed, and indirect. RL1 sets up the
formal model — the **Markov Decision Process** — and the planning algorithms that
*solve* it when the model is fully known. (RL2 handles the case where it isn't.)

## The MDP — five pieces

- **States `S`** — the situations the agent can be in.
- **Actions `A`** — the choices available in each state.
- **Transition model `T(s, a, s') = P(s' | s, a)`** — the probability of landing
  in `s'` after taking action `a` in state `s`. Transitions can be
  **stochastic** — the world is noisy.
- **Reward function `R(s)`** (or `R(s,a)`, `R(s,a,s')`) — the immediate scalar
  payoff.
- **Discount factor `γ ∈ [0,1)`** — how much future reward is worth relative to
  immediate reward.

**The Markov property** is the load-bearing assumption: the next state depends
**only on the current state and action**, not on the history of how you got
there. The present is a sufficient statistic for the future. If your problem
isn't Markov, you make it Markov by enriching the state.

## Policies, returns, and the discount factor

A **policy `π(s)`** maps states to actions — it *is* the agent's behavior, the
thing we're solving for. The goal is the policy that maximizes the **expected
discounted return**:

```
G = R(s₀) + γ·R(s₁) + γ²·R(s₂) + γ³·R(s₃) + ...
```

Why discount with `γ`:

- **`γ < 1` keeps the infinite sum finite** (bounded rewards ⇒ bounded return) —
  a mathematical necessity for infinite-horizon problems.
- It encodes a **preference for sooner reward**. `γ → 0`: myopic, only immediate
  reward matters. `γ → 1`: far-sighted, distant rewards count almost fully.
- `γ` is a genuine modeling choice and it changes the optimal policy — a low `γ`
  can make the agent take a quick small reward over a larger distant one.

**Credit assignment** is *the* hard problem here: a reward arrives now, but which
of the many past actions deserves the credit? Discounting plus the value
functions below are the machinery that solves it.

## Value functions and the Bellman equations

The **value of a state** under a policy is the expected return from that state.
The **optimal value function `V*(s)`** is the best achievable expected return
from `s`. It satisfies the **Bellman optimality equation** — the single most
important equation in the unit:

```
V*(s) = R(s) + γ · max_a  Σ_{s'} T(s, a, s') · V*(s')
```

In words: the value of a state is its immediate reward plus the discounted
expected value of the best action available. The optimal policy is then
**greedy** with respect to `V*`:

```
π*(s) = argmax_a  Σ_{s'} T(s, a, s') · V*(s')
```

There is also an action-value form, **`Q*(s,a)`** — the value of taking action
`a` in `s` then acting optimally — which RL2 needs because it doesn't require
knowing `T`.

The Bellman equation is **recursive** (a state's value is defined in terms of
its successors' values) and it defines a **fixed point**. The two planning
algorithms are two ways of reaching that fixed point.

## Value Iteration

Turn the Bellman *equation* into an *update rule* and iterate:

```
V_{k+1}(s) ← R(s) + γ · max_a Σ_{s'} T(s,a,s') · V_k(s')
```

Start with arbitrary `V₀`, apply the update to every state, repeat. The Bellman
operator is a **contraction mapping** (factor `γ`), so by the contraction
mapping theorem this **converges to the unique `V*`** — guaranteed,
geometrically fast. Extract `π*` greedily at the end. You can stop early: once
`V` changes by less than a threshold, the greedy policy is usually already
optimal.

## Policy Iteration

Alternate two steps:

1. **Policy evaluation** — given the current policy `π`, compute its value
   function `Vπ` exactly (solve the linear Bellman system for that fixed policy —
   no `max`, so it's linear).
2. **Policy improvement** — make a new policy greedy with respect to `Vπ`.

Repeat. Each round produces a policy at least as good as the last, and since
there are finitely many policies, it **converges to `π*` in a finite number of
iterations** — typically *fewer iterations* than value iteration, but each
iteration is more expensive (it solves a linear system). Value iteration vs.
policy iteration — more iterations of cheap updates vs. fewer iterations of
expensive ones — is a standard exam contrast and exactly what the RL report
analyzes.

## Why RL1 anchors the unit

Everything in RL2 is "what do you do when you **don't know `T` and `R`**?" —
Q-learning is the model-free echo of value iteration. So nail down here: the
five MDP components, the Markov property, the role of `γ`, the Bellman
optimality equation, and *why* both planning algorithms converge. The RL report
wants you to **hand-trace a few iterations** of value and policy iteration on a
small MDP — not just call a library — so practice that.

---

## Review Questions

**Conceptual checks**

1. List the five components of an MDP and state the Markov property precisely.
   What do you do if your real problem violates it?
2. What is a policy, and why is it the object we are actually solving for (as
   opposed to the value function)?
3. Give two distinct reasons the discount factor `γ` is needed — one
   mathematical, one about agent behavior.

**Derivation / math**

4. Write the Bellman optimality equation for `V*` and explain each term. Then
   write the greedy policy extracted from `V*`.
5. Why does value iteration converge? Name the property of the Bellman operator
   and the theorem that guarantees it, and say what governs the rate.
6. Policy iteration's evaluation step solves a *linear* system, but value
   iteration's update has a `max`. Explain why evaluation is linear and the
   optimality update is not.

**Analysis — "why does it behave this way"**

7. Take a 4-state gridworld of your own design and hand-trace two iterations of
   value iteration. Show the values changing.
8. Value iteration typically needs *more iterations* than policy iteration, yet
   is often used anyway. Explain the per-iteration cost tradeoff.
9. Show, with a small example, how lowering `γ` can change which policy is
   optimal — make the agent prefer a near small reward over a far larger one.

**Exam-style**

10. Define the credit assignment problem and explain how discounting and value
    functions address it.
11. Contrast value iteration and policy iteration on: what each iteration does,
    iteration count to convergence, per-iteration cost, and convergence
    guarantee.
12. For the RL report you solve a "small" and a "large" MDP with both methods.
    Predict how the iteration counts and wall-clock times will differ between
    the two algorithms as problem size grows, and justify it.
