Title: Machine Learning Methods: Classification without negative examples
Date: 2014-12-20 09:58
Author: Jonathan Landy
Category: Methods, Theory
Tags: methods
Slug: methods-regression-without-negative-examples
Status: published
Attachments: wp-content/uploads/2014/12/plot.jpg, wp-content/uploads/2014/12/plot1.jpg

Here, we discuss some methods for carrying out classification when only positive examples are available. The latter half of our discussion borrows heavily from W.S. Lee and B. Liu, Proc. ICML-2003 (2003), which we supplement somewhat.  

[Follow @efavdb](http://twitter.com/efavdb)  

Follow us on twitter for new submission alerts!

**I. Generic logistic regression.**  
[Logistic regression](http://en.wikipedia.org/wiki/Logistic_regression) is a commonly used tool for estimating the level sets of a Boolean function $y$ on a set of feature vectors $\textbf{F}$: In a sense, you can think of it as a method for playing the game \`\`Battleship" on whatever data set you're interested in. Its application requires knowledge of the $\{(\textbf{f}_i,y_i)\}$ pairs on a training set $\textbf{E} \subseteq \textbf{F}$, with label $y_i = 0,1$ for negative and positive examples, respectively. Given these training examples, logistic regression estimates for arbitrary feature vector $\textbf{f}$,  
$$ h(\textbf{f}) = \frac{1}{1 + \exp \left [ - \textbf{T} \cdot \textbf{f} \right]} \approx y, $$where the coefficient vector $\textbf{T}$ is taken to be that vector that minimizes  
$$ J(h) \equiv -\frac{1}{\vert \textbf{E} \vert}\sum_{i=1}^{\vert \textbf{E} \vert} y_i \log(h_i) + (1-y_i) \log(1- h_i) + \frac{\Lambda}{2}\sum_j T_j^2, $$ a convex cost function that strongly penalizes poor estimates on the training set.

**II. Problem statement: no negative examples.**  
Consider now a situation where all training examples given are positive -- i.e., no negative examples are available. One realistic realization of this scenario might involve a simple data set of movies already viewed by some Netflix customer. From this information, one would like to estimate the full subset of the available movies that the customer would watch, given time. We'll assign value $y = 1$ to such movies and $y=0$ to movies he wouldn't watch. Notice that the generic logistic regression approach outlined above would return a default-positive result if applied to this problem: Assigning $h = 1$ to all of $\textbf{F}$ minimizes $J$. This means that no information contained in $\textbf{E}$ is actually utilized in the logistic learning process -- a counterintuitive choice for structured $\textbf{E}$ (e.g., the case where all movies watched thus far have been in a single category -- martial arts films, say).

**III. Noisy labeling.**  
Some reasonable, alternative approaches do not return the default-positive response in the situation above. To see this, we first review here noisy labeling problems. Suppose we are given a training set with noisy labeling $y^{\prime}$: Truly-positive examples $(y = 1)$ are stochastically mislabeled in this set with frequency $\alpha$ as negative $(y^{\prime} = 0)$, and truly-negative examples $(y=0)$ are mislabeled with frequency $\beta$ as positive $(y^{\prime} = 1)$. For hypothesis $h$, let $$C(h) = Pr[h = 0 \vert y = 1]+ Pr[h = 1 \vert y= 0],$$ the rate at which $h$ mislabels positive examples in the training set added to the rate at which it mislabels negative examples. Similarly, we define $C^{\prime}(h)$ as above, but with $y$ replaced by $y^{\prime}$. Because $y^{\prime}$ is stochastic, we also average it in this case, giving $$C^{\prime}(h) = \left \langle Pr[h = 0 \vert y^{\prime} = 1]+ Pr[h = 1 \vert y^{\prime}= 0] \right \rangle_{y^{\prime}}.$$ With these definitions, we have [see Blum and Michael (1998) or derive yourself] $$ C(h) \propto C^{\prime}(h),$$ with $\text{sign}(C) = \text{sign}(1 - \alpha - \beta) \times \text{sign}(C^{\prime})$. This result is very useful whenever we take $C(h)$ as our cost function$^1$: Provided the total noise rate $\alpha + \beta <1$, it implies that we can find the \`\`$C$-optimizing" $h$ within any class of hypotheses by optimizing instead $C^{\prime}$ -- a quantity that we can estimate given any particular noisy labeling realization $y^{\prime}_0$ as $$C^{\prime}(h) \approx \left (Pr[h = 0 \vert y^{\prime} = 1]+ Pr[h = 1 \vert y^{\prime}= 0] \right ) \vert_{y^{\prime} =y^{\prime}_0}.$$

**IV. Application to no-negatives problem.**  
To make connection between the no-negatives and noisy-labeling problems, one can remodel the former as one where all unlabeled examples are considered to actually be negative examples ($y^{\prime}_0 = 0$). This relabeling gives a correct label to all examples in the original training set $\textbf{E}$ (where $y = y^{\prime}_0 = 1$) as well as to all truly-negative examples (where $y = y^{\prime}_0 = 0$). However, all positive examples not in $\textbf{E}$ are now incorrectly labeled (they are assigned $y^{\prime}_0 = 0$): This new labeling $y^{\prime}_0$ is noisy, with $\alpha = Pr(y^{\prime}_0 =0 \vert y =1)$ and $\beta = Pr(y^{\prime}_0 =1 \vert y = 0 ) = 0$. We can now apply the Blum and Michael approach: We first approximate $C^{\prime}$ as above, making use of the particular noisy label we have access to. Second, we minimize the approximated $C^{\prime}$ over some class of hypotheses $\{h\}$. This will in general return a non-uniform hypothesis (i.e., one that now makes use of the information contained in $\textbf{E}$).

**V. Hybrid noisy-logistic approach of Lee and Liu (plus a tweak).**  
The $C \propto C^{\prime}$ result is slick and provides a rigorous method for attacking the no-negatives problem. Unfortunately, $C^{\prime}$ is not convex, and as a consequence it can be difficult to minimize for large $\vert \textbf{F} \vert$ -- in fact, its minimization is NP-hard. To mitigate this issue, Lee and Liu combine the noisy relabeling idea -- now well-motivated by the Blum and Michael analysis -- with logistic regression. They also suggest a particular re-weighting of the observed samples. However, we think that their particular choice of weighting is not very well-motivated, and we suggest here that one should instead pick an optimal weighting through consideration of a cross-validation set. With this approach, the method becomes:

​1) As above, assign examples in $\textbf{E}$ label $y^{\prime} = 1$ and examples in $\textbf{F} - \textbf{E}$ label $y^{\prime} = 0$.  
2) Construct the weighted logistic cost function $$ J(h; \rho) \equiv -\frac{1}{\vert \textbf{E} \vert}\sum_{i=1}^{\vert \textbf{E} \vert}  
\rho y^{\prime}_i \log(h_i) + (1-\rho) (1-y^{\prime}_i) \log(1- h_i) + \frac{\Lambda}{2}\sum_j T_j^2, $$ with $\rho \in [0,1]$, a re-weighting factor. (Lee and Liu suggest$^2$ using $\rho = 1-\frac{\vert \textbf{E} \vert}{\vert \textbf{F} \vert}$).  
3) Minimize $J$. By evaluating performance on a cross-validation set using your favorite criteria, optimize $\rho$ and $\Lambda$.

**V. Toy example.**  
Here, we provide a toy system that allows for a sense of how the latter method discussed above works in practice. Given is a set of $60$ grid points in the plane, which can be added/subtracted individually to the positive training set ($\textbf{E}$, green fill) by mouse click (a few are selected by default). The remaining points are considered to not be in the training set, but are relabeled as negative examples -- this introduces noise, as described above. Clicking compute returns the $h$ values for each grid point, determined by minimizing the weighted cost function $J$ above: Here, we use the features $\{1,x,y,x^2,xy,$ $y^2,x^3, x^2 y,$ $x y^2, y^3\}$ to characterize each point. Those points with $h$ values larger than $0.5$ (i.e., those the hypothesis estimates as positive) are outlined in black. We have found that by carefully choosing the $\rho$ and $\Lambda$ values (often to be large and small, respectively), one can get a good fit to most training sets. By eye, the optimal weighting seems to often be close -- but not necessarily equal to -- the value suggested by Lee and Liu.

Your browser does not support the canvas tag.

</p>  
<p>JavaScript is required to view the contents of this page.</p>  
<p>

*Fig. 1: Interactive weighted noisy-no-negatives solver. Click \`\`compute" to run logistic regression.*

**V. Discussion.**  
In this note, we have discussed methods for tackling classification sans negative examples -- a problem that we found perplexing at first sight. It is interesting that standard logistic regression returns a default-positive result for such problems, while the two latter methods we discussed here are based on assuming that all points in $\textbf{F} - \textbf{E}$ are negatives. In fact, this assumption seems to be the essence of all the other methods referenced in Lee and Liu's paper. Ultimately, these methods will only work if the training set provides a good sampling of the truly-positive space. If this is the case, then \`\`defocusing" a bit, or blurring one's eyes, will give a good sense of where the positive space sits. In the noisy-logistic approach, a good choice of $\rho$ and $\Lambda$ should effect a good result. Of course, when the training set does not sample the full positive space well, one can still use this approach to get a good approximation for the outline of the subspace sampled.

**Footnotes:**  
$[1]$: The target function $y$ provides the unique minimum of $C$. Therefore, choosing $C$ as our cost function and minimizing it over some class of hypotheses $\{h\}$ should return a reasonable estimate for $y$ (indeed, if $y$ is in the search class, we will find it).

$[2]$: Lee and Liu justify their weighting suggestion on the basis that it means that a randomly selected positive example contributes with expected weight $>0.5$ (see their paper). Yet, other weighting choices give even larger expected weights to the positive examples, so this is a poor justification. Nevertheless, their weighting choice does have the nice feature that the positive and negative spaces are effectively sampled with equal frequency. If optimizing over $\rho$ is too resource-costly for some application, using their weighting suggestion may be reasonable for this reason.
