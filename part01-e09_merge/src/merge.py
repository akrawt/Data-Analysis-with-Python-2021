#!/usr/bin/env python3

def merge(L1, L2):
    
    s1 = len(L1)
    s2 = len(L2)

    i = 0
    j = 0
    newList = []

    while i < s1 and j <s2:
        if L1[i] <L2[j]:
            newList.append(L1[i])
            i+= 1
        else:
            newList.append(L2[j])
            j+=1

    newList = newList + L1[i:] + L2[j:]

    return newList

def main():
    L1 = [7,6,5,3,1]
    L2 = [10,3,2,1]
    print(merge(L1,L2))

if __name__ == "__main__":
    main()
