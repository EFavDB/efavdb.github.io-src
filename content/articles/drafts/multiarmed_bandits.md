Title: Multiarmed bandits in the context of reinforcement learning
Date: 2020-02-01
Author: Cathy Yeh
Category: Tools
Tags: reinforcement learning, multiarmed bandits
Slug: multiarmed-bandits


Reinforcement learning (RL) treats the problem of trying to achieve a
goal in an environment where we aren't instructed about which actions
to take to achieve that goal.  Instead, we try different actions and
evaluate how good our actions are in different situations presented by
the environment in response to our actions.


# Introduction

The problem of maximizing the rewards from a multiarmed bandit, a
slot machine with multiple arms or levers, is a great introduction to
key RL concepts, namely:

**unlike supervised learning, no ground truth supplied**: Each slot
has a different distribution of rewards, but the person/agent (let's call
him Andrew) playing the machine does not know that distribution.

**agent has a a goal**: Maximize total $$$!  For the simple bandit
problem, this goal is equivalent to maximizing the reward for each
slot pull.

**estimating the values for different actions**: Andrew starts
developing a sense for the value of each slot (as measured by the
average reward from that slot) as he continues pulling levers.  A
simple way Andrew might estimate the value of each slot is just
averaging the dollar amounts for all trials per slot.  (Detail: In our
bandit example, the reward per slot is not deterministic, but
described by a stationary distribution.)

**choosing actions to reach that goal, balancing exploration
vs. exploitation**: Andrew can take many different strategies for
deciding which slot arm to pull.  For example, based on a few trials,
one arm may appear to yield the highest rewards, but Andrew may decide
to try others occasionally to improve his estimates of their rewards.

We now go into some more depth on each of these concepts with code for
concreteness.

# Ground truth is hidden in our multiarmed bandit

The `Bandit` class initializes a multiarmed bandit. The distribution
of rewards per arm follows a Gaussian distribution with some mean
dollar amount.

```python
class Bandit:
    """N-armed bandit with stationary distribution of rewards per arm.
    Each arm (action) is identified by an integer.
    """
    def __init__(self, n_arms: int, mu: float, sigma: float):
        self.n_arms = n_arms
        self.std = sigma
        # a dict of the mean action_value per arm, w/ each action_value sampled from a Gaussian
        self.action_values = {k: s for k, s in enumerate(np.random.normal(mu, sigma, n_arms))}
        self.actions = list(self.action_values.keys())  # arms of the bandit
        
    def __call__(self, action: int) -> float:
        """Get reward from bandit for action"""
        return np.random.normal(self.action_values[action], self.std)
```

Implementation detail: the means per arm, stored in
`self.action_values`, are drawn from a Gaussian distribution upon
initialization).

Andrew doesn't know the true mean rewards per arm -- he only sees a
sample reward when he takes the action of pulling on a particular
bandit arm (`__call__`).


# Action, reward, update strategy

Andrew's trajectory in pursuit of his goal of maximizing his rewards
can be understood as a sequence of steps.  For every action he takes,
he gets a reward.  He has a fixed strategy for selecting the actions
to take, but this strategy takes in his latest reward for an action as
input, and performs a computation with that input that affects the
probability of the next actions he will take.


```python
class BaseBanditAlgo(ABC):
    """Base class for algorithms to maximize the rewards 
    for the multiarmed bandit problem"""
    def __init__(self, bandit: Bandit):
        self.bandit = bandit
        self.timestep = 0
        self.rewards = []
    
    @abstractmethod
    def _select_action(self) -> int:
        pass
    
    @abstractmethod
    def _update_for_action_and_reward(self, action: int, reward: float):
         pass
    
    def run(self) -> float:
        action = self._select_action()
        reward = self.bandit(action)
        self._update_for_action_and_reward(action, reward)
        return reward
    
    def __call__(self, n_timesteps: int):
        for i in range(n_timesteps):
            self.timestep += 1
            self.rewards.append(self.run())
```

## Two types of strategies: value based and policy based

We can divide the types of strategies into two categories:

1. value based - agents that try to directly estimate the value of
   each action (and whose policies, i.e. probability of selecting an
   action, are therefore implicit, since the agent will want to choose
   the action that has the highest value)
2. policy based - agents that don't try to directly estimate the value
   of an action and instead directly store the policy, i.e. the
   probability of taking each action.

An example of a **value based** strategy / action-value method for the
bandit problem is the `EpsilonGreedy` approach, which selects the
optimal action with probability $1-\epsilon$, but choose a random arm
a fraction $\epsilon$ of the time as part of its exploration strategy.

```python
class EpsilonGreedy(BaseEstimateActionValueAlgo):
    """Greedy algorithm that explores/samples from the non-greedy action some fraction, 
    epsilon, of the time.
    
    - For a basic greedy algorithm, set epsilon = 0.
    - For optimistic intialization, set q_init > mu, the mean of the Gaussian from
      which the real values per bandit arm are sampled (default is 0).
    """
    def __init__(self, bandit: Bandit, epsilon: float, **kwargs):
        super().__init__(bandit, **kwargs)
        self.epsilon = epsilon

    def _select_action(self) -> int:
        if np.random.sample() < self.epsilon:
            # take random action
            a = np.random.choice(self.bandit.actions)
        else:
            # take greedy action
            a = max(self.est_action_values, key=lambda key: self.est_action_values[key])
        return a
```

(See end of post for additional action-value methods.)

An example of a **policy based** strategy is the `GradientBandit`
method, which stores its policy, the probability per action in
`self.preferences`.  It learns these preferences by doing stochastic
gradient ascent along the preferences in the gradient of the expected
reward in `_update_for_action_and_reward` (see [1] for derivation).

```python
class GradientBandit(BaseBanditAlgo):
    """Algorithm that does not try to estimate action values directly and, instead, tries to learn
    a preference for each action (equivalent to stochastic gradient ascent along gradient in expected
    reward over preferences).
    """
    def __init__(self, bandit: Bandit, alpha: float):
        super().__init__(bandit)
        self.alpha = alpha  # step-size
        self.reward_baseline_avg = 0
        self.preferences = {action: 0 for action in bandit.actions}
        self._calc_probs_from_preferences()
    
    def _calc_probs_from_preferences(self):
        """Probabilities per action follow a Boltzmann distribution over the preferences """
        exp_preferences_for_action = {action: np.exp(v) for action, v in self.preferences.items()}
        partition_fxn = sum(exp_preferences_for_action.values())
        self.probabilities_for_action = OrderedDict({action: v / partition_fxn for action, v in 
                                                     exp_preferences_for_action.items()})

    def _select_action(self) -> int:
        return np.random.choice(list(self.probabilities_for_action.keys()), 
                                p=list(self.probabilities_for_action.values()))
    
    def _update_for_action_and_reward(self, action, reward):
        """Update preferences"""
        reward_diff = reward - self.reward_baseline_avg
            
        # can we combine these updates into single expression using kronecker delta?
        self.preferences[action] += self.alpha * reward_diff * (1 - self.probabilities_for_action[action])
        for a in self.bandit.actions:
            if a == action:
                continue
            else:
                self.preferences[a] -= self.alpha * reward_diff * self.probabilities_for_action[a]

        self.reward_baseline_avg += 1/self.timestep * reward_diff
        self._calc_probs_from_preferences()
```

The `GradientBandit` is an example of a policy gradient method,
discussed in Chapter 13 of [1].


# Simplifications of the multibandit problem from RL

The multiarmed bandit problem shares many concepts from RL, but also
presents many simplifications.  Looking ahead towards the full RL
problem, the simplifications include:

- There is just a single state (single state Markov Decision Process),
  in the sense that Andrew is always presented with the same
  multiarmed bandit; his actions have no effect on subsequent states.
  Andrew therefore did not have to associate different actions to
  different states (in the lingo of [1], the bandit problem is a
  "nonassociate task").

- Andrew gets immediate feedback/reward for each action, and each
  action does not affect subsequent rewards or probability of the next
  state (since there is only one state).  He therefore is not faced
  with the difficult problem of assigning credit for a particular
  action he took which may have affected the rewards received in a
  subsequent state many timesteps later.


# Extra: Total rewards for different bandit algorithms

We have discussed a bunch of different bandit algorithms, but haven't
see what rewards they yield in practice!  After all, Andrew's goal was to
maximize his cumulative rewards.

In this
[Jupyter notebook](https://github.com/frangipane/reinforcement-learning/blob/master/00-Introduction/multiarmed_bandits.ipynb),
we run the algorithms through a range of values for their parameters
to compare their cumulative rewards across 1000 timesteps (also
averaged across many trials of different bandits to smooth things
out).  In the end, we arrive at a plot of the parameter study, that
reproduces Figure 2.6 in [1].

![![parameter study]({static}/images/reproduce_multiarmed_bandit_parameter_study.png)]({static}/images/reproduce_multiarmed_bandit_parameter_study.png)


# References

[1] Sutton and Barto - [Reinforcement Learning: An Introduction (2nd
Edition)](http://incompleteideas.net/book/RLbook2018.pdf)
