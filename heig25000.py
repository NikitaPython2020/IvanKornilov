import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

data = pd.read_csv('C:/Users/user/Desktop/Нетология/01. Подготовка/ds3-spring-2018/0. Preparatory week/0.3 Math and stat/hw_25000.csv', names = ['index','height_inches','weight_pounds'] , header = 0)

data['height_inches']=data['height_inches']*2.54



zheight = stats.mstats.zscore(data['height_inches'])
#print(zheight)

#print(np.mean(zheight), np.std(zheight))

#plt.hist(zheight,bins = 50)

#stats.probplot(zheight,dist='norm',plot = plt)

#plt.show()

customheight = 185

z5core = (customheight-np.mean(data['height_inches'])) / np.std(data['height_inches'])
#print(1 - stats.norm.cdf(z5core))
#print(stats.norm.interval(0.99))

sample = data.head(100)

se = np.std(sample['height_inches'])/np.sqrt(len(sample['height_inches']))

confidenceCoef = stats.norm.interval(0.95)[1]

print(
    np.mean(sample['height_inches']) - confidenceCoef*se,
    np.mean(sample['height_inches']) + confidenceCoef * se
)

bins = np.linspace(150, 190, 50)

data['sample'] = data['height_inches'] + 3

#plt.hist(data['height_inches'], bins, alpha = 0.5)
#plt.hist(data['sample'].head(20), bins, alpha = 0.5)

#plt.show()

print(stats.ttest_1samp(sample,data['height_inches'].mean()))

data['height_inches'].plot.density()

plt.show()
