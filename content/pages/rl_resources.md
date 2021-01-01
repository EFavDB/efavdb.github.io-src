Title: Getting started in reinforcement learning
Date: 2020-04-25
Author: Cathy Yeh
Slug: rl-resources
Layout: pages
Status: hidden

[TOC]

*Last updated: 2020-07-12*

We’ve collected some resources for getting started in reinforcement learning (RL).  Comments or suggestions are welcome!

A significant part of modeling in RL takes place *outside* of neural networks, with nets being just one component.  We therefore recommend starting with classic RL theory before proceeding to deep RL.

Roughly in order of recommended progression:

## Quick surveys of RL

Before embarking on a full course of study, get some high-level orientation from these lively blog posts:

- [Deep reinforcement learning doesn’t work yet](https://www.alexirpan.com/2018/02/14/rl-hard.html), blog by Alex Irpan - good look at current problems in deep RL, many entertaining examples (doesn’t go into details of algorithms)
- [Pong from pixels](http://karpathy.github.io/2016/05/31/rl/), blog by Andrej Karpathy - goes into details of implementing policy gradient algorithm on the pong Atari game to illustrate RL in action, accompanied by sweet, simple code
- [OpenAI Meta-Learning and Self-Play](https://www.youtube.com/watch?v=9EN_HoEk3KY), video lecture by Ilya Sutskever -- introduces core ideas in RL simply and with great insight, leading to research directions (still at a high level)

## Foundations

Do in parallel:

- **David Silver’s UCL course on RL** [video lectures](https://www.davidsilver.uk/teaching/) - condenses important concepts from Sutton and Barto while maintaining continuity, clear and insightful explanations
- **Introduction to Reinforcement Learning**, Sutton and Barto’s (S&B) classic text, free [online copy available](http://incompleteideas.net/book/RLbook2018.pdf)

Comments:

- David Silver’s course closely follows S&B up through about lecture 5.  We recommend watching each video lecture first, then reviewing the corresponding material in the text afterwards.
- Function approximation, where neural networks (deep RL) become relevant, is not until lecture 6.
Silver’s course doesn’t include links to exercises, but we’ve provided code for an example model from his first few lectures (discussed in our blog post [introducing RL](https://www.efavdb.com/intro-rl-toy-example) and [solving](https://www.efavdb.com/reinforcement-learning-dynamic-programming) the problem with dynamic programming).

## Additional video lectures
**Sergey Levine’s Berkeley Deep RL course**, [CS285](http://rail.eecs.berkeley.edu/deeprlcourse/)

Comments:

- Levine’s course is more advanced than Silver's, with a brisker approach to deep RL (less time spent on classical RL basics).  Like Silver, Levine is a fantastic lecturer and provides a valuable complementary perspective, e.g. more discussion about convergence properties of algorithms, additional intuition on why policy gradients are high variance.  We enjoyed interleaving the Silver and Levine lectures to get multiple takes on the same topics.
- The content from the first half of Levine’s course overlaps with Silver’s, while the second half of the course moves beyond core concepts and brings you to the cutting edge in RL.

## Exercises and implementations

- **Denny Britz’s [reinforcement learning repo](https://github.com/dennybritz/reinforcement-learning)** - instructional exercises and self-contained implementations.  A great accompaniment to David Silver’s course and Sutton and Barto.
- **OpenAI’s [Spinning up in RL](https://spinningup.openai.com/en/latest/)** - self-contained, lightweight implementations of different RL algorithms
    * “Introduction to RL” section is a bit terse for a first exposure to RL, but docs are an excellent reference otherwise, particularly if you’re ready to start implementing deep RL algorithms.
    * Includes instructive usage of auxiliary tools for deep learning, like [logging](https://github.com/openai/spinningup/blob/master/spinup/algos/pytorch/vpg/vpg.py#L183) and MPI [parallelization](https://github.com/openai/spinningup/blob/master/spinup/algos/pytorch/vpg/vpg.py#L180)
- **[OpenAI gym](https://github.com/openai/gym)** - a toolkit for creating custom environments for running your RL algorithms, including a good number of [ready-to-go implementations](https://gym.openai.com/envs/). The API is simple and intuitive.

## Miscellaneous

- [Openreview.net](https://openreview.net/) - it’s hard to place the impact/context of the latest research when you’re just coming to a field, so the publicly available feedback from experts reviewing the papers is invaluable
- **Benchmarks and baselines** - not sure if your implementation of an RL algorithm is performing as expected?  Check out the rl-baselines-zoo [benchmarks](https://github.com/araffin/rl-baselines-zoo/blob/master/benchmark.md), achieved from standardized implementations of RL algorithms using [Stable Baselines](https://github.com/hill-a/stable-baselines).
