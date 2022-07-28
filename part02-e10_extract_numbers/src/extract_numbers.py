#!/usr/bin/env python3

def extract_numbers(s):

    words =[]
    splitted = s.split()
    print(splitted)
    for word in splitted:
        try:
            word =int(word)
            words.append(word)
        except:
            try:
                word = float(word)
                words.append(word)
            except:
                continue


    return words

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
