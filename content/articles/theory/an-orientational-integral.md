Title: An orientational integral
Date: 2019-07-02 07:04
Author: Jonathan Landy
Category: Theory
Slug: an-orientational-integral
Status: published

We evaluate an integral having to do with vector averages over all
orientations in an n-dimensional space.





Problem definition
------------------

Let $\hat{v}$ be a unit vector in $n$-dimensions and consider the orientation average of
\begin{eqnarray} \tag{1} \label{1}
J \equiv \langle \hat{v} \cdot \vec{a}_1 \hat{v} \cdot \vec{a}_2 \ldots \hat{v} \cdot \vec{a}_k \rangle
\end{eqnarray}
where $\vec{a}_1, \ldots, \vec{a}_k$ are some given fixed vectors. For example, if all $\vec{a}_i$ are equal to $\hat{x}$, we want the orientation average of $v_x^k$.

Solution
--------

We'll evaluate our integral using parameter differentiation of the multivariate Gaussian integral. Let
\begin{eqnarray} \nonumber
I &=& \frac{1}{(2 \pi)^{n/2}} \int e^{- \frac{\vert \vec{v} \vert^2}{2} + \sum_{i=1}^k \alpha_i \vec{v} \cdot \vec{a}_i} d^nv \\ \tag{2} \label{2}
&=& \exp \left [- \frac{1}{2} \vert \sum_{i=1}^k \alpha_i \vec{a}_i \vert^2 \right]
\end{eqnarray}
The expression in the second line follows from completing the square in the exponent in the first -- for review, see our post on the normal distribution, [here](http://efavdb.github.io/normal-distributions). Now, we consider a particular derivative of $I$ with respect to the $\alpha$ parameters. From the first line of (\ref{2}), we have
\begin{eqnarray} \tag{3} \label{3}
\partial_{\alpha_1}\ldots \partial_{\alpha_k}I \vert_{\vec{\alpha}=0} &=& \frac{1}{(2 \pi)^{n/2}} \int e^{- \frac{\vert \vec{v} \vert^2}{2}} \prod_{i=1}^k \vec{v} \cdot \vec{a}_i d^n v \\
&\equiv & \frac{1}{(2 \pi)^{n/2}} \int_0^{\infty} e^{- \frac{\vert \vec{v} \vert^2}{2}} v^{n + k -1} dv \int \prod_{i=1}^k \hat{v} \cdot \vec{a}_i d \Omega_v \\
&=& \frac{2^{k/2 - 1}}{\pi^{n/2}} \Gamma(\frac{n+k}{2}) \times \int \prod_{i=1}^k \hat{v} \cdot \vec{a}_i d \Omega_v
\end{eqnarray}
The second factor above is almost our desired orientation average $J$ -- the only thing it's missing is the normalization, which we can get by evaluating this integral without any $\vec{a}$'s.

Next, we evaluate the parameter derivative considered above in a second way, using the second line of (\ref{2}). This gives,
\begin{eqnarray} \tag{4} \label{4}
\partial_{\alpha_1}\ldots \partial_{\alpha_k}I \vert_{\vec{\alpha}=0} &=& \partial_{\alpha_1}\ldots \partial_{\alpha_k} \exp \left [- \frac{1}{2} \vert \sum_{i=1}^k \alpha_i \vec{a}_i \vert^2 \right] \vert_{\vec{\alpha}=0} \\
&=& \sum_{\text{pairings}} (\vec{a}_{i_1} \cdot \vec{a}_{i_2}) (\vec{a}_{i_3} \cdot \vec{a}_{i_4})\ldots (\vec{a}_{i_{k-1}} \cdot \vec{a}_{i_k})
\end{eqnarray}
The sum here is over all possible, unique pairings of the indices. You can see this is correct by carrying out the differentiation one parameter at a time.

To complete the calculation, we equate (\ref{3}) and (\ref{4}). This gives
\begin{eqnarray} \tag{5}\label{5}
\int \prod_{i=1}^k \hat{v} \cdot \vec{a}_i d \Omega_v = \frac{\pi^{n/2}} {2^{k/2 - 1}\Gamma(\frac{n+k}{2})}\sum_{\text{pairings}} (\vec{a}_{i_1} \cdot \vec{a}_{i_2}) (\vec{a}_{i_3} \cdot \vec{a}_{i_4})\ldots (\vec{a}_{i_{k-1}} \cdot \vec{a}_{i_k})
\end{eqnarray}
Again, to get the desired average, we need to divide the above by the normalization factor. This is given by the value of the integral (\ref{5}) when $k = 0$. This gives,
\begin{eqnarray}\tag{6}\label{6}
J = \frac{1}{2^{k/2}}\frac{\Gamma(n/2)}{\Gamma(\frac{n+k}{2})} \sum_{\text{pairings}} (\vec{a}_{i_1} \cdot \vec{a}_{i_2}) (\vec{a}_{i_3} \cdot \vec{a}_{i_4})\ldots (\vec{a}_{i_{k-1}} \cdot \vec{a}_{i_k})
\end{eqnarray}

Example
-------

Consider the case where $k=2$ and $\vec{a}_1 = \vec{a}_2 = \hat{x}$. In this case, we note that the average of $\hat{v}_x^2$ is equal to the average along any other orientation. This means we have
\begin{eqnarray}\nonumber \tag{7} \label{7}
\langle \hat{v}_x^2 \rangle &=& \frac{1}{n} \sum_{i=1}^n \langle \hat{v}_x^2 + \hat{v}_y^2 + \ldots \rangle \\
&=& \frac{1}{n}
\end{eqnarray}
We get this same result from our more general formula: Plugging in $k=2$ and $\vec{a}_1 = \vec{a}_2 = \hat{x}$ into (\ref{6}), we obtain
\begin{eqnarray}\nonumber \tag{8} \label{8}
\langle \hat{v}_x^2 \rangle &=& \frac{1}{2}\frac{\Gamma(n/2)}{\Gamma(\frac{n}{2} + 1)} \\
&=& \frac{1}{n}
\end{eqnarray}
The two results agree.
