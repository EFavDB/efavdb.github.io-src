Title: Pricing dividend stocks
Date: 2020-12-20
Author: Jonathan Landy
Category: Finance
Slug: pricing-dividend-stocks
Status: published

We review how one can price a dividend-bearing stock by simply discounting its dividend stream using the value suggested by the Capital Asset Pricing Model (CAPM).  As an example, we consider the price of AT&T common stock.  The model result matches the current market price quite well.  Varying inputs to the model also allows us to explore how its price might adjust to changes in company performance.



Discounted revenue equations
----------------------------
In this note, we'll consider the value of a stock that generates a discrete set of dividends, with dividend $D_t$ paid out at time $t$, for $t \in \{1, 2, \ldots\}$.  To estimate a fair price $V_0$ for the stock today (assumed to be just after the most recent dividend payout at $t=0$), we'll consider how the value evolves over time.  If we purchase and hold the stock now, then at period $1$, we'll still have the stock but also a dividend.  The total expected fair value at that time will then sum to
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
Formula (\ref{value_geometric}) is the result that we will use below to approximately price dividend-bearing stocks.  Note that it is a function of only three quantities:  $D_0$ -- the most recent dividend value, $g$ -- the assumed growth rate of the dividends, and $d$ -- the "discount rate", which in principle could vary person to person.  To price a stock, one need only plug in values for these three quantities.  To set $D_0$, we can simply look up the value of the most recent dividend. To set $g$, we can forecast the business prospects of the company.  To set $d$, we should pick a value that reflects both how risk-averse we are and also how much risk the company in question carries:  $d$ should be set smaller for more risk averse individuals and for companies carrying more risk.

In the next two sections, we <em>(i)</em> show how one can use the Capital Asset Pricing Model (CAPM) to estimate the "market" value of $d$, and <em>(ii)</em> use our results to estimate a fair market price for AT&T's stock.



CAPM discount rate 
------------------

The CAPM provides a method for estimating the return one should expect from a stock.  Combining this with our analysis above, we can get an estimate for discount rate $d$ the market applies to a stock.  Plugging this into (\ref{value_geometric}) then gives a self-consistent estimate for the stock's fair market price.  To make the connection, we first note that (\ref{discount}) implies that the expected return on holding the stock for one period is given by
\begin{eqnarray}
E(r_{stock}) &\equiv & \log \left ( \frac{E(V_{1} + D_{1})}{V_0}\right)\\ 
&=&  \log (1/d)
\tag{8}\label{grow_at_d_inv}
\end{eqnarray}
Next, we quote the CAPM's estimate for the return of a stock$^1$ 
\begin{eqnarray} \tag{9} \label{capm}
E(r_{stock, capm}) = r_{risk free} + \beta \times \left (r_{market} - r_{risk free} \right).
\end{eqnarray}
Here, $r_{risk free}$ is typically taken as the rate of growth of short-term treasury bonds, $r_{market}$ is the mean growth rate of the market as a whole -- often the historical growth rate of the S&P500 is used here, and $\beta$ is the slope in a fit of the stock's past total returns to those of the market.  Tests of this prediction have been carried out, and the model has been found to be fairly accurate.  We can therefore approximate the market's expectation for the return on the stock to be that given by CAPM.  Equating $E(r_{stock})$ and $E(r_{stock, capm})$ from the last two lines gives the CAPM approximation for the market discount rate,
\begin{eqnarray}
d_{market} &\approx& \exp \left (-E(r_{stock, capm}) \right) \\
&=& \exp \left ( - r_{risk free} - \beta \times \left (r_{market} - r_{risk free} \right) \right)
 \tag{10} \label{market_d}
\end{eqnarray}
These equations give us a reasonable method for setting $d$, enabling us to estimate what the market as a whole should think is a fair price for a given stock.  We turn now to our application, the pricing of AT&T's common stock.

# Application: AT&T (ticker T)
We are now ready to consider the fair market value of AT&T's common stock.  Recall that we need three quantities to price the stock, $D_0$, $d$, and $g$. We consider each of these below.

*THE MOST RECENT DIVIDEND*

A quick online search for the dividend history of AT&T's shows that a $52$ cent dividend was payed in October 2020 -- [link](https://www.nasdaq.com/market-activity/stocks/t/dividend-history).  Therefore,
\begin{eqnarray}
D_0 = 0.52 \tag{10}
\end{eqnarray}
This company pays out dividends quarterly.

*THE DIVIDEND GROWTH RATE*

The link above also shows that the dividend paid by AT&T in 2015 was $47$ cents per quarter.  The historical quarterly growth rate of the dividend over this period has therefore been
\begin{eqnarray}
g_{historical} &=& (52 / 47)^{1 / 20} \\
&\approx & 1.005 \tag{11}
\end{eqnarray}
Here, the exponent was one over the number of quarters considered between October 2015 and October 2020 -- 20 quarters.

It is important to note that the historical growth rate is not necessarily that which we can expect going forward.  In fact, AT&T has already declared a dividend for January 2021 of $52$ cents, the same value as was distributed each quarter in 2020.  In each of the past five years, the company raised dividends with each new year.  The upcoming dividend therefore signals a change in growth rate -- at least in the short-term.  If a value near $g\approx 1.000$ better describes the behavior of AT&T in the near term, this will significantly affect its stock price.  We estimate prices for a set of $g$ values below to highlight this dependence.

*THE MARKET DISCOUNT RATE*

To evaluate the CAPM market discount rate, we need to know a stock's beta.  This can be obtained through a regression or it can simply be looked up online.   Doing this for AT&T we see a current value quoted near $0.7$.  However, over the last five years the value has varied, going as low as $0.3$ or so in 2016 -- [link](https://www.zacks.com/stock/chart/T/fundamental/beta).  Since the value has fluctuated over time, we'll quote values below for a few possible forward looking betas, $\{0.3, 0.5, 0.7, 0.9\}$.  To convert these to discount rates, we used the `capm_d_quarterly` method below -- python code that implements (\ref{market_d}).  You can see that we assume a risk-free rate of $0.07\%$, and a market growth rate of $9.8\%$ -- these are the current short-term treasury rates and historical average S&P500 rates, according to an online search.  The discount rates that result for our chosen betas are 

\begin{eqnarray}
d_{beta = 0.3} &=& 0.993 \\
d_{beta = 0.5}  &=& 0.988 \\
d_{beta = 0.7}  &=& 0.983 \\
d_{beta = 0.9}  &=& 0.978 
 \tag{12} \label{discounting_macys}
\end{eqnarray}

*FINAL CAPM PRICES*

We now have everything we need to estimate a fair market price for AT&T.  We simply need to plug the values for $D_0$, $g$, and $d$ we have obtained above into the pricing equation, (\ref{value_geometric}).  Our code snippet below takes care of this for us and the values that it provides are printed underneath.

Reviewing the output, we see a large range of possible price values as we vary our degrees of freedom -- the values range from $18$ to over $200$! (The NaN value in the table corresponds to a situation where the growth rate is larger than the discount rate, which is not possible long term).  These results indicate that there is strong sensitivity in the price of a stock to its growth rate and beta.  E.g., we note that if we plug in today's values of $\beta = 0.7$ and $g = 1.000$ (marked with an * in the table below), we get a value of $29.39$ dollars  --  amazingly close to the last traded value of $29.40$ on 12/18 (not bad!).  However, we note that if the company were able to quickly return to the old steady growth rate of $1.005$, we'd move to the cell just right of the current value, giving a price of $41$ dollars -- an impressive gain.

Should we buy the stock?  That's for you to decide -- hopefully the results here have helped provide a mental framework useful for thinking through that question.

```python
import numpy as np
import pandas as pd

R_RISK_FREE = 0.0007
R_MARKET = 0.098
D_0 = 0.51

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
    if (d * g > 1):
        return None
    else:
        return D_0 * d * g / (1 - d * g)

results = []
for beta in (0.3, 0.5, 0.7, 0.9):
    for g in (0.99, 0.995, 1.0, 1.005, 1.01):
        results.append({
            'beta':beta,
            'g': g,
            'price':capm_price(beta=beta, g=g, D_0=D_0)})
df = pd.DataFrame(results)
print pd.pivot_table(df, values='price', index=['beta'], columns=['g'])

# # output
# g         0.990      0.995      1.000       1.005       1.010
# beta                                                         
# 0.3   28.850623  40.594413  67.995569  204.979922         NaN
# 0.5   22.526179  29.140479  41.082910   69.133459  213.387273
# 0.7   18.459807  22.703362  29.392585*  41.497605   70.069095
# 0.9   15.625393  18.579209  22.856848   29.605283   41.834554
```

# Footnotes

[1]  For a simple derivation of CAPM's main results, see Derman, "A boys guide to pricing and hedging".  As a caveat, we note that one of the primary assumptions of CAPM is that market prices are set by rational market participants.
