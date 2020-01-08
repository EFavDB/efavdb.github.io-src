Title: Multi-armed bandits: exploration vs. exploitation in a nonassociative setting
Date: 2020-02-01
Author: Cathy Yeh
Category: Tools
Tags:
Slug:

points

Reinforcement Learning (RL) 

- what is multiarmed bandit => unlike supervised learning, not told
  the correct action to take during training.

- why does it help us understand RL?
  - illustrate balance exploration vs exploitation
  - deals with the problem of selecting actions to maximize cumulative
    reward.
  - there is just a single state here (single state MDP) --> what is
    the state? (presented with the same multiarmed bandit,
    i.e. distribution of rewards per arm, every timestep)

- simplification from RL: 
  - get immediate feedback/reward for each action.  each action does
    not affect subsequent rewards.
  - is a nonassociative task: because there is only one state.
    **WRONG: therefore, bandit also lacks a "policy" that maps action to
    different states, or equivalently, its policy is trivial since
    pi(a|s) = 1** 

  - k arms -> selecting of an arm constitutes an action?  since we're
    always in the same state,

- provides examples of action-value methods (which also exist in RL)
    AND gradient bandit method, whose counterpart is policy gradient
    method (S & B chp 13).
    
    


Sutton and Barto (S & B) begins with the multi-armed bandit problem
since it's a nice problem to study before looking at the full
reinforcement learning (RL) problem.

Like RL problems, bandits also involve a tradeoff between exploration
vs. exploitation of the environment / bandit in order to decide on the
best action to take.
  
- exploration: try pulling other arms besides the arm that is
  currently estimated to return the highest reward
- exploitation: only pull the arm with the highest estimated reward.

Some takeaways:

Greedy methods want to keep taking actions that will give rise to the
greatest rewards, based on the agent's estimates / representation of
the distribution of rewards for the arms per bandit. 

There are many different ways we can encourage exploitation:


[Jupyter notebook](https://github.com/frangipane/reinforcement-learning/blob/master/00-Introduction/multiarmed_bandits.ipynb)
