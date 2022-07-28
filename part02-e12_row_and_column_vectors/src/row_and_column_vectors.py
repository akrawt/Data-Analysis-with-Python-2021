#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    row_num,col_num = np.shape(a)
    return (np.vsplit(a,row_num))

def get_column_vectors(a):
    row_num,col_num = np.shape(a)
    return (np.hsplit(a,col_num))

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
