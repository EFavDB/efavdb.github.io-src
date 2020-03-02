Title: NBA week 1 summary, week 2 predictions
Date: 2014-11-14 23:22
Author: Dustin McIntosh
Category: NBA prediction project
Tags: NBA
Slug: nba-week-1-summary-week-2-predictions
Status: published

[![week1Table]({static}/wp-content/uploads/2014/11/week1Table.png)]({static}/wp-content/uploads/2014/11/week1Table.png)

The first week of our NBA game outcome prediction experiment is in the books!   We had a prediction accuracy of 32/51 (= 63%).  A summary of the results broken down by game point spread is given at right. The point spreads shown are from the actual games, and the accuracy values shown are the fraction of correct predictions for games within the particular point spread range specified in that row. 

Our accuracy this past week was significantly lower than we achieved on the 2013-2014 historical data.  In training on the first 800 games of that season we achieved approximately 70% accuracy on the remaining 430 games, after [incorporating momentum](http://efavdb.github.io/nba-weekly-predictions-up) into the prediction.  This past week, our model had only 70 games from the current season to train on, relying on last year’s data to supplement the training.   For this reason, we feel 63% is actually pretty reasonable for our first week. In fact, we had a few very good days late in the week — and, of course, we are particularly proud to have correctly predicted [this](http://gfycat.com/ScaredConsciousGoldfinch).  

Our predictions for the next week are now up as well.  This week we have further incorporated fatigue into the model - keeping track of the number of games each team has played in the five days preceding a game. When applied to the prior season data, we found that this feature helped boost our accuracy by about 2%.
