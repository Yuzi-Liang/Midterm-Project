import dateProcess

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

dftrain = pd.read_csv('../data/training_dataset.csv')
dftrain['date'] = dateProcess.dateConvert(dftrain['date'])
for i in range(0, len(dftrain['sqft_lot'])):
    dftrain['sqft_lot'][i] = 1/dftrain['sqft_lot'][i]

describe = dftrain.describe()
describe.to_csv('summary.csv')

predictor_list = ['id', 'date', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
       'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above',
       'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long',
       'sqft_living15', 'sqft_lot15']
axs = [0]*3
fig1, axs[0] = plt.subplots(nrows=3, ncols=3)
fig2, axs[1] = plt.subplots(nrows=3, ncols=3)
fig3, axs[2] = plt.subplots(nrows=3, ncols=3)

plt.subplots_adjust(left=0.03, bottom=0.05, right=0.97, top=0.95, wspace=0.2, hspace=0.3)
i = 0
j = 0
for predictor in predictor_list:
    dftrain.plot.scatter(x=predictor, y='price', s=0.5, ax=axs[j][i // 3, i % 3])
    i = i + 1
    if i == 9:
        i = 0
        j = j + 1

plt.show()