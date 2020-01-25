Title: Introduction to reinforcement learning by example
Date: 2020-02-14
Author: Cathy Yeh
Category: Machine learning
Tags: reinforcement learning, machine learning
Slug: intro-reinforcement-learning-example
Status: published

We’ll introduce reinforcement learning (RL) using a toy example: a student going through college.  This example is lifted directly from David Silver’s [lecture notes](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) on RL.


## Student in toy college

We model the student as an agent in a college environment who can move between five states: CLASS 1, 2, 3, the FACEBOOK state, and SLEEP state.  The states are represented by the four circles and square in \fig().  The SLEEP state -- the square with no outward bound arrows -- is a terminal state, i.e. once a student reaches that state, her journey is finished.

(TODO: diagram should label states).

Actions that a student can take in her current state are labeled in red (facebook/quit/study/sleep/pub) and influence which state she’ll find herself in next.

In this model, most state transitions are deterministic functions of the action in the current state, e.g. if she decides to study in CLASS 1, then she’ll definitely advance to CLASS 2.  The single non-deterministic state transition is if she goes pubbing while in CLASS 3, where the pubbing action is indicated by a solid dot.  Depending on how reckless the night of pubbing was, she can end up in CLASS 1, 2 or 3 with probability 0.2, 0.4, or 0.4, respectively.

The model also specifies the reward $R$ associated with acting in one state and ending up in the next.  In this example, the dynamics $p(s’,r|s,a)$, are given to us, i.e. we have a full model of the environment, and, hopefully, the rewards have been designed to capture the actual end goal of the student.

## Markov Decision Process

Formally, we’ve modeled the student’s college experience as a finite Markov Decision Process (MDP), which is the framework that underpins the RL approach to sequential decision-making problems.

The dynamics are Markov because the probability of ending up in the next state depends only on the current state and action, not on any history leading up to the current state, and the MDP is finite because there are a finite number of states, rewards, and actions.

The components of an MDP are:

- $S$ - the set of possible states
- $R$ - the set of (scalar) rewards
- $A$ - the set of possible actions in each state

where the dynamics of the system are described by the probabilities of receiving a reward in the next state given the current state and action taken, $p(s’,r|s,a)$.

The student’s agency in this environment comes from how she acts in each state.  The mapping of a state to actions is the **policy**, $\pi(a|s) := p(a|s)$, which can be a deterministic or stochastic function of her current state.  Suppose we have an indifferent student who always chooses actions randomly.  We can sample from the MDP to get some example trajectories the student might experience with this policy:

**trajectories**:
```
(CLASS1)--[facebook]-->(FACEBOOK)--[facebook]-->(FACEBOOK)--[facebook]-->(FACEBOOK)--[facebook]-->(FACEBOOK)--[quit]-->(CLASS1)--[facebook]-->(FACEBOOK)--[quit]-->(CLASS1)--[study]-->(CLASS2)--[sleep]-->(SLEEP)

(FACEBOOK)--[quit]-->(CLASS1)--[study]-->(CLASS2)--[study]-->(CLASS3)--[study]-->(SLEEP)

(SLEEP)

(CLASS1)--[facebook]-->(FACEBOOK)--[quit]-->(CLASS1)--[study]-->(CLASS2)--[sleep]-->(SLEEP)

(FACEBOOK)--[facebook]-->(FACEBOOK)--[facebook]-->(FACEBOOK)--[facebook]-->(FACEBOOK)--[facebook]-->(FACEBOOK)--[quit]-->(CLASS1)--[facebook]-->(FACEBOOK)--[quit]-->(CLASS1)--[study]-->(CLASS2)--[study]-->(CLASS3)--[pub]-->(CLASS2)--[study]-->(CLASS3)--[study]-->(SLEEP)
``` 

This [jupyter notebook](https://github.com/frangipane/reinforcement-learning/blob/master/02-dynamic-programming/student_MDP.ipynb) for contains code for sampling the trajectories under the random policy in the student environment.


**Rewards following a random policy**:

Under this random policy, what total reward would the student expect when starting from any of the states?  We can estimate the expected rewards by summing up the rewards per trajectory and plotting the distributions of total rewards per starting state:

[![histogram of sampled returns]({static}/images/intro_rl_histogram_sampled_returns.png)]({static}/images/intro_rl_histogram_sampled_returns.png)


## Maximizing rewards: discounted return and value functions

We’ve just seen how we can estimate rewards starting from each state given some policy.  Next, we’ll formalize our goal in terms of maximizing rewards.

### Returns

We simply summed the rewards from the sample trajectories above, but the quantity we often want to maximize in practice is the **discounted return**:

\begin{eqnarray}\label{return} \tag{1}
G_t := R_{t+1} + \gamma R_{t+2} + … = \sum_{k=0}^\infty \gamma^k R_{t+k+1}
\end{eqnarray}

where $0 \leq \gamma \leq 1$.  $\gamma$ is the *discount rate* which characterizes how much we weight rewards now vs. later.  Discounting is mathematically useful for avoiding infinite returns in MDPs without a terminal state and allows us to account for uncertainty in the future when we don’t have a perfect model of the environment.

### Value functions

Earlier, we were able to estimate the expected undiscounted returns (\fig()) starting from each state by sampling from the MDP under a random policy.  Formally, the state value function $v_{\pi}(s)$ is the expected return when starting in state $s$, following policy $\pi$:

\begin{eqnarray}\label{state-value} \tag{2}
v_{\pi}(s) = \mathbb{E}_{\pi}[G_t | S_t = s]
\end{eqnarray}

The state value function can be written as a recursive relationship, the Bellman expectation equation, which is **central to learning $v_{\pi}$ and searching for good policies** for many RL methods:

\begin{eqnarray}\label{state-value-bellman} \tag{3}
v_{\pi}(s) &=& \mathbb{E}_{\pi}[G_t | S_t = s] \\
       &=& \mathbb{E}_{\pi}[R_{t+1} + \gamma G_{t+2} | S_t = s] \\
       &=& \sum_{a} \pi(a|s) \sum_{s’, r} p(s’, r | s, a) [r + \gamma v_{\pi}(s’) ]
\end{eqnarray}

This equation expresses the value of a state as an average over the discounted value of its neighbor / successor states, plus the expected reward transitioning from $s$ to $s’$, and $v_{\pi}$ is the unique* solution.  Note that the distribution of rewards depends on the student’s policy since her actions influence her future rewards.

We can “just” solve the Bellman equation for the value function instead of sampling to estimate it as we did in (\fig()) from the MDP.  For the student toy example (a small number of states and full knowledge of the environment) a direct solution is feasible, e.g. by directly solving the system of linear equations or iteratively using dynamic programming.  Here is the solution to \eq() for the student example:

[TODO: insert diagram of student MDP with state value functions]

We can verify that the solution is self-consistent by spot-checking the value of a state in terms of the values of its neighboring states according to the Bellman equation, e.g. the CLASS1 state with $v_{\pi}(\text{CLASS1}) = -1.3$:

$$
v_{\pi}(\text{CLASS1}) = 0.5 [-2 + 2.7] + 0.5 [-1 + -2.3] = -1.3
$$

Another value function is the action-value function $q_{\pi}(s, a)$, which is the expected return from a state $s$ if we follow a policy $\pi$ after taking an action $a$:

\begin{eqnarray}\label{action-value} \tag{4}
q_{\pi}(s, a) := \mathbb{E}_{\pi} [ G_t | S_t = s, A = a ]
\end{eqnarray}

**Why $q$ in addition to $v$?**

The action-value function is useful because it helps us decide what action to take in a particular state.  For example, in our [post]({SITEURL}/multiarmed-bandits) on multiarmed bandits (an example of a simple single-state MDP) we gave examples of some agents whose strategy centered on estimating the action-value function of the slot machine and using those estimates to inform which slot machine arms to pull in order to maximize rewards.

We can also write the state-value and action-value functions in terms of each other.  For example, the state-value function can be viewed as an average over the action-value functions for that state, weighted by the probability of taking each action from that state:

\begin{eqnarray}\label{state-value-one-step-backup} \tag{5}
v_{\pi}(s) = \sum_{a} \pi(a|s) q_{\pi}(s, a)
\end{eqnarray}

[TODO: should I talk about backup diagrams?  How are they useful? See S&B p. 60]

## Optimal value and policy

The crux of the RL problem is finding a policy that maximizes the expected return.  A policy $\pi$ is defined to be better than another policy $\pi’$ if $v_{\pi}(s) > v_{\pi’}(s)$ for all states.  We are guaranteed* an optimal state-value function $v_*$ which corresponds to one or more optimal policies $\pi*$.

Recall that the value function for an arbitrary policy was self-consistently characterized in terms of an average over the action-values for that state, leading to the Bellman expectation equation.  In contrast, the optimal value function $v_*$ must be consistent with following a policy that selects the action(s) that maximize the action-value functions from a state, i.e. taking a $\max$ (\ref{state-value-bellman-optimality}) instead of an average (\ref{state-value-one-step-backup}) over $q$s, leading to the **Bellman optimality equation** for $v_*$:

\begin{eqnarray}\label{state-value-bellman-optimality} \tag{6}
v_*(s) &=& \max_a q_{\pi*}(s, a) \\
    &=& \max_a \mathbb{E} [R_{t+1} + \gamma v_*(S_{t+1}) | S_t = s, A_t = a] \\
    &=& \max_a \sum_{s’, r} p(s’, r | s, a) [r + \gamma v_*(s’) ]
\end{eqnarray}

The MDP is "solved" when we know the optimal value function, since the optimal policy immediately follows; namely, take the action in a state that maximizes the right hand side of (\ref{state-value-bellman-optimality}).  The [principle of optimality](https://en.wikipedia.org/wiki/Bellman_equation#Bellman's_Principle_of_Optimality), which applies to the Bellman optimality equation, means that this greedy policy actually corresponds to the optimal policy!

Note: Unlike the Bellman expectation equations, the Bellman optimality equations are a nonlinear system of equations due to taking the max.  Analogous equations exist for the action-value functions $q_*(s,a)$.

Here is the optimal state value function and policy for the student example, which we solve for in a later post:

[TODO insert diagram of optimal policy in student example]

Compare the values per state under the optimal policy vs the random policy in figure ().  The value in every state under the optimal policy exceeds the value under the random policy.

## Summary

We’ve discussed how the problem of sequential decision making can be framed as an MDP using the student toy MDP as an example.  The goal in RL is to figure out a policy -- what actions to take in each state -- that maximizes our returns.

MDPs provide a framework for approaching the problem by defining the value of each state, the value functions, and using the value functions to define what a “best policy” means.  The value functions are unique solutions to the Bellman equations, and the MDP is “solved” when we know the optimal value function.

*The uniqueness of the solution to the Bellman equations for finite MDPs is stated without proof in Ref [2], but Ref [1] motivates it briefly via the contraction mapping theorem.

### Example code

Code for sampling from the student environment under a random policy in order to generate the trajectories and histograms of returns is available in this [jupyter notebook](https://github.com/frangipane/reinforcement-learning/blob/master/02-dynamic-programming/student_MDP.ipynb).

The [code](https://github.com/frangipane/reinforcement-learning/blob/master/02-dynamic-programming/discrete_limit_env.py) for the student environment is modeled after OpenAI gym standards, specifically the `gym.envs.toy_text.DiscreteEnv` environment.


## References

[1] David Silver's RL Course Lecture 2 - ([video](https://www.youtube.com/watch?v=lfHX2hHRMVQ),
  [slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/MDP.pdf))

[2] Sutton and Barto -
  [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/RLbook2018.pdf) - Chapter 3: Finite Markov Decision Processes
