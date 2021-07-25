import numpy as np
import pandas as pd

phones = pd.read_csv("phones.csv")

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

X = phones[["disk", "year"]]
y = phones["os"]

cl = DecisionTreeClassifier().fit(X, y)

print(cl.predict(X[1:2])[0], y[1])

