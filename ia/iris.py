import numpy as np 
import matplotlib as plt
import panda as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

iris = load_iris()
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.2)
model = SVC(C=100)
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
confusion_matrix(Y_test, Y_pred)
