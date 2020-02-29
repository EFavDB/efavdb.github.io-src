Title: Linear Regression
Date: 2016-05-29 11:27
Author: Jonathan Landy
Category: Methods, Theory
Slug: linear-regression
Status: published
Attachments: wp-content/uploads/2016/05/line-3-e1464543342963.jpg, wp-content/uploads/2016/05/line-2.jpg, wp-content/uploads/2016/05/line-4.jpg, wp-content/uploads/2016/05/scatter.jpg, wp-content/uploads/2016/05/line-1.jpg, wp-content/uploads/2016/05/line.jpg

We review classical linear regression using vector-matrix notation. In particular, we derive a) the least-squares solution, b) the fit's coefficient covariance matrix -- showing that the coefficient estimates are most precise along directions that have been sampled over a large range of values (the high variance directions, a la PCA), and c) an unbiased estimate for the underlying sample variance (assuming normal sample variance in this last case). We then review how these last two results can be used to provide confidence intervals / hypothesis tests for the coefficient estimates. Finally, we show that similar results follow from a Bayesian approach.

Last edited July 23, 2016.





### Introduction

Here, we consider the problem of fitting a linear curve to $N$ data points of the form $(\vec{x}_i, y_i),$ where the $\{\vec{x}_i\}$ are column vectors of predictors that sit in an $L$-dimensional space and the $\{y_i\}$ are the response values we wish to predict given the $\{x_i\}$. The linear approximation will be defined by a set of coefficients, $\{\beta_j\}$ so that
\begin{align}
\hat{y}_i \equiv \sum_j x_{i,j} \beta_j = \vec{x}_i^T \cdot \vec{\beta} . \tag{1} \label{1}
\end{align}
We seek the $\vec{\beta}$ that minimizes the average squared $y$ error,
\begin{align} \tag{2} \label{2}
J = \sum_i \left ( y_i - \hat{y}_i \right)^2 = \sum_i \left (y_i - \vec{x}_i^T \cdot \vec{\beta} \right)^2.
\end{align}
It turns out that this is a problem where one can easily derive an analytic expression for the optimal solution. It's also possible to derive an expression for the variance in the optimal solution -- that is, how much we might expect the optimal parameter estimates to change were we to start with some other $N$ data points instead. These estimates can then be used to generate confidence intervals for the coefficient estimates. Here, we review these results, give a simple interpretation to the theoretical variance, and finally show that the same results follow from a Bayesian approach.

### Optimal solution

We seek the coefficient vector that minimizes (\ref{2}). We can find this by differentiating this cost function with respect to $\vec{\beta}$, setting the result to zero. This gives,
\begin{align} \tag{3}
\partial_{\beta_j} J = 2 \sum_i \left (y_i - \sum_k x_{i,k} \beta_k \right) x_{i,j} = 0.
\end{align}
We next define the matrix $X$ so that $X_{i,j} = \vec{x}_{i,j}$. Plugging this into the above, we obtain
\begin{align}
\partial_{\beta_j} J &= 2 \sum_i X_{j,i}^T \left (y_i - \sum_k X_{i,k} \beta_k \right) = 0 \\
&= X^T \cdot \left ( \vec{y} - X \cdot \vec{\beta}\right ) = 0.\tag{4}
\end{align}
Rearranging gives
\begin{align}
X^T X \cdot \vec{\beta} = X^T \cdot \vec{y} \to
\vec{\beta} = (X^T X)^{-1} \cdot X^T \cdot \vec{y} \tag{5} \label{optimal}
\end{align}
This is the squared-error-minimizing solution.

### Parameter covariance matrix

Now, when one carries out a linear fit to some data, the best line often does not go straight through all of the data. Here, we consider the case where the reason for the discrepancy is not that the posited linear form is incorrect, but that there are some hidden variables not measured that the $y$-values also depend on. Assuming our data points represent random samples over these hidden variables, we can model their effect as adding a random noise term to the form (\ref{1}), so that
\begin{align}\tag{6} \label{noise}
y_i = \vec{x}_i^T \cdot \vec{\beta}_{true} + \epsilon_i,
\end{align}
with $\langle \epsilon_i \rangle =0$, $\langle \epsilon_i^2 \rangle = \sigma^2$, and $\vec{\beta}_{true}$ the exact (but unknown) coefficient vector.

Plugging (\ref{noise}) into (\ref{optimal}), we see that $\langle \vec{\beta} \rangle = \vec{\beta}_{true}$. However, the variance of the $\epsilon_i$ injects some uncertainty into our fit: Each realization of the noise will generate slightly different $y$ values, causing the $\vec{\beta}$ fit coefficients to vary. To estimate the magnitude of this effect, we can calculate the covariance matrix of $\vec{\beta}$. At fixed (constant) $X$, plugging in (\ref{optimal}) for $\vec{\beta}$ gives
\begin{align}
cov(\vec{\beta}, \vec{\beta}) &= cov \left( (X^T X)^{-1} \cdot X^T \cdot \vec{y} , \vec{y}^T \cdot X \cdot (X^T X)^{-1, T} \right) \\
&= (X^T X)^{-1} \cdot X^T \cdot cov(\vec{y}^T, \vec{y} ) \cdot X \cdot (X^T X)^{-1, T}
\\
&= \sigma^2 \left( X^T X \right)^{-1} \cdot X^T X \cdot \left( X^T X \right)^{-1, T} \\
&= \sigma^2 \left( X^T X \right)^{-1}. \tag{7} \label{cov}
\end{align}
In the third line here, note that we have assumed that the $\epsilon_i$ are independent, so that $cov(\vec{y},\vec{y}) = \sigma^2 I.$ We've also used the fact that $X^T X$ is symmetric.

To get a feel for the significance of (\ref{cov}), it is helpful to consider the case where the average $x$ values are zero. In this case,
\begin{align}
\left( X^T X \right)_{i,j} &\equiv& \sum_k \delta X_{k,i} \delta X_{k,j} \equiv N \times \langle x_i, x_j\rangle. \tag{8} \label{corr_mat}
\end{align}
[![margin around decision boundary]({static}/wp-content/uploads/2016/05/scatter.jpg)]({static}/wp-content/uploads/2016/05/scatter.jpg) That is, $X^T X$ is proportional to the correlation matrix of our $x$ values. This correlation matrix is real and symmetric, and thus has an orthonormal set of eigenvectors. The eigenvalue corresponding to the $k$-th eigenvector gives the variance of our data set's $k$-th component values in this basis -- details can be found in our [article on PCA](http://efavdb.com/principal-component-analysis/). This implies a simple interpretation of (\ref{cov}): The variance in the $\vec{\beta}$ coefficients will be lowest for predictors parallel to the highest variance PCA components (eg $x_1$ in the figure shown) and highest for predictors parallel to the lowest variance PCA components ($x_2$ in the figure). This observation can often be exploited during an experiment's design: If a particular coefficient is desired to high accuracy, one should make sure to sample the corresponding predictor over a wide range.

[Note: Cathy gives an interesting, alternative interpretation for the parameter estimate variances in a follow-up post, [here](http://efavdb.com/interpret-linear-regression/).]

### Unbiased estimator for $\sigma^2$

The result (\ref{cov}) gives an expression for the variance of the parameter coefficients in terms of the underlying sample variance $\sigma^2$. In practice, $\sigma^2$ is often not provided and must be estimated from the observations at hand. Assuming that the $\{\epsilon_i\}$ in (\ref{noise}) are independent $\mathcal{N}(0, \sigma^2)$ random variables, we now show that the following provides an unbiased estimate for this variance:
$$
S^2 \equiv \frac{1}{N-L} \sum_i \left ( y_i - \vec{x}_i^T \cdot \vec{\beta} \right) ^2. \tag{9} \label{S}
$$
Note that this is a normalized sum of squared residuals from our fit, with $(N-L)$ as the normalization constant -- the number of samples minus the number of fit parameters. To prove that $\langle S^2 \rangle = \sigma^2$, we plug in (\ref{optimal}) for $\vec{\beta}$, combining with (\ref{noise}) for $\vec{y}$. This gives
\begin{align} \nonumber
S^2 &= \frac{1}{N-L} \sum_i \left ( y_i - \vec{x}_i^T \cdot (X^T X)^{-1} \cdot X^T \cdot \{ X \cdot \vec{\beta}_{true} + \vec{\epsilon} \} \right) ^2 \\ \nonumber
&= \frac{1}{N-L} \sum_i \left ( \{y_i - \vec{x}_i^T \cdot\vec{\beta}_{true} \} - \vec{x}_i^T \cdot (X^T X)^{-1} \cdot X^T \cdot \vec{\epsilon} \right) ^2 \\
&= \frac{1}{N-L} \sum_i \left ( \epsilon_i - \vec{x}_i^T \cdot (X^T X)^{-1} \cdot X^T \cdot \vec{\epsilon} \right) ^2 \tag{10}. \label{S2}
\end{align}
The second term in the last line is the $i$-th component of the vector
$$
X \cdot (X^T X)^{-1} \cdot X^T \cdot \vec{\epsilon} \equiv \mathbb{P} \cdot \vec{\epsilon}. \tag{11} \label{projection}
$$
Here, $\mathbb{P}$ is a projection operator -- this follows from the fact that $\mathbb{P}^2 = \mathbb{P}$. When it appears in (\ref{projection}), $\mathbb{P}$ maps $\vec{\epsilon}$ into the $L$-dimensional coordinate space spanned by the $\{\vec{x_i}\}$, scales the result using (\ref{corr_mat}), then maps it back into its original $N$-dimensional space. The net effect is to project $\vec{\epsilon}$ into an $L$-dimensional subspace of the full $N$-dimensional space (more on the $L$-dimensional subspace just below). Plugging (\ref{projection}) into (\ref{S2}), we obtain
$$
S^2 = \frac{1}{N-L} \sum_i \left ( \epsilon_i - (\mathbb{P} \cdot \vec{\epsilon})_i \right)^2 \equiv \frac{1}{N-L} \left \vert \vec{\epsilon} - \mathbb{P} \cdot \vec{\epsilon} \right \vert^2. \label{S3} \tag{12}
$$
This final form gives the result: $\vec{\epsilon}$ is an $N$-dimensional vector of independent, $\mathcal{N}(0, \sigma^2)$ variables, and (\ref{S3}) shows that $S^2$ is equal to $1/(N-L)$ times the squared length of an $(N-L)$-dimensional projection of it (the part along $\mathbb{I} - \mathbb{P}$). The length of this projection will on average be $(N-L) \sigma^2$, so that $\langle S^2 \rangle = \sigma^2$.

We need to make two final points before moving on. First, because $S^2$ is a sum of $(N-L)$ independent $\mathcal{N}(0, \sigma^2)$ random variables, it follows that
$$
\frac{(N-L) S^2}{\sigma^2} \sim \chi_{N-L}^2. \tag{13} \label{chi2}
$$
Second, $S^2$ is independent of $\vec{\beta}$: We can see this by rearranging (\ref{optimal}) as
$$
\vec{\beta} = \vec{\beta}_{true} + (X^T X)^{-1} \cdot X^T \cdot \vec{\epsilon}. \tag{14} \label{beta3}
$$
We can left multiply this by $X$ without loss to obtain
$$
X \cdot \vec{\beta} = X \cdot \vec{\beta}_{true} + \mathbb{P} \cdot \vec{\epsilon}, \tag{15} \label{beta2}
$$
where we have used (\ref{projection}). Comparing (\ref{beta2}) and (\ref{S3}), we see that the components of $\vec{\epsilon}$ that inform $\vec{\beta}$ are in the subspace fixed by $\mathbb{P}$. This is the space complementary to that informing $S^2$, implying that $S^2$ is independent of $\vec{\beta}$.

### Confidence intervals and hypothesis tests

The results above immediately provide us with a method for generating confidence intervals for the individual coefficient estimates (continuing with our Normal error assumption): From (\ref{beta3}), it follows that the coefficients are themselves Normal random variables, with variance given by (\ref{cov}). Further, $S^2$ provides an unbiased estimate for $\sigma^2$, proportional to a $\chi^2_{N-L}$ random variable. Combining these results gives
$$
\frac{\beta_{i,true} - \beta_{i}}{\sqrt{\left(X^T X\right)^{-1}_{ii} S^2}} \sim t_{(N-L)}. \tag{16}
$$
That is, the pivot at left follows a Student's $t$-distribution with $(N-L)$ degrees of freedom (i.e., it's proportional to the ratio of a standard Normal and the square root of a chi-squared variable with that many degrees of freedom). A rearrangement of the above gives the following level $\alpha$ confidence interval for the true value:
$$
\beta_i - t_{(N-L), \alpha /2} \sqrt{\left(X^T X \right)^{-1}_{ii} S^2}\leq \beta_{i, true} \leq \beta_i + t_{(N-L), \alpha /2} \sqrt{\left(X^T X \right)^{-1}_{ii} S^2} \tag{17} \label{interval},
$$
where $\beta_i$ is obtained from the solution (\ref{optimal}). The interval above can be inverted to generate level $\alpha$ hypothesis tests. In particular, we note that a test of the null -- that a particular coefficient is actually zero -- would not be rejected if (\ref{interval}) contains the origin. This approach is often used to test whether some data is consistent with the assertion that a predictor is linearly related to the response.

[Again, see Cathy's follow-up post [here](http://efavdb.com/interpret-linear-regression/) for an alternate take on these results.]

### Bayesian analysis

The final thing we wish to do here is consider the problem from a Bayesian perspective, using a flat prior on the $\vec{\beta}$. In this case, assuming a Gaussian form for the $\epsilon_i$ in (\ref{noise}) gives
\begin{align}\tag{18} \label{18}
p(\vec{\beta} \vert \{y_i\}) \propto p(\{y_i\} \vert \vec{\beta}) p(\vec{\beta}) = \mathcal{N} \exp \left [ -\frac{1}{2 \sigma^2}\sum_i \left (y_i - \vec{\beta} \cdot \vec{x}_i \right)^2\right].
\end{align}
Notice that this posterior form for $\vec{\beta}$ is also Gaussian, and is centered about the solution (\ref{optimal}). Formally, we can write the exponent here in the form
\begin{align}
-\frac{1}{2 \sigma^2}\sum_i \left (y_i - \vec{\beta} \cdot \vec{x}_i \right)^2 \equiv -\frac{1}{2} \vec{\beta}^T \cdot \frac{1}{\Sigma^2} \cdot \vec{\beta}, \tag{19}
\end{align}
where $\Sigma^2$ is the covariance matrix for the components of $\vec{\beta}$, as implied by the posterior form (\ref{18}). We can get the components of its inverse by differentiating (\ref{18}) twice. This gives,
\begin{align}
\left ( \frac{1}{\Sigma^2}\right)_{jk} &= \frac{1}{2 \sigma^2} \partial_{\beta_j} \partial_{\beta_k} \sum_i \left (y_i - \vec{\beta} \cdot \vec{x}_i \right)^2 \\
&= -\frac{1}{\sigma^2}\partial_{\beta_j} \sum_i \left (y_i - \vec{\beta} \cdot \vec{x}_i \right) x_{i,k} \\
&= \frac{1}{\sigma^2} \sum_i x_{i,j} x_{i,k} = \frac{1}{\sigma^2} (X^T X)_{jk}. \tag{20}
\end{align}
In other words, $\Sigma^2 = \sigma^2 (X^T X)^{-1}$, in agreement with the classical expression (\ref{cov}).

### Summary

In summary, we've gone through one quick derivation of linear fit solution that minimizes the sum of squared $y$ errors for a given set of data. We've also considered the variance of this solution, showing that the resulting form is closely related to the principal components of the predictor variables sampled. The covariance solution (\ref{cov}) tells us that all parameters have standard deviations that decrease like $1/\sqrt{N}$, with $N$ the number of samples. However, the predictors that are sampled over wider ranges always have coefficient estimates that more precise. This is due to the fact that sampling over many different values allows one to get a better read on how the underlying function being fit varies with a predictor. Following this, assuming normal errors, we showed that $S^2$ provides an unbiased estimate, chi-squared estimator for the sample variance -- one that is independent of parameter estimates. This allowed us to then write down a confidence interval for the $i$-th coefficient. The final thing we have shown is that the Bayesian, Gaussian approximation gives similar results: In this approach, the posterior that results is centered about the classical solution, and has a covariance matrix equal to that obtained by classical approach.
