import dateProcess
import Regression

import pandas as pd
import numpy as np
import statsmodels.api as sm
import math

predictor_list = ['id', 'date', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
       'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long',
       'sqft_living15', 'sqft_lot15']

sorted_list = []
R2 = [0]*len(predictor_list)
dftrain = pd.read_csv('../data/training_dataset.csv')
dftrain['date'] = dateProcess.dateConvert(dftrain['date'])
Y = dftrain.pop('price')

for i, p in enumerate(predictor_list):
    sorted_list.append(p)
    for predictor in list(set(sorted_list)^set(predictor_list)):
        print(predictor)
        print()
        dftrain.pop(predictor)
    X = sm.add_constant(dftrain)
    est = Regression.OLSFit(X, Y)
    R2[i] = est.rsquared
    sorted_list.pop(-1)

