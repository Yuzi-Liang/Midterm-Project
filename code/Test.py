import readFile
import Regression

dftest = readFile.testingFile()
est = Regression.regressionResult()
print(est.summary())
X = 
Y_predict = est.predict(dftest)



