Title: Martingales
Date: 2017-10-20 07:44
Author: Jonathan Landy
Category: Finance
Tags: theory
Slug: martingales
Status: published

Here, I give a quick review of the concept of a Martingale. A Martingale is a sequence of random variables satisfying a specific expectation conservation law. If one can identify a Martingale relating to some other sequence of random variables, its use can sometimes make quick work of certain expectation value evaluations.

This note is adapted from Chapter 2 of Stochastic Calculus and Financial Applications, by Steele.





### Definition

Often in random processes, one is interested in characterizing a sequence of random variables $\{X_i\}$. The example we will keep in mind is a set of variables $X_i \in \{-1, 1\}$ corresponding to the steps of an unbiased random walk in one-dimension. A Martingale process $M_i = f(X_1, X_2, \ldots X_i)$ is a derived random variable on top of the $X_i$ variables satisfying the following conservation law
\begin{align} \tag{1}
E(M_i | X_1, \ldots X_{i-1}) = M_{i-1}.
\end{align}
For example, in the unbiased random walk example, if we take $S_n = \sum_{i=1}^n X_i$, then $E(S_n) = S_{n-1}$, so $S_n$ is a Martingale. If we can develop or identify a Martingale for a given $\{X_i\}$ process, it can often help us to quickly evaluate certain expectation values relating to the underlying process. Three useful Martingales follow.

1.  Again, the sum $S_n = \sum_{i=1}^n X_i$ is a Martingale, provided $E(X_i) = 0$ for all $i$.
2.  The expression $S_n^2 - n \sigma^2$ is a Martingale, provided $E(X_i) = 0$ and $E(X_i^2) = \sigma^2$ for all $i$. Proof: \begin{align} \tag{2}
    E(S_n^2 | X_1, \ldots X_{n-1}) &= \sigma^2 + 2 E(X_n) S_{n-1} + S_{n-1}^2 - n \sigma^2\\
    &= S_{n-1}^2 - (n-1) \sigma^2.
    \end{align}
3.  The product $P_n = \prod_{i=1}^n X_i$ is a Martingale, provided $E(X_i) = 1$ for all $i$. One example of interest is
    \begin{align} \tag{3}
    P_n = \frac{\exp \left ( \lambda \sum_{i=1}^n X_i\right)}{E(\exp \left ( \lambda X \right))^n}.
    \end{align}
    Here, $\lambda$ is a free tuning parameter. If we choose a $\lambda$ such that $E(\exp(\lambda X)) = 1$ for our process, we can get a particularly simple form.

### Stopped processes

In some games, we may want to setup rules that say we will stop the game at time $\tau$ if some condition is met at index $\tau$. For example, we may stop a random walk (initialized at zero) if the walker gets to either position $A$ or $-B$ (wins $A$ or loses $B$). This motivates defining the stopped Martingale as,
\begin{align}
M_{n \wedge \tau} = \begin{cases}
M_n &\text{if } \tau \geq n \\
M_{\tau} &\text{else}. \tag{4}
\end{cases}
\end{align}
Here, we prove that if $M_n$ is a Martingale, then so is $M_{n \wedge \tau} $. This is useful because it will tell us that the stopped Martingale has the same conservation law as the unstopped version.

First, we note that if $A_i \equiv f_2(X_1, \ldots X_{i-1})$ is some function of the observations so far, then the transformed process
\begin{align} \tag{5}
\tilde{M}_n \equiv M_0 + \sum_{i=1}^n A_i (M_i - M_{i-1})
\end{align}
is also a Martingale. Proof:
\begin{align} \tag{6}
E(\tilde{M}_n | X_1, \ldots X_{n-1}) = A_n \left ( E(M_n) - M_{n-1} \right) + \tilde{M}_{n-1} = \tilde{M}_{n-1}.
\end{align}

With this result we can prove the stopped Martingale is also a Martingale. We can do that by writing $A_i = 1(\tau \geq i)$ -- where $1$ is the indicator function. Plugging this into the above, we get the transformed Martingale,
\begin{align} \nonumber \tag{7}
\tilde{M}_n &= M_0 + \sum_{i=1}^n 1(\tau \geq i) (M_i - M_{i-1}) \\
&= \begin{cases}
M_n & \text{if } \tau \geq n \
M_{\tau} & \text{else}.
\end{cases}
\end{align}
This is the stopped Martingale -- indeed a Martingale, by the above.

### Example applications

###

#### Problem 1

Consider an unbiased random walker that takes steps of size $1$. If we stop the walk as soon as he reaches either $A$ or $-B$, what is the probability that he is at $A$ when the game stops?

Solution: Let $\tau$ be the stopping time and let $S_n = \sum_{i=1}^n X_i$ be the walker's position at time $n$. We know that $S_n$ is a Martingale. By the above, so then is $S_{n \wedge \tau}$, the stopped process Martingale. By the Martingale property
\begin{align} \tag{8}
E(S_{n \wedge \tau}) = E(S_{i \wedge \tau})
\end{align}
for all $i$. In particular, plugging in $i = 0$ gives $E(S_{n \wedge \tau}) = 0$. If we take $n \to \infty$, then
\begin{align} \tag{9}
\lim_{n \to \infty} E(S_{n \wedge \tau}) \to E(S_{\tau}) = 0.
\end{align}
But we also have
\begin{align} \tag{10}
E(S_{\tau}) = P(A) * A - (1 - P(A)) B.
\end{align}
Equating (9) and (10) gives
\begin{equation} \tag{11}
P(A) = \frac{B}{A + B}
\end{equation}

##### Problem 2

In the game above, what is the expected stopping time? Solution: Use the stopped version of the Martingale $S_n^2 - n \sigma^2$.

##### Problem 3

In a biased version of the random walk game, what is the probability of stopping at $A$? Solution: Use the stopped Martingale of form $P_n = \frac{\exp \left ( \lambda \sum_{i=1}^n X_i\right)}{E(\exp \left ( \lambda X \right))^n}$, with $\exp[\lambda] = q/p$, where $p = 1-q$ is the probability of step to the right.
