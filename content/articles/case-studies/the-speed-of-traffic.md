Title: The speed of traffic
Date: 2019-06-14 09:21
Author: Jonathan Landy
Category: Case studies
Tags: theory, traffic
Slug: the-speed-of-traffic
Status: published

We use a simple argument to estimate the speed of traffic on a highway as a function of the density of cars. The idea is to simply calculate the maximum speed that traffic could go without supporting a growing traffic jam.

  
  


### Jam dissipation argument

To estimate the speed of traffic as a function of density, we'll calculate an upper bound and argue that actual traffic speeds must be described by an equation similar to that obtained. To derive our upper bound, we'll consider what happens when a small traffic jam forms. If the speed of cars is such that the rate of exit from the jam is larger than the rate at which new cars enter the jam, then the jam will dissipate. On the other hand, if this doesn't hold, the jam will grow, causing the speed to drop until a speed is obtained that allows the jam to dissipate. This sets the bound. Although we consider a jam to make the argument simple, what we really have in mind is any other sort of modest slow-down that may occur.

To begin, we introduce some definitions. (1) Let $\lambda$ be the density of cars in units of $[cars / mile]$. (2) Next we consider the rate of exit from a jam: Note that when traffic is stopped, a car cannot move until the car in front of it does. Because a human is driving the car, there is a slight delay between the time that one car moves and the car behind it moves. Let $T$ be this delay time in $[hours]$. (3) Let $v$ be the speed of traffic outside the jam in units of $[miles / hour]$.

With the above definitions, we now consider the rate at which cars exit a jam. This is the number of cars that can exit the jam per hour, which is simply  
\begin{eqnarray} \tag{1} \label{1}  
r_{out} = \frac{1}{T}.  
\end{eqnarray}  
Next, the rate at which cars enter the jam is given by  
\begin{eqnarray} \tag{2} \label{2}  
r_{in} = \lambda v.  
\end{eqnarray}  
Requiring that $r_{out} > r_{in}$ we get  
\begin{eqnarray} \label{3} \tag{3}  
v < \frac{1}{\lambda T}.  
\end{eqnarray}  
This is our bound and estimate for the speed of traffic. We note that this form for $v$ follows from dimensional analysis, so the actual rate of traffic must have the same algebraic form as our upper bound (\ref{3}) -- it can differ by a constant factor in front, but should have the same $\lambda$ and $T$ dependence.

### Plugging in numbers

I estimate $T$, the delay time between car movements to be about one second, which in hours is  
\begin{eqnarray} \tag{4} \label{4}  
T \approx 0.00028\ [hour].  
\end{eqnarray}  
Next for $\lambda$, note that a typical car is about 10 feet long and a mile is around 5000 feet, so the maximum for $\lambda$ is around $ \lambda \lesssim 500 [cars / mile]$. Consider a case where there is a car every 10 car lengths or so. In this case, the density will go down from the maximum by a factor of 10, or  
\begin{eqnarray}\tag{5} \label{5}  
\lambda \approx 50 \ [cars / mile].  
\end{eqnarray}  
Plugging (\ref{4}) and (\ref{5}) into (\ref{3}), we obtain  
\begin{eqnarray}  \tag{6}
v \lesssim \frac{1}{0.00028 * 50} \approx 70\ [mile / hour],  
\end{eqnarray}  
quite close to our typical highway traffic speeds (and speed limits).

### Final comments

The above bound clearly depends on what values you plug in -- I picked numbers that seemed reasonable, but admit I adjusted them a bit till I got the final number I wanted for $v$. Anecdotally, I've found the result to work well at other densities: For example, when traffic is slow on the highway near my house, if I see that there is a car every 5 car lengths, the speed tends to be about $30 [miles / hour]$ -- so scaling rule seems to work. The last thing I should note is that wikipedia has an article outlining some of the extensive research literature that's been done on traffic flows -- you can see that [here](https://en.wikipedia.org/wiki/Traffic_flow).
