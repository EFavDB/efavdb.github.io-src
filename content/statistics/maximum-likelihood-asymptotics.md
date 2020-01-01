Title: Maximum-likelihood asymptotics
Date: 2015-12-30 00:01
Author: Jonathan Landy
Category: Statistics
Slug: maximum-likelihood-asymptotics
Status: published

In this post, we review two facts about maximum-likelihood estimators: 1) They are consistent, meaning that they converge to the correct values given a large number of samples, $N$, and 2) They satisfy the [Cramer-Rao](http://efavdb.com/multivariate-cramer-rao-bound/) lower bound for unbiased parameter estimates in this same limit -- that is, they have the lowest possible variance of any unbiased estimator, in the $N\gg 1$ limit.

  
[Follow @efavdb](http://twitter.com/efavdb)  
Follow us on twitter for new submission alerts!

### Introduction

We begin with a simple example maximum-likelihood inference problem: Suppose one has obtained $N$ independent samples $\{x_1, x_2, \ldots, x_N\}$ from a Gaussian distribution of unknown mean $\mu$ and variance $\sigma^2$. In order to obtain a maximum-likelihood estimate for these parameters, one asks which $\hat{\mu}$ and $\hat{\sigma}^2$ would be most likely to generate the samples observed. To find these, we first write down the probability of observing the samples, given our model. This is simply  
$$  
P(\{x_1, x_2, \ldots, x_N\} \vert \mu, \sigma^2) = \exp\left [ \sum_{i=1}^N \left (-\frac{1}{2} \log (2 \pi \sigma^2) -\frac{1}{2 \sigma^2} (x_i - \mu)^2\right ) \right ]. \tag{1} \label{1}  
$$  
To obtain the maximum-likelihood estimates, we maximize (\ref{1}): Setting its derivatives with respect to $\mu$ and $\sigma^2$ to zero and solving gives  
\begin{align}\label{mean}  
\hat{\mu} &= \frac{1}{N} \sum_i x_i \tag{2} \\  
\hat{\sigma}^2 &= \frac{1}{N} \sum_i (x_i - \hat{\mu})^2. \tag{3} \label{varhat}  
\end{align}  
These are mean and variance values that would be most likely to generate our observation set $\{x_i\}$. Our solutions show that they are both functions of the random observation set. Because of this, $\hat{\mu}$ and $\hat{\sigma}^2$ are themselves random variables, changing with each sample set that happens to be observed. Their distributions can be characterized by their mean values, variances, etc.

The average squared error of a parameter estimator is determined entirely by its bias and variance -- see eq (2) of [prior post](http://efavdb.com/bayesian-linear-regression/). Now, one can show that the $\hat{\mu}$ estimate of (\ref{mean}) is unbiased, but this is not the case for the variance estimator (\ref{varhat}) -- one should (famously) divide by $N-1$ instead of $N$ here to obtain an unbiased estimator$^1$. This shows that maximum-likelihood estimators need not be unbiased. Why then are they so popular? One reason is that these estimators are guaranteed to be unbiased when $N$, the sample size, is large. Further, in this same limit, these estimators achieve the minimum possible variance for any unbiased parameter estimate -- as set by the fundamental [Cramer-Rao](http://efavdb.com/multivariate-cramer-rao-bound/) bound. The purpose of this post is to review simple proofs of these latter two facts about maximum-likelihood estimators$^2$.

### Consistency

Let $P(x \vert \theta^*)$ be some distribution characterized by a parameter $\theta^*$ that is unknown. We will show that the maximum-likelihood estimator converges to $\theta^*$ when $N$ is large: As in (\ref{1}), the maximum-likelihood solution is that $\theta$ that maximizes  
$$\tag{4} \label{4}  
J \equiv \frac{1}{N}\sum_{i=1}^N \log P(x_i \vert \theta),  
$$  
where the $\{x_i\}$ are the independent samples taken from $P(x \vert \theta^*)$. By the law of large numbers, when $N$ is large, this average over the samples converges to its population mean. In other words,  
$$\tag{5}  
\lim_{N \to \infty}J \rightarrow \int_x P(x \vert \theta^*) \log P(x \vert \theta) dx.  
$$  
We will show that $\theta^*$ is the $\theta$ value that maximizes the above. We can do this directly, writing  
$$  
\begin{align}  
J(\theta) - J(\theta^*) & = \int_x P(x \vert \theta^*) \log \left ( \frac{P(x \vert \theta) }{P(x \vert \theta^*)}\right) \\  
& \leq \int_x P(x \vert \theta^*) \left ( \frac{P(x \vert \theta) }{P(x \vert \theta^*)} - 1 \right) \\  
& = \int_x P(x \vert \theta) - P(x \vert \theta^*) = 1 - 1 = 0. \tag{6} \label{6}  
\end{align}  
$$  
Here, we have used $\log t \leq t-1$ in the second line. Rearranging the above shows that $J(\theta^*) \geq J(\theta)$ for all $\theta$ -- when $N \gg 1$, meaning that $J$ is maximized at $\theta^*$. That is, the maximum-likelihood estimator $\hat{\theta} \to \theta^*$ in this limit$^3$.

### Optimal variance

To derive the variance of a general maximum-likelihood estimator, we will see how its average value changes upon introduction of a small Bayesian prior, $P(\theta) \sim \exp(\Lambda \theta)$. The trick will be to evaluate the change in two separate ways -- this takes a few lines, but is quite straightforward. In the first approach, we do a direct maximization: The quantity to be maximized is now  
$$ \label{7}  
J = \sum_{i=1}^N \log P(x_i \vert \theta) + \Lambda \theta. \tag{7}  
$$  
Because we take $\Lambda$ small, we can use a Taylor expansion to find the new solution, writing  
$$ \label{8}  
\hat{\theta} = \theta^* + \theta_1 \Lambda + O(\Lambda^2). \tag{8}  
$$  
Setting the derivative of (\ref{7}) to zero, with $\theta$ given by its value in (\ref{8}), we obtain  
$$  
\sum_{i=1}^N \partial_{\theta} \left . \log P(x_i \vert \theta) \right \vert_{\theta^*} + \sum_{i=1}^N \partial_{\theta}^2 \left . \log P(x_i \vert \theta) \right \vert_{\theta^*} \times \theta_1 \Lambda + \Lambda + O(\Lambda^2) = 0. \tag{9} \label{9}  
$$  
The first term here goes to zero at large $N$, as above. Setting the terms at $O(\Lambda^1)$ to zero gives  
$$  
\theta_1 = - \frac{1}{ \sum_{i=1}^N \partial_{\theta}^2 \left . \log P(x_i \vert \theta) \right \vert_{\theta^*} }. \tag{10} \label{10}  
$$  
Plugging this back into (\ref{8}) gives the first order correction to $\hat{\theta}$ due to the perturbation. Next, as an alternative approach, we evaluate the change in $\theta$ by maximizing the $P(\theta)$ distribution, expanding about its unperturbed global maximum, $\theta^*$: We write, formally,  
$$\tag{11} \label{11}  
P(\theta) = \exp\left [ - a_0 - a_2 (\theta - \theta^*)^2 - a_3 (\theta - \theta^*)^3 + \ldots + \Lambda \theta \right].  
$$  
Differentiating to maximize (\ref{11}), and again assuming a solution of form (\ref{8}), we obtain  
$$\label{12} \tag{12}  
-2 a_2 \times \theta_1 \Lambda + \Lambda + O(\Lambda^2) = 0 \ \ \to \ \ \theta_1 = \frac{1}{2 a_2}.  
$$  
We now require consistency between our two approaches, equating (\ref{10}) and (\ref{12}). This gives an expression for $a_2$. Plugging this back into (\ref{11}) then gives (for the unperturbed distribution)  
$$\tag{13} \label{13}  
P(\theta) = \mathcal{N} \exp \left [ N \frac{ \langle \partial_{\theta}^2 \left . \log P(x, \theta) \right \vert_{\theta^*} \rangle }{2} (\theta - \theta^*)^2 + \ldots \right].  
$$  
Using this Gaussian approximation$^4$, we can now read off the large $N$ variance of $\hat{\theta}$ as  
$$\tag{14} \label{14}  
var(\hat{\theta}) = - \frac{1}{N} \times \frac{1}{\langle \partial_{\theta}^2 \left . \log P(x, \theta) \right \vert_{\theta^*} \rangle }.  
$$  
This is the lowest possible value for any unbiased estimator, as set by the Cramer-Rao bound. The proof shows that maximum-likelihood estimators always saturate this bound, in the large $N$ limit -- a remarkable result. We discuss the intuitive meaning of the Cramer-Rao bound in a [prior post](http://efavdb.com/multivariate-cramer-rao-bound/).

### Footnotes

[1] To see that (\ref{varhat}) is biased, we just need to evaluate the average of $\sum_i (x_i - \hat{\mu})^2$. This is

$$  
\overline{\sum_i x_i^2 - 2 \sum_{i,j} \frac{x_i x_j}{N} + \sum_{i,j,k} \frac{x_j x_k}{N^2}} = N \overline{x^2} - (N-1) \overline{x}^2 - \overline{x^2} \\  
= (N-1) \left ( \overline{x^2} - \overline{x}^2 \right) \equiv (N-1) \sigma^2.  
$$  
Dividing through by $N$, we see that $\overline{\hat{\sigma}^2} = \left(\frac{N-1}{N}\right)\sigma^2$. The deviation from the true variance $\sigma^2$ goes to zero at large $N$, but is non-zero for any finite $N$: The estimator is biased, but the bias goes to zero at large $N$.

[2] The consistency proof is taken from lecture notes by D. Panchenko, see [here](http://ocw.mit.edu/courses/mathematics/18-443-statistics-for-applications-fall-2006/lecture-notes/lecture3.pdf). Professor Panchenko is quite famous for having proven the correctness of the Parisi ansatz in replica theory. Our variance proof is original -- please let us know if you have seen it elsewhere. Note that it can also be easily extended to derive the covariance matrix of a set of maximum-likelihood estimators that are jointly distributed -- we cover only the scalar case here, for simplicity.

[3] The proof here actually only shows that there is no $\theta$ that gives larger likelihood than $\theta^*$ in the large $N$ limit. However, for some problems, it is possible that more than one $\theta$ maximizes the likelihood. A trivial example is given by the case where the distribution is actually only a function of $(\theta - \theta_0)^2$. In this case, both values $\theta_0 \pm (\theta^* - \theta_0)$ will necessarily maximize the likelihood.

[4] It's a simple matter to carry this analysis further, including the cubic and higher order terms in the expansion (\ref{11}). These lead to correction terms for (\ref{14}), smaller in magnitude than that given there. These terms become important when $N$ decreases in magnitude.
