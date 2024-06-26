# -*- coding: utf-8 -*-
# iris-trainsizesplot.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=200)
learning_curve_train = []
learning_curve_test = []
train_sizes = np.linspace(0.1, 1.0, 10)
for train_size in train_sizes:
    num_samples = int(train_size * len(X_train))
    x_subset = X_train[:num_samples]
    y_subset = y_train[:num_samples]
    model.fit(x_subset, y_subset)
    y_pred_train = model.predict(x_subset)
    acc_train = accuracy_score(y_subset, y_pred_train)
    learning_curve_train.append(acc_train)
    y_pred_test = model.predict(X_test)
    acc_test = accuracy_score(y_test, y_pred_test)
    learning_curve_test.append(acc_test)
plt.figure(figsize=(10, 6))
plt.title("Learning curves")
plt.xlabel("Training set size")
plt.ylabel("Accuracy")
plt.grid(True)
plt.plot(train_sizes * len(X_train), learning_curve_train, 'o-', color="r", label="Training accuracy")
plt.plot(train_sizes * len(X_train), learning_curve_test, 'o-', color="b", label="Test accuracy")
plt.legend(loc="best")
plt.show()
