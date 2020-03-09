Title: Multivariate Cramer-Rao inequality
Date: 2015-06-20 09:00
Author: Jonathan Landy
Category: Statistics
Slug: multivariate-cramer-rao-bound
Status: published

The Cramer-Rao inequality addresses the question of how accurately one can estimate a set of parameters $\vec{\theta} = \{\theta_1, \theta_2, \ldots, \theta_m \}$ characterizing a probability distribution $P(x) \equiv P(x; \vec{\theta})$, given only some samples $\{x_1, \ldots, x_n\}$ taken from $P$. Specifically, the inequality provides a rigorous lower bound on the covariance matrix of any unbiased set of estimators to these $\{\theta_i\}$ values. In this post, we review the general, multivariate form of the inequality, including its significance and proof.




### Introduction and theorem statement

The analysis of data very frequently requires one to attempt to characterize a probability distribution. For instance, given some random, stationary process that generates samples $\{x_i\}$, one might wish to estimate the mean $\mu$ of the probability distribution $P$ characterizing this process. To do this, one could construct an estimator function $\hat{\mu}(\{x_i\})$ -- a function of some samples taken from $P$ -- that is intended to provide an approximation to $\mu$. Given $n$ samples, a natural choice is provided by
\begin{eqnarray}
\hat{\mu}(\{x_i\}) = \frac{1}{n}\sum_{i = 1}^n x_i, \tag{1}
\end{eqnarray}
the mean of the samples. This particular choice of estimator will always be unbiased given a stationary $P$ -- meaning that it will return the correct result, on average. However, each particular sample set realization will return a slightly different mean estimate. This means that $\hat{\mu}$ is itself a random variable having its own distribution and width.

More generally, one might be interested in a distribution characterized by a set of $m$ parameters $\{\theta_i\}$. Consistently good estimates to these values require estimators with distributions that are tightly centered around the true $\{\theta_i\}$ values. The Cramer-Rao inequality tells us that there is a fundamental limit to how tightly centered such estimators can be, given only $n$ samples. We state the result below.

<b>Theorem:</b> The multivariate Cramer-Rao inequality

Let $P$ be a distribution characterized by a set of $m$ parameters $\{\theta_i\}$, and let $\{\hat{\theta_i}\equiv \hat{\theta_i}(\{x_i\})\}$ be an unbiased set of estimator functions for these parameters. Then, the covariance matrix (see definition below) for the $\hat{\{\theta_i\}}$ satisfies,

\begin{eqnarray} \tag{2} \label{cramer_rao_bound}
cov(\hat{\theta}, \hat{\theta}) \geq \frac{1}{n} \times \frac{1}{ cov(\nabla_{\vec{\theta}} \log P(x),\nabla_{\vec{\theta}} \log P(x) )}.
\end{eqnarray}

Here, the inequality holds in the sense that left side of the above equation, minus the right, is positive semi-definite. We discuss the meaning and significance of this equation in the next section.

### Interpretation of the result

To understand (\ref{cramer_rao_bound}), we must first review a couple of definitions. These follow.

**Definition 1**. Let $\vec{u}$ and $\vec{v}$ be two jointly-distributed vectors of stationary random variables. The covariance matrix of $\vec{u}$ and $\vec{v}$ is defined by
$$
cov(\vec{u}, \vec{v})_{ij} = \overline{(u_{i}- \overline{u_i})(v_{j}- \overline{v_j})} \equiv \overline{\delta u_{i} \delta v_{j}}\tag{3} \label{cov},
$$
where we use overlines for averages. In words, (\ref{cov}) states that $cov(\vec{u}, \vec{v})_{ij}$ is the correlation function of the fluctuations of $u_i$ and $v_j$.

**Definition 2**. A real, square matrix $M$ is said to be positive semi-definite if
$$
\vec{a}^T\cdot M \cdot \vec{a} \geq 0 \tag{4} \label{pd}
$$
for all real vectors $\vec{a}$. It is positive definite if the \`\`$\geq$" above can be replaced by a \`\`$>$".

The interesting consequences of (\ref{cramer_rao_bound}) follow from the following observation:

**Observation**. For any constant vectors $\vec{a}$ and $\vec{b}$, we have
$$
cov(\vec{a}^T\cdot\vec{u}, \vec{b}^T \cdot \vec{v}) = \vec{a}^T \cdot cov(\vec{u}, \vec{v}) \cdot \vec{b}. \tag{5} \label{fact}
$$
This follows from the definition (\ref{cov}).

Taking $\vec{a}$ and $\vec{b}$ to both be along $\hat{i}$ in (\ref{fact}), and combining with (\ref{pd}), we see that (\ref{cramer_rao_bound}) implies that
$$
\sigma^2(\hat{\theta}_i^2) \geq \frac{1}{n} \times \left (\frac{1}{ cov(\nabla_{\vec{\theta}} \log P(x),\nabla_{\vec{\theta}} \log P(x) )} \right)_{ii},\tag{6}\label{CRsimple}
$$
where we use $\sigma^2(x)$ to represent the variance of $x$. The left side of (\ref{CRsimple}) is the variance of the estimator function $\hat{\theta}_i$, whereas the right side is a function of $P$ only. This tells us that there is fundamental -- distribution-dependent -- lower limit on the uncertainty one can achieve when attempting to estimate *any parameter characterizing a distribution*. In particular, (\ref{CRsimple}) states that the best variance one can achieve scales like $O(1/n)$, where $n$ is the number of samples available$^1$ -- very interesting!

Why is there a relationship between the left and right matrices in (\ref{cramer_rao_bound})? Basically, the right side relates to the inverse rate at which the probability of a given $x$ changes with $\theta$: If $P(x \vert \theta)$ is highly peaked, the gradient of $P(x \vert \theta)$ will take on large values. In this case, a typical observation $x$ will provide significant information relating to the true $\theta$ value, allowing for unbiased $\hat{\theta}$ estimates that have low variance. In the opposite limit, where typical observations are not very $\theta$-informative, unbiased $\hat{\theta}$ estimates must have large variance$^2$.

We now turn to the proof of (\ref{cramer_rao_bound}).

### Theorem proof

Our discussion here expounds on that in the [online text](http://sfb649.wiwi.hu-berlin.de/fedc_homepage/xplore/tutorials/mvahtmlframe74.html) of Cízek, Härdle, and Weron. We start by deriving a few simple lemmas. We state and derive these sequentially below.

**Lemma 1** Let $T_j(\{x_i\}) \equiv \partial_{\theta_j} \log P(\{x_i\}; \vec{\theta})$ be a function of a set of independent sample values $\{x_i\}$. Then, the average of $T_j(\{x_i\})$ is zero.

*Proof:* We obtain the average of $T_j(\{x_i\})$ through integration over the $\{x_i\}$, weighted by $P$,
$$
\int P(\{x_i\};\vec{\theta}) \partial_{\theta_j} \log P(\{x_i\}; \vec{\theta}) d\vec{x} = \int P \frac{\partial_{\theta_j} P}{P} d\vec{x} = \partial_{\theta_j} \int P d\vec{x} = \partial_{\theta_j} 1 = 0. \tag{7}
$$

**Lemma 2**. The covariance matrix of an unbiased $\hat{\theta}$ and $\vec{T}$ is the identity matrix.

*Proof:* Using (\ref{cov}), the assumed fact that $\hat{\theta}$ is unbiased, and Lemma 1, we have
$$\begin{align}
cov \left (\hat{\theta}(\{x_i\}), \vec{T}(\{x_i\}) \right)_{jk} &= \int P(\{x_i\}) (\hat{\theta}_j - \theta_j ) \partial_{\theta_k} \log P(\{x_i\}) d\vec{x}\\ & = \int (\hat{\theta}_j - \theta_j ) \partial_{\theta_k} P d\vec{x} \\
&= -\int P \partial_{\theta_k} (\hat{\theta}_j - \theta_j ) d \vec{x} \tag{8}
\end{align}
$$
Here, we have integrated by parts in the last line. Now, $\partial_{\theta_k} \theta_j = \delta_{jk}$. Further, $\partial_{\theta_k} \hat{\theta}_j = 0$, since $\hat{\theta}$ is a function of the samples $\{x_i\}$ only. Plugging these results into the last line, we obtain
$$
cov \left (\hat{\theta}, \vec{T} \right)_{jk} = \delta_{jk} \int P d\vec{x} = \delta_{jk}. \tag{9}
$$

**Lemma 3**. The covariance matrix of $\vec{T}$ is $n$ times the covariance matrix of $\nabla_{\vec{\theta}} \log P(x_1 ; \vec{\theta})$ -- a single-sample version of $\vec{T}$.

*Proof:* From the definition of $\vec{T}$, we have
$$
T_j = \partial_{\theta_j} \log P(\{x_i\}, \vec{\theta}) = \sum_{i=1}^n \partial_{\theta_j} \log P(x_i, \vec{\theta}), \tag{10}
$$
where the last line follows from the fact that the $\{x_i\}$ are independent, so that $P(\{x_i\}, \vec{\theta}) = \prod P(x_i; \vec{\theta})$. The sum on the right side of the above equation is a sum of $n$ independent, identically-distributed random variables. If follows that their covariance matrix is $n$ times that for any individual.

**Lemma 4**. Let $x$ and $y$ be two scalar stationary random variables. Then, their correlation coefficient is defined to be $\rho \equiv \frac{cov(x,y)}{\sigma(x) \sigma(y)}$. This satisfies
$$
-1 \leq \rho \leq 1 \label{c_c} \tag{11}
$$

*Proof:* Consider the variance of $\frac{x}{\sigma(x)}+\frac{y}{\sigma(y)}$. This is
$$
\begin{align}
var \left( \frac{x}{\sigma(x)}+\frac{y}{\sigma(y)} \right) &= \frac{\sigma^2(x)}{\sigma^2(x)} + 2\frac{ cov(x,y)}{\sigma(x) \sigma(y)} + \frac{\sigma^2(y)}{\sigma^2(y)} \\
&= 2 + 2 \frac{ cov(x,y)}{\sigma(x) \sigma(y)} \geq 0. \tag{12}
\end{align}
$$
This gives the left side of (\ref{c_c}). Similarly, considering the variance of $\frac{x}{\sigma(x)}-\frac{y}{\sigma(y)}$ gives the right side.

We're now ready to prove the Cramer-Rao result.

**Proof of Cramer-Rao inequality**. Consider the correlation coefficient of the two scalars $\vec{a} \cdot \hat{\theta}$ and $ \vec{b} \cdot \vec{T}$, with $\vec{a}$ and $\vec{b}$ some constant vectors. Using (\ref{fact}) and Lemma 2, this can be written as
$$\begin{align}
\rho & \equiv \frac{cov(\vec{a} \cdot \hat{\theta} ,\vec{b} \cdot \vec{T})}{\sqrt{var(\vec{a} \cdot \hat{\theta})var(\vec{b} \cdot \vec{T})}} \\
&= \frac{\vec{a}^T \cdot \vec{b}}{\left(\vec{a}^T \cdot cov(\hat{\theta}, \hat{\theta}) \cdot \vec{a} \right)^{1/2} \left( \vec{b}^T \cdot cov(\vec{T},\vec{T}) \cdot \vec{b} \right)^{1/2}}\leq 1. \tag{13}
\end{align}
$$
The last inequality here follows from Lemma 4. We can find the direction $\hat{b}$ where the bound above is most tight -- at fixed $\vec{a}$ -- by maximizing the numerator while holding the denominator fixed in value. Using a Lagrange multiplier to hold $\left( \vec{b}^T \cdot cov(\vec{T},\vec{T}) \cdot \vec{b} \right) \equiv 1$, the numerator's extremum occurs where
$$
\vec{a}^T + 2 \lambda \vec{b}^T \cdot cov(\vec{T},\vec{T}) = 0 \ \ \to \ \ \vec{b}^T = - \frac{1}{2 \lambda} \vec{a}^T \cdot cov(\vec{T}, \vec{T})^{-1}. \tag{14}
$$
Plugging this form into the prior line, we obtain
$$
- \frac{\vec{a}^T \cdot cov(\vec{T},\vec{T})^{-1} \cdot \vec{a}}{\left(\vec{a}^T \cdot cov(\hat{\theta}, \hat{\theta}) \cdot \vec{a} \right)^{1/2} \left(\vec{a}^T \cdot cov(\vec{T},\vec{T})^{-1} \cdot \vec{a} \right)^{1/2}}\leq 1. \tag{15}
$$
Squaring and rearranging terms, we obtain
$$
\vec{a}^T \cdot \left (cov(\hat{\theta},\hat{\theta}) - cov(\vec{T},\vec{T})^{-1} \right ) \cdot \vec{a} \geq 0. \tag{16}
$$
This holds for any \\(\vec{a}\\), implying that $cov(\hat{\theta}, \hat{\theta}) - cov(\vec{T},\vec{T})^{-1}$ is positive semi-definite -- see (\ref{pd}). Applying Lemma 3, we obtain the result$^3$. $\blacksquare$

Thank you for reading -- we hope you enjoyed.

[1] More generally, (\ref{fact}) tells us that an observation similar to (\ref{CRsimple}) holds for any linear combination of the $\{\theta_i\}$. Notice also that the proof we provide here could also be applied to any individual $\theta_i$, giving $\sigma^2(\hat{\theta}_i) \geq 1/n \times 1/\langle(\partial_{\theta_i} \log P)^2\rangle$. This is easier to apply than (\ref{cramer_rao_bound}), but is less stringent.

[2] It might be challenging to intuit the exact function that appears on the right side of $(\ref{cramer_rao_bound})$. However, the appearance of $\log P$'s does make some intuitive sense, as it allows the derivatives involved to measure rates of change relative to typical values, $\nabla_{\theta} P / P$.

[3] The discussion here covers the \`\`standard proof" of the Cramer-Rao result. Its brilliance is that it allows one to work with scalars. In contrast, when attempting to find my own proof, I began with the fact that all covariance matrices are positive definite. Applying this result to the covariance matrix of a linear combination of $\hat{\theta}$ and $\vec{T}$, one can quickly get to results similar in form to the Cramer-Rao bound, but not quite identical. After significant work, I was eventually able to show that $\sqrt{cov(\hat{\theta},\hat{\theta})} - 1/\sqrt{cov(\vec{T},\vec{T}) } \geq 0$. However, I have yet to massage my way to the final result using this approach -- the difficulty being that the matrices involved don't commute. By working with scalars from the start, the proof here cleanly avoids all such issues.
