'''
Author: Clayton Branstetter
KUID: 3089206
Date: 09/25/2021
Lab: lab#02
Last modified: 09/29/2021
Purpose: Creating a numerator/denominator
'''

def longdivision(numerator, denominator):
  #find out what the answer is
  #7 / 3 = 2 Remainder 1
  #numerator / denominator = answer remainder 1
  answer=int(numerator)/int(denominator)
  #modulo
  remainder = int(numerator)%int(denominator)
  print("{} / {} = {} remainder {}".format(numerator, denominator, int(answer), remainder))

closing = "N"
while(closing == "N"):
  #input field "enter a numerator"
  numerator = input("numerator: ")
  #input field "enter a denominator"
  denominator=input("denominator: ")
  if int(denominator) == 0:
    print("Sorry, you may not divide by 0")
  else:
  #runs the function/puts out results
    longdivision(numerator, denominator)
  #input field "do you want to exit (Y/y)" needs to be able to process capital and lowercase
  closing = input("Do you want to exit? (Y/N): ").upper()
  #Exiting
  if (closing) == "Y":
    print("Exiting...")
