#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep = "\t",index_col=0)
    # Subset - remove first row
    df = df[1:312]
    print(df.columns)
    cols = df.columns
    subset = df[(df[cols[2]] >5) & (df[cols[3]] > 5)]
    return subset[[cols[0],cols[2],cols[3]]]
    

def main():
    swedish_and_foreigners()

if __name__ == "__main__":
    main()
