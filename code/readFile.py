import pandas as pd
import dateProcess

def trainingFile():
    dftrain = pd.read_csv('../data/training_dataset.csv')

    # preprocessing
    dftrain['renovated_time'] = dateProcess.renovatedTime(dftrain['date'], dftrain['yr_built'], dftrain['yr_renovated'])
    dftrain['date'] = dateProcess.dateConvert(dftrain['date'])
    dftrain['isRenovated'] = dateProcess.isRenovated(dftrain['yr_renovated'])
    dftrain.pop('yr_renovated')

    for i in range(0, len(dftrain['sqft_lot'])):
        dftrain['sqft_lot'][i] = 1/dftrain['sqft_lot'][i]
        dftrain['sqft_lot15'][i] = 1/dftrain['sqft_lot15'][i]

    popList = ['id', 'zipcode']
    for id in popList:
        dftrain.pop(id)
    return dftrain

def testingFile():
    dftrain = pd.read_csv('../data/test_dataset.csv')

    # preprocessing
    dftrain['renovated_time'] = dateProcess.renovatedTime(dftrain['date'], dftrain['yr_built'], dftrain['yr_renovated'])
    dftrain['date'] = dateProcess.dateConvert(dftrain['date'])
    dftrain['isRenovated'] = dateProcess.isRenovated(dftrain['yr_renovated'])
    dftrain.pop('yr_renovated')

    for i in range(0, len(dftrain['sqft_lot'])):
        dftrain['sqft_lot'][i] = 1 / dftrain['sqft_lot'][i]
        # dftrain['sqft_lot15'][i] = 1/dftrain['sqft_lot15'][i]

    popList = ['id', 'zipcode']
    for id in popList:
        dftrain.pop(id)
    return dftrain

predictor_list = ['date', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
       'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement', 'yr_built', 'lat', 'long',
       'sqft_living15', 'sqft_lot15', 'renovated_time', 'isRenovated']