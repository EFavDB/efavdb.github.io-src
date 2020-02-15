Title: Introduction to OpenAI Scholars 2020
Date: 2020-02-14 09:00
Author: Cathy Yeh
Category: Misc
Tags: OpenAI, reinforcement learning, machine learning, deep learning
Slug: openai-scholars-intro
Status: published

Two weeks ago, I started at the [OpenAI Scholars](https://openai.com/blog/openai-scholars-spring-2020/) program, which provides the opportunity to study and work full time on a project in an area of deep learning over 4 months.  I’m having a blast!  It’s been a joy focusing 100% on learning and challenging myself in an atmosphere full of friendly intellectual energy and drive.

My mentor is Jerry Tworek, an OpenAI research scientist who works on reinforcement learning (RL) in robotics, and I’ve also chosen to focus on RL during the program.  I constructed a [syllabus](https://docs.google.com/document/d/1MlM5bxMqqiUIig5I6Y28fegvbqokjuvS2llVd2dIIRE/edit?usp=sharing) that will definitely evolve over time, but I’ll try to keep it up-to-date to serve as a useful record for myself and a guide for others who might be interested in a similar course of study.

Some casual notes from the last two weeks:

(1) There are manifold benefits to working on a topic that is in my mentor’s area of expertise.  For example, I’ve already benefited from Jerry’s guidance on major concepts I should focus on in my first month, namely, getting my hands dirty with model-free RL divided broadly into Q-Learning and Policy Gradients, and intuition around hyperparameter tuning and debugging RL problems.

(2) **Weights & Biases** at [wandb.com](wandb.com) is a fantastic free tool for tracking machine learning experiments that is used by a many people at OpenAI.  It was staggeringly simple to integrate wandb with my training script -- both for local runs and in the cloud!  Just ~4 extra lines of code, and logged metrics automagically appear in my wandb dashboard, with auto-generated plots grouped by experiment name, saved artifacts, etc.

Here's an example of a [dashboard](https://app.wandb.ai/frangipane/dqn?workspace=user-frangipane) tracking experiments for my first attempt at implementing a deep RL algorithm from scratch (DQN, or Deep Q learning).  The script that is generating the experiments is still a work in progress, but you can see how few lines were required to integrate with wandb [here](https://github.com/frangipane/reinforcement-learning/blob/master/DQN/dqn.py).  Stay tuned for a blog post about DQN itself in the future!

(3) I've found it very helpful to parallelize reading Sutton and Barto's [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/RLbook2018.pdf), *the* classic text on RL, with watching David Silver's pedagogical online [lectures](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html).  Silver's lectures follow the book closely for the first few chapters, then start condensing several chapters per lecture beginning around lecture 4 or 5, which is helpful for the compressed time over which I'm hoping to ramp up on RL!  Silver also supplements with insightful explanations and material that aren't covered in the book.

Note, Silver was an author on the [DQN Atari](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf) paper that kicked off deep learning in RL in 2015, so his lecture 6 on Value Function Approximation ([video](https://www.youtube.com/watch?v=UoPei5o4fps), [slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/FA.pdf)) is a perfect accompaniment to reading the paper.
