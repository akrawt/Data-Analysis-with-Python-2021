#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep =";")
    # Delete empty rows
    d_row = df.dropna(how = "all")
    print(df)
    print("----------")
    print(d_row)
    d_col = d_row.dropna(how = "all", axis =1)
    print(d_col)
    
    # Get rid of culumns that only contain missin gvalues
    return d_col


def main():
    cyclists()
    
if __name__ == "__main__":
    main()
