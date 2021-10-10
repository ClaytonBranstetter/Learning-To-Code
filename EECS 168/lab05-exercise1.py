'''
Author: Clayton Branstetter
KUID: 3089206
Date: 10/10/2021
Lab: lab#05
Last modified: 10/10/2021
Purpose: Web History Simulator
'''


# Create the functions

BROWSERHISTORY = []

CurrentListItem = 0

def display_url(URL):
  BROWSERHISTORY.append(URL)

def display_history():
  print("Oldest")
  print("===========")


  i = 0
  want = CurrentListItem
  for historyitem in BROWSERHISTORY:
    i = i + 1
    if i == want:
      historyitem = historyitem + " <=="
    print(historyitem)
  print("===========")
  print("Newest")

  # Ask the user to enter a command
while(True):
  command = input("Enter a command: ").split()
  # Determine what to do based on the user's input
  if command[0].upper() == "NAVIGATE":
    myurl = command[1]
    CurrentListItem = CurrentListItem + 1
    display_url(URL=myurl)
  elif command[0].upper() == "BACK":
    CurrentListItem = CurrentListItem - 1
    if CurrentListItem < 1:
      CurrentListItem = 1
    #print("DEBUG: CurrentListItem {}".format(CurrentListItem))
  elif command[0].upper() == "FORWARD":
    CurrentListItem = CurrentListItem + 1
    if CurrentListItem > len(BROWSERHISTORY):
      CurrentListItem = len(BROWSERHISTORY)
    #print("DEBUG: CurrentListItem2 {}".format(CurrentListItem))
  elif command[0].upper() == "HISTORY":
    pass
  elif command[0].upper() == "EXIT":
    print("Thanks for using my browser. ")
    # Exit input and loop
    break
  else:
    print("You did not input a valid command. ")
  display_history()
