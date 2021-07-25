import pandas as pd

ratings = pd.read_csv('C:/users/user/Desktop/Нетология/01. Подготовка/ratings.csv')

print(ratings.tail(5))

ItData = ratings.groupby( by = ['userId']).agg([min,max]).reset_index()
ItData['diff'] = ItData['timestamp']['max'] - ItData['timestamp']['min']

LT = ItData['diff'].mean()

print(LT / 3600 / 24)