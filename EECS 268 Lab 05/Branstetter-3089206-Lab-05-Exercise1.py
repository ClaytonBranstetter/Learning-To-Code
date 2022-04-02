'''
Author: Clayton Branstetter
KUID: 3089206
Date: 03/29/2022
Lab: lab#05
Last modified: 04/01/2022
Purpose: Recursive Power Function
'''


def pow(x, y):
    """Calculation of x^y"""
    if y==0: #x^0 = 1
        return 1
    return x*pow(x,y-1) #x^y = x*x^(y-1)

def main():
    base = int(input("Enter a base: "))
    power = int(input("Enter a power: "))
    while power < 0: #the exponent must be zero or larger
        print("Sorry, your exponent must be zero or larger.")
        power = int(input("Enter a power: "))
    print("Answer: ", pow(base, power))

