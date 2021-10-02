'''
Author: Clayton Branstetter
KUID: 3089206
Date: 10/02/2021
Lab: lab#04
Last modified: 10/02/2021
Purpose: Going to the Grocery Store
'''

import sys

# Create the main menu
def main_menu():
  while(True):

    print()
    print('''Welcome to your Shopping List!

    Select a number for the action you would to do:

    1) View shopping list
    2) Add item to shopping list
    3) Check off item from shopping list
    4) Check if item(s) are on shopping list
    5) How many items are on shopping list
    6) Clear shopping list
    7) Print shopping list
    8) Exit
    ''')

    # Ask the user to make a selection
    selection = input("Make your selection: ")

    # Determine which action to perfrom based on the user's selection
    if selection == "1":
      display_list()
    elif selection == "2":
      add_item()
    elif selection == "3":
      remove_item()
    elif selection == "4":
      check_item()
    elif selection == "5":
      list_length()
    elif selection == "6":
      clear_list()
    elif selection == "7":
      print_list()
    elif selection == "8":
      print("Thank you for shopping with us, goodbye.")
      sys.exit()
    else: print("You did not make a valid selection.")

# Add a few items to the shopping list
shopping_list = ["apples", "bananas", "carrots", "bread", "potatoes"]
print(shopping_list)

# Displays all items on the shopping list
def display_list():
  print()
  print("--- SHOPPING LIST ---")
  for i in shopping_list:
    print("* " + i)

# Adds an item to the shopping list
def add_item():
  item = input("Enter the item you wish to add to the shopping list: ")
  shopping_list.append(item)
  print(item + " has been added to the shopping list.")

# Remove an item from the shopping list
def remove_item():
  item = input("Enter the item you wish to remove from the shopping list: ")
  shopping_list.remove(item)
  print(item + " has been removed from the shopping list.")

# Check to see if a particular item is on the shopping list
def check_item():
  item = input("What item would you like to check on the shopping list? ")
  if item in shopping_list:
    print("Yes, " + item + " are on the shopping list.")
  else:
    print("No, " + item + " that item is not on the shopping list.")

# How many items are on the shopping list
def list_length():
  print("There are", len(shopping_list), "item(s) on the shopping list")

# Remove everything from the shopping list
def clear_list():
  shopping_list.clear()
  print("The shopping list is now empty")

def print_list():
  print("Here is your shopping list")
  print(*shopping_list, sep = "\n")



# Run the function main_menu - which will run the shopping list app
main_menu()