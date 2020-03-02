Title: A review of parameter regularization and Bayesian regression
Date: 2015-10-11 00:01
Author: Jonathan Landy
Category: Statistics
Slug: bayesian-linear-regression
Status: published

Here, we review parameter regularization, which is a method for improving regression models through the penalization of non-zero parameter estimates. Why is this effective? Biasing parameters towards zero will (of course!) unfavorably bias a model, but it will also reduce its variance. At times the latter effect can win out, resulting in a net reduction in generalization error. We also review Bayesian regressions -- in effect, these generalize the regularization approach, biasing model parameters to any specified prior estimates, not necessarily zero.

This is the second of a series of posts expounding on topics discussed in the text, ["An Introduction to Statistical Learning"](http://www-bcf.usc.edu/~gareth/ISL/). Here, we cover material from its Chapters 2 and 6. See prior post [here](http://efavdb.github.io/leave-one-out-cross-validation).





### Introduction and overview

In this post, we will be concerned with the problem of fitting a function of the form
$$\label{function}
y(\vec{x}_i) = f(\vec{x}_i) + \epsilon_i \tag{1},
$$
where $f$ is the function's systematic part and $\epsilon_i$ is a random error. These errors have mean zero and are iid -- their presence is meant to take into account dependences in $y$ on features that we don't have access to. To "fit" such a function, we will suppose that one has chosen some appropriate regression algorithm (perhaps a linear model, a random forest, etc.) that can be used to generate an approximation $\hat{f}$ to $y$, given a training set of example $(\vec{x}_i, y_i)$ pairs.

The primary concern when carrying out a regression is often to find a fit that will be accurate when applied to points not included in the training set. There are two sources of error that one has to grapple with: Bias in the algorithm -- sometimes the result of using an algorithm that has insufficient flexibility to capture the nature of the function being fit, and variance -- this relates to how sensitive the resulting fit is to the samples chosen for the training set. The latter issue is closely related to the concept of [overfitting](https://en.wikipedia.org/wiki/Overfitting).

To mitigate overfitting, [parameter regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics)) is often applied. As we detail below, this entails penalizing non-zero parameter estimates. Although this can favorably reduce the variance of the resulting model, it will also introduce bias. The optimal amount of regularization is therefore determined by appropriately balancing these two effects.

In the following, we carefully review the mathematical definitions of model bias and variance, as well as how these effects contribute to the error of an algorithm. We then show that regularization is equivalent to assuming a particular form of Bayesian prior that causes the parameters to be somewhat "sticky" around zero -- this stickiness is what results in model variance reduction. Because standard regularization techniques bias towards zero, they work best when the underlying true feature dependences are sparse. When this is not true, one should attempt an analogous variance reduction through application of the more general Bayesian regression framework.

### Squared error decomposition

The first step to understanding regression error is the following identity: Given any fixed $\vec{x}$, we have
$$
\begin{align}
\overline{\left (\hat{f}(\vec{x}) - y(\vec{x}) \right)^2} &= \overline{\left (\hat{f}(\vec{x}) - \overline{\hat{f}(\vec{x})} \right)^2} + \left (\overline{\hat{f}(\vec{x})} - f(\vec{x}) \right)^2 + \overline{ \epsilon^2} \\
& \equiv var\left(\hat{f}(\vec{x})\right) + bias\left(\hat{f}(\vec{x})\right)^2 + \overline{\epsilon^2}. \tag{2}\label{error_decomp}
\end{align}
$$
Here, overlines represent averages over two things: The first is the random error $\epsilon$ values, and the second is the training set used to construct $\hat{f}$. The left side of (\ref{error_decomp}) gives the average squared error of our algorithm, at point $\vec{x}$ -- i.e., the average squared error we can expect to get, given a typical training set and $\epsilon$ value. The right side of the equation decomposes this error into separate, independent components. The first term at right -- the variance of $\hat{f}(\vec{x})$ -- relates to how widely the estimate at $\vec{x}$ changes as one randomly samples from the space of possible training sets. Similarly, the second term -- the algorithm's squared bias -- relates to the systematic error of the algorithm at $\vec{x}$. The third and final term above gives the average squared random error -- this provides a fundamental lower bound on the accuracy of any estimator of $y$.

We turn now to the proof of (\ref{error_decomp}). We write the left side of this equation as
$$\label{detail}
\begin{align} \tag{3}
\overline{\left (\hat{f}(\vec{x}) - y(\vec{x}) \right)^2} &= \overline{\left ( \left \{\hat{f}(\vec{x}) - f(\vec{x}) \right \} - \left \{ y(\vec{x}) - f(\vec{x}) \right \} \right)^2}\\
&=
\overline{\left ( \hat{f}(\vec{x}) - f(\vec{x}) \right)^2}
- 2 \overline{ \left (\hat{f}(\vec{x}) - f(\vec{x}) \right ) \left (y(\vec{x}) - f(\vec{x}) \right ) }
+ \overline{ \left (y(\vec{x}) - f(\vec{x}) \right)^2}.
\end{align}
$$
The middle term here is zero. To see this, note that it is the average of the product of two independent quantities: The first factor, $\hat{f}(\vec{x}) - f(\vec{x})$, varies only with the training set, while the second factor, $y(\vec{x}) - f(\vec{x})$, varies only with $\epsilon$. Because these two factors are independent, their average product is the product of their individual averages, the second of which is zero, by definition. Now, the third term in (\ref{detail}) is simply $\overline{\epsilon^2}$. To complete the proof, we need only evaluate the first term above. To do that, we write
$$\begin{align} \tag{4} \label{detail2}
\overline{\left ( \hat{f}(\vec{x}) - f(\vec{x}) \right)^2} &=
\overline{\left ( \left \{ \hat{f}(\vec{x}) - \overline{\hat{f}(\vec{x})} \right \}- \left \{f(\vec{x}) -\overline{\hat{f}(\vec{x})} \right \}\right)^2} \\
&=
\overline{\left ( \hat{f}(\vec{x}) - \overline{\hat{f}(\vec{x})} \right)^2}
-2
\overline{ \left \{ \hat{f}(\vec{x}) - \overline{\hat{f}(\vec{x})} \right \} \left \{f(\vec{x}) -\overline{\hat{f}(\vec{x})} \right \} }
+
\left ( f(\vec{x}) -\overline{\hat{f}(\vec{x})} \right)^2.
\end{align}
$$
The middle term here is again zero. This is because its second factor is a constant, while the first averages to zero, by definition. The first and third terms above are the algorithm's variance and squared bias, respectively. Combining these observations with (\ref{detail}), we obtain (\ref{error_decomp}).

### Bayesian regression

In order to introduce Bayesian regression, we focus on the special case of least-squares regressions. In this context, one posits that the samples generated take the form (\ref{function}), with the error $\epsilon_i$ terms now iid, Gaussian distributed with mean zero and standard deviation $\sigma$. Under this assumption, the probability of observing values $(y_1, y_2,\ldots, y_N)$ at $(\vec{x}_1, \vec{x}_2,\ldots,\vec{x}_N)$ is given by
$$
\begin{align}
\tag{5} \label{5}
P(\vec{y} \vert f) &= \prod_{i=1}^N \frac{1}{(2 \pi \sigma)^{1/2}} \exp \left [-\frac{1}{2 \sigma^2} (y_i - f(\vec{x}_i))^2 \right]\\
&= \frac{1}{(2 \pi \sigma)^{N/2}} \exp \left [-\frac{1}{2 \sigma^2} (\vec{y} - \vec{f})^2 \right],
\end{align}
$$
where $\vec{y} \equiv (y_1, y_2,\ldots, y_N)$ and $\vec{f} \equiv (f_1, f_2,\ldots, f_N)$. In order to carry out a maximum-likelihood analysis, one posits a parameterization for $f(\vec{x})$. For example, one could posit the linear form,
$$\tag{6}
f(\vec{x}) = \vec{\theta} \cdot \vec{x}.
$$
Once a parameterization is selected, its optimal $\vec{\theta}$ values are selected by maximizing (\ref{5}), which gives the least-squares fit.

One sometimes would like to nudge (or bias) the parameters away from those that maximize (\ref{5}), towards some values considered reasonable ahead of time. A simple way to do this is to introduce a Bayesian prior for the parameters $\vec{\theta}$. For example, one might posit a prior of the form
$$ \tag{7} \label{7}
P(f) \equiv P(\vec{\theta}) \propto \exp \left [- \frac{1}{2\sigma^2} (\vec{\theta} - \vec{\theta}_0)
\Lambda (\vec{\theta} - \vec{\theta}_0)\right].
$$
Here, $\vec{\theta}_0$ represents a best guess for what $\theta$ should be before any data is taken, and the matrix $\Lambda$ determines how strongly we wish to bias $\theta$ to this value: If the components of $\Lambda$ are large (small), then we strongly (weakly) constrain $\vec{\theta}$ to sit near $\vec{\theta}_0$. To carry out the regression, we combine (\ref{5}-\ref{7}) with Bayes' rule, giving
$$
\tag{8}
P(\vec{\theta} \vert \vec{y}) = \frac{P(\vec{y}\vert \vec{\theta}) P(\vec{\theta})}{P(\vec{y})}
\propto \exp \left [-\frac{1}{2 \sigma^2} (\vec{y} - \vec{\theta} \cdot \vec{x})^2 - \frac{1}{2\sigma^2} (\vec{\theta} - \vec{\theta}_0)
\Lambda (\vec{\theta} - \vec{\theta}_0)\right].
$$
The most likely $\vec{\theta}$ now minimizes the quadratic "cost function",
$$\tag{9} \label{9}
F(\theta) \equiv (\vec{y} - \vec{\theta} \cdot \vec{x})^2 +(\vec{\theta} - \vec{\theta}_0)
\Lambda (\vec{\theta} - \vec{\theta}_0),
$$
a Bayesian generalization of the usual squared error. With this, our heavy-lifting is at an end. We now move to a quick review of regularization, which will appear as a simple application of the Bayesian method.

### Parameter regularization as special cases

The most common forms of regularization are the so-called "ridge" and "lasso". In the context of least-squares fits, the former involves minimization of the quadratic form
$$
\tag{10} \label{ridge}
F_{ridge}(\theta) \equiv (\vec{y} - \hat{f}(\vec{x}; \vec{\theta}))^2 + \Lambda \sum_i \theta_i^2,
$$
while in the latter, one minimizes
$$
\tag{11} \label{lasso}
F_{lasso}(\theta) \equiv (\vec{y} - \hat{f}(\vec{x}; \vec{\theta}))^2 + \Lambda \sum_i \vert\theta_i \vert.
$$
The terms proportional to $\Lambda$ above are the so-called regularization terms. In elementary courses, these are generally introduced to least-squares fits in an ad-hoc manner: Conceptually, it is suggested that these terms serve to penalize the inclusion of too many parameters in the model, with individual parameters now taking on large values only if they are really essential to the fit.

While the conceptual argument above may be correct, the framework we've reviewed here allows for a more sophisticated understanding of regularization: (\ref{ridge}) is a special case of (\ref{9}), with $\vec{\theta}_0$ set to $(0,0,\ldots, 0)$. Further, the lasso form (\ref{lasso}) is also a special-case form of Bayesian regression, with the prior set to $P(\vec{\theta}) \propto \exp \left (- \frac{\Lambda}{2 \sigma^2} \sum_i \vert \theta_i \vert \right)$. As advertised, regularization is a form of Bayesian regression.

Why then does regularization "work"? For the same reason any other Bayesian approach does: Introduction of a prior will bias a model (if chosen well, hopefully not by much), but will also effect a reduction in its variance. The appropriate amount of regularization balances these two effects. Sometimes -- but not always -- a non-zero amount of bias is required.

### Discussion

In summary, our main points here were three-fold: (i) We carefully reviewed the mathematical definitions of model bias and variance, deriving (\ref{error_decomp}). (ii) We reviewed how one can inject Bayesian priors to regressions: The key is to use the random error terms to write down the probability of seeing a particular observational data point. (iii) We reviewed the fact that the ridge and lasso -- (\ref{ridge}) and (\ref{lasso}) -- can be considered Bayesian priors.

Intuitively, one might think introduction of a prior serves to reduce the bias in a model: Outside information is injected into a model, nudging its parameters towards values considered reasonable ahead of time. In fact, this nudging introduces bias! Bayesian methods work through reduction in variance, not bias -- A good prior is one that does not introduce too much bias.

When, then, should one use regularization? Only when one expects the optimal model to be largely sparse. This is often the case when working on machine learning algorithms, as one has the freedom there to throw a great many feature variables into a model, expecting only a small (a prior, unknown) minority of them to really prove informative. However, when not working in high-dimensional feature spaces, sparseness should not be expected. In this scenario, one should reason some other form of prior, and attempt a variance reduction through the more general Bayesian framework.
