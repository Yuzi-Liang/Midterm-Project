import dateProcess
import Regression

import pandas as pd
import statsmodels.api as sm
import operator

def listMinus(l1, l2):
    l3 = l1[:]
    for i in l2:
        for j in l3:
            if i == j:
                l3.remove(i)
    return l3

predictor_list = ['id', 'date', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
       'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long',
       'sqft_living15', 'sqft_lot15']

sorted_list = []
R2_list = []

dftrain = pd.read_csv('../data/training_dataset.csv')
dftrain['date'] = dateProcess.dateConvert(dftrain['date'])
popList = ['id', 'zipcode']
for id in popList:
    dftrain.pop(id)
predictor_list = listMinus(predictor_list, popList)
Y = dftrain.pop('price')

for step in range(1, len(predictor_list)):
    R2 = [0] * (len(predictor_list) - len(sorted_list))



    for i, p in enumerate(listMinus(predictor_list, sorted_list)):  # pick a best model for each step

        dftrain2 = dftrain.copy()
        sorted_list.append(p)

        for predictor in listMinus(predictor_list, sorted_list):  # set predictors
            dftrain2.pop(predictor)

        X = sm.add_constant(dftrain2)
        est = Regression.OLSFit(X.astype(float), Y)
        R2[i] = est.rsquared
        sorted_list.pop(-1)

    max_index, max_number = max(enumerate(R2), key=operator.itemgetter(1))

    sorted_list.append(listMinus(predictor_list, sorted_list)[max_index])
    R2_list.append(max_number)



print(sorted_list)
print(R2_list)

print(len(sorted_list))
print(len(R2_list))



