from sklearn.datasets import make_regression
from sklearn.datasets import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib as plt
import numpy as np
import panda as pd


data = pd.read_csv('location.csv', index_col=0)
X = np.array(data['loyer']).reshape(data.shape[0], 1)
Y = np.array(data['surface']).reshape(data.shape[0], 1)
poly_model = PolynomialFeatures(degree=4)
model = LinearRegression()
model = 

plt.scatter(X, Y, s=4)
plt.scatter(X, Ypred, c='r', s=4)
mode.coef_