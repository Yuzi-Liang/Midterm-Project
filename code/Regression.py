import dateProcess

import pandas as pd
import numpy as np
import statsmodels.api as sm
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def OLSFit(X, Y):
    """
    - X: Predictors dataframe
    - Y: Targets dataframe
    """
    est = sm.OLS(Y, X)
    est2 = est.fit()
    return est2

def RSS(y_true, y_predicted):
    """
    - y_true: Actual values
    - y_predicted: Predicted values
    """
    y_true = np.array(y_true)
    y_predicted = np.array(y_predicted)
    rss = np.sum(np.square(y_true - y_predicted))
    return rss

def RSE(y_true, y_predicted):
    """
    - y_true: Actual values
    - y_predicted: Predicted values
    """
    rss = RSS(y_true, y_predicted)
    rse = math.sqrt(rss / (len(y_true) - 2))
    return rse

# dftrain = pd.read_csv('../data/training_dataset-2.csv')
# dftest = pd.read_csv('../data/test_dataset-2.csv')

dftrain = pd.read_csv('../data/kc_house_data.csv')

popList = ['id', 'date', 'zipcode', 'yr_renovated', 'lat', 'long']
for id in popList:
    dftrain.pop(id)

Y = dftrain.pop('price')
X = sm.add_constant(dftrain)

est = OLSFit(X, Y)
Y_predict = est.predict(X)
print(est.summary())
plt.scatter(Y, Y_predict, s=0.5)
plt.plot(Y, Y, c='r')
plt.show()