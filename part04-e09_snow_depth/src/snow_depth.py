#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv", sep =",")
    summary = df.describe()
    max_depth = summary.iloc[7,4]
    return max_depth

def main():
    print(f"Max snow depth: {snow_depth()}")

if __name__ == "__main__":
    main()
