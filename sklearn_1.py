from matplotlib import pyplot as plt
import seaborn as sns
from pylab import rcParams
rcParams['figure.figsize'] = (9, 6)
from sklearn.datasets import load_boston

X, y = load_boston(return_X_y = True)

print(X.shape)


