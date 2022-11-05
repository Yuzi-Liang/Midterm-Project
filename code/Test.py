import readFile
import Regression

import statsmodels.api as sm

dftest = readFile.testingFile()
est = Regression.regressionResult()
print(est.summary())
X = sm.add_constant(dftest)
Y_predict = est.predict(X)
print(Y_predict)




