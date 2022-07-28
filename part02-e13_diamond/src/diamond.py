#!/usr/bin/env python3

import numpy as np

def diamond(n):
    a = np.eye(n,n,dtype= int)
    c = np.flip(a,axis = 1)
    c = np.delete(c,n-1,1)
    ac = np.concatenate((c,a),axis = 1)
    #print(a)
    #print(c)
    d = np.eye(n,n,dtype=int)
    d = d[1:]
    e = np.flip(d,axis=1)
    #print(ac)
    e = e[0:n-1,1:n]
    #print(d)
    print(e)
    de = np.concatenate((d,e),axis = 1)
    #print(de)
    print("---")

    acde = np.concatenate((ac,de))
    #print(acde)
    return acde

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()


