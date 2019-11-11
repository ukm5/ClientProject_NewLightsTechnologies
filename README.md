# Client Project: Disaster Prediction with Twitter

### Introduction

The goal of this project is twofold 1) To collect tweet message data relating to the #wildfires Twitter hashtag using Twitters's API and 2) Use the tweet message data in conjunction with a Logistic Regression in order to train a model that will classify Tweets into several classes based on their relevance to a predicted disaster type. Success will be evaluated by the models ability to accurately classify Tweets based on the accuracy score of the testing data. Being able to accurately predict the disaster connected to any given Tweet may be of use to disaster relief organizations seeking to get firsthand reports of disasters in real time almost instantaneously after any given Tweet is posted publicly. These firsthand reports may be used to decide how to more efficiently distribute relief personnel and other humanitarian assets and resources in the case of emergency. 

#### Twitter API Scraping & Data Collection

Twitter's REST API was used in conjunction with Tweepy and a Twitter Developer Account to pull Tweets into Pandas DataFrames. Our Twitter Developer account was used to generate a consumer key, consumer secret, access token and access secret. These Twitter credentials were saved as a .json file and an instance of Tweepy's API class was authenticated using these credentials. A class called StreamListener was borrowed from a past project by Edithlyer. At this point, Tweet data was pulled in real time and converted into a Pandas DataFrame to be fed into the EDA and cleaning phase.

Additional tweet data was gathered from CrisisLex.org (https://crisislex.org/), a website that is used to house datasets and lexicons that are useful to those interested broadcasting information and modeling disaster response.

#### EDA and Data Cleaning

Tweets regarding the wildfires and Tweets related to other natural disasters were first read into Pandas DataFrames from .csv files originating from CrisisLex.org (https://crisislex.org/). Columns were converted to lowercase and stripped of punctuation. Information regarding informativeness was added to the data and the data were labeled as being of the fire class with label '0' and output to .csv. For each of the disaster types, a label was assigned to the disaster according to the following scheme:

Fire: 0
Tropical Storm: 1
Earthquakes: 2
Man-Made: 3
Floods: 4
Others: 5
Unrelated: 99

For bookkeeping purposes, the name of each .csv file was then appended to a list. Finally, all of the labelled disaster data was compiled into a master file.

#### Preprocessing and Visualizations

The data was read into Pandas DataFrames, English stopwords were removed and the frequency of the most common words contained within fire related tweets was plotted on a bar chart for visualization. The data was then output to .csv to be fed into the modeling stage.

#### Modeling

The first model that was developed was a binary classifier that labeled each tweet in the dataset as being a flood or not a flood (1 and 0 respectively). For this model, a pipeline was used to vectorize the text data and then apply logistic regression to classify the Tweets. The gridsearch considered parameters such as the number of maximum features, turned all letters to lowercase, removed English stopwords and considered 1-grams and 2-grams. The model was fit and scored with statistics as follows:

CVEC/LR Training Score: 98.96%
CVEC/LR Testing Score:  97.82%

The second model that was developed was a multiclass classification algorithm that labelled each disaster according to the following scheme:

Fire: 0
Tropical Storm: 1
Earthquakes: 2
Man-Made: 3
Floods: 4
Others: 5

For this model, a pipeline was used to vectorize the text data using TFIDF and then classify the Tweets using the OneVsRestClassifier. The gridsearch varied parameters such as the number of maximum features, lettering case, the presence of English stopwords and the n-gram range. The model was fit and scored with statistics as follows:

CVEC/LR Training Score: 88.30%
CVEC/LR Testing Score:  87.73%

The third model that was implemented was a KMeans clustering algorithm with 4 clusters. In reference to our project, Text Clustering aims at grouping similar text units together within a collection of documents. This task is unsupervised since, unlike in text classification, we have no prior idea about the categories. Running k-means  for the same data set with multiple parameters, the results of the clustering process will be different and hence the accuracy calculated. The word ‘clustering’ means grouping similar things together. The most commonly used clustering method is K-Means (because of its simplicity). Preprocess your data before performing K-Means: K-Means is sensitive to outliers, just like every other algorithm that uses average/mean values.
Clustering was also a way of seeing strategies to improve the multiclass model scores. Multiclass classifiers have overlapping vocabulary and increasing dimesnions wouldbe useful in better classifying. In our model reported here, we use all the parameters in our original multiclass model and additional cluster labels. We use 5 cluster labels and since clustering is a blackbox,the assumption is the vocabulary is getting clustered based on underlying similarities, for example, there could be words common to floods and tropical storms. And this is exactly what we hope our model will capture. The model showed significant improvement as shown here:

CVEC/LR Training Score: 95.02%
CVEC/LR Testing Score:  92.28%

Following the creation of the three models, the team realized that about half of the fire-related tweets were actually duplicates and dropped the unneccesary data. 45% of the freshly scraped California Wildfire tweets were duplicates. Our end objective was to see the effectof our model on current or recent disaster. We employed our multiclass classifier model on the California wildfire related tweets to observe tweets that show resemblance to those from flood or man-made disaster tweets. Our model classified the CA wildfiretweets into the categories mentioned above. It is not surprising that no tweets were classified as Tropical Storm. The remaining tweets were classified as follows:

| Disaster Type | Percentage|
|---|---|---|
| Man-made | 39.47 |
| Fire| 26.36 |
| Floods | 20.24 |
| Others (Haze, fog etc) | 0.21 |
| Earthquakes | 0.04 |
| Unrelated | 13.68 |

While this at first might seem incorrect, it is useful to realize that some of the tweets that were tagged as floods showed vocabulary similar to those in tweets from flood related areas. For example, some of the tweets tagged as floods were reporting the need for drinking water, water contamination, and road closures/power outages. The latter two things, such as road closures and power outages, are more common in flood affected areas. And this is exactly what our model is promised to do and is doing it reasonably well with room for large improvements. 

#### Executive Summary

Pre-labelled tweets and text messages were scraped from Twitter’s API from social media and messaging that have taken place following past natural disasters. During and post disasters it is  difficult to recognize critical tweets that require immediate attention from response teams, and those which do not. Survey says, typically only 1 in 1000 messages actually require direct attention. This mechanism is more helpful in capturing the nuance in the text accurately as compared to simply using a keyword search. After initial cleaning the data and constructing, an ML pipeline is constructed, maximising accuarcy. Finally the model is to be deployed to a web app where new messages can be predicted and categorised. 

CONCLUSION: This project created a supervised machine learning model using natural language processing that accurately categorised tweets/messages to be forwarded to relevant disaster response teams. 

#### References and Citations

A. Olteanu, C. Castillo, F. Diaz, S. Vieweg. 2014. CrisisLex: A Lexicon for Collecting and Filtering Microblogged Communications in Crises. In Proceedings of the AAAI Conference on Weblogs and Social Media (ICWSM'14). AAAI Press, Ann Arbor, MI, USA.
