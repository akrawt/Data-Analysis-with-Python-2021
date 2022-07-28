#!/usr/bin/env python3

def word_frequencies(filename = "src/alice.txt"):

    d = {}
    words = []
    with open(filename,"r") as f:
        for line in f:
            splitted = line.split()
            stripped =[i.strip("""!"#$%&'()*,-./:;?@[]_""") for i in splitted]
            for i in stripped:
                words.append(i)
            
    wordset = set(words)
    for i in wordset:
        cnt = words.count(i)
        d[i] = cnt
    
    return d
 


def main():
    print(word_frequencies())

if __name__ == "__main__":
    main()
