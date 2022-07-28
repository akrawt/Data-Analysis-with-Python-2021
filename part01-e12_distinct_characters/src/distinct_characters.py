#!/usr/bin/env python3

def distinct_characters(L):

    newDict = {}
    
    for x,i in enumerate(L):
        print(newDict)
        newDict[i] = len(set(L[x]))

    return newDict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()

   

    

