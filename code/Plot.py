import readFile

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

dftrain = readFile.trainingFile()
predictor_list = readFile.predictor_list

describe = dftrain.describe()
# describe.to_csv('summary.csv')

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