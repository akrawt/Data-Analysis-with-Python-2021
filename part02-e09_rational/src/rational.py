#!/usr/bin/env python3

from pickle import FALSE, TRUE
from sqlalchemy import false, true


class Rational(object):

    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    # Java toString:
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    """
    5/8 + 2/3
    15/24 + 16/24
    31/24
    """
    def __add__(self,num):
        new_denom = self.denominator * num.denominator
        nume1 = self.numerator * num.denominator
        nume2 = num.numerator * self.denominator
        new_nume = nume1 + nume2
        return Rational(new_nume,new_denom)
    
    def __sub__(self,num):
        new_denom = self.denominator * num.denominator
        nume1 = self.numerator * num.denominator
        nume2 = num.numerator * self.denominator
        new_nume = nume1 - nume2
        return Rational(int(new_nume),new_denom)
    
    def __mul__(self,num):
        new_nume = self.numerator * num.numerator
        new_denom = self.denominator * num.denominator
        return Rational(new_nume,new_denom)

    def __truediv__(self,num):
        new_nume = self.numerator * num.denominator
        new_denom = self.denominator * num.numerator
        return Rational(new_nume,new_denom)

    def __eq__(self,num):
        return self.numerator == num.numerator and self.denominator == num.denominator

    def __gt__(self,num):
        new_denom = int(self.denominator) * int(num.denominator)
        mult1 = new_denom / self.denominator
        mult2 = new_denom / num.denominator
        return mult1 * self.numerator > mult2 * self.denominator

    def __lt__(self, num):
        new_denom = int(self.denominator) * int(num.denominator)
        mult1 = new_denom / self.denominator
        mult2 = new_denom / num.denominator
        return mult1 * self.numerator < mult2 * self.denominator

    

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))
if __name__ == "__main__":
    main()
