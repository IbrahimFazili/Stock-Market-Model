# just a basic linear regression model of Google's stock prices
# beginning of my machine learning study

#!pip install quandl #<-- need this because quandl doesn't get recognized

import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate


df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

#this is the percent difference between the highest and lowest price of the 
#stock in the day
df['HL_change'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0

#this is the percent difference between the opening and closing price
df['percent_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_change', 'percent_Change', 'Adj. Volume']]

df.fillna(-99999, inplace=True)

#this is the number of days ahead we are predicting the price, subject to change
#the 0.1
predicted_days = int(math.ceil(0.1 * len(df)))

#this is what we want to predict, subject to change
predicting_col = 'Adj. Close'

df['Prediction'] = df[predicting_col].shift(-predicted_days)
df.dropna(inplace=True)

features = np.array(df.dropna(['Prediction'], 1))
prediction = np.array(df['Prediction'])

#features = preprocessing.scale(features)

y = np.array(df['Prediction'])

features_train, features_test, prediction_train, prediction_test = cross_validation.train_test_split(features, prediction, test_size = 0.2)

clf = LinearRegression()
clf.fit(features_train, predictin_train)
accuracy = clf.score(features_test, prediction_test)

print(accuracy)
