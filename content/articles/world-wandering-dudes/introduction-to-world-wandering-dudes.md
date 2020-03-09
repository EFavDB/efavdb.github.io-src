Title: A Framework for Studying Population Dynamics
Date: 2020-03-08
Author: Dustin McIntosh
Category: World Wandering Dudes
Tags: python, statistics, world wandering dudes
Slug: world-wandering-dudes
Status: published

In this post, I want to briefly introduce a new side project for the blog with applications to understanding population dynamics, natural selection, game theory, and probably more.

[World Wandering Dudes](https://github.com/dustinmcintosh/world_wandering_dudes) is a simulation framework in which you initiate a “world” which consists of a “field” and a set of “creatures” (dudes). The field has food on it. Each day, the creatures run around gathering the food which they need to eat, survive, and reproduce.

###Example

Here’s an example of a few days passing in a world in which food randomly sprouts each day and never spoils, initiated with a single creature (particular note: after day 1 passes and there are two creatures, one of them doesn't store enough food to reproduce at the end of the day):
![]({static}/images/the_first_days.gif)

Taking a snapshot of the world at the end of each day for the first 20 or so days you can see as the creatures take over the full field before coming to some equilibrium state.
![]({static}/images/each_day.gif)

###How the world works

A. Each day consists of a number of discrete time steps.  During each time step, the creatures move around the field randomly, if they find food they grab it from the field and store it.

B. At the end of the day, a few things happen:

1. Each creature must eat some food.  If they don’t have enough stored, they die.

2. If they have enough food after eating, they may also reproduce.  Offspring may have mutated properties (e.g., they may move a little faster each time step - speedy creatures - or they may eat less food - efficient creatures)

3. The food may spoil throughout the world (or not) and new food may sprout on the field.

###Examining the historical record

You can also look at this historical recordfor the field and examine some metrics including total creature count, birth/death rate, the mutation composition of the creatures, amount of stored food, amount of ungathered food, and more:
![]({static}/images/example_history.png)
Some phenomenological notes on this particular case (more details on the math behind some of this in future posts):

* The dynamics of the world are stochastic. For example, sometimes the first creature doesn’t find any food and dies immediately.
* The creature population initially grows roughly exponentially as food become plentiful across the map and most creatures find plenty of food.
* With the accumulated food on the field from the initial low-population days, the creatures grow in numbers beyond a sustainable population and a period of starvation and population culling follows. :(
* The population reaches an equilibrium at which thenumber  of creatures on the field is nearly the same as the amount of food sprouted on the field each day (it’s not exactly equal!).
* At equilibrium, the rate at which creatures are being born is equal to the rate at which they die (on average) and both appear to be about a third of the total population (it’s not a third!).
* As mentioned above, upon reproduction the creatures will mutate and more fit creatures may take over the world. In this particular case, efficient creatures come about first and quickly take over the population. The world can actually sustain a higher population of efficient vs normal/speedy creatures, so the total population increases accordingly.
* Shortly thereafter, a few speedy creatures start to show up and they, slowly, take over the world, out-competing the efficient creatures and slowly suppressing the overall population.

More to come on extensions of this project and understanding the math behind it in the future.

# Check it out yourself

The github repository is [here](https://github.com/dustinmcintosh/world_wandering_dudes).

You’ll need git and a github account, python 3, and a bunch of the usual python packages for data science.

```bash
git clone https://github.com/dustinmcintosh/world_wandering_dudes

cd world_wandering_dudes
```

Update the directory for saving figures in ```SET_ME.py```.

Run the sample code:

```bash
python scripts/basic_simulation.py
```
You can recycle the same world again using:

```bash
python scripts/basic_simulation.py -wp my_world.pkl
```
