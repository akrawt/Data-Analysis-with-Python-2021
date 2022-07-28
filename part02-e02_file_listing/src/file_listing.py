#!/usr/bin/env python3

import re


def file_listing(filename = "src/listing.txt"):

    l = []
            #digit one or more times
            # space one or more times
            # word character one or more times
            #space one or more times
            # digit one or more times
            # space o o m t
            # digit oomt : digit oomt
            #space oomt
            #any character one or more times
    exp = r'(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s(.+)'
    with open(filename, "r") as f:
        for i in f:
            size,month,day,hour,minute,filename = re.search(exp,i).groups()
            l.append((int(size),month,int(day),int(hour),int(minute),filename))

        
    return l

def main():
    print(file_listing())
    
if __name__ == "__main__":
    main()
