import matplotlib as plt
import numpy as np

from sklearn.datasets import make_regression

x,Y = make_regression(n_samples=100,n_features=1, noise=10)
Y= Y.reshape(Y.shape[0],1)
x = np.hstack((x, np.ones(x.shape)))
beta = np.random.randn(2,1)

def descente_gradient(X, Y, beta, learning_rate, n_iterations):
    historique = np.zeros(n_iterations)
    for k in range(0, n_iterations):
        beta = beta -learning_rate*gradient(X,Y,beta)
        historique[k] = erreur_quadratique (X, Y, beta)
    return beta, historique

beta_final , cost_history= descente_gradient(X, Y, beta,
                     learning_rate=0.01, n_iterations=1000)
prediction = model(X,beta_final)

plt.scatter(x, y)
plt.scatter(x, prediction, c='r')

def model(X,beta):
    return X.dot(Beta)
model(X,Beta)-Y

def erreur_quadratique(X,y,beta):
    n=len(y)
    return (np.sum(model(X,beta)-y)**2)/(2*n)

