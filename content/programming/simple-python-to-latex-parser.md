Title: Simple python to LaTeX parser
Date: 2016-11-18 12:59
Author: jslandy
Category: Programming
Slug: simple-python-to-latex-parser
Status: published

We demo a script that converts python numerical commands to LaTeX format. A notebook available on our GitHub page will take this and pretty print the result.

  
[Follow @efavdb](http://twitter.com/efavdb)  
Follow us on twitter for new submission alerts!

### Introduction

Here, we provide a simple script that accepts numerical python commands in string format and converts them into LaTeX markup. An example input / output follows:

```  
s = 'f(x_123, 2) / (2 + 3/(1 + z(np.sqrt((x + 3)/3)))) + np.sqrt(2 ** w) * np.tanh(2 * math.pi* x)'  
print command_to_latex(s)

## output:  
\frac{f \left ({x}_{123} , 2 \right )}{2 + \frac{3}{1 + z \left ( \sqrt{\frac{x + 3}{3}} \right )}} + \sqrt{{2}^{w}} \cdot \tanh \left (2 \cdot \pi \cdot x \right )  
```

If the output shown here is plugged into a LaTeX editor, we get the following result:

$$\tag{1}  
\frac{f \left ({x}_{123} , 2 \right )}{2 + \frac{3}{1 + z \left ( \sqrt{\frac{x + 3}{3}} \right )}} + \sqrt{{2}^{w}} \cdot \tanh \left (2 \cdot \pi \cdot x \right )  
$$  
Our Jupyter [notebook](https://github.com/EFavDB/python_command_to_latex) automatically pretty prints to this form.

We provide the script here as it may be useful for two sorts of applications: 1) facilitating write-ups of completed projects, and 2) visualizing typed-up formulas to aid checks of their accuracy. The latter is particularly helpful for lengthy commands, which are often hard to read in python format.

We note that the python package sympy also provides a simple command-to-latex parser. However, I have had trouble getting it to output results if any functions appear that have not been defined -- we illustrate this issue in the notebook.

As usual, our code can be downloaded from our github page [here](https://github.com/EFavDB/python_command_to_latex).

### Code

The main code segment follows. The method command_to_latex recursively computes the LaTeX for any combinations of variables grouped together via parentheses. The base case occurs when there are no parentheses left, at which point the method parse_simple_eqn is called, which converts simple commands to LaTeX. The results are then recombined within the recursive method. Additional replacements can be easily added in the appropriate lines below.

```  
def parse_simple_eqn(q):  
""" Return TeX equivalent of a command  
without parentheses. """  
# Define replacement rules.  
simple_replacements = [[' ', ''],  
['**', '^'], ['*', ' \cdot '],  
['math.', ''], ['np.', ''],  
['pi', '\pi'] , ['tan', '\tan'],  
['cos', '\cos'], ['sin', '\sin'],  
['sec', '\sec'], ['csc', '\csc']]  
complex_replacements = [['^', '{{{i1}}}^{{{i2}}}'],  
['_', '{{{i1}}}_{{{i2}}}'],  
['/', '\frac{{{i1}}}{{{i2}}}'],  
['sqrt','\sqrt{{{i2}}}']]  
# Carry out simple replacements  
for pair in simple_replacements:  
q = q.replace(pair[0], pair[1])  
# Now complex replacements  
for item in ['*', '/', '+', '-', '^', '_', ',', 'sqrt']:  
q = q.replace(item, ' ' + item + ' ')  
q_split = q.split()  
for index, item in enumerate(q_split):  
for pair in complex_replacements:  
if item == pair[0]:  
if item == 'sqrt':  
match_str = " ".join(q_split[index:index+2])  
else:  
match_str = " ".join(q_split[index-1:index+2])  
q = q.replace(match_str, pair[1].format(  
i1=q_split[index-1], i2=q_split[index+1]))  
return q

def command_to_latex(q, index=0):  
""" Recursively eliminate parentheses. Once  
removed, apply parse_simple_eqn. """  
open_index, close_index = -1, -1  
for q_index, i in enumerate(q):  
if i == '(':  
open_index = q_index  
elif i == ')':  
close_index = q_index  
break  
if open_index != -1:  
o = q[:open_index] + '@' + str(index) + q[close_index + 1:]  
m = q[open_index + 1:close_index]  
o_tex = command_to_latex(o, index + 1)  
m_tex = command_to_latex(m, index + 1)  
# Clean up redundant parentheses at recombination  
r_index = o_tex.find('@' + str(index))  
if o_tex[r_index - 1] == '{':  
return o_tex.replace('@'+str(index), m_tex)  
else:  
return o_tex.replace('@'+str(index),  
' \left (' + m_tex + ' \right )')  
else:  
return parse_simple_eqn(q)  
```

That's it!
