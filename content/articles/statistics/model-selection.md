Title: Hyperparameter sample-size dependence
Date: 2016-08-21 00:00
Author: Jonathan Landy
Category: Statistics
Slug: model-selection
Status: published
Attachments: wp-content/uploads/2016/05/title-1.jpg, wp-content/uploads/2016/05/title.jpg

Here, we briefly review a subtlety associated with machine-learning model selection: the fact that the optimal hyperparameters for a model can vary with training set size, $N.$ To illustrate this point, we derive expressions for the optimal strength for both $L_1$ and $L_2$ regularization in single-variable models. We find that the optimal $L_2$ approaches a finite constant as $N$ increases, but that the optimal $L_1$ decays exponentially fast with $N.$ Sensitive dependence on $N$ such as this should be carefully extrapolated out when optimizing mission-critical models.





### Introduction

There are two steps one must carry out to fit a machine-learning model. First, a specific model form and cost function must be selected, and second the model must be fit to the data. The first of these steps is often treated by making use of a training-test data split: One trains a set of candidate models to a fraction of the available data and then validates their performance using a hold-out, test set. The model that performs best on the latter is then selected for production.

Our purpose here is to highlight a subtlety to watch out for when carrying out an optimization as above: the fact that the optimal model can depend sensitively on training set size $N$. This observation suggests that the training-test split paradigm must sometimes be applied with care: Because a subsample is used for training in the first, selection step, the model identified as optimal there may not be best when training on the full data set.

To illustrate the above points, our main effort here is to present some toy examples where the optimal hyperparameters can be characterized exactly: We derive the optimal $L_1$ and $L_2$ regularization strength for models having only a single variable. These examples illustrate two opposite limits: The latter approaches a finite constant as $N$ increases, but the former varies exponentially with $N$. This shows that strong $N$-dependence can sometimes occur, but is not necessarily always an issue. In practice, a simple way to check for sensitivity is to vary the size of your training set during model selection: If a strong dependence is observed, care should be taken during the final extrapolation.

We now walk through our two examples.

### $L_2$ optimization

We start off by positing that we have a method for generating a Bayesian posterior for a parameter $\theta$ that is a function of a vector of $N$ random samples $\textbf{x}$. To simplify our discussion, we assume that -- given a flat prior -- this is unbiased and normal with variance $\sigma^2$. We write $\theta_0 \equiv \theta_0(\textbf{x})$ for the maximum a posteriori (MAP) value under the flat prior. With the introduction of an $L_2$ prior, the posterior for $\theta$ is then
$$\tag{1}
P\left(\theta \vert \theta_0(\textbf{x})\right) \propto \exp\left( - \frac{(\theta - \theta_0)^2}{2 \sigma^2} - \Lambda \theta^2 \right).
$$
Setting the derivative of the above to zero, the point-estimate, MAP is given by
$$\tag{2}
\hat{\theta} = \frac{\theta_0}{1 + 2 \Lambda \sigma^2}.
$$
The average squared error of this estimate is obtained by averaging over the possible $\theta_0$ values. Our assumptions above imply that $\theta_0$ is normal about the true parameter value, $\theta_*$, so we have
\begin{eqnarray}
\langle (\hat{\theta} - \theta_*)^2 \rangle &\equiv& \int_{\infty}^{\infty} \frac{1}{\sqrt{2 \pi \sigma^2}}
e^{ - \frac{(\theta_0 - \theta_*)^2}{2 \sigma^2}} \left ( \frac{\theta_0}{1 + 2 \Lambda \sigma^2} - \theta_* \right)^2 d \theta_0 \\
&=& \frac{ 4 \Lambda^2 \sigma^4 \theta_*^2 }{(1 + 2 \Lambda \sigma^2 )^2} + \frac{\sigma^2}{\left( 1 + 2 \Lambda \sigma^2 \right)^2}. \tag{3} \label{error}
\end{eqnarray}
The optimal $\Lambda$ is readily obtained by minimizing this average error. This gives,
$$ \label{result}
\Lambda = \frac{1}{2 \theta_*^2}, \tag{4}
$$
a constant, independent of sample size. The mean squared error with this choice is obtained by plugging (\ref{result}) into (\ref{error}). This gives
$$
\langle (\hat{\theta} - \theta_*)^2 \rangle = \frac{\sigma^2}{1 + \sigma^2 / \theta_*^2}. \tag{5}
$$
Notice that this is strictly less than $\sigma^2$ -- the variance one would get without regularization -- and that the benefit is largest when $\sigma^2 \gg \theta_*^2$. That is, $L_2$ regularization is most effective when $\theta_*$ is hard to differentiate from zero -- an intuitive result!

### $L_1$ optimization

The analysis for $L_1$ optimization is similar to the above, but slightly more involved. We go through it quickly. The posterior with an $L_1$ prior is given by
$$ \tag{6}
P\left(\theta \vert \theta_0(\textbf{x})\right) \propto \exp\left( - \frac{(\theta - \theta_0)^2}{2 \sigma^2} - \Lambda \vert \theta \vert \right).
$$
Assuming for simplicity that $\hat{\theta} > 0$, the MAP value is now
$$ \tag{7}
\hat{\theta} = \begin{cases}
\theta_0 - \Lambda \sigma^2 & \text{if } \theta_0 - \Lambda \sigma^2 > 0 \\
0 & \text{else}.
\end{cases}
$$
The mean squared error of the estimator is
$$ \tag{8}
\langle (\hat{\theta} - \theta_*)^2 \rangle \equiv \int \frac{1}{\sqrt{2 \pi \sigma^2}}
e^{ - \frac{(\theta_0 - \theta_*)^2}{2 \sigma^2}} \left ( \hat{\theta} - \theta_* \right)^2 d \theta_0.
$$
This can be evaluated in terms of error functions. The optimal value of $\Lambda$ is obtained by differentiating the above. Doing this, one finds that it satisfies the equation
$$ \tag{9}
e^{ - \frac{(\tilde{\Lambda}- \tilde{\theta_*})^2}{2} } + \sqrt{\frac{\pi}{2}} \tilde{\Lambda} \ \text{erfc}\left( \frac{\tilde{\Lambda} - \tilde{\theta_*}}{\sqrt{2}} \right ) = 0,
$$
where $\tilde{\Lambda} \equiv \sigma \Lambda$ and $\tilde{\theta_*} \equiv \theta_* / \sigma$. In general, the equation above must be solved numerically. However, in the case where $\theta_* \gg \sigma$ -- relevant when $N$ is large -- we can obtain a clean asymptotic solution. In this case, we have $\tilde{\theta_*} \gg 1$ and we expect $\Lambda$ small. This implies that the above equation can be approximated as
$$ \tag{10}
e^{ - \frac{\tilde{\theta_*}^2}{2} } - \sqrt{2 \pi} \tilde{\Lambda} \sim 0.
$$
Solving gives
\begin{eqnarray} \tag{11}
\Lambda \sim \frac{1}{\sqrt{2 \pi \sigma^2}} e^{ - \frac{\theta_*^2}{2 \sigma^2}} \sim \frac{\sqrt{N}}{\sqrt{2 \pi \sigma_1^2}} e^{ - \frac{N \theta_*^2}{2 \sigma_1^2}}.
\end{eqnarray}
Here, in the last line we have made the $N$-dependence explicit, writing $\sigma^2 = \sigma_1^2 / N$ -- a form that follows when our samples $\textbf{x}$ are independent. Whereas the optimal $L_2$ regularization strength approaches a constant, our result here shows that the optimal $L_1$ strength decays exponentially to zero as $N$ increases.

### Summary

The subtlety that we have discussed here is likely already familiar to those with significant applied modeling experience: optimal model hyperparameters can vary with training set size. However, the two toy examples we have presented are interesting in that they allow for this $N$ dependence to be derived explicitly. Interestingly, we have found that the MSE-minimizing $L_2$ regularization remains finite, even at large training set size, but the optimal $L_1$ regularization goes to zero in this same limit. For small and medium $N$, this exponential dependence represents a strong sensitivity to $N$ -- one that must be carefully taken into account when extrapolating to the full training set.

One can imagine many other situations where hyperparameters vary strongly with $N$. For example, very complex systems may allow for ever-increasing model complexity as more data becomes available. Again, in practice, the most straightforward method to check for this is to vary the size of the training set during model selection. If strong dependence is observed, this should be extrapolated out to obtain the truly optimal model for production.
