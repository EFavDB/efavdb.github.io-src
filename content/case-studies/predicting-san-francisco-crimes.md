Title: Machine learning to predict San Francisco crime
Date: 2015-07-20 03:01
Author: damienrj
Category: Case studies
Slug: predicting-san-francisco-crimes
Status: published
Attachments: wp-content/uploads/2015/07/Insel_Alcatraz.jpg

In today's post, we document our submission to the recent [Kaggle](https://www.kaggle.com/c/sf-crime) competition aimed at predicting the category of San Francisco crimes, given only their time and location of occurrence. As a reminder, Kaggle is a site where one can compete with other data scientists on various data challenges.  We took this competition as an opportunity to explore the Naive Bayes algorithm. With the few steps discussed below, we were able to quickly move from the middle of the pack to the top 33% on the competition leader board, all the while continuing with this simple model!

  
[Follow @efavdb](http://twitter.com/efavdb)  
Follow us on twitter for new submission alerts!

Introduction
------------

As in all cities, crime is a reality San Francisco: Everyone who lives in San Francisco seems to know someone whose car window has been smashed in, or whose bicycle was stolen within the past year or two. Even Prius' car batteries are apparently considered [fair game](http://abc7news.com/news/exclusive-car-battery-thefts-from-hybrid-cars-on-the-rise-in-san-francisco-/725532/) by the city's diligent thieves.  The challenge we tackle today involves attempting to guess the class of a crime committed within the city, given the time and location it took place. Such studies are representative of efforts by many police forces today: Using machine learning approaches, one can get an improved understanding of which crimes occur where and when in a city -- this then allows for better, [dynamic allocation of police resources](http://www.forbes.com/sites/emc/2014/06/03/data-analysis-helps-police-departments-fight-crime/). To aid in the SF [challenge](https://www.kaggle.com/c/sf-crime), Kaggle has provided about 12 years of crime reports from all over the city -- a data set that is pretty interesting to comb through.

Here, we outline our approach to tackling this problem, using the Naive Bayes classifier. This is one of the simplest classification algorithms, the essential ingredients of which include combining [Bayes' theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem "Bayes' theorem") with an independence assumption on the features (this is the "naive" part).  Although simple, it is still a popular method for text categorization. For example, using word frequencies as features, this approach can accurately classify emails as spam, or whether a particular a piece of text was written by a specific author.  In fact, with careful preprocessing, the algorithm is often [competitive](http://people.csail.mit.edu/jrennie/papers/icml03-nb.pdf) with more advanced methods, including support vector machines.

 

**Loading package and data**
----------------------------

Below, we show the relevant commands needed to load all the packages and training/test data we will be using. As in previous posts, we will work with [Pandas](http://pandas.pydata.org/) for quick and easy data loading and wrangling. We will be having a post dedicated to Pandas in the near future, so stay tuned! We start off with using the parse_dates method to convert the Dates column of our provided data -- which can be downloaded [here](https://www.kaggle.com/c/sf-crime/data)-- from string to datetime format.

```  
import pandas as pd  
from sklearn.cross_validation import train_test_split  
from sklearn import preprocessing  
from sklearn.metrics import log_loss  
from sklearn.naive_bayes import BernoulliNB  
from sklearn.linear_model import LogisticRegression  
import numpy as np

#Load Data with pandas, and parse the first column into datetime  
train=pd.read_csv('train.csv', parse_dates = ['Dates'])  
test=pd.read_csv('test.csv', parse_dates = ['Dates'])  
```

The training data provided contains the following fields:

***Date*** -  date + timestamp  
***Category*** - The type of crime, Larceny, etc.  
***Descript*** - A more detailed description of the crime.  
***DayOfWeek*** - Day of crime: Monday, Tuesday, etc.  
***PdDistrict ***- Police department district.  
***Resolution***- What was the outcome, Arrest, Unfounded, None, etc.  
***Address*** - Street address of crime.  
***X and Y*** - GPS coordinates of crime.

As we mentioned earlier, the provided data spans almost 12 years, and both the training data set and the testing data set each have about 900k records. At this point we have all the data in memory. However, the majority of this data is categorical in nature, and so will require some more preprocessing.

How to handle categorical data
------------------------------

Many machine learning algorithms -- including that which we apply below -- will not accept categorical, or text, features. What is the best way to convert such data into numerical values? A natural idea is to convert each unique string to a unique value.  For example, in our data set we might take the crime category value to correspond to one numerical feature, with Larceny set to 1, Homicide to 2, etc.  However, this scheme can cause problems for many algorithms, because they will incorrectly assume that nearby numerical values imply some sort of similarity between the underlying categorical values.

To avoid the problem noted above, we will instead binarize our categorical data, using vectors of 1's and 0's. For example, we will write

    larceny = 1,0,0,0,...
    homicide = 0,1,0,0,...
    prostitution  = 0,0,1,0,...
    ...

 

There are a variety of methods to do this encoding, but Pandas has a particularly nice method called [get_dummies()](http://pandas.pydata.org/pandas-docs/version/0.13.1/generated/pandas.get_dummies.html) that can go straight from your column of text to a binarized array.  Below, we also convert the crime category labels to integer values using the method [LabelEncoder](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html), and use Pandas to extract the hour from each time point. We then convert the districts, weekday, and hour into binarized arrays and combine them into a new dataframe. ** ** We then split up the train_data into a training and validation set so that we have a way of accessing the model performance while leaving the test data untouched.

 

```  
#Convert crime labels to numbers  
le_crime = preprocessing.LabelEncoder()  
crime = le_crime.fit_transform(train.Category)

#Get binarized weekdays, districts, and hours.  
days = pd.get_dummies(train.DayOfWeek)  
district = pd.get_dummies(train.PdDistrict)  
hour = train.Dates.dt.hour  
hour = pd.get_dummies(hour)

#Build new array  
train_data = pd.concat([hour, days, district], axis=1)  
train_data['crime']=crime

#Repeat for test data  
days = pd.get_dummies(test.DayOfWeek)  
district = pd.get_dummies(test.PdDistrict)

hour = test.Dates.dt.hour  
hour = pd.get_dummies(hour)

test_data = pd.concat([hour, days, district], axis=1)

training, validation = train_test_split(train_data, train_size=.60)  
```

 

**Model development**
---------------------

For this competition the metric used to rate the performance of the model is the multi-class [log_loss](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html) -- smaller values of this loss correspond to improved performance.

#### First pass

For our first quick pass, we used just the day of the week and district for features in our classifier training. We also carried out a Logistic Regression (LR) on the data in order to get a feel for how the Naive Bayes (NB) model was performing. The results from the NB model gave us a log-loss of 2.62, while LR after tuning was able to give 2.62. However, LR took 60 seconds to run, while NB took only 1.5 seconds! As a reference, the current top score on the leader board is about 2.27, while the worst is around 35. Not bad performance!

```  
features = ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday',  
'Wednesday', 'BAYVIEW', 'CENTRAL', 'INGLESIDE', 'MISSION',  
'NORTHERN', 'PARK', 'RICHMOND', 'SOUTHERN', 'TARAVAL', 'TENDERLOIN']

training, validation = train_test_split(train_data, train_size=.60)  
model = BernoulliNB()  
model.fit(training[features], training['crime'])  
predicted = np.array(model.predict_proba(validation[features]))  
log_loss(validation['crime'], predicted)

#Logistic Regression for comparison  
model = LogisticRegression(C=.01)  
model.fit(training[features], training['crime'])  
predicted = np.array(model.predict_proba(validation[features]))  
log_loss(validation['crime'], predicted)

```

 

#### Submission code

```  
model = BernoulliNB()  
model.fit(train_data[features], train_data['crime'])  
predicted = model.predict_proba(test_data[features])

#Write results  
result=pd.DataFrame(predicted, columns=le_crime.classes_)  
result.to_csv('testResult.csv', index = True, index_label = 'Id' )  
```

With the above model performing well, we used our code to write out our predictions on the test set to csv format, and submitted this to Kaggle. It turns out we got a score of 2.61 which is slightly better than our validation set estimate. The was a good enough score to put us in the to 50%. Pretty good for a first try!

#### Second pass

To improve the model further, we next added the time to the feature list used in training. This clearly provides some relevant information, as some types of crime happen more during the day than the night. For example, we expect public drunkenness to probably go up in the late evening.  Adding this feature we were able to push our log-loss score down to 2.58 -- quick and easy progress!  As a side note, we also tried leaving the hours as a continuous variable, but this did not lead to any score improvements.  After training on the whole data set again, we also get 2.58 on the test date. This moved us up another 32 spots, giving a final placement of 76/226!

```  
features = ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday',  
'Wednesday', 'BAYVIEW', 'CENTRAL', 'INGLESIDE', 'MISSION',  
'NORTHERN', 'PARK', 'RICHMOND', 'SOUTHERN', 'TARAVAL', 'TENDERLOIN']

features2 = [x for x in range(0,24)]  
features = features + features2  
```

Discussion
----------

Although Naive Bayes is a fairly simple model, properly wielded it can give great results.  In fact, in this competition our results were competitive with teams who were using much more complicated models, e.g. neural nets. We also learned a few other interesting things here: For example, Pandas' get_dummies() method looks like it will be a huge timesaver when dealing with categorical data. Till next time -- keep your Prius safe!  
[![Open GitHub Repo](http://efavdb.com/wp-content/uploads/2015/03/GitHub_Logo.png)](https://github.com/EFavDB/SF-Crime "GitHub Repo")
