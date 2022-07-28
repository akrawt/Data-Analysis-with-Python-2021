#!/usr/bin/env python3

def triple(number: int):
    return number *3

def square(number: int):
    return number**2

def main():
    for i in range(1,11):

        tri = triple(i)
        squ = square(i)
        if(squ > tri):
            break
        print(f"triple({i})=={tri} square({i})=={squ}")

if __name__ == "__main__":
    main()
