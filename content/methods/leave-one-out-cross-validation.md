Title: Leave-one-out cross-validation
Date: 2015-08-01 16:08
Author: jslandy
Category: Methods, Theory
Slug: leave-one-out-cross-validation
Status: published

This will be the first of a series of short posts relating to subject matter discussed in the text, ["An Introduction to Statistical Learning"](http://www-bcf.usc.edu/~gareth/ISL/). This is an interesting read, but it often skips over statement proofs -- that's where this series of posts comes in! Here, I consider the content of Section 5.1.2: This gives a lightning-quick "short cut" method for evaluating a regression's leave-one-out cross-validation error. The method is applicable to any least-squares linear fit.

  
[Follow @efavdb](http://twitter.com/efavdb)  
Follow us on twitter for new submission alerts!

### Introduction: Leave-one-out cross-validation

When carrying out a [regression analysis](https://en.wikipedia.org/wiki/Regression_analysis), one is often interested in two types of error measurement. The first is the training set error and the second is the generalization error. The former relates to how close the regression is to the data being fit. In contrast, the generalization error relates to how accurate the model will be when applied to other points. The latter is of particular interest whenever the regression will be used to make predictions on new points.

[Cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)) provides one method for estimating generalization errors. The approach centers around splitting the training data available into two sets, *a cross-validation training set* and *cross-validation test set*. The first of these is used for training a regression model. Its accuracy on the test set then provides a generalization error estimate. Here, we focus on a special form of cross-validation, called *leave-one-out cross-validation* (LOOCV). In this case, we pick only one point as the test set. We then build a model on all the remaining, complementary points, and evaluate its error on the single-point held out. A generalization error estimate is obtained by repeating this procedure for each of the training points available, averaging the results.

LOOCV can be computationally expensive because it generally requires one to construct many models -- equal in number to the size of the training set. However, for the special case of least-squares polynomial regression we have the following "short cut" identity:  
$$ \label{theorem} \tag{1}  
\sum_i \left ( \tilde{y}_i - y_i\right)^2 = \sum_i \left ( \frac{\hat{y}_i - y_i}{1 - h_i}\right)^2.  
$$  
Here, $y_i$ is the actual label value of training point $i$, $\tilde{y}_i$ is the value predicted by the cross-validation model trained on all points except $i$, $\hat{y}_i$ is the value predicted by the regression model trained on all points (including point $i$), and $h_i$ is a function of the coordinate $\vec{x}_i$ -- this is defined further below. Notice that the left side of (\ref{theorem}) is the LOOCV sum of squares error (the quantity we seek), while the right can be evaluated given only the model trained on the full data set. Fantastically, this allows us to evaluate the LOOCV error using only a single regression!

### Statement proof

Consider the LOOCV step where we construct a model trained on all points except training example $k$. Using a linear model of form $\tilde{y}(\vec{x}) \equiv \vec{x}^T \cdot \vec{\beta}_k$ -- with $\vec{\beta}_k$ a coefficient vector -- the sum of squares that must be minimized is  
$$\tag{2} \label{error_sum}  
J_k \equiv \sum_{i \not = k} \left ( \tilde{y}_i - y_i \right)^2 = \sum_{i \not = k} \left (\vec{x}^T_i \cdot \vec{\beta}_k - y_i \right)^2.  
$$  
Here, we're using a subscript $k$ on $\vec{\beta}_k$ to highlight the fact that the above corresponds to the case where example $k$ is held out. We minimize (\ref{error_sum}) by taking the gradient with respect to $\vec{\beta}_k$. Setting this to zero gives the equation  
$$\tag{3}  
\left( \sum_{i \not = k} \vec{x}_i \vec{x}_i^T \right) \cdot \vec{\beta}_k = \sum_{i \not = k} y_i \vec{x}_i.  
$$  
Similarly, the full model (trained on all points) coefficient vector $\vec{\beta}$ satisfies  
$$\tag{4} \label{full_con}  
\left( \sum_{i} \vec{x}_i \vec{x}_i^T \right) \cdot \vec{\beta} \equiv M \cdot \vec{\beta} = \sum_{i} y_i \vec{x}_i.  
$$  
Combining the prior two equations gives,  
$$\tag{5}  
\left (M - \vec{x}_k \vec{x}_k^T \right) \cdot \vec{\beta}_k = \left (\sum_{i} y_i \vec{x}_i\right) - y_k \vec{x}_k = M\cdot \vec{\beta} - y_k \vec{x}_k.  
$$  
Using the definition of $\tilde{y}_k$, rearrangement of the above leads to the identity  
$$\tag{6}  
M \cdot \left ( \vec{\beta}_k - \vec{\beta} \right) = \left (\tilde{y}_k - y_k \right) \vec{x}_k.  
$$  
Left multiplication by $\vec{x}_k^T M^{-1}$ gives,  
$$\tag{7}  
\tilde{y}_k - \hat{y}_k = \left( \tilde{y}_k - y_k\right) - \left( \hat{y}_k - y_k \right) = \vec{x}_k^T M^{-1} \vec{x}_k \left (\tilde{y}_k - y_k \right).  
$$  
Finally, combining like-terms, squaring, and summing gives  
$$\tag{8}  
\sum_k \left (\tilde{y}_k - y_k \right) ^2 = \sum_k \left (\frac{\hat{y}_k - y_k}{1 -\vec{x}_k^T M^{-1} \vec{x}_k } \right)^2.  
$$  
This is (\ref{theorem}), where we now see the parameter $h_k \equiv \vec{x}_k^T M^{-1} \vec{x}_k$. This is referred to as the "leverage" of $\vec{x}_k$ in the text. Notice also that $M$ is proportional to the correlation matrix of the $\{\vec{x}_i\}$. $\blacksquare$
