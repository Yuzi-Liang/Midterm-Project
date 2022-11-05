import readFile
import Regression

import statsmodels.api as sm
import pandas as pd
import numpy as np


def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


dftest = readFile.testFile()
est = Regression.regressionResult()
X = sm.add_constant(dftest)
Y_predict = est.predict(X)

# export the .csv file
dfOutput = pd.read_csv('../data/test_dataset.csv')
temp = []
for each in Y_predict:
    temp.append(each)
dfOutput['price'] = temp
dfOutput = dfOutput[['id', 'price']]
dfOutput.to_csv('PredictPrice.csv', index=False)





