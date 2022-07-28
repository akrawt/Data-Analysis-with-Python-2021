#!/usr/bin/env python3

import numpy as np
import scipy.linalg

"""
X
[1,2,3]
[4,5,6]

<x,y>
1*2+2*6+3*1

||x||
sqrt(<x,x>)
sqrt(1*1+2*2+3*3)


Y
[2,6,1]
[3,5,2]

"""
def vector_angles(X, Y):
    """
    scalar_xy = np.inner(X,Y)
    sum_xy = np.sum(scalar_xy, axis = 1)

    scalar_x = np.inner(X,X)
    sum_x = np.sum(scalar_x,axis = 1)
    ip_x = np.sqrt(sum_x)

    scalar_y = np.inner(Y,Y)
    sum_y = np.sum(scalar_y,axis = 1)
    ip_y = np.sqrt(sum_y)
"""
    length = X.shape[0]
    res = np.zeros(length)

    for i in range(length):
        res[i] = (np.dot(X[i],Y[i]/scipy.linalg.norm(X[i])/scipy.linalg.norm(Y[i])))
    
    #cos = sum_xy / (ip_x * ip_y)
    clipped = np.clip(res,-1,1)
    angles = np.arccos(clipped)


    return np.degrees(angles)

def main():
    x = np.array([[1,2,3],[4,5,6]])
    y = np.array([[2,6,1],[3,5,2]])
    print(vector_angles(x,y))
    

if __name__ == "__main__":
    main()
