Title: Improved Bonferroni correction factors for multiple pairwise comparisons
Date: 2016-04-10 07:58
Author: Jonathan Landy
Category: Statistics
Slug: bonferroni-correction-for-multiple-pairwise-comparison-tests
Status: published
Attachments: wp-content/uploads/2016/03/Untitled-2.jpg, wp-content/uploads/2016/03/Untitled-2-2.jpg, wp-content/uploads/2016/03/Untitled-2-1.jpg

A common task in applied statistics is the pairwise comparison of the responses of $N$ treatment groups in some statistical test -- the goal being to decide which pairs exhibit differences that are statistically significant. Now, because there is one comparison being made for each pairing, a naive application of the Bonferroni correction analysis suggests that one should set the individual pairwise test sizes to $\alpha_i \to \alpha_f/{N \choose 2}$ in order to obtain a desired family-wise type 1 error rate of $\alpha_f$. Indeed, this solution is suggested by many texts. However, implicit in the Bonferroni analysis is the assumption that the comparisons being made are each mutually independent. This is not the case here, and we show that as a consequence the naive approach often returns type 1 error rates far from those desired. We provide adjusted formulas that allow for error-free Bonferroni-like corrections to be made.

(edit (7/4/2016): After posting this article, I've since found that the method we suggest here is related to / is a generalization of Tukey's range test -- see [here](https://en.wikipedia.org/wiki/Tukey%27s_range_test).)

(edit (6/11/2018): I've added the notebook used below to our Github, [here](https://github.com/EFavDB/improved_bonferroni))





### Introduction

In this post, we consider a particular kind of statistical test where one examines $N$ different treatment groups, measures some particular response within each, and then decides which of the ${N \choose 2}$ pairs appear to exhibit responses that differ significantly. This is called the pairwise comparison problem (or sometimes "posthoc analysis"). It comes up in many contexts, and in general it will be of interest whenever one is carrying out a multiple-treatment test.

Our specific interest here is in identifying the appropriate individual measurement error bars needed to guarantee a given family-wise type 1 error rate, $\alpha_f$. Briefly, $\alpha_f$ is the probability that we incorrectly make any assertion that two measurements differ significantly when the true effect sizes we're trying to measure are actually all the same. This can happen due to the nature of statistical fluctuations. For example, when measuring the heights of $N$ identical objects, measurement error can cause us to incorrectly think that some pair have slightly different heights, even though that's not the case. A classical approach to addressing this problem is given by the Bonferroni approximation: If we consider $\mathcal{N}$ independent comparisons, and each has an individual type 1 error rate of $\alpha_i,$ then the family-wise probability of not making any type 1 errors is simply the product of the probabilities that we don't make any individual type 1 errors,
$$ \tag{1} \label{bon1}
p_f = (1 - \alpha_f) = p_i^{\mathcal{N}} \equiv \left ( 1 - \alpha_i \right)^{\mathcal{N}} \approx 1 - \mathcal{N} \alpha_i.
$$
The last equality here is an expansion that holds when $p_f$ is close to $1$, the limit we usually work in. Rearranging (\ref{bon1}) gives a simple expression,
$$ \tag{2} \label{bon2}
\alpha_i = \frac{\alpha_f}{\mathcal{N}}.
$$
This is the (naive) Bonferroni approximation -- it states that one should use individual tests of size $\alpha_f / \mathcal{N}$ in order to obtain a family-wise error rate of $\alpha_f$.

The reason why we refer to (\ref{bon2}) as the naive Bonferroni approximation is that it doesn't actually apply to the problem we consider here. The reason why is that $p_f \not = p_i^{\mathcal{N}}$ in (\ref{bon1}) if the $\mathcal{N}$ comparisons considered are not independent: This is generally the case for our system of $\mathcal{N} = {N \choose 2}$ comparisons, since they are based on an underlying set of measurements having only $N$ degrees of freedom (the object heights, in our example). Despite this obvious issue, the naive approximation is often applied in this context. Here, we explore the nature of the error incurred in such applications, and we find that it is sometimes very significant. We also show that it's actually quite simple to apply the principle behind the Bonferroni approximation without error: One need only find a way to evaluate the true $p_f$ for any particular choice of error bars. Inverting this then allows one to identify the error bars needed to obtain the desired $p_f$.

### General treatment

In this section, we derive a formal expression for the type 1 error rate in the pairwise comparison problem. For simplicity, we will assume 1) that the uncertainty in each of our $N$ individual measurements is the same (e.g., the variance in the case of Normal variables), and 2) that our pairwise tests assert that two measurements differ statistically if and only if they are more than $k$ units apart.

To proceed, we consider the probability that a type 1 error does not occur, $p_f$. This requires that all $N$ measurements sit within $k$ units of each other. For any set of values satisfying this condition, let the smallest of the set be $x$. We have $N$ choices for which of the treatments sit as this position. The remaining $(N-1)$ values must all be within the region $(x, x+k)$. Because we're considering the type 1 error rate, we can assume that each of the independent measurements takes on the same distribution $P(x)$. These considerations imply
$$ \tag{3} \label{gen}
p_{f} \equiv 1 - \alpha_{f} = N \int_{-\infty}^{\infty} P(x) \left \{\int_x^{x+k} P(y) dy \right \}^{N-1} dx.
$$
Equation (\ref{gen}) is our main result. It is nice for a couple of reasons. First, its form implies that when $N$ is large it will scale like $a \times p_{1,eff}^N$, for some $k$-dependent numbers $a$ and $p_{1,eff}$. This is reminiscent of the expression (\ref{bon1}), where $p_f$ took the form $p_i^{\mathcal{N}}$. Here, we see that the correct value actually scales like some number to the $N$-th power, not the $\mathcal{N}$-th. This reflects the fact that we actually only have $N$ independent degrees of freedom here, not ${N \choose 2}$. Second, when the inner integral above can be carried out formally, (\ref{gen}) can be expressed as a single one-dimensional integral. In such cases, the integral can be evaluated numerically for any $k$, allowing one to conveniently identify the $k$ that returns any specific, desired $p_f$. We illustrate both points in the next two sections, where we consider Normal and Cauchy variables, respectively.

### Normally-distributed responses

We now consider the case where the individual statistics are each Normally-distributed about zero, and we reject any pair if they are more than $k \times \sqrt{2} \sigma$ apart, with $\sigma^2$ the variance of the individual statistics. In this case, the inner integral of (\ref{gen}) goes to
$$\tag{4} \label{inner_g}
\frac{1}{\sqrt{2 \pi \sigma^2}} \int_x^{x+k \sqrt{2} \sigma} \exp\left [ -\frac{y^2}{2 \sigma^2} \right] dy = \frac{1}{2} \left [\text{erf}(k + \frac{x}{\sqrt{2} \sigma}) - \text{erf}(\frac{x}{\sqrt{2} \sigma})\right].
$$
Plugging this into (\ref{gen}), we obtain
$$\tag{5} \label{exact_g}
p_f = \int \frac{N e^{-x^2 / 2 \sigma^2}}{\sqrt{2 \pi \sigma^2}} \exp \left ((N-1) \log \frac{1}{2} \left [\text{erf}(k + \frac{x}{\sqrt{2} \sigma}) - \text{erf}(\frac{x}{\sqrt{2} \sigma})\right]\right)dx.
$$
This exact expression (\ref{exact_g}) can be used to obtain the $k$ value needed to achieve any desired family-wise type 1error rate. Example solutions obtained in this way are compared to the $k$-values returned by the naive Bonferroni approach in the table below. The last column $p_{f,Bon}$ shown is the family-wise success rate that you get when you plug in $k_{Bon},$ the naive Bonferroni $k$ value targeting $p_{f,exact}$.

| $N$ | $p_{f,exact}$ |$k_{exact}$ | $k_{Bon}$ | $p_{f, Bon}$ |
|---|---|---|----|---|
4 | 0.9 | 2.29 | 2.39 | 0.921 |
8 | 0.9 | 2.78 | 2.91 | 0.929 |
4 | 0.95 | 2.57 | 2.64 | 0.959 |
8 | 0.95 | 3.03 | 3.1 | 0.959 |

Examining the table shown, you can see that the naive approach is consistently overestimating the $k$ values (error bars) needed to obtain the desired family-wise rates -- but not dramatically so. The reason for the near-accuracy is that two solutions basically scale the same way with $N$. To see this, one can carry out an asymptotic analysis of (\ref{exact_g}). We skip the details and note only that at large $N$ we have
$$\tag{6} \label{asy_g}
p_f \sim \text{erf} \left ( \frac{k}{2}\right)^N
\sim \left (1 - \frac{e^{-k^2 / 4}}{k \sqrt{\pi}/2} \right)^N.
$$
This is interesting because the individual pairwise tests have p-values given by
$$ \tag{7} \label{asy_i}
p_i = \int_{-k\sqrt{2}\sigma}^{k\sqrt{2}\sigma} \frac{e^{-x^2 / (4 \sigma^2)}}{\sqrt{4 \pi \sigma^2 }} = \text{erf}(k /\sqrt{2}) \sim 1 - \frac{e^{-k^2/2}}{k \sqrt{\pi/2}}.
$$
At large $k$, this is dominated by the exponential. Comparing with (\ref{asy_g}), this implies
$$ \tag{8} \label{fin_g}
p_f \sim \left (1 - \alpha_i^{1/2} \right)^N \sim 1 - N \alpha_i^{1/2} \equiv 1 - \alpha_f.
$$
Fixing $\alpha_f$, this requires that $\alpha_i$ scale like $N^{-2}$, the same scaling with $N$ as the naive Bonferroni solution. Thus, in the case of Normal variables, the Bonferroni approximation provides an inexact, but reasonable approximation (nevertheless, we suggest going with the exact approach using (\ref{exact_g}), since it's just as easy!). We show in the next section that this is not the case for Cauchy variables.

### Cauchy-distributed variables

We'll now consider the case of $N$ independent, identically-distributed Cauchy variables having half widths $a$,
$$ \tag{9} \label{c_dist}
P(x) = \frac{a}{\pi} \frac{1}{a^2 + x^2}.
$$
When we compare any two, we will reject the null if they are more than $ka$ apart. With this choice, the inner integral of (\ref{gen}) is now
$$
\tag{10} \label{inner_c}
\frac{a}{\pi} \int_x^{x+ k a} \frac{1}{a^2 + y^2} dy =\\ \frac{1}{\pi} \left [\tan^{-1}(k + x/a) - \tan^{-1}(x/a) \right].
$$
Plugging into into (\ref{gen}) now gives

$$\tag{11} \label{exact_c}
p_f = \int \frac{N a/\pi}{a^2 + x^2} e^{(N-1) \log
\frac{1}{\pi} \left [\tan^{-1}(k + x/a) - \tan^{-1}(x/a) \right]
}.
$$
This is the analog of (\ref{exact_g}) for Cauchy variables -- it can be used to find the exact $k$ value needed to obtain a given family-wise type 1 error rate. The table below compares the exact values to those returned by the naive Bonferroni analysis [obtained using the fact that the difference between two independent Cauchy variables of width $a$ is itself a Cauchy distributed variable, but with width $2a$].

| $N$ | $p_{f,exact}$ |$k_{exact}$ | $k_{Bon}$ | $p_{f, Bon}$ |
|---|---|---|----|---|
4 | 0.9 | 27 | 76 | 0.965 |
8 | 0.9 | 55 | 350 | 0.985 |
4 | 0.95 | 53 | 153 | 0.983 |
8 | 0.95 | 107 | 700 | 0.993 |

In this case, you can see that the naive Bonferroni approximation performs badly. For example, in the last line, it suggests using error bars that are seven times too large for each point estimate. The error gets even worse as $N$ grows: Again, skipping the details, we note that in this limit, (\ref{exact_c}) scales like
$$\tag{12} \label{asym_c}
p_f \sim \left [\frac{2}{\pi} \tan^{-1}(k/2) \right]^N.
$$
This can be related to the individual $p_i$ values, which are given by
$$ \tag{13} \label{asym2_c}
p_i = \int_{-ka}^{ka} \frac{2 a / \pi}{4 a^2 + x^2}dx = \frac{2}{\pi}\tan^{-1}(k/2).
$$
Comparing the last two lines, we obtain
$$ \tag{14} \label{asym3_c}
p_f \equiv 1 - \alpha_f \sim p_i^N \sim 1 - N \alpha_i.
$$
Although we've been a bit sloppy with coefficients here, (\ref{asym3_c}) gives the correct leading $N$-dependence: $k_{exact} \sim 1/\alpha_i \propto N$. We can see this linear scaling in the table above. This explains why $k_{exact}$ and $k_{Bon}$ -- which scales like ${N \choose 2} \sim N^2$ -- differ more and more as $N$ grows. In this case, you should definitely never use the naive approximation, but instead stick to the exact analysis based on (\ref{exact_c}).

### Conclusion

Some people criticize the Bonferroni correction factor as being too conservative. However, our analysis here suggests that this feeling may be due in part to its occasional improper application. The naive approximation simply does not apply in the case of pairwise comparisons because the ${N \choose 2}$ pairs considered are not independent -- there are only $N$ independent degrees of freedom in this problem. Although the naive correction does not apply to the problem of pairwise comparisons, we've shown here that it remains a simple matter to correctly apply the principle behind it: One can easily select any desired family-wise type 1 error rate through an appropriate selection of the individual test sizes -- just use (\ref{gen})!

We hope you enjoyed this post -- we anticipate writing a bit more on hypothesis testing in the near future.
