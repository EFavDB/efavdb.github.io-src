Title: linselect
Date: 2018-04-28 07:59
Author: jslandy
Slug: linselect
Layout: pages
Status: hidden

*A fast, flexible, and performant feature selection package for python.*

Welcome! This page contains an FAQ and links to a running list of tutorials for `linselect` -- a python feature selection package built on top of the *efficient stepwise linear regression algorithm*.

Tutorials
---------

-   [linselect demo: a tech sector stock analysis](http://efavdb.com/linselect-demo)
    In this post, we demonstrate `linselect`'s basic API by exploring the relationship between the daily percentage lifts of 50 tech stocks over one trading year. We will be interested in identifying minimal stock subsets that can be used to predict the lifts of the others.

FAQ
---

-   **Where can I download the package?**
    *Answer*: Instructions can be found on our GitHub, [here](https://github.com/efavdb/linselect). The `README.md` file contains some helpful background, and the `docs` folder contains doc-strings and some basic API examples.
-   **What is a target, a feature, a predictor set?**  
    *Answer*: These are terms I use to refer to variables in a data set. For example, if we're trying to fit a variable $y$ using some components of a vector of variables $\textbf{x}$, I'd refer to $y$ as the target and the components of $\textbf{x}$ as the features. If a feature is actually used in the model, I say it is in the "predictor set".
-   **Why do we sometimes call a feature a column?**  
    *Answer*: The feature data we pass into `linselect` must take the form of an $m \times n$ array. The columns of this array correspond to the different features and the rows to different samples from their distribution.
-   **What is feature selection?**  
    *Answer*: Roughly speaking, the typical goal of feature selection is to identify a minimal set of features in a given data set that retain all or most of the predictive power of the full data set. Removing the other features can help us be more memory efficient, and it can also improve model performance and training times. Identifying which features are most important in a given problem can also provide useful insight.
-   **What is stepwise selection?**  
    *Answer*: This is one approach to feature selection wherein one tracks the performance of a model as features are added or removed from its predictor set. Typically, in a forward step one adds to the model that feature not currently used that best improves the model. In a reverse step, you do the opposite: Remove that feature from the predictor set that results in the least drop in performance. This process pushes us towards a feature set exhibiting maximal predictive power and minimal redundancy. You can take this approach using any kind of model, but linear models are special because the process can be made to run very fast.
-   **What if my problem is not linear?**  
    *Answer*: It depends. In my work, I often find that the linear selection methods used here are sufficient: I can use `linselect` to pick a good feature set, and then plug this into a production, non-linear model, e.g., a random forest -- with the end result being a more lean feature set that is as predictive as the original.

    However, there are certainly non-linear problems out there where a linear tool cannot be used to identify the most important features. In such cases, I'd try: (1) Building non-linear features ahead of time (e.g., polynomial features), then using `linselect` on these, or (2) using a non-linear method. The downside with non-linear methods is that they are usually much slower. The trick that allows linear fits to go so fast is really a fundamental miracle that we should all appreciate and take advantage of, IMHO.

-   **Any gotchas?**  
    *Answer*: The algorithm requires *numerical* data! If there are any nans, strings, Boolean's etc., it will cause the fits to fail -- often after taking some time to attempt to evaluate the data correlation matrix. Pre-clean your data!

