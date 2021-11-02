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
  userinput = input("Enter a command: ").split()
  command = userinput[0].upper()
  # Determine what to do based on the user's input
  if command == "NAVIGATE":
    myurl = command[1]
    CurrentListItem = CurrentListItem + 1
    display_url(URL=myurl)
  elif command == "BACK":
    CurrentListItem = CurrentListItem - 1
    if CurrentListItem < 1:
      CurrentListItem = 1
    #print("DEBUG: CurrentListItem {}".format(CurrentListItem))
  elif command == "FORWARD":
    CurrentListItem = CurrentListItem + 1
    if CurrentListItem > len(BROWSERHISTORY):
      CurrentListItem = len(BROWSERHISTORY)
    #print("DEBUG: CurrentListItem2 {}".format(CurrentListItem))
  elif command == "HISTORY":
    pass
  elif command == "EXIT":
    print("Thanks for using my browser. ")
    # Exit input and loop
    break
  else:
    print("You did not input a valid command. ")
  display_history()
