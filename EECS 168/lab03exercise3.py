'''
Author: Clayton Branstetter
KUID: 3089206
Date: 09/30/2021
Lab: lab#03
Last modified: 09/30/2021
Purpose: Outbreak!
'''


def fibonacci(n):
    n = int(n)
    # Check if n less than 0
    if n < 0:
        return 0
    # Check if n is 0
    elif n == 0:
        return 0
    # Check if n is 1,2, or 3
    elif n == 1:
        return 1
    elif n == 2:
        return 8
    elif n == 3:
        return 22
    else:
        return fibonacci(n-1) + fibonacci(n-2) + fibonacci(n-3)


while(True):
  day = input("What day do you want a sick count for?: ")
  if int(day) <= 0:
    print("Invalid day")
  else:
    print("Total people with flue: {}".format(fibonacci(day)))
