#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

import scipy

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        new_label=scipy.stats.mode(real_labels[idx])[0][0]  # Choose the most common label among data points in the cluster
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep = "\t")
    print(df)

    # Take a look at features X1 and X2
    #plt.scatter(df.iloc[:,0],df.iloc[:,1])
    #plt.show()

    # Extraxt features
    features = df.loc[:,["X1","X2"]]
    # Extract labels
    labels = df.loc[:,"y"]

    final_list = []
    # Use np.arange instead of range to be able to use float instead of integer
    for i in np.arange(0.05,0.2,0.05):
        print(i)
        model = DBSCAN(eps = i)
        model.fit(features)
        
        # Number of clusters
        n_clusters = len(set(model.labels_))

        # Number of outliers
        outliers = 0

        if -1 in model.labels_:
            n_clusters -= 1
            outliers += 1
        

        permutation = find_permutation(n_clusters,labels,model.labels_)
        new_labels = [ permutation[label] for label in model.labels_] 

        # Accuracy score
        acc = accuracy_score(labels,new_labels)
        # Append sol to list
        final_list.append([i,acc,n_clusters,outliers])

    # Make df from list
    final_df = pd.DataFrame(final_list,columns = ["eps","Score","Clusters","Outliers"],dtype = "float")
    return final_df

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
