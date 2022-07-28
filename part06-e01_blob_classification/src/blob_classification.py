#!/usr/bin/env python3

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split

# feature matrix = X, label vector = y
# return accuracy score of prediction
# prediction using gaussianNB
# train_test_split to spolit dataset into two parts ( random_state = 0)
# training set size of 75%

def blob_classification(X, y):
    train_X, test_X, train_y, test_y = train_test_split(X,y,train_size = 0.75, test_size = 0.25, random_state = 0)
    # Choose a model
    model = GaussianNB()
    # Fit model
    model.fit(train_X,train_y)

    # Accuracy score
    y_fitted = model.predict(test_X)
    acc = metrics.accuracy_score(test_y,y_fitted)
    return acc

def main():
    X,y = datasets.make_blobs(100, 2, centers=2, random_state=2, cluster_std=2.5)
    print("The accuracy score is", blob_classification(X, y))
    a=np.array([[2, 2, 0, 2.5],
                [2, 3, 1, 1.5],
                [2, 2, 6, 3.5],
                [2, 2, 3, 1.2],
                [2, 4, 4, 2.7]])
    accs=[]
    for row in a:
        X,y = datasets.make_blobs(100, int(row[0]), centers=int(row[1]),
                                  random_state=int(row[2]), cluster_std=row[3])
        accs.append(blob_classification(X, y))
    print(repr(np.hstack([a, np.array(accs)[:,np.newaxis]])))

if __name__ == "__main__":
    main()
