#!/usr/bin/env python3

import pandas as pd

def cities():
    pop = pd.Series([643272,279044,231853,223027,201810])
    area = pd.Series([715.48,528.03,689.59,240.35,2817.52])
    col = ["Population","Total area"]
    ind = ["Helsinki","Espoo","Tampere","Vantaa","Oulu"]

    return pd.DataFrame({col[0] : pop.values,col[1] : area.values}, index = ["Helsinki","Espoo","Tampere","Vantaa","Oulu"])
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
