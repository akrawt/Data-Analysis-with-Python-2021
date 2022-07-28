#!/usr/bin/env python3

def find_matching(L, pattern):

    indices = []

    for i,x in enumerate(L):
        if pattern in x:
            indices.append(i)

    return indices

def main():
    pass

if __name__ == "__main__":
    main()
