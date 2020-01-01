Title: Normal Distributions
Date: 2017-05-13 21:48
Author: Jonathan Landy
Category: Review, Statistics, Theory
Slug: normal-distributions
Status: published
Attachments: wp-content/uploads/2017/05/carl-f-gauss-4.jpg

I review -- and provide derivations for -- some basic properties of Normal distributions. Topics currently covered: (i) Their normalization, (ii) Samples from a univariate Normal, (iii) Multivariate Normal distributions, (iv) Central limit theorem.

  
[Follow @efavdb](http://twitter.com/efavdb)  
Follow us on twitter for new submission alerts!

### Introduction

[![carl-f-gauss-4]({static}/wp-content/uploads/2017/05/carl-f-gauss-4.jpg)]({static}/wp-content/uploads/2017/05/carl-f-gauss-4.jpg)

This post contains a running list of properties (with derivations) relating to Normal (Gaussian) distributions. Normal distributions are important for two principal reasons: Their significance a la the central limit theorem and their appearance in saddle point approximations to more general integrals. As usual, the results here assume familiarity with calculus and linear algebra.

Pictured at right is an image of Gauss -- \`\`Few, but ripe."

### Normalization

-   Consider the integral  
    \begin{eqnarray} \tag{1}  
    I = \int_{-\infty}^{\infty} e^{-x^2} dx.  
    \end{eqnarray}  
    To evaluate, consider the value of $I^2$. This is  
    \begin{eqnarray}\tag{2}  
    I^2 &=& \int_{-\infty}^{\infty} e^{-x^2} dx \int_{-\infty}^{\infty} e^{-y^2} dy \\  
    &=& \int_0^{\infty} e^{-r^2} 2 \pi r dr = -\pi e^{-r^2} \vert_0^{\infty} = \pi.  
    \end{eqnarray}  
    Here, I have used the usual trick of transforming the integral over the plane to one over polar $(r, \theta)$ coordinates. The result above gives the normalization for the Normal distribution.

### Samples from a univariate normal

-   Suppose $N$ independent samples are taken from a Normal distribution. The sample mean is defined as $\hat{\mu} = \frac{1}{N}\sum x_i$ and the sample variance as $\hat{S}^2 \equiv \frac{1}{N-1} \sum (x_i - \hat{\mu})^2$. These two statistics are independent. Further, the former is Normal distributed with variance $\sigma^2/N$ and the latter is proportional to a $\chi_{N-1}^2.$

    *Proof:* Let the sample be $\textbf{x} = (x_1, x_2, \ldots, x_N)$. Then the mean can be written as $\textbf{x} \cdot \textbf{1}/N$, the projection of $\textbf{x}$ along $\textbf{1}/N$. Similarly, the sample variance can be expressed as the squared length of $\textbf{x} - (\textbf{x} \cdot \textbf{1} / N)\textbf{1} = \textbf{x} - (\textbf{x} \cdot \textbf{1} / \sqrt{N})\textbf{1}/\sqrt{N}$, which is the squared length of $\textbf{x}$ projected into the space orthogonal to $\textbf{1}$. The independence of the $\{x_i\}$ implies that these two variables are themselves independent, the former Normal and the latter $\chi^2_{N-1}.$

-   The result above implies that the weight for sample $\textbf{x}$ can be written as  
    \begin{eqnarray} \tag{3}  
    p(\textbf{x} \vert \mu, \sigma^2) = \frac{1}{(2 \pi \sigma^2)^{N/2}} \exp\left [ - \frac{1}{2 \sigma^2}\left ( - N (\hat{\mu} - \mu)^2 - (N-1)S^2\right) \right].  
    \end{eqnarray}
-   Aside on sample variance: Given independent samples from any distribution, dividing by $N-1$ gives an unbiased estimate for the population variance. However, if the samples are not independent (eg, direct trace from MCMC), this factor is not appropriate: We have  
    \begin{eqnarray} \nonumber  
    (N-1)E(S^2) = E(\sum (x_i - \overline{x})^2)  
    &=& E(\sum (x_i - \mu)^2 - N ( \overline{x} - \mu)^2 ) \\ \tag{4}  
    &=& N [\sigma^2 - \text{var}(\overline{x})] \label{sample_var}  
    \end{eqnarray}  
    If the samples are independent, the above gives $(N-1) \sigma^2$. However, if the samples are all the same, $\text{var}(\overline{x}) = \sigma^2$, giving $S^2=0$. In general, the relationship between the samples determines whether $S^2$ is biased or not.
-   From the results above, the quantity  
    \begin{eqnarray} \label{t-var} \tag{5}  
    (\hat{\mu}- \mu)/(S/\sqrt(N))  
    \end{eqnarray}  
    is the ratio of two independent variables -- the numerator a Normal and the denominator the square root of an independent $\chi^2_{N-1}$ variable. This quantity follows a universal distribution called the $t$-distribution. One can write down closed-form expressions for the $t$. For example, when $N=2$, you get a Cauchy variable: the ratio of one Normal over the absolute value of another, independent Normal (see above). In general, $t$-distributions have power law tails. A key point is that we cannot evaluate (\ref{t-var}) numerically if we do not know $\mu$. Nevertheless, we can use the known distribution of the above to specify its likely range. Using this, we can then construct a confidence interval for $\mu$.
-   Consider now a situation where you have two separate Normal distributions. To compare their variances you can take samples from the two and then construct the quantity  
    \begin{eqnarray}\label{f-var} \tag{6}  
    \frac{S_x / \sigma_x}{ S_y/ \sigma_y}.  
    \end{eqnarray}  
    This is the ratio of two independent $\chi^2$ variables, resulting in what is referred to as an $F$-distributed variable. Like (\ref{t-var}), we often cannot evaluate (\ref{f-var}) numerically. Instead, we use a tabulated cdf of the $F$-distribution to derive confidence intervals for the ratio of the two underlying variances. Aside: The $F$-distribution arises in the analysis of both ANOVA and linear regression. Note also that the square of a $t$-distributed variable (Normal over the square root of a $\chi^2$ variable) is $F$-distributed.

### Multivariate Normals

-   Consider a set of jointly-distributed variables $x$ having normal distribution  
    \begin{eqnarray} \tag{7}  
    p(x) = \sqrt{\frac{ \text{det}(M)} {2 \pi}} \exp \left [- \frac{1}{2} x^T \cdot M \cdot x \right ],  
    \end{eqnarray}  
    with $M$ a real, symmetric matrix. The correlation of two components is given by  
    \begin{eqnarray}\tag{8}  
    \langle x_i x_j \rangle = M^{-1}_{ij}.  
    \end{eqnarray}  
    *Proof:* Let  
    \begin{eqnarray}\tag{9}  
    I = \int dx \exp \left [- \frac{1}{2} x^T \cdot M \cdot x \right ].  
    \end{eqnarray}  
    Then,  
    \begin{eqnarray}\tag{10}  
    \partial_{M_{ij}} \log I = -\frac{1}{2} \langle x_i x_j \rangle.  
    \end{eqnarray}  
    We can also evaluate this using the normalization of the integral as  
    \begin{eqnarray} \nonumber  
    \partial_{M_{ij}} \log I &=& - \frac{1}{2} \sum_{\alpha} \frac{1}{\lambda_{\alpha}} \partial_{M_{ij}} \lambda_{\alpha} \\ \nonumber  
    &=& - \frac{1}{2} \sum_{\alpha} \frac{1}{\lambda_{\alpha}} v_{\alpha i } v_{\alpha j} \\  
    &=& - \frac{1}{2} M^{-1}_{ij}. \tag{11}  
    \end{eqnarray}  
    Here, I've used the result $ \partial_{M_{ij}} \lambda_{\alpha} = v_{\alpha i } v_{\alpha j}$. I give a proof of this next. The last line follows by expressing $M$ in terms of its eigenbasis. Comparing the last two lines above gives the result.
-   Consider a matrix $M$ having eigenvalues $\{\lambda_{\alpha}\}$. The first derivative of $\lambda_{\alpha}$ with respect to $M_{ij}$ is given by $v_{\alpha, i} v_{\alpha, j}$, where $v_{\alpha}$ is the unit eigenvector corresponding to the eigenvalue $\lambda_{\alpha}$.

    *Proof:* The eigenvalue in question is given by  
    \begin{eqnarray} \tag{12}  
    \lambda_{\alpha} = \sum_{ij} v_{\alpha i} M_{ij} v_{\alpha j}.  
    \end{eqnarray}  
    If we differentiate with respect to $M_{ab}$, say, we obtain  
    \begin{eqnarray} \nonumber  
    \partial_{M_{ab}} \lambda_{\alpha} &=& \sum_{ij} \delta_{ia} \delta_{jb} v_{\alpha i} v_{\alpha j} + 2 v_{\alpha i} M_{ij} \partial_{M_{ab}} v_{\alpha j} \\  
    &=& v_{\alpha a} v_{\alpha b} + 2 \lambda_{\alpha} v_{\alpha } \cdot \partial_{M_{ab}} v_{\alpha }  
    \tag{13}.  
    \end{eqnarray}  
    The last term above must be zero since the length of $v_{\alpha }$ is fixed at $1$.

-   The conditional distribution. Let $x$ be a vector of jointly distributed variables of mean zero and covariance matrix $\Sigma$. If we segment the variables into two sets, $x_0$ and $x_1$, the distribution of $x_1$ at fixed $x_0$ is also normal. Here, we find the mean and covariance. We have  
    \begin{eqnarray} \label{multivargaucond} \tag{14}  
    p(x) = \mathcal{N} \exp \left [ -\frac{1}{2} x_0^T \Sigma^{-1}_{00} x_0\right] \exp \left [ -\frac{1}{2} \left \{ x_1^T \Sigma^{-1}_{11} x_1 + 2 x_1^T \Sigma^{-1}_{10} x_0 \right \} \right]  
    \end{eqnarray}  
    Here, $\Sigma^{-1}_{ij}$ refers to the $i-j$ block of the inverse. To complete the square, we write  
    \begin{eqnarray} \tag{15}  
    x_1^T \Sigma^{-1}_{11} x_1 + 2 x_1^T \Sigma^{-1}_{10} x_0 + c = (x_1^T + a) \Sigma^{-1}_{11} ( x_1 + a).  
    \end{eqnarray}  
    Comparing both sides, we find  
    \begin{eqnarray} \tag{16}  
    x_1^T \Sigma^{-1}_{10} x_0 = x_1^T \Sigma^{-1}_{11} a  
    \end{eqnarray}  
    This holds for any value of $x_1^T$, so we must have  
    \begin{eqnarray}\tag{17}  
    a = \left( \Sigma^{-1}_{11} \right)^{-1} \Sigma^{-1}_{10} x_0 .  
    \end{eqnarray}  
    Plugging the last few results into (\ref{multivargaucond}), we obtain  
    \begin{eqnarray} \nonumber  
    p(x) = \mathcal{N} \exp \left [ -\frac{1}{2} x_0^T \left( \Sigma^{-1}_{00} -  
    \Sigma^{-1}_{01} \left( \Sigma^{-1}_{11} \right)^{-1} \Sigma^{-1}_{10} \right) x_0\right] \\ \times  
    \exp \left [ -\frac{1}{2} \left (x_1 + \left( \Sigma^{-1}_{11} \right)^{-1} \Sigma^{-1}_{10} x_0 \right) \Sigma^{-1}_{11} \left (x_1 + \left( \Sigma^{-1}_{11} \right)^{-1} \Sigma^{-1}_{10} x_0 \right) \right ] \tag{18} \label{multivargaucondfix}  
    \end{eqnarray}  
    This shows that $x_0$ and $x_1 + \left( \Sigma^{-1}_{11} \right)^{-1} \Sigma^{-1}_{10} x_0 $ are independent. This formula also shows that the average value of $x_1$ shifts at fixed $x_0$,  
    \begin{eqnarray}\tag{19}  
    \langle x_1 \rangle = \langle x_1 \rangle_0 - \left( \Sigma^{-1}_{11} \right)^{-1} \Sigma^{-1}_{10} x_0.  
    \end{eqnarray}  
    With some work, we can rewrite this as  
    \begin{eqnarray} \tag{20}  
    \langle x_1 \rangle = \langle x_1 \rangle_0 + \Sigma_{10} \frac{1}{\Sigma_{00}}x_0.  
    \end{eqnarray}  
    There are two ways to prove this equivalent form holds. One is to make use of the expression for the inverse of a block matrix. The second is to note that the above is simply the linear response to a shift in $x_0$ -- see post on linear regression.
-   If we integrate over $x_1$ in (\ref{multivargaucondfix}), we obtain the distribution for $x_0$. This is  
    \begin{eqnarray} \tag{21}  
    p(x_0) = \mathcal{N} \exp \left [ -\frac{1}{2} x_0^T \left( \Sigma^{-1}_{00} -  
    \Sigma^{-1}_{01} \left( \Sigma^{-1}_{11} \right)^{-1} \Sigma^{-1}_{10} \right) x_0\right]  
    \end{eqnarray}  
    The block-diagonal inverse theorem can be used to show that this is equivalent to  
    \begin{eqnarray} \tag{22}  
    p(x_0) = \mathcal{N} \exp \left [ -\frac{1}{2} x_0^T \left( \Sigma_{00} \right)^{-1} x_0\right]  
    \end{eqnarray}  
    Another way to see this is correct is to make use of the fact that the coefficient matrix in the normal is the inverse of the correlation matrix. We know that after integrating out the values of $x_1$, we remain normal, and the covariance matrix will simply be given by that for $x_0$.
-   The covariance of the CDF transform in multivariate case -- a result needed for fitting Gaussian Copulas to data: Let $x_1, x_2$ be jointly distributed Normal variables with covariance matrix  
    \begin{eqnarray}  
    C = \left( \begin{array}{cc}  
    1 & \rho \\  
    \rho & 1  
    \end{array} \right)  
    \end{eqnarray}  
    The CDF transform of $x_i$ is defined as  
    \begin{eqnarray}  
    X_i \equiv \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x_i} \exp\left( -\frac{\tilde{x}_i^2}{2} \right)d\tilde{x}_i.  
    \end{eqnarray}  
    Here, we'll calculate the covariance of $X_1$ and $X_2$. Up to a constant that does not depend on $\rho$, this is given by the integral  
    \begin{eqnarray}  
    J \equiv \frac{1}{\sqrt{(2 \pi)^2 \text{det} C}} \int d\vec{x} \exp\left( -\frac{1}{2} \vec{x} \cdot C^{-1} \cdot \vec{x} \right)  
    \frac{1}{2 \pi} \int_{-\infty}^{x_1}\int_{-\infty}^{x_2} \exp\left( -\frac{\tilde{x}_1^2}{2} -\frac{\tilde{x}_2^2}{2} \right)d\tilde{x}_1 d\tilde{x}_2.  
    \end{eqnarray}  
    To progress, we first write  
    \begin{eqnarray}  
    \exp\left( -\frac{\tilde{x}_i^2}{2} \right ) = \frac{1}{\sqrt{2\pi }}\int \exp \left (- \frac{1}{2} k_i^2 + i k \tilde{x}_i \right )  
    \end{eqnarray}  
    We will substitute this equation into the prior line and then integrate over the $\tilde{x}_i$ using the result  
    \begin{eqnarray}  
    \int_{-\infty}^{x_i} \exp \left ( i k \tilde{x}_i \right ) d \tilde{x}_i = \frac{e^{i k_i x_i}}{i k_i}.  
    \end{eqnarray}  
    This gives  
    \begin{eqnarray}  
    J = \frac{-1}{(2 \pi)^3 \sqrt{\text{det} C} } \int_{k_1} \int_{k_2} \frac{e^{-\frac{1}{2} (k_1^2 + k_2^2)}}{k_1 k_2}  
    \int d\vec{x} \exp\left( -\frac{1}{2} \vec{x} \cdot C^{-1} \cdot \vec{x} + i \vec{k} \cdot \vec{x} \right)  
    \end{eqnarray}  
    The integral on $\vec{x}$ can now be carried out by completing the square. This gives  
    \begin{eqnarray}  
    J = \frac{1}{(2 \pi)^2} \int_{k_1} \int_{k_2} \frac{1}{k_1 k_2}  
    \exp\left( -\frac{1}{2} \vec{k} \cdot (C + I) \cdot \vec{k} \right)  
    \end{eqnarray}  
    We now differentiate with respect to $\rho$ to get rid of the $k_1 k_2$ in the denominator. This gives  
    \begin{eqnarray} \nonumber  
    \partial_{\rho} J &=& \frac{1}{(2 \pi)^2} \int_{k_1} \int_{k_2}  
    \exp\left( -\frac{1}{2} \vec{k} \cdot (C + I) \cdot \vec{k} \right) \\ \nonumber  
    &=& \frac{1}{2 \pi } \frac{1}{\sqrt{\text{det}(C + I)}} \\  
    &=& \frac{1}{4 \pi } \frac{1}{\sqrt{1 - \frac{\rho^2}{4}}}.  
    \end{eqnarray}  
    The last step is to integrate with respect to $\rho$, but we will now switch back to the original goal of calculating the covariance of the two CDF transforms, $P$, rather than $J$ itself. At $\rho = 0$, we must have $P(\rho=0) = 0$, since the transforms will also be uncorrelated in this limit. This gives  
    \begin{eqnarray} \nonumber  
    P &=& \int_0^{\rho} \frac{1}{4 \pi } \frac{1}{\sqrt{1 - \frac{\rho^2}{4}}} d \rho \\  
    &=& \frac{1}{2 \pi } \sin^{-1} \left( \frac{\rho}{2} \right). \tag{23}  
    \end{eqnarray}  
    Using a similar calculation, we find that the diagonal terms of the CDF covariance matrix are $1/12$.

### Central Limit Theorem

-   Let $x_1, x_2, \ldots, x_N$ be IID random variables with an mgf that exists near $0$. Let $E(x_i) = \mu$ and $\text{var}(x_i) = \sigma^2$. Then the variable $\frac{\overline{x} - \mu}{\sigma / \sqrt{N}}$ approaches standard normal as $N \to \infty$.

    *Proof:* Let $y_i =\frac{x_i - \mu}{\sigma}$. Then,  
    \begin{eqnarray}\tag{24}  
    \tilde{y} \equiv \frac{\overline{x} - \mu}{\sigma / \sqrt{N}} = \frac{1}{\sqrt{N}} \sum_i y_i.  
    \end{eqnarray}  
    Using the fact that the mgf of a sum of independent variables is given by the product of their mgfs, the quantity at left is  
    \begin{eqnarray} \tag{25}  
    m_{\tilde{y}}(t) = \left [ m_{y}\left (\frac{t}{\sqrt{N}} \right) \right]^n.  
    \end{eqnarray}  
    We now expand the term in brackets using a Taylor series, obtaining  
    \begin{eqnarray} \tag{26}  
    m_{\tilde{y}}(t) = \left [1 + \frac{t^2}{2 N } + O\left (\frac{t^3}{ N^{3/2}} \right) \right]^N \to \exp\left ( \frac{t^2}{2} \right),  
    \end{eqnarray}  
    where the latter form is the fixed $t$ limit as $N \to \infty$. This is the mgf for a $N(0,1)$ variable, proving the result.

-   One can get a sense of the accuracy of the normal approximation at fixed $N$ through consideration of higher moments. For example, if we have an even distribution with mgf $1 + x^2 /2 + (1 + \kappa^{\prime}) x^4 / 8 + \ldots$. Then the mgf for the scaled average above will be  
    \begin{eqnarray}\nonumber  
    m_{\tilde{y}} &=& \left [1 + \frac{t^2}{2 N } + \frac{(1 + \kappa^{\prime}) t^4}{8 N^2 } + \ldots \right]^N \\  
    &=& 1 + \frac{t^2}{2} + \left (1 + \frac{\kappa^{\prime}}{ N } \right) \frac{t^4}{8} + \ldots \tag{27}  
    \end{eqnarray}  
    This shows that the deviation in the kurtosis away from its $N(0,1)$ value decays like $1/N$.

