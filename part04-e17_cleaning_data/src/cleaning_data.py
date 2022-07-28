#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv",sep = "\t")
    print(df)
    print(df.dtypes)

    # First clean
    df.loc[[0],["Last"]] = "nan"
    df.loc[[0],["Start"]] = "2017"
    df.loc[[3],["Seasons"]] = "2"
    # Convert "Start","Last" and "Seasons" column to int
    df = df.astype({"Start" : np.integer, "Last" : float, "Seasons" :np.integer})

    print(df)
    print(df.dtypes)
    # String Operations vp
    lf = df["Vice-president"].str.split(expand = True)
    lf = lf.replace(",","",regex = True)
    print(lf.dtypes)
    lf1 = lf.loc[:,0].str.capitalize()
    lf2 = lf.loc[:,1].str.capitalize()
    print(lf1,lf2)
    lf = pd.concat([lf1,lf2], axis = 1)

    # Dick Cheney
    temp = lf.loc[2,0]
    lf.loc[2,0] = lf.loc[2,1]
    lf.loc[2,1] = temp

    # Al Gore
    temp = lf.loc[3,0]
    lf.loc[3,0] = lf.loc[3,1]
    lf.loc[3,1] = temp
    lf = lf.loc[:,0] + " " + lf.loc[:,1]

    # vp col = cleaned vp col
    df["Vice-president"] = lf
    print(lf)
    print(df)


    # String Operations p
    pf = df["President"].str.split(expand = True)
    pf = pf.replace(",","",regex = True)
    print(pf.dtypes)
    pf1 = pf.loc[:,0].str.capitalize()
    pf2 = pf.loc[:,1].str.capitalize()
    print(pf1,pf2)
    pf = pd.concat([pf1,pf2], axis = 1)

    # Dick Cheney
    temp = pf.loc[2,0]
    pf.loc[2,0] = pf.loc[2,1]
    pf.loc[2,1] = temp

    # Al Gore
    temp = pf.loc[3,0]
    pf.loc[3,0] = pf.loc[3,1]
    pf.loc[3,1] = temp
    pf = pf.loc[:,0] + " " + pf.loc[:,1]

    df["President"] = pf
    print(df.dtypes)
    print(df)
    return df

def main():
    cleaning_data()

if __name__ == "__main__":
    main()
