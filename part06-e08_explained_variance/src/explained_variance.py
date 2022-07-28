#!/usr/bin/env python3

import pandas as pd
import numpy as np
from  sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():

    df = pd.read_csv("src/data.tsv", sep = "\t")

    pca = PCA()

    pca.fit(df)

    # Fit PCA to the data

    #Return two lists or two 1D arrays
    # 1. contain variance of all features
    var = df.var(axis = 0)
    # 2. contain explained variance by the PCA
    expl_var  = pca.explained_variance_

    return var, expl_var

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))

    var_list = " ".join([f"{x:.3f}" for x in v])
    ev_list = " ".join([f"{x:.3f}" for x in ev])
    print(f"The variances are: {var_list}")
    print(f"The explained variances after PCA are: {ev_list}")
    
    plt.plot(np.arange(1,11), np.cumsum(ev))
    plt.show()


if __name__ == "__main__":
    main()
