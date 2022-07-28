#!/usr/bin/env python3

def transform(s1, s2):

    split1 = s1.split()
    split2 = s2.split()
    print(split1)
    print(type(split1))

    # Convert string values in list to integer values
    split1 = list(map(int,split1))
    split2 = list(map(int,split2))

    print(split1)
    
    zipped = list(zip(split1,split2))
    print(zipped)
    final = list(map(lambda x: x[0] * x[1], zipped))
    print(list(map(lambda x: x[0] * x[1], zipped)))

    return final

def main():
    s1 = "1 5 3"
    s2 = "2 6 -1"
    transform(s1,s2)
    

if __name__ == "__main__":
    main()
