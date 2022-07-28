#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    #CHeck if sum of first m elements larger 
    # than sum of last m elements
    # get the rowlength
    mid = int(a.shape[1] / 2)

    first_elements_larger = np.sum(a[:,:mid],1) > np.sum(a[:,mid:],1)
    print(first_elements_larger)
    return a[first_elements_larger]

def main():
    aarr =  np.array([[8,9,3,8,8,3],
                      [0,5,3,9,9,3],
                      [5,7,6,0,4,4],
                      [7,8,1,6,2,9],
                      [2,1,3,5,8,7]])
    print(aarr[::,0:3])
    print(aarr[:,3:])


 

if __name__ == "__main__":
    main()
