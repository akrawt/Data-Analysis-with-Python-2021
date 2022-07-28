#!/usr/bin/env python3

def reverse_dictionary(d):

    reversedDictionary = {}

    for key in d:
        for value in  d[key]:
            try:
                reversedDictionary[value].append(key)
            except:
                reversedDictionary[value] = [key]
    print(reversedDictionary)
    return reversedDictionary

def main():
    d = {1:"akex", 3: ["bre","rara"],2 :"kokolores"}
    reverse_dictionary(d)


if __name__ == "__main__":
    main()
