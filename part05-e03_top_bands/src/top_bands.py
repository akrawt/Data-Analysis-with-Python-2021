#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv("src/bands.tsv", sep ="\t")
    top = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep = "\t")

    bands["Band"] = bands["Band"].str.upper()
    merged = pd.merge(bands,top, left_on = "Band", right_on = "Artist")
    print(merged)
    return merged

def main():
    top_bands()

if __name__ == "__main__":
    main()
