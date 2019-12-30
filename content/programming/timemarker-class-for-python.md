Title: TimeMarker class for python
Date: 2019-09-14 22:31
Author: jslandy
Category: Programming, python, Tools
Slug: timemarker-class-for-python
Status: published

We give a simple class for marking the time at different points in a code block and then printing out the time gaps between adjacent marked points. This is useful for identifying slow spots in code.

[Follow @efavdb](http://twitter.com/efavdb)

The TimeMarker class
--------------------

In the past, whenever I needed to speed up a block of python code, the first thing I would do was import the time package, then manually insert a set of lines of the form `t1 = time.time() `, `t2 = time.time() `, etc. Then at the end, `print t2 - t1, t3 -t2, ... `, etc. This works reasonably well, but I found it annoying and time consuming to have to save each time point to a different variable name. In particular, this prevented quick copy and paste of the time marker line. I finally thought to fix it this evening: Behold the `TimeMarker` class, which solves this problem for me:

```  
import time

class TimeMarker():

def __init__(self):  
self.markers = []

def mark(self):  
self.markers.append(time.time())

def print_markers(self):  
for pair in zip(self.markers, self.markers[1:]):  
print pair[1] - pair[0]  
```

Here is a simple code example:  
```  
tm = TimeMarker()

tm.mark()  
sum(range(10 ** 2))  
tm.mark()  
sum(range(10 ** 6))  
tm.mark()

tm.print_markers()  
# (output...)  
# 7.9870223999e-05  
# 0.0279731750488  
```  
The key here is that I can quickly paste the `tm.mark()` repeatedly throughout my code and quickly check where the slow part sits.
