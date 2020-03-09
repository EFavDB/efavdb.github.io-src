Title: Measles vaccination rate by USA state and relation to mean outbreak size
Date: 2015-02-25 13:40
Author: Damien RJ
Category: Case studies
Slug: vaccination-rates
Status: published
Attachments: wp-content/uploads/2015/02/measles_vaccine.png, wp-content/uploads/2015/02/measles_thumb.png

In this post, we provide a quick overview of the data and science of measles spread. Making use of python (code provided) we extract from a CDC data set the 2012 youth vaccination rate for each USA state -- see figure below. To aid in the interpretation of this data, we also review and describe the results of a generalized \`\`SIR" model for disease spread. The model -- analyzed in [our last post](http://http://efavdb.github.io/math-of-measles) -- predicts that measles outbreaks are supported only if the vaccination rate is below 94%. At higher rates, infection spread is suppressed, and outbreaks do not occur. As seen in the figure, the majority of the states sit just below this critical number, and so are predicted to support youth outbreaks.

<iframe width="600" height="533" frameborder="0" src="//plot.ly/~damienrj/179.embed"></iframe>

Measles vaccination rate by USA state for youths under 36 months in age, 2012. Dashed line at 94% is estimated critical vaccination rate needed to suppress outbreaks. The mean USA youth rate is about 91%.

#### **Introduction: History of measles in America**

Measles is a highly-contagious, serious illness estimated to currently be contracted by about 20 million individuals each year, globally. Just prior to the arrival of the first measles vaccine in 1963 (developed by [John Enders](http://en.wikipedia.org/wiki/John_Franklin_Enders) and his colleagues) approximately 500,000 Americans contracted the disease annually, approximately 50,000 of which required hospitalization -- a rate of 1/10. Among these individuals, approximately 500 would die each year, equating to a 1/1000 mortality rate. As yet, there is [no treatment](http://www.mayoclinic.org/diseases-conditions/measles/basics/treatment/con-20019675) available to combat the measles virus, once contracted. Consequently, similar hospitalization and mortality rates [continue to hold today](http://en.wikipedia.org/wiki/Measles#Epidemiology). Sadly, the mortality rate among the malnourished can be as high as 1/10.

<iframe width="600" height="533" frameborder="0" src="//plot.ly/~damienrj/262.embed"></iframe>

Here, the vaccination rate shown is for youths, under 48 months in first brach (up to 1985), and under 36 months in the latter branch.

Contemporary contraction rates in the USA are now extremely low, on the order of [50-500 per year](http://www.cdc.gov/measles/cases-outbreaks.html). This is likely a consequence of the strong local adoption of measles vaccinations, with 91% of young children here now receiving the vaccine prior to their third birthday. The most recent large-scale USA outbreak of the disease happened between the years of 1989 and 1991, when the vaccination rates of children were significantly lower, hovering around 70%. This outbreak centered within poorer, urban areas where the vaccination rates were [substantially lower](http://www.cdc.gov/vaccines/pubs/pinkbook/meas.html) than the national average. A summary plot of USA contraction counts and youth vaccination rates by year is shown above -- the two curves are highly anti-correlated. Note that this plot is **click and drag zoomable**, which is useful for setting the scale appropriately for recent years. Data [source 1](http://jid.oxfordjournals.org/content/189/Supplement_1/S17.long), [source 2](http://www.cdc.gov/mmwr/preview/mmwrhtml/mm6316a4.htm); no youth vaccination rate data available between 1985-1991. Full-population averages have been in the 90's [for some decades](http://www.nature.com/news/measles-by-the-numbers-a-race-to-eradication-1.16897), likely due to elementary school matriculation requirements.

#### **Modeling disease spread**

The striking USA historical data suggests a very strong relationship between the vaccination rate within a community and the frequency and size of the measles outbreaks that it supports. In fact, simple models for disease spread suggest a phase-transition-like (exhibiting abrupt changes) outbreak size dependence on vaccination rates. This is illustrated below, where we plot the predicted measles contraction rate against a population's vaccination rate -- as returned by a generalized [SIR model for disease spread](http://en.wikipedia.org/wiki/Epidemic_model#The_SIR_model): Notice that in the far left side of this plot, the model predicts that disease spread is completely suppressed. However, below a critical vaccination rate (the stated 94% mark -- a number consistent with [published estimates for measles](http://jid.oxfordjournals.org/content/196/10/1433.full)), outbreaks begin to be supported, growing in size with further decrease of the vaccination rate.

<iframe width="600" height="533" frameborder="0" src="//plot.ly/~damienrj/275.embed"></iframe>

The generalized SIR model predicts that a measles outbreak size changes in a phase-transition-like manner with vaccination rate. Further, at about 85% vaccination, the outbreak population fraction and the unvaccinated fraction curves cross. At this point, the outbreak captures nearly all unvaccinated and also a finite fraction of the vaccinated, who begin to become infected due to frequent encounters with disease.

A detailed study of the SIR model's [solution](http://efavdb.github.io/math-of-measles) is not necessary to understand why disease spread exhibits a phase-transition-like form. Qualitatively, this behavior is a consequence of a simple balance of rates: If the rate at which a disease spreads is greater than the rate at which the ill recover, outbreaks grow and expand. However, if patients recover more quickly than they can spread the disease, outbreak expansion is suppressed, and the number of infected individuals will decrease with time. The balance of these competing effects is tuned by the frequency of vaccination, which directly affects the first of these rates -- that at which the disease can spread. Because measles is [highly contagious](http://www.cdc.gov/measles/about/transmission.html), its balance point occurs around the relatively-high 94% mark seen in the figure -- this is the vaccination rate needed to have the average rate of disease spread just equal to the average rate of recovery. An info-graphic illustrating these points can be found [here](http://www.vaccines.gov/basics/protection/).

#### **Model implications for USA youth**

At the start of this post, we presented CDC estimates for the mean, by-state vaccination rates within the USA. Now that we have reviewed the results of the SIR model, we can begin to appreciate the significance of this data more deeply. First -- as we noted above -- we see that many states have youth vaccination rates that sit just below the critical 94% level, and thus on average should support small measles outbreaks. The graph of the previous section also allows us to estimate the mean size of a measles outbreak (once sparked) within any community below the critical vaccination rate: The further a state is from the 94% mark, the larger its mean outbreak size should be. Although all states are doing reasonably well, when considered on [a global scale](http://www.npr.org/blogs/goatsandsoda/2015/02/06/384068229/measles-vaccination-rates-tanzania-does-better-than-u-s), it is important to realize that many sit in a region of the plot where the response to a decrease in vaccination rate is most dramatic -- the curve's slope is largest just to the right of 94% vaccination. This means, e.g., that a 1% decrease in vaccination rate will result in a greater than 1% increase in the size of the average outbreak supported within that state. This observation is modestly worrisome, as the risk of contraction for all individuals -- even those vaccinated -- is always proportional to the number of cases present in any outbreak.

**Important caveats:**

-   Vaccination rates fluctuate between cities, neighborhoods, etc. This means that simple state averages may not accurately characterize your local community's vaccination rate -- the quantity most relevant to your personal infection risk. See, for instance, the plot for California by county shown [here](http://www.huffingtonpost.com/2015/02/03/measles-us-facts_n_6581922.html).
-   Our results are based on a descriptive, but simple model. They are intended only to provide one with a qualitative picture of the forces governing measles spread. Detailed, peer-reviewed treatments (this is just a blog...) can be found in the literature.
-   Consult a licensed physician for qualified information on vaccines, measles etc.

 

#### **Discussion**

Interestingly, [humans are the only known carriers](http://en.wikipedia.org/wiki/Measles#Cause) of the measles virus. Consequently, with [growing global vaccination rates](http://www.nature.com/news/measles-by-the-numbers-a-race-to-eradication-1.16897), it may one day soon be possible to totally extinguish the disease. Looking back on the historical USA data helps one realize that this would be a truly remarkable accomplishment! In fact, were the USA in isolation, our current vaccination rates would likely be sufficient to bring this about. However, we are not, and sporadic outbreaks continue to occur here, ignited through international travel of infected individuals. These outbreaks can occur because our youth vaccination rates are below the critical 94% level needed to suppress them.

The science of disease spread is very interesting. For those with a mathematical background, we suggest taking a look at [our prior post](http://http://efavdb.github.io/math-of-measles), where we solve the SIR model analytically. Many additional insights into disease spread -- not covered here -- can be gleaned through the study of this model. Likewise, those with a programming background can play with the code that we provide below to sort through the CDC's data sets in different ways. For instance, one can easily alter this code to view how vaccination rates vary by socio-economic background, rather than by state, etc. One can also use the same procedures to sort through many other interesting data sets provided by the CDC and others.

#### **Methods: Wrangling the CDC measles data sets**

##### **Grabbing and loading data**

In this section, we outline our numerical analysis of the CDC measles vaccination rate data set. To follow along, you must first download the files.  Current data can be found [here](http://www.cdc.gov/nchs/nis/data_files.htm), and data corresponding to years before 2009 [here](http://www.cdc.gov/nchs/nis/data_files_09_prior.htm).  Three files are needed.  The [Dataset file](ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/nis/nispuf12.dat), the [Codebook](ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NIS/NISPUF12_CODEBOOK.PDF) that explains how to read the dataset files, and the [Data User’s Guide](ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NIS/NISPUF12_DUG.PDF) which provides details about the data, including methodology and statistics descriptions.

In our analysis, we will make use of a few python packages.  In particular, we will use [Pandas](http://pandas.pydata.org/) to construct high performance data structures, called DataFrames. These are easy to use, and they allow for fast, straightforward data manipulation -- both helpful features for data wrangling. We will utilize the groupby DataFrame method, which enables one to easily segment data according to values along different feature directions. To illustrate, we will split our data by state name.  We will then use the [Plot.ly](https://plot.ly/) package to generate the interactive plots included above.

To get a feel for the CDC data, a good first step is to look at the data in a text editor.  Doing this, we quickly notice multiple rows of characters having no vernacular significance.  The codebook allows one to interpret these characters.  It also explains that each row corresponds to a different child surveyed, and that each row has a fixed number of entries, many corresponding to different vaccines. We will read these rows in one at a time -- making use of a for loop -- to save on memory. As each line is processed, we keep only what we need -- here that info relevant to the MMR vaccine.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'password')

#Create some empty lists to store the data
child_ID = []
house_ID = []
patient_data = []
measles = []
state = []
stratum = []
weights = [] #No virgin islands
weights_v = []
mmr = []

#First we need to read in the data file, and parse the data
#using the datasheet
with open('nispuf12.dat', 'r') as f:
	for line in f:
		child_ID.append(line[0:6])
		house_ID.append(line[6:11])
		patient_data.append(line[11:12])
		measles.append(line[260:261])
		state.append(line[181:183])
		stratum.append(line[88:92])
		weights.append(line[50:69])
		weights_v.append(line[31:50])
		mmr.append(line[261:262])
```

##### **Cleaning data**

Now that everything is parsed and loaded into arrays, we will insert our data into a dictionary with key given by the column header.  We then convert this into a DataFrame. To streamline the process, we will also replace all the missing values with a NAN, and also convert all relevant entries from string to number format.  We will also replace the stateID numbers with their written names.  Lastly, we will remove all the incomplete patient files.

```python
#Create a dataframe in pandas for data manipulation
d= {'child':child_ID, 'house':house_ID, 'state':state,
	'patient_data':patient_data, 'measles':measles,
	'MMR':mmr, 'stratum':stratum, 'weights':weights,
	'weights_v':weights_v}
data = pd.DataFrame(d);

#Clean up the data to assign . to NAN
data['measles'] = data['measles'].replace(
		['1', '0', '.'], [1, 0, 'NAN'])

#Convert the data to numberic values
data = data.convert_objects(convert_numeric=True)

#Replace the state ID code with the state's name
num,name = np.loadtxt(
		'state_ID.txt',unpack=True,dtype=str,delimiter=',')

data['state'] = data['state'].replace(
		num.astype(np.int64), name)

#Find all the values where there is complete provider data.
#We will look at only the complete patient records,
#and remove records column which is now only one value.
ind = np.where(data.patient_data==1)[0]
data = data.iloc[ind]
data.drop(['patient_data'],inplace=True,axis=1)
```

Below, we provide some examples of our resulting, cleaned data points. The weight columns here are described further below. The first of these is used for analyses including the Virgin Islands, the other when they are not.

```
MMR child house measles state stratum weights weights_v
0 1 11 1 1 Texas 1054 65.155698 120.163273
1 1 21 2 1 Texas 2055 33.652064 52.360361
3 1 41 4 1 Massachusetts 1002 216.529889 271.502218
5 1 61 6 1 Georgia 1025 231.557156 562.130094
6 1 71 7 1 South Carolina 1030 150.109737 238.018808

```

##### **Weighting to get averaged statistics**

We now have our data cleaned and ready to go. However, some additional work needs to be done before we can evaluate various statistics of interest. This is because the CDC data set is not a random sample, but instead a [stratified sample](http://en.wikipedia.org/wiki/Stratified_sampling) -- i.e. one geared towards obtaining reasonable accuracy among many minority groups, and not simply among the averaged population. The weight factors are the key to extracting averaged statistics from this data, as explained in the user guide. For example, the average is essentially just a weighted average, and the standard error can be calculated using a Taylor-Series approach. The easiest way to apply this to our data is to make use of custom functions. Once constructed, these can then be easily applied to different DataFrame groupings.

```python
# Lets define a function to caluclate the vaccination rate
# for the group we are looking at, and the standard error
def calculate_rate_and_error(data):
    # The rate is calucated useing a weighted average
    rate = (data.MMR * data.weights_v).sum() / data.weights_v.sum()
    
    # The error is calculated using the formula from the data sheet
    data['Z'] = data.weights_v*(data.MMR-rate) / data.weights_v.sum()
    zhi = data.groupby(['stratum','house']).agg(np.sum).Z
    zh = zhi.groupby(level='stratum').sum()
    # Number of households per stratum
    nk = zhi.groupby(level='stratum').count()
    zh = zh/nk
    
    stratum_labels = zh.index.values
    var=np.zeros(len(nk))
    ind = 0
    for a in stratum_labels:
        delta2 = (zhi.loc[a] - zh[a])**2
        delta2 = delta2.sum()
        var[ind]=(nk[a]/(nk[a]-1.)) * delta2
        ind += 1
    
    standard_error = np.sqrt(sum(var))
    return rate, standard_error
```

If we apply this function to our whole DataFrame, we will get the national MMR vaccination rate and standard error.

```
calculate_rate_and_error(data)
# output: (0.90767842904073048, 0.0043003916851249895)
```

##### **Data segmentation -- stats by group**

But we can also do more! If we first apply the DateFrame's groupby method, we can split the data along any feature of interest. For example, below we split the data along the state column. This generates subgroups for each state. Next, we use the apply method to run our custom function on all the different groups of data. We then clean up the output, unzip the tuple and generate a graph showing the MMR vaccination rate by state. It should be evident that with only modest effort, one can modify this code to group the data in many varying ways -- all that needs to be done is to adjust the arguments of the groupby command.

```python
# Now that we have our function it is easy to calculate values
# for any group.

# To examine rates by state, we will group by state
grouped=data.groupby('state')

# We then apply our function to the grouped data, and save
# it as a data frame
result = pd.DataFrame(grouped.apply(calculate_rate_and_error))

# To conver the results from:
# state
# Alabama (0.931323319509, 0.017837146103)
# Alaska (0.862202058663, 0.0257844894834)
# to
# Rate Standard Error
# state
# Alabama 0.931323 0.017837
# Alaska 0.862202 0.025784
# We use the following code

new_col_list = ['Rate','Standard Error']
for n,col in enumerate(new_col_list):
	result[col] = result[0].apply(lambda x: x[n])
	result.drop(0, axis=1, inplace=True)

# Make a sorted copy of the data
sorted = result.sort_index(by='Rate', ascending=True)
result['Rate']=result['Rate']*100

# Save a csv file if wanted
result.to_csv('Rate 2012.csv', float_format='%5.2f')

# Generate an online plot
data = Data([
	Bar(
		y=sorted.index.values ,
		x=sorted['Rate'],
		orientation='h'
	)
])
plot_url = py.plot(data, filename='plot')
```
