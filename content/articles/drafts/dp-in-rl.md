Title: Dynamic programming in reinforcement learning
Date: 2020-02-21
Author: Cathy Yeh
Category: Machine learning
Tags: reinforcement learning, machine learning
Slug: reinforcement-learning-dynamic-programming
Status: published

## Background

We discuss how to use dynamic programming (DP) to solve reinforcement learning (RL) problems where we have a perfect model of the environment.  DP is a general approach to solving problems by breaking them into subproblems that can be solved separately, cached, then combined to solve the overall problem.  The value functions in Markov Decision Processes, which obey the recursive Bellman equations, satisfy these properties.

We’ll use a toy model, taken from [1], of a student transitioning between five states in college, which we also used in our [introduction]() to RL.

![student MDP]({static}/images/student_mdp.png)

The dynamics of the environment are described by the probabilities of receiving a reward in the next state given the current state and action taken, $p(s’, r | s, a)$.  The agent’s (student’s) policy, i.e. mapping from states to actions, is $\pi(a|s) := p(a|s)$.

## The role of value functions in RL

The goal of the student is to find the optimal policy $\pi_*$ that will maximize the expected cumulative rewards, the discounted return, in each state $s$.  The value functions, $v_{\pi}(s)$ and $q_{\pi}(s, a)$, in MDPs formalize this goal.  Not only do we want to be able to calculate the value function for an arbitrary policy, i.e. *prediction*, but we'll also use the value functions to find an optimal policy.

## Policy evaluation

Policy evaluation deals with the problem of calculating the value function for some arbitrary policy.  Recall from our last post []() that the value functions obey self-consistent, recursive relation, the Bellman expectation equations, that write the value of each state in terms of an average over the values of its successor / neighboring states, along with the expected reward along the way.  The Bellman expectation equation for $v_{\pi}(s)$ is:

\begin{eqnarray}\label{state-value-bellman} \tag{1}
v_{\pi}(s) &=& \mathbb{E}_{\pi}[G_t | S_t = s] \\
       &=& \sum_{a} \pi(a|s) \sum_{s’, r} p(s’, r | s, a) [r + \gamma v_{\pi}(s’) ]
\end{eqnarray}

DP turns (\ref{state-value-bellman}) into an update rule (\ref{policy-evaluation}), $\{v_k(s’)\} \rightarrow v_{k+1}(s)$  which iteratively converges towards the solution, $v_\pi(s)$, for (\ref{state-value-bellman}):

\begin{eqnarray}\label{policy-evaluation} \tag{2}
v_{k+1}(s) = \sum_{a} \pi(a|s) \sum_{s’, r} p(s’, r | s, a) [r + \gamma v_k(s’) ]
\end{eqnarray}

The following python code implements the iterative policy evaluation algorithm, taken from Denny Britz’s notes on RL (see [References](#References) at end of post), which we reproduce below:
```python
def policy_eval(policy, env, discount_factor=1.0, theta=0.00001):
    """
    Evaluate a policy given an environment and a full description of the environment's dynamics.
    
    Args:
        policy: [S, A] shaped matrix representing the policy.
        env: OpenAI env. env.P represents the transition probabilities of the environment.
            env.P[s][a] is a list of transition tuples (prob, next_state, reward, done).
            env.nS is a number of states in the environment.
            env.vA is a vector of the number of actions per state in the environment.
        theta: We stop evaluation once our value function change is less than theta for all states.
        discount_factor: Gamma discount factor.
    
    Returns:
        Vector of length env.nS representing the value function.
    """
    # Start with a random (all 0) value function
    V = np.zeros(env.nS)
    while True:
        delta = 0
        # For each state, perform a "full backup"
        for s in range(env.nS):
            v = 0
            # Look at the possible next actions
            for a, action_prob in enumerate(policy[s]):
                # For each action, look at the possible next states...
                for  prob, next_state, reward, done in env.P[s][a]:
                    # Calculate the expected value. Ref: Sutton book eq. 4.6.
                    v += action_prob * prob * (reward + discount_factor * V[next_state])
            # How much our value function changed (across any states)
            delta = max(delta, np.abs(v - V[s]))
            V[s] = v
        # Stop evaluating once our value function change is below a threshold
        if delta < theta:
            break
    return np.array(V)
```

Applying policy evaluation to our student model for an agent with a random policy, we arrive at the following state value function (see [jupyter notebook](https://github.com/frangipane/reinforcement-learning/blob/master/02-dynamic-programming/student_MDP_dynamic_programming_solutions.ipynb)):

![student MDP value function random policy]({static}/images/student_mdp_values_random_policy.png)


## Finding the optimal value functions and policy

### Policy iteration

We can evaluate the value functions for a given policy by turning the Bellman expectation equation (\ref{state-value-bellman}) into an update equation with the iterative policy evaluation algorithm.

But how do we use value functions to achieve our end goal of finding an optimal policy that corresponds to the optimal value functions?

Imagine we know the value function for a policy.  If taking the greedy action, $\text{arg} \max_a q_{\pi}(s,a)$, from any state in that policy is not consistent with that policy, or, equivalently, $\max_a q_{\pi}(s,a) > v_\pi(s)$, then the policy is not optimal; for instance, we can improve the policy by taking the greedy action in that state and then onwards following the original policy.

The *policy iteration* algorithm involves taking turns calculating the value function for a policy (policy evaluation) and improving on the policy (policy improvement) by taking the greedy action in each state for that value function until converging to $\pi_*$ and $v_*$ (see [2] for pseudocode for policy iteration).

### Value iteration

Unlike policy iteration, the value iteration algorithm does not require complete convergence of policy evaluation before policy improvement, and, in fact, makes use of just a single iteration of policy evaluation.  Just as policy evaluation could be viewed as turning the Bellman expectation equation into an update, value iteration turns the Bellman optimality equation into an update.

In our previous [post]() introducing RL using the student example, we saw that the optimal value functions are the solutions to the Bellman optimality equation, e.g. for the optimal state-value function:

\begin{eqnarray}\label{state-value-bellman-optimality} \tag{3}
v_*(s) &=& \max_a q_{\pi*}(s, a) \\
    &=& \max_a \mathbb{E} [R_{t+1} + \gamma v_*(S_{t+1}) | S_t = s, A_t = a] \\
    &=& \max_a \sum_{s’, r} p(s’, r | s, a) [r + \gamma v_*(s’) ]
\end{eqnarray}

As a DP update equation, (\ref{state-value-bellman-optimality}) becomes:
\begin{eqnarray}\label{value-iteration} \tag{4}
v_{k+1}(s) = \max_a \sum_{s’, r} p(s’, r | s, a) [r + \gamma v_k(s’) ]
\end{eqnarray}

Value iteration combines (truncated) policy evaluation with policy improvement in a single step; the state-value functions are updated with the averages of the value functions of the neighbor states that can occur from a greedy action, i.e. the action that maximizes the right hand side of (\ref{value-iteration}).

The following python code implements the value iteration algorithm, also taken from Denny Britz’s [notes](#References) on RL, with slight modifications for our particular student model:

```python
def value_iteration(env, theta=0.0001, discount_factor=1.0):
    """
    Value Iteration Algorithm.
    
    Args:
        env: OpenAI env. env.P represents the transition probabilities of the environment.
            env.P[s][a] is a list of transition tuples (prob, next_state, reward, done).
            env.nS is a number of states in the environment. 
            env.vA is a vector of the number of actions per state in the environment.
        theta: We stop evaluation once our value function change is less than theta for all states.
        discount_factor: Gamma discount factor.
        
    Returns:
        A tuple (policy, V) of the optimal policy and the optimal value function.
    """
    
    def one_step_lookahead(state, V):
        """
        Helper function to calculate the value for all action in a given state.
        
        Args:
            state: The state to consider (int)
            V: The value to use as an estimator, Vector of length env.nS
        
        Returns:
            A vector of length env.vA[state] containing the expected value of each action.
        """
        A = np.zeros(env.vA[state])
        for a in range(env.vA[state]):
            for prob, next_state, reward, _ in env.P[state][a]:
                A[a] += prob * (reward + discount_factor * V[next_state])
        return A
    
    V = np.zeros(env.nS)
    while True:
        # Stopping condition
        delta = 0
        # Update each state...
        for s in range(env.nS):
            # Do a one-step lookahead to find the best action
            A = one_step_lookahead(s, V)
            best_action_value = np.max(A)
            # Calculate delta across all states seen so far
            delta = max(delta, np.abs(best_action_value - V[s]))
            # Update the value function. Ref: Sutton book eq. 4.10. 
            V[s] = best_action_value        
        # Check if we can stop 
        if delta < theta:
            break
    
    # Create a deterministic policy using the optimal value function
    policy = [np.zeros(nA) for nA in env.vA]
    for s in range(env.nS):
        # One step lookahead to find the best action for this state
        A = one_step_lookahead(s, V)
        best_action = np.argmax(A)
        # Always take the best action
        policy[s][best_action] = 1.0
    return policy, V
```

Applying value iteration to our student model, we arrive at the following optimal state value function, with the optimal policy delineated by red arrows (see [jupyter notebook](https://github.com/frangipane/reinforcement-learning/blob/master/02-dynamic-programming/student_MDP_dynamic_programming_solutions.ipynb)):

![student MDP optimal policy and value function]({static}/images/student_mdp_optimal_policy.png)

## Summary

We’ve discussed how to solve for (1) the value functions of an arbitrary policy, (2) the optimal value functions and optimal policy.  Solving for (1) involves turning the Bellman expectation equations into an update, whereas (2) involves turning the Bellman optimality equations into an update.  These algorithms are guaranteed to converge (see [1] for notes on how the contraction mapping theorem guarantees convergence).

You can see the application of both policy evaluation and value iteration to the student model problem in this [jupyter notebook](https://github.com/frangipane/reinforcement-learning/blob/master/02-dynamic-programming/student_MDP_dynamic_programming_solutions.ipynb).

## <a name="References">References</a>

[1] David Silver's RL Course Lecture 2 - ([video](https://www.youtube.com/watch?v=Nd1-UUMVfz4),
  [slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/DP.pdf))

[2] Sutton and Barto -
  [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/RLbook2018.pdf) - Chapter 4: Dynamic Programming

[3] Denny Britz’s [notes](https://github.com/dennybritz/reinforcement-learning/tree/master/DP) on RL and DP, including crisp implementations in code of policy evaluation, policy iteration, and value iteration for the gridworld example discussed in [2].

[4] Deep RL Bootcamp Lecture 1: Motivation + Overview + Exact Solution Methods, by Pieter Abbeel ([video](https://www.youtube.com/watch?v=qaMdN6LS9rA), [slides](https://drive.google.com/open?id=0BxXI_RttTZAhVXBlMUVkQ1BVVDQ)) - a very compressed intro.
