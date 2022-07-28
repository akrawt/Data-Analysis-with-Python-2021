#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self,name):
        self.start = name
    
    def write(self,s):
        print(f'{self.start}{s}')

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
