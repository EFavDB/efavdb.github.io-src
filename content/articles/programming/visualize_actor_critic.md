Title: Visualizing an actor critic algorithm in real time
Date: 2020-05-07 12:00
Author: Cathy Yeh
Category: Programming
Tags: programming, tools, python, reinforcement learning
Slug: visualize-actor-critic
Status: published


Deep reinforcement learning algorithms can be hard to debug, so it helps to visualize as much as possible in the absence of a stack trace [1].  How do we know if the learned policy and value functions make sense?  Seeing these quantities plotted in real time as an agent is interacting with an environment can help us answer that question.

Here’s an example of an agent wandering around a custom [gridworld](https://github.com/frangipane/gym-minigrid) environment.  When the agent executes the `toggle` action in front of an unopened red gift, it receives a reward of 1 point, and the gift turns grey/inactive.

<iframe width="640" height="360" src="https://www.youtube.com/embed/M3PMwPFRoc8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The model is an actor critic, a type of policy gradient algorithm (for a nice introduction, see Jonathan’s [battleship]({static}/battleship) post or [2]) that uses a neural network to parametrize its policy and value functions.

This agent barely "meets expectations" -- notably getting stuck at an opened gift between frames 5-35 -- but the values and policy mostly make sense.  For example, we tend to see spikes in value when the agent is immediately in front of an unopened gift while the policy simultaneously outputs a much higher probability of taking the appropriate `toggle` action in front of the unopened gift.  (We'd achieve better performance by incorporating some memory into the model in the form of an [LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)).

We’re sharing a little helper code to generate the matplotlib plots of the value and policy functions that are shown in the video.

<script src="https://gist.github.com/frangipane/4adca6481bf55f2260ff215c5686851b.js"></script>

**Comments**

- Training of the model is not included.  You'll need to load a trained actor critic model, along with access to its policy and value functions for plotting.  Here, the trained model has been loaded into `agent` with a `get_action` method that returns the `action` to take, along with a numpy array of `policy` probabilities and a scalar `value` for the observation at the current time step.
- The minigridworld environment conforms to the OpenAI gym API, and the `for` loop is a standard implementation for interacting with the environment.
- The gridworld environment already has a built in method for rendering the environment in iteractive mode `env.render('human')`.
- Matplotlib's `autoscale_view` and `relim` functions are used to make updates to the figures at each step.  In particular, this allows us to show what appears to be a sliding window over time of the value function line plot.  When running the script, the plots pop up as three separate figures.


### References

[1] Berkeley Deep RL bootcamp - Core Lecture 6 Nuts and Bolts of Deep RL Experimentation -- John Schulman ([video](https://youtu.be/8EcdaCk9KaQ) | [slides](https://drive.google.com/open?id=0BxXI_RttTZAhc2ZsblNvUHhGZDA)) - great advice on the debugging process, things to plot

[2] OpenAI Spinning Up: [Intro to policy optimization](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)
