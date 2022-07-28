#!/usr/bin/env python3
from functools import reduce
import numpy as np
"""

"""
def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0],dtype = int)
    else:
        gen = (a for i in range (abs(n)))
        mp = reduce(lambda x,y: x@y, gen)
        if n > 0:
            return mp
        else:
            return np.linalg.inv(mp)


def main():
    a = np.array([[1,2],[3,4]])
    print(matrix_power(a,0))
    

if __name__ == "__main__":
    main()
