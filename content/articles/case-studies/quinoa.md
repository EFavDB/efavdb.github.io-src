Title: 2 + 1 = 4, by quinoa
Date: 2020-07-03
Author: Jonathan Landy
Category: Cooking math
Slug: quinoa packing
Status: published


<p align="center">
         <img src="images/quinoa.jpg">
</p>

I was struck the other day by the following:  The cooking instructions on my
Bob's tri-colored quinoa package said to combine 2 cups of water with 1 cup of
dried quinoa, which would ultimately create 4 cups of cooked quinoa.  See image
above.

My first reaction was to believe that some error had been made.  However, I
then realized that the explanation was packing:  When one packs spheres or
awkward solid geometric shapes into a container, they cannot fill the space
completely.  Little pockets of air sit between the spheres.  A quick google
search for the packing fraction of spheres gives a value of $0.75$ for a
crystalline structure and about $0.64$ for random packings -- apparently a
universal law.

We can get a similar number out from my quinoa instructions: Suppose that
before the quinoa is cooked, the water fills its volume completely.  However,
after cooking, the water is absorbed into the quinoa.  For simplicity, assume
the quinoa is spherical before and after cooking.  In this case, the quinoa
solids themselves should have the same packing fraction before and after.
However, the two cups of water went from being fully space filling to being
sucked into the quinoa -- forced to share its packing fraction. This implies
that
\begin{eqnarray} \tag{1} \label{1}
2 = \rho \times 3,
\end{eqnarray}
where $\rho$ is the packing fraction of the quinoa "spheres".  We have $3$ on
the right as the solids in the quinoa continue to make up for the same volume
before and after.  We conclude that the packing fraction is $\rho = 2/3$, very
close to the googled value of $\rho = 0.64$.
