'''
Author: Clayton Branstetter
KUID: 3089206
Date: 03/28/2022
Lab: lab#05
Last modified: 04/01/2022
Purpose: Good Old Fibonacci
'''


def fibonacci(n):
        """ Calculation of the fibonacci sequence for a given n>=0"""
        if n==0 or n==1:
            return 1 # fibonacci(0) = 1 or fibonacci(1) = 1
        return fibonacci(n-1) + fibonacci(n-2) # Fi=Fi-1 + Fi-2 if i>1

def main():
    inp = input(" Enter mode and value: ")
    list_inp = inp.split()
    try:
        mode = list_inp[0]
        if mode not in ['-v', '-i']:
            raise RuntimeError
        n = int(list_inp[1])
        if n<0:  # n must >= 0
            raise RuntimeError
        if mode == "-i":
            print(fibonacci(n)) # print the ith Fibonacci number
        elif mode == "-v":
            # verify where the user wants to know if the number given is in the Fibonacci sequence
            i=0
            m = fibonacci(i)
            while m<n:
                m = fibonacci(i)
                i+=1
            if m==n:
                print(f"{n} is in the sequence")
            else:
                print(f"{n} is not in the sequence")
    except:
        print('invalid input')


main()