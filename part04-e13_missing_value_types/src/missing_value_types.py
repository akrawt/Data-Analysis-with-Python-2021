#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    independ = [None,1917,1776,1523,None,1992]
    president = [None,"Niinistö","Trump",None,"Steinmeier","Putin"]
    ind = ["United Kingdom","Finland","USA","Sweden","Germany","Russia"]
    df = pd.DataFrame({"State": ind,"Year of independence" : independ,"President": president}).set_index("State")
    print(df)
    return df
               
def main():
    missing_value_types()

if __name__ == "__main__":
    main()
