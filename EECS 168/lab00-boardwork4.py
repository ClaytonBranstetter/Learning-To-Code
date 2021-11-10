'''
Author: Clayton Branstetter
KUID: 3089206
Date: 11/04/2021
Lab: lab#00
Last modified: 11/04/2021
Purpose: Calculator
'''

import sys

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Use num1, num2 as x,y
# Use choice as input
# Check to make sure user wants another calculation
# Break while(True) if not
# Make Invalid Input statement if wrong input from user


while(True):
    choice = input("Enter choice(1, 2, 3, 4): ")
    if choice in ('1', '2', '3', '4'):
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
      elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
      elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
      elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Would you like another calculation? [Y/N]: ").upper
        if next_calculation == "N":
          break

    else:
      print("Invalid Input, please try again.")
