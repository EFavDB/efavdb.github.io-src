Title: Mathematics of measles
Date: 2015-02-25 13:37
Author: Jonathan Landy
Category: Statistics
Slug: math-of-measles
Status: published

Here, we introduce -- and outline a solution to -- a generalized SIR model for infectious disease. This is referenced in our [following post](http://efavdb.com/vaccination-rates/) on measles and vaccination rates. Our generalized SIR model differs from the [original SIR model](http://en.wikipedia.org/wiki/Epidemic_model#The_SIR_model) of Kermack and McKendrick in that we allow for two susceptible sub-populations, one vaccinated against disease and one not. We conclude by presenting some python code that integrates the equations numerically. An example solution obtained using this code is given below.  

  



[caption width="800" caption="Solution shown corresponds to a 20% unvaccinated population, a condition supporting outbreak."][iframe src="https://plot.ly/~Jonathan Landy/58" width="90%" height="450"][/caption]

#### **The model**

The equations describing our generalized SIR model are  
\begin{eqnarray}\label{eq1}  
\dot{S}_{U} &=& - b_{U} S_{U} I\\ \label{eq2}  
\dot{S}_{V} &=& - b_{V} S_{V} I\\ \label{eq3}  
\dot{R} &=& k I\\  
1 &=& I + R + S_U + S_V \label{Ieq}  
\end{eqnarray}  
Here, $S_{U}$, $S_{V}$, $I$, and $R$ are population fractions corresponding to those unvaccinated and as yet uninfected, vaccinated and as yet uninfected, currently infected and contagious, and once contagious but no longer (recovered, perhaps), respectively. The first two equations above are instances of the [law of mass action](http://en.wikipedia.org/wiki/Law_of_mass_action). They approximate the infection rates as being proportional to the rates of susceptible-infected individual encounters. We refer to $b_{U}$ and $b_{V}$ here as the *infection rate parameters* of the two subpopulations. The third equation above approximates the dynamics of recovery: The form chosen supposes that an infected individual has a fixed probability of returning to health each day. We will refer to $k$ as the *recovery rate parameter*. The final equation above simply states that the subpopulation fractions have to always sum to one.

#### **Parameter estimation**

We can estimate the values $b_{U}$ and $b_{V}$ by introducing a close contact number ($ccn$) variable, which is the average number of close contacts that individual infected, contagious people make per day. As a rough ball park, let us suppose that $ccn \approx 3$. According to the CDC, an un-vaccinated person making close contact with someone with measles has a 90$%$ chance of contracting the illness. On the other hand, those who have been vaccinated a single time have a 95$%$ chance of being immune to the disease. Let's estimate that the combined population of individuals who have been vaccinated have a 1$%$ chance of contracting the illness upon close contact. These considerations suggest  
\begin{eqnarray}  
b_{U} \approx 3 \times 0.9 &=& 0.27, \ \  
b_{V} \approx 3 \times 0.01 &=& 0.03  
\end{eqnarray}  
The value of $k$ can be simply estimated using the fact that infected individuals are only contagious for about $8$ days, only four of which occur before rash appears. Assuming those who are showing symptoms quickly stop circulating, this suggests about five \`\`effectively contagious" days, or  
\begin{eqnarray}  
k \approx 1/5 = 0.2.  
\end{eqnarray}  
Note that here and elsewhere, we measure time in units of days.

It's important to note that, although the qualitative properties of the solutions to our model are insensitive to parameter value variations, this is not true for the numerical values that it predicts. We have chosen parameter values that seem reasonable to us. Further, with these choices, many of the model's key quantitative values line up with corresponding CDC estimates. Those interested can experiment to see what sort of flexibility is allowed through modest parameter variation.

#### **Solution by quadrature**

Equations (\ref{eq1}-\ref{eq3}) give  
\begin{eqnarray}\label{Svals}  
S_{U} = S_{U0} e^{ - \frac{b_{U} R}{k}}, \ \ \  
S_{V} = S_{V0} e^{- \frac{b_{V} R}{k}}.  
\end{eqnarray}  
Combining with (\ref{Ieq}) and integrating gives  
\begin{eqnarray}  
\frac{\dot{R}}{k} =I_0 -S_{U0} \left [ e^{ - \frac{b_{U} R}{k}}- 1 \right ] - S_{20} \left [e^{ - \frac{b_{V} R}{k}}- 1 \right ] - R  
\end{eqnarray}  
Integrating again,  
\begin{eqnarray}  
kt = \int_{0}^R \frac{d R^{\prime}}{I_0 -S_{U0} \left [ e^{ - \frac{b_{U} R^{\prime}}{k}}- 1 \right ] - S_{V0} \left [e^{ - \frac{b_{V} R^{\prime}}{k}}- 1 \right ] - R^{\prime}} \label{solution}.  
\end{eqnarray}  
This implicitly defines $R$ as function of time.

#### **Small time behavior**

At small $t$, $R$ is also small, so (\ref{solution}) can be approximated as  
\begin{eqnarray}  
k t = \int_{0}^R \frac{d R^{\prime}}{I_0 + \left [ \frac{ b_{U} S_{U0}}{k} +\frac{ b_{V} S_{V0}}{k} - 1 \right ]R^{\prime}}.  
\end{eqnarray}  
This form can be integrated analytically. Doing so, and solving for $R$, we obtain  
\begin{eqnarray}  
R = \frac{k}{b_{U} S_{U0} + b_{V} S_{V0} - k} \left \{e^{ (b_{U} S_{U0} + b_{V} S_{V0} - k )t } -1 \right \}, \ \ \  
I = I_0 e^{ (b_{U} S_{U0} + b_{V} S_{V0} - k )t}.  
\end{eqnarray}  
Early disease spread is characterized by either exponential growth or decay, governed by the sign of the parameter combination $b_{U} S_{U0} + b_{V} S_{V0} - k$: a phase transition!

#### **Total contractions**

The total number of people infected in an outbreak can be obtained by evaluating $R$ at long times, where $I = 0$. In this limit, using (\ref{Ieq}) and (\ref{Svals}), we have  
\begin{eqnarray}  
S_{U0} e^{- \frac{b_{U} R}{k}}+ S_{V0} e^{ - \frac{b_{V} R}{k}}+ R = 1.  
\end{eqnarray}  
This equation can be solved numerically to obtain the total contraction count as a function of the model parameters and initial conditions. A plot against $S_{U0}$ of such a solution for our measles-appropriate parameter estimates is given in our [next post](http://efavdb.com/vaccination-rates/).

#### **Numerical integration in python**

Below, we provide code that can be used to integrate (\ref{eq1}-\ref{Ieq}). The plot shown in our introduction provides one example solution. It's quite interesting to see how the solutions vary with parameter values, and we suggest that those interested try it out.

```  
#Solving the SIR model for infectious disease. JSL 2/18/2015  
import math

ccn = 3 #\`\`close contact number" = people per day  
#interacting closely with typical infected person

k = 1./5 #Rate of 'recovery' [1].  
b1 = ccn*0.9 #Approximate infection rate un-vaccinated [3].  
b2 = ccn*0.01 #Approximate infection rate un-vaccinated [4].

#Initial conditions (fraction of people in each category)  
I0 = 0.001 #initial population fraction infected.  
S10 = 0.2 #population fraction unvaccinated.  
S20 = 1 - I0 - S10 #population fraction vacccinated.  
R0 = 0.0 #intial recovered fraction.

dt = 0.01 #integration time step  
days = 100 #total days considered

I = [I0 for i in range(int(days/dt))]  
S1 = [S10 for i in range(int(days/dt))]  
S2 = [S20 for i in range(int(days/dt))]  
R = [R0 for i in range(int(days/dt))]

for i in range(1,int(days/dt)):

S1[i] = S1[i-1] - b1 * S1[i-1] * I[i-1] * dt  
S2[i] = S2[i-1] - b2 * S2[i-1] * I[i-1] * dt  
I[i] = I[i-1] + (b1 * S1[i-1] * I[i-1] + \  
b2 * S2[i-1] * I[i-1] - k*I[i-1] ) * dt  
R[i] = R[i-1] + k * I[i-1] * dt

time = [dt * i for i in range(0, int(days/dt))]

%pylab inline  
plt.plot(time, I, color = 'red')  
plt.plot(time, S1, color = 'blue')  
plt.plot(time, S2, color = 'green')  
plt.plot(time, R, color = 'black')  
plt.plot(time[:1400],[I0* math.exp((b1 *S10 + b2* S20 - k)*t) \  
for t in time[:1400]],color = 'purple')  
plt.axis([0, 100, 10**(-4),1])  
plt.yscale('log')  
plt.xlabel('time [days]')  
plt.ylabel('population %\'s')  
plt.show()

#[1] Measles patients are contagious for eight days  
# four of which are before symptoms appear. [2]  
#[2] http://www.cdc.gov/measles/about/transmission.html  
#[3] Assume infected have close contact with five people/day.  
# 90% of the un-vaccinated get sick in such situations.  
#[4] Single vaccination gives ~95% immunity rate [5]. Many  
# have two doses, which drops rate to very low.  
#[5] http://www.cdc.gov/mmwr/preview/mmwrhtml/00053391.htm

```
