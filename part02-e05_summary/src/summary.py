#!/usr/bin/env python3

import sys
import math

# sum, average, standart dev
def summary(filename):
    l = []

    with open(filename,"r") as f:
        for i in f:
            try:
                l.append(float(i))
            except:
                pass
    sm = sum(l)
    av = sum(l) / len(l)
        
    # Standart deviation
    top = 0
    for i in l:
        top += (av-i)**2
    std = math.sqrt((top / (len(l) - 1)))
    return (sm,av,std)

def main():
    files = sys.argv[1:]
    for file in files:
        sm,av,std = summary(file)  
        print(f"File: {file} Sum: {sm:.6f} Average: {av:.6f} Stddev: {std:.6f}")

if __name__ == "__main__":
    main()
