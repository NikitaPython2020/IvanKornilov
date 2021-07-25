import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.rc("font", size=18)

phones = pd.read_csv('phones.csv')
fig = plt.figure(figsize=(10,10))
ax = plt.axes()

print(phones.head(7))

ax.scatter(phones["year"], phones["price"], s=100)

plt.show()

from sklearn.linear_model import LinearRegression

X = phones[["disk", "year"]]
y = phones["price"]

reg = LinearRegression().fit(X, y)

[b1, b2] = reg.coef_
a = reg.intercept_

def reg_prediction(dim_1, dim_2):
    return a + b1 * dim_1 + b2 * dim_2

print(reg_prediction(X.disk[1], X.year[1]))


#d1, d2 = list(), list()

#for x in np.linspace(min(phones["disk"]), max(phones["year"]), 100):
#    for y in np.linspace(min(phones["disk"]), max(phones["year"]), 100):
#        d1.append(x)
#        d2.append(y)
#d1 = np.array(d1).reshape(-1, 1)
#d2 = np.array(d2).reshape(-1, 1)
#p = reg.predict(np.concatenate([d1, d2], axis=1))

#fig = plt.figure(figsize=(10,10))
#ax = plt.axes(projection="3d")

#ax.scatter(phones["disk"], phones["year"], phones["price"], s=100)

#ax.plot_trisurf(d1.ravel(), d2.ravel(), p.ravel(), alpha=0.2)

#ax.set_xlabel("disk")
#ax.set_ylabel("year")
#ax.set_zlabel("price")

#ax.elev = 27

#plt.show()
