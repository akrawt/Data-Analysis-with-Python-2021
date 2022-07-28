#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):

    return pd.Series(s.index.values,s.values)

def main():
    s = pd.Series(['a','b','c'])
    print(inverse_series(s))

if __name__ == "__main__":
    main()
