'''
Author: Clayton Branstetter
KUID: 3089206
Date: 10/02/2021
Lab: lab#04
Last modified: 10/02/2021
Purpose: List comparisons
'''
import sys

def ave(input):
  return sum(input)/len(input)

def build_list():
  mylist = []
  done = "N"
  while(done == "N"):
    mylist.append(int(input("What value to add?: ")))
    done = input("Are you done? [Y/N]").upper()
  return mylist

list1 = build_list()
list2 = build_list()
list3 = list1 + list2

if sum(list1) > sum(list2):
  print("List 1 is larger by {}".format(sum(list1) - sum(list2)))

if sum(list2) > sum(list1):
  print("List 1 is smaller by {}".format(sum(list2) - sum(list1)))

if ave(list1) > ave(list2):
  print("List 1 is larger by {}".format(ave(list1) - ave(list2)))

if ave(list2) > ave(list1):
  print("List 1 is smaller by {}".format(ave(list2) - ave(list1)))

print("This is all the values")
print(list3)

print("this is the unique values")
print(set(list3))

len(list3) - len(set(list3))

if list2 == list1[::-1]:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

sys.exit()