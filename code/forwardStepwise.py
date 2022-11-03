import dateProcess
import Regression

import pandas as pd
import numpy as np
import statsmodels.api as sm
import math
import operator

predictor_list = ['id', 'date', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
       'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long',
       'sqft_living15', 'sqft_lot15']

sorted_list = []

for step in range(1, len(predictor_list)):
    R2 = [0] * len(predictor_list)

    for i, p in enumerate(predictor_list):
        dftrain = pd.read_csv('../data/training_dataset.csv')
        dftrain['date'] = dateProcess.dateConvert(dftrain['date'])
        Y = dftrain.pop('price')

        sorted_list.append(p)
        for predictor in list(set(predictor_list)^set(sorted_list)):
            dftrain.pop(predictor)
        X = sm.add_constant(dftrain)
        est = Regression.OLSFit(X.astype(float), Y)
        R2[i] = est.rsquared
        sorted_list.pop(-1)

    max_index, max_number = max(enumerate(R2), key=operator.itemgetter(1))
    sorted_list.append(predictor_list[max_index])


