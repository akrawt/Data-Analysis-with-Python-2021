#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep ="\t")
    # Subset Publisher and WoC
    publisher = df.loc[:,"Publisher"] 
    woc = df.loc[:,"WoC"]
    result = pd.concat([publisher,woc],axis = 1)
    print(result)
    # Best as DF
    best = result.groupby("Publisher")["WoC"].sum()
    best = best.sort_values(ascending = False)
    print(best)
    # Get best Publisher
    top_pub = best.index[0]

    final = df[df.Publisher == top_pub]

    print(final)
    print(top_pub)
    

    return final

def main():
    best_record_company()
    

if __name__ == "__main__":
    main()
