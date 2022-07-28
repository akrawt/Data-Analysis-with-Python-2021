#!/usr/bin/env python3
import pandas as pd

def read_series():

    index = []
    word = []

    while True:
        inp = input("Your input")
        # if empty break
        if inp == "":
            break
        else:
            # split indece and string
            splitted = inp.split()

            if len(splitted) > 2:
                raise Exception
            
            index.append(splitted[0])
            word.append(splitted[1])
    
    return pd.Series(word, index)
            

def main():
    print(read_series())

if __name__ == "__main__":
    main()
