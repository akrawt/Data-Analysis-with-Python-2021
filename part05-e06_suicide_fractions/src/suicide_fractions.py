#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():

    df = pd.read_csv("src/who_suicide_statistics.csv" , sep = ",")
    print(df)

    
    # Drop the colums year, sex, age - they are not needed
    df.drop(["year","sex","age"], axis = "columns", inplace = True)
    
    #Make a new column for suicide ratio
    df["suicide_ratio"] = df["suicides_no"] / df["population"]
    print(df)

    df2 = df.groupby("country")
    print(df2)
    df2 = df2["suicide_ratio"].mean()
    print(df2)
    return df2
    

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
