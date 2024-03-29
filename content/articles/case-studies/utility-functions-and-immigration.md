Title: Utility functions and immigration
Date: 2019-06-21 09:24
Author: Jonathan Landy
Category: Case studies
Slug: utility-functions-and-immigration
Status: published

We consider how the GDP or utility output of a city depends on the number of people living within it. From this, we derive some interesting consequences that can inform both government and individual attitudes towards newcomers.

Edit 9/2022: The model here can't be complete because it doesn't take into account
city capacity.  The true utility functions should be shaped like $S$-curves.
Nevertheless, the arguments here can provide some insight into "growth"-phase
dynamics and preferences.


### The utility function and benefit per person

In this post, we will consider an idealized town whose net output $U$ (the GDP) scales as a power law with the number of people $N$ living within it. That is, we'll assume,  
\begin{eqnarray} \tag{1} \label{1}  
U(N) = a N^{\gamma}.  
\end{eqnarray}  
We'll assume that the average benefit captured per person is their share of this utility,  
\begin{eqnarray} \tag{2} \label{2}  
BPP(N) = U(N) / N = a N^{\gamma -1}.  
\end{eqnarray}  
What can we say about the above $a$ and $\gamma$? Well, we must have $a> 0$ if the society is productive. Further, because we know that cities allow for more complex economies as the number of occupants grow, we must have $\gamma > 1$. These are the only assumptions we will make here. Below, we'll see that these assumptions imply some interesting consequences.

### Marginal benefits

When a new person immigrates to a city, its $N$ value goes up by one. Here, we consider how the utility and benefit per person changes when this occurs. The increase in net utility is simply  
\begin{eqnarray}\tag{3} \label{3}  
\partial_N U(N) = a \gamma N^{\gamma -1}.  
\end{eqnarray}  
Notice that because we have $\gamma > 1$, (\ref{3}) is a function that increases with $N$. That is, cities with larger populations benefit more (as a collective) per immigrant newcomer than those cities with smaller $N$ would. This implies that the governments of large cities should be more enthusiastic about welcoming of newcomers than those of smaller cities.

Now consider the marginal benefit per person when one new person moves to this city. This is simply  
\begin{eqnarray}\tag{4} \label{4}  
\partial_N BPP(N) = a (\gamma - 1) N^{\gamma -2}.  
\end{eqnarray}  
Notice that this is different from the form (\ref{3}) that describes the marginal increase in total city utility. In particular, while (\ref{4}) is positive, it is not necessarily increasing with $N$: If $\gamma < 2$, (\ref{4}) decreases with $N$. Cities having $\gamma$ values like this are such that the net new wealth captured per existing citizen -- thanks to each new immigrant -- quickly decays to zero. The consequence is that city governments and existing citizens can have a conflict of interest when it comes to immigration.

### Equilibration

In a local population that has freedom of movement, we can expect the migration of people to push the benefit per person to be equal across cities. In cases like this, we should then have  
\begin{eqnarray}\tag{5} \label{5}  
a_i N^{\gamma_i -1} \approx a_j N^{\gamma_j -1},  
\end{eqnarray}  
for each city $i$ and $j$ for which there is low mutual migration costs. We point out that this is not the same result required to maximize the net, global output. This latter score is likely that which an authoritarian government might try to maximize. To maximize net utility, we need to have the marginal utility per city equal across cities, which means  
\begin{eqnarray}\tag{6} \label{6}  
\partial_N U_i(N) = \partial_N U_j(N)  
\end{eqnarray}  
or,  
\begin{eqnarray}\tag{7} \label{7}  
a_i \gamma_i N^{\gamma_i -1} = a_j \gamma_j N^{\gamma_j -1}.  
\end{eqnarray}  
We see that (\ref{5}) and (\ref{7}) differ in that there are $\gamma$ factors in (\ref{7}) that are not present in (\ref{5}). This implies that as long as the $\gamma$ values differ across cities, there will be a conflict of interest between the migrants and the government.
