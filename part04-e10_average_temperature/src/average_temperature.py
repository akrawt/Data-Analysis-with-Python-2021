#!/usr/bin/env python3

import pandas as pd

from numpy import average

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv", sep =",")
    df_july = df[df.m == 7]
    
    amount = sum(df_july.loc[:,"Air temperature (degC)"])
    return amount / 31

def main():
    print(f"Average temperature in July: {average_temperature():.1f}")

if __name__ == "__main__":
    main()
