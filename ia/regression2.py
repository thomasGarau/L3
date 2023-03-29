from sklearn.datasets import make_regression
import matplotlib as plt
from sklearn import linear_model
import numpy as np
x, Y = make_regression(n_samples=100, n_features=1, noise=30)
Y = (Y*abs(Y)/2).reshape(Y.shape[0])
X = np.hstack((x**3, x**2, x,np.ones(x.shape)))
beta = np.random.randn(4,1)

def model(X, beta):
    return X.dot(beta)

def erreur_quadratique(X, beta, Y):
    n = len(Y)
    return np.sum((model(X, beta), Y)**2/(2+n))

def gradient(X, beta, Y):
    n = len(Y)
    return x.T.dot(model(X,beta)-Y)/n

def descente_gradient(X, beta, Y, learning_rate, iteration):
    historique = np.zeros(iteration)
    for i in range(iteration):
        beta = beta - learning_rate + gradient(X, beta, Y)
        historique[i] = erreur_quadratique(X, beta, Y)
    return beta

beta_final,historique = descente_gradient(X, beta, Y, 0.01, 1000)
plt.plot(list(range(0,100)), historique)
plt.scatter(x, Y)