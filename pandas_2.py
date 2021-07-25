import pandas as pd
import numpy as np



#trainings = pd.read_csv('C:/Users/user/Desktop/Нетология/01. Подготовка/ds3-spring-2018/0. Preparatory week/0.2 Python for DS/train.csv')


#print(trainings.tail(10))

datalist = [
    {'date': '2017-07-01', 'value': 100},
    {'date': '2017-07-02', 'value': 200},
    {'date': '2017-07-03', 'value': 300},
    {'date': '2017-07-04', 'value': 400},
    {'date': '2017-07-05', 'value': 500},
]

dataListPd = pd.DataFrame(datalist)

dataDict = {
    'date': ['2017-07-01', '2017-07-02', '2017-07-03', '2017-07-04', '2017-07-05'],
    'value': [100,200,300,400,500]
}

dataDictPd = pd.DataFrame.from_dict(dataDict)

dataNP = np.random.rand(3)

dataSeriesPd = pd.Series(dataNP, index=['first','second','third'])

print(dataSeriesPd)
