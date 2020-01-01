Title: Reshaping Data in R
Date: 2015-06-06 19:17
Author: Cathy Yeh
Category: Programming
Tags: programming, R
Slug: reshaping-data-in-r
Status: published


Today, we'll talk about reshaping data in R. At the same time, we'll see how for-loops can be avoided by using R functionals (functions of functions). Functionals are faster than for-loops and make code easier to read by clearly laying out the intent of a loop.  

  


### The Task

Suppose you're given the two tables below, saved as individual .csv files.  Each table contains measurements of plant height on specific days. The plants are split into fertilizer treatment groups A and B, and each plant can be uniquely identified by its id.

Day 1

day

group

id

height

1

A

A.1

1.1

1

A

A.2

1.2

1

B

B.1

1.0

1

B

B.2

0.9

Day 2

day

group

id

height

2

A

A.1

1.5

2

A

A.2

1.5

2

B

B.1

2.1

2

B

B.2

1.9

Your task is to split the data by treatment group rather than day. The desired output is one file per group, with day on the vertical of the new tables, plant id on the horizontal, and height as the value inside the table. For example, the new table for group A would be:

Group A

day

A.1

A.2

1

1.1

1.2

2

1.5

1.5

This example can be manually formatted in Excel pretty quickly, but in real life, data only looks like this if you're in first grade. So, we're going to take a little time to write a script now in order to save a lot of time in the future.

### The code broken down

First, let's load some libraries that are useful for reshaping data.

```  
library("plyr")  
library("reshape2")  
```

(To install, e.g. the plyr package, simply type `install.packages("plyr")` in the R console.)

Then store the full names, including directory path, of the files in a character vector. Here, the input .csv files are stored in the subdirectory "input".

```  
in_files = list.files(path = "input", pattern="*.csv", full.names = T)  
```

Now, we'll use `lapply(...)`, one of base R's functionals, to read the input files into a list of data frames, which we call list_dfperday.

```  
list_dfperday = lapply(in_files, read.csv)  
```

`lapply()` loops over the the names of the files in `in_files`

-   to each file, apply the function `read.csv()`, which reads the contents of the file into a data frame
-   output the result into a list of data frames, called dfs, of the same length as the character vector containing the file names

Bind together (rbind) the data frames in the list by rows into a single data frame, so we can more conveniently subset the data by group.

```  
df = ldply(list_dfperday, rbind)  
```

In the `plyr` package, the first two letters in the "--ply" functions indicate what type of object is being transformed into another. In this case, we are reshaping a list ('l') of data frames into a data frame ('d'), hence "ldply".

Define a function to cast the data into a data frame with a shape specified by the formula ` day ~ id`: per *day* (x-variable), output the corresponding height (value.var) of each plant *id* (y-variable).

```  
cast_short = function(mydata) dcast(mydata, day ~ id, value.var = height)  
```

So the function "cast_short" takes as its argument a data frame "mydata" (containing columns "day" and "id") and returns a reshaped data frame with "day" on the rows and "id" on the columns.

Now apply the function we just defined to each treatment group. Store the outcome of each application of `cast_short` into a list. (Also compare to the earlier use of `ldply`.)

```  
list_dfpergroup = dlply(df, .(group), cast_short)  
```

It's finally time to write the formatted data frames to .csv files. We'll output them in a new directory called "output" with the aid of another base R functional `mapply`.

```  
outdir = "output"  
outnames = paste0(names(list_dfpergroup),".csv")

dir.create(outdir)  
mapply(function(x,y) write.csv(x, file.path(outdir,y), row.names=F),  
list_dfpergroup,  
outnames)  
```

`mapply` allows functions with multiple arguments to be applied in a loop. Here, we've defined an anonymous, i.e. unnamed, function within mapply that has two arguments: the value of *x* is given by list_dfpergroup, and *y* is given by the character vector outnames. In other words, mapply steps through the list and vector simultaneously, writing list_dfpergroup$_i$ to a file named outnames$_i$.

### The code in one piece

Now here's the code all in one piece. Note that the core reshaping takes place in three lines, starting at the line containing `ldply`.

```  
library("plyr")  
library("reshape2")

in_files = list.files(path = "input", pattern="*.csv", full.names = T)  
list_dfperday = lapply(in_files, read.csv)

df = ldply(list_dfperday, rbind)  
cast_short = function(mydata) dcast(mydata, day ~ id, value.var = height)  
list_dfpergroup = dlply(df, .(group), cast_short)

outdir = "output"  
outnames = paste0(names(list_dfpergroup),".csv")

dir.create(outdir)  
mapply(function(x,y) write.csv(x, file.path(outdir,y), row.names=F),  
list_dfpergroup,  
outnames)  
```
