Title: NBA week 11 summary, week 12 predictions
Date: 2015-01-23 12:12
Author: Jonathan Landy
Category: NBA prediction project
Slug: nba-week-11-summary-week-12-predictions
Status: published

Again, reasonably good accuracy this past week -- 36/54, or 66.6% overall. The breakdown by point spread is given below, and the new predictions are up.

We made a couple of changes to the dashboard this week. First, it has a new, cleaner look, thanks to [Jaireh Tecarro](http://www.jairehtecarro.com/), who kindly donated a redesign. Secondly, we discovered that our prior processing code implementation was inadvertently defaulting to a non-smooth rendering mode as a consequence of some coordinate transformations that we were making use of. This behavior was not explained in the general processing references, and so came as a surprise to us. We've reimplemented some of the drawing commands in order to avoid the problem, and we've documented it in our [processing tips and tricks post](http://efavdb.github.io/processing-and-processing-js-tips-and-tricks).

| Point spread | # games | Accuracy |
| -- | -- | -- |
| < 5 | 11 | 45% |
| 5-9 | 23 | 65% |
| 10-14 | 18 | 78% |
| >14 | 18 | 72% |