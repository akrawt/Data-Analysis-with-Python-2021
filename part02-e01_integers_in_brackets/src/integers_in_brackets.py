#!/usr/bin/env python3


import re


def integers_in_brackets(s):
    
    l = (re.findall(r'\[\s*(?:\+(?=\d))?(-?\d+)\s*]', s))

    b = [int(x) for x in l]

    return b

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")) 

if __name__ == "__main__":
    main()
