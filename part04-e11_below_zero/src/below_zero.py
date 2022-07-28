#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    temp = df["Air temperature (degC)"] <0
    count = len(df[temp])
    print(df)
    print(temp)
    print(count)
    return count

def main():
    print(f"Number of days below zero: {below_zero()}")
    
if __name__ == "__main__":
    main()
