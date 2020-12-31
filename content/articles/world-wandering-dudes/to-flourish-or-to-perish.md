Title: A Framework for Studying Population Dynamics
Date: 2021-01-01
Author: Dustin McIntosh
Category: World Wandering Dudes
Tags: python, statistics, world wandering dudes
Slug: to-flourish-or-to-perish
Status: published

In this post, I explore some basic math behind the World Wandering Dudes framework previously introduced in this post.  To briefly reintroduce the system: imagine a 2-D square lattice of $M$ sites with food distributed randomly with a density $\rho_{food}$.  Creatures wander randomly (via random walk) across the field taking $N$ steps per day, gathering food they come across.  At the end of each day, if a creature has no food it dies, if a creature has exactly 1 food, it survives, if a creature has 2 or more food, it survives and reproduces.  The food will then resprout.