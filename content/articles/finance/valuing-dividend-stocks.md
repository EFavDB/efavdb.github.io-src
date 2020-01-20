Title: Valuing dividend stocks
Date: 2020-01-13
Author: Jonathan Landy
Category: Finance
Slug: valuing-dividend-stocks
Status: published

We review how one can value a dividend-bearing stock by treating it as a risky revenue stream.  As an example, we consider the fair value of Macy's stock as a function of some input parameters.  Comparing the output to the observed market price provides some insight into the market's current opinion of the company.




Discounted revenue equations
----------------------------
Here, we'll consider the value of a stock that generates a discrete set of dividends, with dividend $D_t$ paid out at time $t$, for $t \in \{1, 2, \ldots\}$.  To estimate a fair price $V_0$ for the stock today (assumed to be just after the most recent dividend payout at $t=0$), we'll consider how the value evolves over time.  If we purchase and hold the stock now, then at period $1$, we'll still have the stock but also a dividend.  The total expected fair value at that time will then sum to
\begin{eqnarray} \tag{1} \label{ev_step}
\text{expected value at period 1} \equiv E(V_1 + D_1).
\end{eqnarray}
Of course, because there is some risk in our investment, the expected value above may not be realized.  To take this into account -- as well as the fact that inflation and other concerns cause us to prefer money now over money later -- we will assert that we are only willing to pay a fraction $d$ of (\ref{ev_step}) above to acquire and hold the stock now.  That is, we will define the fair price now as
\begin{eqnarray}\label{discount} \tag{2}
V_0 = d \times E(V_1 + D_1).
\end{eqnarray}
Note that at this point, we still don't know the values of $V_0$ or $V_1$ in the above equation.  However, we can make progress if we assume that the same $d$ factor can be applied between any two periods.  In this case, we also have for general $i$,
\begin{eqnarray} \tag{3}
E(V_i) = d \times  E(V_{i+1} + D_{i+1}).
\end{eqnarray}
If we plug this into (\ref{discount}) we obtain
\begin{eqnarray} \tag{4} \label{value}
V_0 = \sum_{i=1}^{\infty} d^i E(D_i)
\end{eqnarray}
This is an expression for the current price that depends only on the future dividends -- quantities that we can attempt to forecast via extrapolations of recent dividend values, or through a thorough analysis of the company's prospects.  To simplify our result further, we'll assume a steady growth for the dividends at rate $g$, so that
\begin{eqnarray} \label{div_growth} \tag{5}
E(D_{t}) = D_0 g^i
\end{eqnarray}
Plugging this form into (\ref{value}), we get
\begin{eqnarray}
V_0 &=& \sum_{i=1}^{\infty} d^i D_0 g^i \\
&=& D_0 \frac{dg}{1 - dg} \tag{6} \label{value_geometric}
\end{eqnarray}
Formula (\ref{value_geometric}) is the result that we will use below to approximately price dividend-bearing stocks.  Note that it is a function of only three quantities:  $D_0$ -- the most recent dividend value, $g$ -- the assumed growth rate of the dividends, and $d$ -- our "discount rate".  To price a stock, we need only plug in values for these three quantities.  To set $D_0$, we can simply look up the value of the most recent dividend. To set $g$, we can forecast the business prospects of the company.  To set $d$, we should pick a value that reflects both how risk-averse we are and also how much risk the company in question carries:  $d$ should be set smaller for more risk averse individuals and for companies carrying more risk.

In the next two sections, we <em>(i)</em> show how one can use the capital asset pricing model (CAPM) to estimate the "market" value of $d$, and <em>(ii)</em> use our results to estimate a fair market price for Macy's stock.



CAPM discount rate 
------------------

We can estimate what value of $d$ is being used by the market as a whole for a given stock by considering how the price of the stock changes from period to period.  From the equations we have derived above, one can show that the expected return on holding the stock for one period is given by$^1$
\begin{eqnarray}
E(r_{stock}) &\equiv & \log \left ( \frac{E(V_{1} + D_{1})}{V_0}\right)\\ 
&=&  \log (1/d)
\tag{8}\label{grow_at_d_inv}
\end{eqnarray}
This says that the expected percentage return in fair value to an individual is given by $1 / d - 1$.  An interesting point about this equation is that -- because $d$ varies person to person -- so does the expected return in fair value, (\ref{grow_at_d_inv}).  This occurs because each person will have a different opinion on the value of the risky dividend stream over time, and therefore the change in the stock's fair value each period.  While this is true, the market price of a stock is something one can simply look up, so it must be set by some "market discount rate", an emergent value collectively applied to the stock in question.  To estimate this value, we need only ask how much the stock price is expected to grow on the market.  An approximate answer to this question is given by the capital asset pricing model (CAPM).  For brevity's sake, we won't derive the CAPM here, but instead simply quote its main result, which states that the expected growth rate of a stock's price on the market is approximately given by
\begin{eqnarray} \tag{9} \label{capm}
E(r_{stock, capm}) = r_{risk free} + \beta \times \left (r_{market} - r_{risk free} \right).
\end{eqnarray}
Here, $r_{risk free}$ is typically taken as the rate of growth of short-term treasury bonds, $r_{market}$ is the mean growth rate of the market as a whole -- often the historical growth rate of the S&P500 is used here, and $\beta$ is the slope in a fit of the stock's past total returns to those of the market.  Tests of this prediction have been carried out, and the model has been found to be fairly accurate.  We can therefore approximate the market's expectation for the return on the stock to be that given by CAPM.  Equating $E(r_{stock})$ and $E(r_{stock, capm})$ from the last two lines gives the CAPM approximation for the market discount rate,
\begin{eqnarray}
d_{market} &\approx& \exp \left (-E(r_{stock, capm}) \right) \\
&=& \exp \left ( - r_{risk free} - \beta \times \left (r_{market} - r_{risk free} \right) \right)
 \tag{10} \label{market_d}
\end{eqnarray}
These equations give us a reasonable method for setting $d$, enabling us to estimate what the market as a whole should think is a fair price for a given stock.  We turn now to an application, the pricing of Macy's stock.

# Application: Macy's
We are now ready to consider the fair market value of Macy's stock.  Recall that we need three quantities to price the stock, $D_0$, $d$, and $g$. We consider each of these below.

*THE MOST RECENT DIVIDEND*

A quick online search for the dividend history of Macy's shows that a $37.75$ cent dividend was payed last December, 12/2019 -- [link out](https://www.zacks.com/stock/chart/M/fundamental/beta).  Therefore,
\begin{eqnarray}
D_0 = 0.3775 \tag{10}
\end{eqnarray}

*THE DIVIDEND GROWTH RATE*

The link above also shows that the dividend paid by Macy's in December 2011 was $10$ cents.  The historical quarterly growth rate of the dividend over this period has therefore been
\begin{eqnarray}
g_{historical} &=& (37.73 / 10)^{1 / 32} \\
&\approx & 1.042 \tag{11}
\end{eqnarray}
Here, the exponent was one over the number of quarters considered between December 2011 and December 2019, -- 8 years and 4 quarters per year equals 32 quarters.  This is an impressive growth rate per quarter.  However, looking into how the business has done recently, it seems unlikely that Macy's will be able to keep this up -- at least in the immediate future.  For this reason, we'll tabulate values below assuming a range of possible $g$ values, given by $\{-1.04, -1.02, 1.0, 1.02, 1.04\}$.

*THE MARKET DISCOUNT RATE*

It is also possible to look up the beta for a stock online.    Doing this for Macy's we found a quoted value$^2$ of $\beta = 0.65$. However, in 2010, the historical quote shows a value of $\beta = 2.0$.  Since the value has fluctuated over time, we'll quote values below for a few possible forward looking betas, $\{0.65, 1.0, 2.0\}$.  To convert these to discount rates, we used the `capm_d_quarterly` method below -- python code implementing (\ref{market_d}).  You can see that we assume a risk-free rate of $1.5\%$, and a market growth rate of $9.8\%$ -- these are the current short-term treasury rates and historical average S&P500 rates, according to an online search.  The three discount rates that result for our chosen betas are 

\begin{eqnarray}
d_{beta = 0.65} &=& 0.982 \\
d_{beta = 1.0}  &=& 0.975 \\
d_{beta = 2.0}  &=& 0.955 \tag{12} \label{discounting_macys}
\end{eqnarray}

*FINAL CAPM PRICES*

We now have everything we need to estimate a fair market price for Macy's.  We simply need to plug the values for $D_0$, $g$, and $d$ we have obtained above into the pricing equation, (\ref{value_geometric}).  Our code snippet below takes care of this for us.  The results are tabulated at the end of the code snippet below.

Reviewing the output, we see a large range of possible price values as we vary our degrees of freedom -- the values range from four to eighty dollars! (The NaN values in our table correspond to situations where the growth rates are larger than the discount rate, which is unphysical -- i.e., not possible long term).  On the one hand, obtaining such a large set of values is disappointing -- clearly we can't use the approach we've taken here to determine precisely the price that should apply today.  However, on the other, our results do help to us to get a handle on the degrees of freedom and how they affect the price.  E.g., the dividend growth rate seems to have the largest effect, with modest changes having very large impacts on the price.  Because this impact is so strong, we can easily pick out which column best reflects the current market price of seventeen dollars -- that with $g=1$.  This suggests the market is anticipating Macy's will maintain but not grow its dividend in the near future.

Should we buy the stock?  That's for you to decide -- hopefully the results here have helped provide a mental framework useful for thinking through that question.

```python
import numpy as np
import pandas as pd

R_RISK_FREE = 0.015
R_MARKET = 0.098
D_0 = 0.3775

def capm_d_quarterly(beta, r_risk_free=R_RISK_FREE, r_market=R_MARKET):
    """
    Return the discount rate from CAPM, on a quaterly basis.
    """
    r_annual = r_risk_free + beta * (r_market - r_risk_free)
    r_quarterly = r_annual / 4.0
    d_quarterly = np.exp(-r_quarterly)
    return d_quarterly

def capm_price(beta, g, D_0):
    """
    Price of stock given its beta, dividend growth rate, and most recent dividend in dollars.
    """
    d = capm_d_quarterly(beta)
    if d * g < 0:
        return None
    else:
        return D_0 * d * g / (1 - d * g)

results = []
for beta in (0.65, 1.0, 2.0):
    for g in (0.96, 0.98, 1.0, 1.02, 1.04):
        results.append({
            'beta':beta,
            'g': g,
            'price':capm_price(beta=beta, g=g, D_0=D_0)})
df = pd.DataFrame(results)
print pd.pivot_table(df, values='price', index=['beta'], columns=['g'])

# output:
g         0.96      0.98       1.00       1.02       1.04
beta                                                     
0.65  6.315028  9.895171  21.711720        NaN        NaN
1.00  5.592369  8.257335  15.220184  80.175470        NaN
2.00  4.199821  5.580832   8.155215  14.646588  62.422493
```

# Footnotes

- [1] Notice that (\ref{grow_at_d_inv}) shows that the period return goes up as $d$ goes down.  On the other hand, the current fair price (\ref{value_geometric})  will go down as $d$ goes down.  This is somewhat counter-intuitive, at least to me.  What it says is that if the market adjusts the $d$ factor for a stock, the current price and the expected return will move in opposite directions.
- [2] Since the value of $\beta$ can change over time, there seems to be some ambiguity as to how it should be measured.  For example, a fit over the last month could given a different value from that over the last year, etc. Which should we use?  For divided stocks, should we smooth out the return from the dividend over the period in question, or keep the dividend return on the days that they are paid out?  These choices could all meaningfully impact the forecasted expected return by CAPM.
