#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    shape = df.shape[0]
    fil = df[df[df.columns[1]] >0].index
    
    # length of the filtered
    amount = len(fil)
    all = shape
    proportion_growing_munc = amount / all
    return proportion_growing_munc


def main():
    df = pd.read_csv("src/municipal.tsv",sep = "\t", index_col= 0)
    data = df[1:312]
    perc = growing_municipalities(data) * 100
    print(f"Proportion of growing municipalities: {perc:.1f}%")
    

if __name__ == "__main__":
    main()
