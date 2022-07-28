#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def toint(x):

    if x == "A":
        return 0
    if x == "C":
        return 1
    if x == "G":
        return 2
    if x == "T":
        return 3
    

def get_features_and_labels(filename):

    # Load content into feature matrix,
    # 2 columns X = feature, y = label vector
    df = pd.read_csv(filename, sep = "\t")

    # Get the labels
    labels = df.loc[:,'y']
    # Get the features and apply the toint function, so each
    # integer represents a letter in a nucleotid
    features = df.loc[:,"X"].apply(lambda x: [toint(y) for y in x])
    print(features)
    # Convert single array to a list
    features = np.array(features.tolist())
    print(features)
   
    return features,labels








def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):

    features, labels = get_features_and_labels(filename)

    model = AgglomerativeClustering(n_clusters= 2,affinity="euclidean", linkage = "average")
    
    model.fit(features)

    permutation = find_permutation(model.n_clusters_,labels,model.labels_)
    new_labels = [permutation[labels] for labels in model.labels_]

    acc = accuracy_score(labels,new_labels)

    return acc

def cluster_hamming(filename):

    features, labels = get_features_and_labels(filename)

    dist = pairwise_distances(features, metric ="hamming")

    model = AgglomerativeClustering(n_clusters = 2, affinity = "precomputed", linkage = "average")

    y_pred = model.fit_predict(dist,labels)
    permutation = find_permutation(model.n_clusters_,labels,y_pred)
    new_labels = [permutation[labels] for labels in model.labels_]

    acc = accuracy_score(labels,new_labels)

    return acc

import scipy
def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        new_label=scipy.stats.mode(real_labels[idx])[0][0]  # Choose the most common label among data points in the cluster
        permutation.append(new_label)
    return permutation
def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))
    #get_features_and_labels("src/data.seq")
if __name__ == "__main__":
    main()
