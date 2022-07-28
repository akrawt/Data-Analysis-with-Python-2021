#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    df = pd.read_csv("src/municipal.tsv", sep = "\t", index_col= 0)
    # Remove whole countries
    df = df[1:312]
    new_df = df.loc[:,["Population","Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]]

    return new_df

def main():
    return

if __name__ == "__main__":
    main()
