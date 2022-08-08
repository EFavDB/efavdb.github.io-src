Title: Spaced repetition can allow for infinite recall
Date: 2022-08-07
Author: Jonathan Landy
Category: Case studies
Slug: memory recall
Status: published


<p align="center">
         <img src="images/jeopardy.jpg">
</p>

My friend Andrew is an advocate of the ``spaced repetition" technique for
memorization of a great many facts [1].  The ideas behind this are two-fold:

- When one first ``learns" a new fact, it needs to be reviewed frequently in
  order to not forget it.  However, with each additional review, the fact can
be retained longer before a refresher is needed to maintain it in recall.

- Because of this, one can maintain a large, growing body of facts in recall
  through daily review:  Each day, one need only review for ten minutes or so,
covering a small number of facts. The facts included should be sampled from the
full library in a way that prefers newer entries, but that also sprinkles in
older facts often enough so that none are ever forgotten.  Apps have been
written to intelligently take care of the sampling process for us.

Taking this framework as correct motivates questioning exactly how far it can
be pushed:  <em>Would an infinitely-long-lived, but forgetful person be able to
recall an infinite number of facts using this method? </em>  $\ldots$ Below, we
show that the answer is: <em>YES!</em>

##### Proof:

We first posit that the number of days $T$ that a fact can be retained before
it needs to be reviewed grows as a power-law in $s$, the number of times it's
been reviewed so far,

\begin{eqnarray} \tag{1}\label{1}
T(s) \sim s^{\gamma},
\end{eqnarray}
with $\gamma > 0$. With this assumption, if $N(t)$ facts are to be recalled
from $t$ days ago, one can show that the amount of work needed today to retain
these will go like (see appendix for a proof of this line)

\begin{eqnarray}\tag{2}\label{2}
w(t) \sim \frac{N(t)}{t^{\gamma / (\gamma + 1)}}.
\end{eqnarray}
The total work needed today is then the sum of work needed for each past day's
facts,

\begin{eqnarray} \tag{3} \label{3}
W(total) = \int_1^{\infty} \frac{N(t)}{t^{\gamma / (\gamma + 1)}} dt.
\end{eqnarray}
Now, each day we only have a finite amount of time to study.  However, the
above total work integral will diverge at large $t$ unless it decays faster
than $1/t$.  To ensure this, we can limit the number of facts retained from
from $t$ days ago to go as

\begin{eqnarray} \tag{4} \label{4}
N(t) \sim \frac{1}{t^{\epsilon}} \times \frac{1}{t^{1 / (\gamma + 1)}},
\end{eqnarray}
where $\epsilon$ is some small, positive constant.  Plugging (\ref{4}) into
(\ref{3}) shows that we are guaranteed a finite required study time each day.
However, after $t$ days of study, the total number of facts retained scales 
as

\begin{eqnarray}
N_{total}(t) &\sim & \int_1^{t} N(t) dt \\
&\sim & \int_0^{t} \frac{1}{t^{1 / (\gamma + 1)}} \\
&\sim & t^{ \gamma / (\gamma + 1)}. \tag{5} \label{5}
\end{eqnarray}
Because we assume that $\gamma > 0$, this grows without bound over time,
eventually allowing for an infinitely large library.

We conclude that -- though we can't remember a fixed number of facts from each
day in the past using spaced repetition -- we can ultimately recall an infinite
number of facts using this method.  To do this only requires that we gradually
curate our previously-introduced facts so that the scaling (\ref{4}) holds at
all times.

### Appendix: Proof of (2) 

Recall that we assume $N(s)$ facts have been reviewed exactly $s$ times.  On a
given day, the number of these that need to be reviewed then goes like

\begin{eqnarray} \tag{A1}\label{A1}
W(s) \sim \frac{N(s)}{T(s)}.
\end{eqnarray}
where $T(s)$ is given in (\ref{1}).  This holds because each of the $N(s)$
facts that have been studied $s$ times so far must be reviewed within $T(s)$
days, or one will be forgotten.  During these $T(s)$ days, each will move to
having been reviewed $s+1$ times.  Therefore,

\begin{eqnarray} \tag{A2} \label{A2}
\frac{ds}{dt} &\sim & \frac{1}{T(s)}
\end{eqnarray}
Integrating this gives $s$ as a function of $t$,

\begin{eqnarray} \tag{A3} \label{A3}
s \sim t^{1 / (\gamma + 1)}
\end{eqnarray}

Plugging this last line and (1) into (A1), we get (2).

## References
[1] See Andrew's blog post on spaced repetition <a
href="https://andrewjudson.com/spaced-repitition/2022/06/03/spaced-repitition.html">
here</a>.

