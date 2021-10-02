'''
Author: Clayton Branstetter
KUID: 3089206
Date: 09/30/2021
Lab: lab#03
Last modified: 10/01/2021
Purpose: Sequence Search
'''

userstring = input("Enter a string: ")
ci = input("Do you want a case-sensitive match? (y/n): ").upper()
searchstring = input("Enter a sequence to count: ")

if ci == "N":
  userstring = userstring.upper()
  searchstring = searchstring.upper()

print("number of occurences: {}".format(userstring.count(searchstring)))
