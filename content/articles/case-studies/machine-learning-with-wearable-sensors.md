Title: Machine learning with wearable sensors
Date: 2015-01-09 12:34
Author: Damien RJ
Category: Case studies, Guest posts
Tags: guest
Slug: machine-learning-with-wearable-sensors
Status: published

A guest post, contributed by Damien Ramunno-Johnson ([LinkedIn](https://www.linkedin.com/profile/view?id=60223336&authType=NAME_SEARCH&authToken=LOV_&locale=en_US&trk=tyah2&trkInfo=tarId%3A1420748440448%2Ctas%3Adamien%2Cidx%3A1-1-1), [bio-sketch](http://www.efavdb.com/about))

  



**Introduction**  
Wearable sensors have become increasingly popular over the last few years with the success of smartphones, fitness trackers, and smart watches. All of these devices create a large amount of data that is ideal for machine learning. Two early examples are the FitBit and Jawbone's up band, both of which analyze sensor input to determine how many steps the user has taken, a metric which is helpful for measuring physical activity. There is no reason to stop there: With all of this data available it is also possible to extract more information. For example, fitness trackers coming out now can also analyze your sleep.

In that spirit, I'm going to show here that it is pretty straightforward to make an algorithm that can differentiate between 6 different states.

1.  Walking
2.  Walking Upstairs
3.  Walking Downstairs
4.  Sitting
5.  Standing
6.  Laying

To do this I am going to use [Python](https://www.python.org/), [Sklearn](http://scikit-learn.org/) and [Plot.ly](https://plot.ly). Plot.ly is a wonderful plotting package that makes interactive graphs you can share. The first step is to import all of the relevant packages.

**Load packages and source data**  
For this example, I used one of the datasets available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones). For this data set 30 subjects were recorded performing activities of daily living (ADL) while carrying a waist-mounted smartphone (Samsung Galaxy II) with embedded inertial sensors. A testing dataset and training dataset are provided. The dataset has 561 features which were created from the sensor data: XYZ acceleration, etc.

```  
from numpy import loadtxt  
import numpy as np  
from sklearn import svm, grid_search  
from sklearn.metrics import accuracy_score, f1_score  
from sklearn.feature_selection import SelectPercentile, f_classif  
import plotly.plotly as py  
from plotly.graph_objs import *  
```

Now that we have loaded all of our packages, it is time to import the data into memory. This data set is not large enough to cause any memory issues, so go ahead and load the whole thing.

```  
data_test = loadtxt("./Wearable/UCI_HAR_Dataset/test/X_test.txt")  
label_test=loadtxt("./Wearable/UCI_HAR_Dataset/test/y_test.txt")  
data_train = loadtxt("./Wearable/UCI_HAR_Dataset/train/X_train.txt")  
label_train = loadtxt("./Wearable/UCI_HAR_Dataset/train/y_train.txt")  
```

**Feature selection**  
Given that this data set has training and testing data with labels, it makes sense to do supervised machine learning. We have over 500 potential features to use, which is a lot. Let's see if we can get by with fewer features. To do that, we will use SK-learn'€™s SelectKBest to keep the top 20 percent of the features, and then transform the data.

```  
selector = SelectPercentile(f_classif, 20)  
selector.fit(data_train, label_train)  
data_train_transformed = selector.transform(data_train)  
data_test_transformed = selector.transform(data_test)  
```

**Machine learning**  
At this point you need to decide which algorithm you want to use. I tried a few of them and got the best results using a [Support Vector Machine](http://scikit-learn.org/stable/modules/svm.html) (SVM). SVMs attempt to determine the decision boundary between two classes that is as far away from the data of both classes as possible. In general they work pretty well.

Let's try some parameters and see how good our results are.

```  
clf = svm.SVC(kernel="rbf", C=1)  
clf.fit(data_train_transformed, label_train)  
pred=clf.predict(data_test_transformed)

print "Accuracy is %.4f and the f1-score is %.4f " % (  
accuracy_score(pred, label_test), f1_score(label_test, pred))  
```

 

```  
>>Accuracy is 0.8812 and the f1-score is 0.8788  
```

**Optimization**  
That's not too bad, but I think we can still optimize our results some more. We could change the parameters manually, or we can automate the task using a [grid search](http://scikit-learn.org/stable/modules/generated/sklearn.grid_search.GridSearchCV.html). This is a handy module that allows you to do a parameter sweep. Below, I set up a sweep using two different kernels and various penalty term values (C) to see if we can raise our accuracy.

```  
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10, 100, 1000, 10000]}  
svr = svm.SVC()  
clf = grid_search.GridSearchCV(svr, parameters)  
clf.fit(data_train_transformed, label_train)  
pred=clf.predict(data_test_transformed)

print "Accuracy is %.4f and the f1-score is %.4f " % (  
accuracy_score(pred, label_test), f1_score(label_test, pred))  
```

 

```  
>>Accuracy is 0.9430 and the f1-score is 0.9430  
```

**Visualization**  
Looks like we are getting pretty good accuracy for using only 20% of the features available to us. You may have also noticed that I am outputting the [F1-Score](http://en.wikipedia.org/wiki/F1_score) which is another measure of the accuracy which takes into account the precision and the recall.

Now let's plot some of these data points to see if we can visualize why this is all working. Here, I am using Plot.ly to make the plot. You can make the plots many different ways including converting matplotlib plots into these online plots. If you click on the "play with this data" link at the bottom of the figure (or click [here](https://plot.ly/~Damien RJ/104)) you can see the code used to make the plot.

[iframe src="https://plot.ly/~Damien RJ/104" width="100%" height="680"]

I picked two of the features to plot, the z acceleration average, and the z acceleration standard deviation. Note, the gravity component of the acceleration was removed and placed into its own feature. Only 3/6 labels are being plotted to make it a little easier to see what is going on. For example, it is easy to see that the walking profile in the top graph differs significantly from those of standing and laying in the bottom two.

**Discussion**  
From the graphs above alone, it would be difficult to differentiate between laying and standing. We might be able to comb through different combinations of features to find a set that is more easily distinguishable, but we are limited by the simple fact that it is hard to visualize data in more than 3 dimensions. If it turns out that more than a handful of features need to be considered simultaneously to separate the different classes, this approach will fail. In contrast, we have seen in our SVM analysis above that it is actually pretty easy to use machine learning to pick out, with high accuracy, a variety of motions from the sensor data. This is a neat application that is currently being applied widely in industry. It illustrates why machine learning is so interesting in general: It allows us to automate data analysis, and apply it to problems where a by-hand, visual analysis is not possible.
