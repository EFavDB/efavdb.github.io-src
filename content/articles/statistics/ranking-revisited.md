Title: How not to sort by average rating, revisited
Date: 2015-07-11 20:30
Author: Jonathan Landy
Category: Statistics
Slug: ranking-revisited
Status: published
Attachments: wp-content/uploads/2015/06/sower21.png, wp-content/uploads/2015/06/sower2.png, wp-content/uploads/2015/06/Pseudotsuga_seed_seedling1.png, wp-content/uploads/2015/06/Pseudotsuga_seed_seedling.png

What is the best method for ranking items that have positive and negative reviews? Some sites, including reddit, have adopted an algorithm suggested by [Evan Miller](http://www.evanmiller.org/) to generate their item rankings. However, this algorithm can sometimes be unfairly pessimistic about new, good items. This is especially true of items whose first few votes are negative -- an issue that can be "gamed" by adversaries. In this post, we consider three alternative ranking methods that can enable high-quality items to more-easily bubble-up. The last is the simplest, but continues to give good results: One simply seeds each item's vote count with a suitable fixed number of hidden "starter" votes.




### Introduction -- a review of Evan Miller's post

In an [insightful prior post](http://www.evanmiller.org/how-not-to-sort-by-average-rating.html), Evan Miller (EM) considered the problem of ranking items that had been reviewed as positive or negative (up-voted or down-voted, represented by a 1 or a 0, respectively) by a sample of users. He began by illustrating that two of the more readily-arrived at solutions to this problem are highly flawed. To review:

**Bad method 1:** Rank item $i$ by $n_i(1) - n_i(0)$, its up-vote count minus its down-vote count.

*Issue:* If one item has garnered 60 up-votes and 40 down-votes, it will get the same score as an item with only 20 votes, all positive. Yet, the latter has a 100% up-vote rate (20 for 20), suggesting that it is of very high quality. Despite this, the algorithm ranks the two equally.

**Bad method 2:** Rank item $i$ by $\hat{p} \equiv n_i(1)/[n_i(0) + n_i(1)]$, its sample up-vote rate (average rating).

*Issue:* If any one item has only one vote, an up-vote, it will be given a perfect score by this algorithm. This means that it will be ranked above all other items, despite the fact that a single vote is not particularly informative/convincing. In general, this method can work well, but only once each item has a significant number of votes.

To avoid the issues of these two bad methods (BMs), EM suggests scoring and ranking each item by the *lower limit of its up-vote-rate confidence interval*. This is ([E.B. Wilson, 1927](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval)),
$$\tag{1} \label{emsol}
p_{W} = \frac{\hat{p} + \frac{z_{\alpha/2}^2}{2n} - z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p}) + \frac{z_{\alpha/2}^2}{4n} }{n}}}{1 + \frac{z_{\alpha/2}^2}{n}},
$$
where $\hat{p}$ is again the sample up-vote rate, $z_{\alpha/2}$ is a positive constant that sets the size of the confidence interval used, and $n$ is the total number of votes that have so far been recorded. The score $p_{W}$ approaches $\hat{p}$ once an item has a significant number of votes -- it consequently avoids the pitfall of BM1 above. By construction, it also avoids the pitfall of BM2. With both of these pitfalls avoided, the EM method can sometimes provide a reasonable, practical ranking system.

### Potential issue with (\ref{emsol})

Although (\ref{emsol}) does a good job of avoiding the pitfall associated with BM2, it can do a poor job of handling a related pitfall: If any new item has only a few votes, and these each happen to be down-votes, its sample up-vote rate will be $\hat{p} = 0$. In this case, (\ref{emsol}) gives
$$\label{problem} \tag{2}
p_{W} = \left .\frac{\hat{p} + \frac{z_{\alpha/2}^2}{2n} - z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p}) + \frac{z_{\alpha/2}^2}{4n} }{n}}}{1 + \frac{z_{\alpha/2}^2}{n}}\right \vert_{\hat{p} = 0} = 0.
$$
Now, $p_W$ is always between $0$ and $1$, so (\ref{problem}) implies that any new, quickly-down-voted item will immediately be ranked below all others. This is extremely harsh and potentially unfair. For example, consider the case of a newly-opened restaurant: If an adversary were to quickly down-vote this restaurant on some ranking site -- the day of its opening -- the new restaurant would be ranked below all others, including the adversary. This would occur even if the new restaurant were of very high true quality. This could have potentially-damaging consequences, for both the restaurant and the ranking site -- whose lists should provide only the best recommendations!

An ideal ranking system should explicitly take into account the large uncertainty present when only a small number of votes have been recorded. The score (\ref{emsol}) does a good job of this on the high $\hat{p}$ end, but a poor job on the low $\hat{p}$ end. This approach may be appropriate for cases where one is risk-averse on the high end only, but in general one should protect against both sorts of quick, strong judgements. Below we consider some alternative, [Bayesian](https://en.wikipedia.org/wiki/Bayesian_statistics) ranking solutions. The last is easy to understand and implement: One simply gives each item a hidden number of up- and down-votes to start with. These hidden "starter" votes can be chosen in various ways -- they serve to simply bias new items towards an intermediate value early on, with the bias becoming less important as more votes come in. This approach avoids each of the pitfalls we have discussed.

### Bayesian formulation

Note: This section and the next are both fairly mathematical. They can be skipped for those wishing to focus on application method only.

To start our Bayesian analysis, we begin by positing a general beta distribution for the up-vote rate prior distribution,
$$\tag{3}\label{beta}
P(p) = \tilde{\mathcal{N}} p^a (1-p)^b.
$$
Here, $\tilde{\mathcal{N}}$ is a normalization factor and $a$ and $b$ are some constants (we suggest methods for choosing their values in the discussion section). The function $P(p)$ specifies an initial guess -- in the absence of any reviews for an item -- for what we think the probability is that it will have up-vote rate $p$. If item $i$ actually has been reviewed, we can update our guess for its distribution using [Bayes' rule](https://en.wikipedia.org/wiki/Bayes'_theorem):
$$\begin{align} \tag{4} \label{BR}
P(p \vert n_i(1), n_i(0)) =\frac{ P( n_i(1), n_i(0) \vert p ) P(p)}{P(n_i(1), n_i(0))} = \mathcal{N} p^{n_i(1)+a}(1-p)^{n_i(0)+b}.
\end{align}
$$
Here, we have evaluated $ P( n(1), n(0) \vert p )$ using the [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution), we've plugged in (\ref{beta}) for $P(p)$, and we've collected all $p$-independent factors into the new normalization factor $\mathcal{N}$. The formula (\ref{BR}) provides the basis for the three ranking methods discussed below.

### Three Bayesian ranking systems

Let's rank!

**Bayesian method 1:** Choose the ordering that is most likely.

It is a simple matter to write down a formal expression for the probability of any ranking. For example, given two items we have
$$
P(p_1 > p_2) = \int_0^1 dp_1 \int_0^{p_1} dp_2 P(p_1) P(p_2). \tag{5} \label{int}
$$
Plugging in (\ref{BR}) for the $P(p_i)$'s, this can be evaluated numerically. Evaluating the probability for the opposite ordering, we can then choose that which is most likely to be correct.

*$\bullet$ Pros:* Approach directly optimizes for the object we're interested in, the ranking -- very appealing!

*$\bullet$ Cons:* Given $N$ items, one has $N!$ integrals to carry out -- untenable for large $N$.

*$\bullet$ Note:* See posssiblywrong's post [here](https://possiblywrong.wordpress.com/2014/05/31/reddits-comment-ranking-algorithm-revisited/) for some related, interesting points.

**Bayesian method 2:** Rank item $i$ by its median $p$-value.

Sorting by an item score provides an approach that will scale well even at large $N$. A natural score to consider is an item's median $p$-value: that which it has a $50/50$ shot of being larger (or smaller) than. Using (\ref{BR}), this satisfies
$$\tag{6}\label{m2}
\frac{\int_0^{p_{med}} p^{n_i(1)+a}(1-p)^{n_i(0)+b} dp}{\int_0^{1} p^{n_i(1)+a}(1-p)^{n_i(0)+b} dp} = 1/2.
$$
The integral at left actually has a name -- it's called the [incomplete beta function](http://mathworld.wolfram.com/IncompleteBetaFunction.html). Using a statistics package, it can be inverted to give $p_{med}$. For example, if we set $a = b = 1$, an item with a single up-vote and no down-votes would get a score of $0.614$. In other words, we'd guess there's a 50/50 shot that the item's up-vote rate falls above this value, so we'd rank it higher than any other item whose $p$ value is known to be smaller than this.

*$\bullet$ Pros:* Sorting is fast. Gives intuitive, meaningful score for each item.

*$\bullet$ Cons:* Inverting (\ref{m2}) can be somewhat slow, e.g. $\sim 10^{-3}$ seconds in Mathematica.

*$\bullet$ Note*: EM also derived this score function, in a follow-up to his original post. However, he motivated it in a slightly different way -- see [here](http://www.evanmiller.org/bayesian-average-ratings.html).

**Bayesian method 3:** Rank item $i$ by its most likely (aka [MAP](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation)) $p$-value.

The most likely $p$-value for each item provides another natural score function. To find this, we simply set the derivative of (\ref{BR}) to zero,
$$
\begin{align}
\partial_p p^{n_i(1)+a}(1-p)^{n_i(0)+b} &= \left (\frac{n_i(1)+a}{p} + \frac{n_i(0)+b}{1-p} \right ) p^{n_i(1)+a}(1-p)^{n_i(0)+b} = 0 \\
\to p = \tilde{p} &\equiv \frac{n_i(1)+a}{(n_i(1)+a) + (n_i(0)+b)}. \tag{7} \label{final}
\end{align}
$$
This form $\tilde{p}$ is interesting because it resembles the sample mean $\hat{p}$ considered above. However, the actual number of up- and down-votes, $n_i(1)$ and $n_i(0)$, are supplemented in (\ref{final}) by $a$ and $b$, respectively. We can thus interpret these values as effective "starter votes", given to each item before any real reviews are recorded. Their effect is to bias our guess for $p$ towards the prior's peak value, with the bias being most strong when $a$ and $b$ are chosen large and/or when we have few actual votes present. For any non-zero choices, (\ref{final}) avoids each of the pitfalls discussed above. Further, it approaches the true up-vote rate in the limit of large review sample sizes, as required.

*$\bullet$ Pros:* Sorting is fast. Simple method for avoiding the common pitfalls.

*$\bullet$ Cons:* Have to pick $a$ and $b$ -- see below for suggested methods.

### Discussion

We consider each of the four ranking methods we've discussed here to be interesting and useful -- the three Bayesian ranking systems, as well as [EM's original system](http://www.evanmiller.org/how-not-to-sort-by-average-rating.html), which works well when one only needs to protect against false positives (again, we note that Bayesian method 2 was also considered by EM in a [follow-up](http://www.evanmiller.org/bayesian-average-ratings.html) to his original post). In practice, the three Bayesian approaches will each tend to return similar, but sometimes slightly different rankings. With regards to "correctness", the essential point is that each method is well-motivated and avoids the common pitfalls. However, the final method is the easiest to apply, so it might be the most practical.

To apply the Bayesian methods, one must specify the $a$ and $b$ values defining the prior, (\ref{BR}). We suggest three methods for choosing these: 1) Choose these values to provide a good approximation to your actual distribution, fitting only to items for which you have good statistics. 2) A/B test to get the ranking that optimizes some quantity you are interested in, e.g. clicks. 3) Heuristics: For example, if simplicity is key, choose $a= b =1$, which biases towards an up-vote rate of $0.5$. If a conservative estimate is desired for new items, one can set $b$ larger than $a$. Finally, if you want to raise the number of actual votes required before the sample rates dominate, simply increase the values of $a$ and $b$ accordingly.

To conclude, we present some example output in the table below. We show values for the Wilson score $p_W$, with $z_{\alpha/2}$ set to $1.281$ in (\ref{emsol}) (the value [reddit uses](https://github.com/reddit/reddit/blob/62db2373f2555df17ebeb13968e243fccfbeff5f/r2/r2/lib/db/_sorts.pyx)), and the seed score $\tilde{p}$, with $a$ and $b$ set to $1$ in (\ref{final}). Notice that the two scores are in near-agreement for the last item shown, which has already accumulated a fair number of votes. However, $p_W$ is significantly lower than $\tilde{p}$ for each of the first three items. For example, the third has an up-vote rate of $66%$, but is only given a Wilson score of $0.32$: This means that it would be ranked below any mature item having an up-vote rate at least this high -- including fairly unpopular items liked by only one in three! This observation explains why it is nearly impossible to have new comments noticed on a reddit thread that has already hit the front page. Were reddit to move to a ranking system that were less pessimistic of new comments, its mature threads might remain dynamic.

| up-votes | down-votes | $p_W$, $z_{\alpha/2}= 1.281$ | $\tilde{p}$, $a=b=1$ |
| -- | -- | -- | -- |
| 1 | 0 | 0.38 | 0.67 |
| 1 | 1 | 0.16 | 0.5 |
| 2 | 1 | 0.32 | 0.6 |
| 40 | 10 | 0.72 | 0.79 |
