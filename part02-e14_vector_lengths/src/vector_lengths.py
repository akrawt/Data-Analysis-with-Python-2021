#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

# 1 2 3 4
# 3 4 5 6
def vector_lengths(a):
    a = a**2
    sums = np.sqrt(a.sum(axis =1))
    return sums

def main():
    ar = np.array([[1,2,3,4],[5,6,7,8],[4,5,6,7]])
    print(vector_lengths(ar))

if __name__ == "__main__":
    main()
