'''
Author: Clayton Branstetter
KUID: 3089206
Date: 09/30/2021
Lab: lab#03
Last modified: 09/30/2021
Purpose: Secret Word Guess
'''

secretphrase = "BRINGCOFFEE"
guesses = 0
print("Guess the secret phrase!")

while(True):
  guess = input("Guess: ").upper()
  guesses += 1
  if len(guess) > len(secretphrase):
    print("Too many characters")
  if len(guess) < len(secretphrase):
    print("Too few characters")
  if len(guess) == len(secretphrase):
    correctletters = 0
    for letter in list(set(guess)):
      correctletters += secretphrase.count(letter)
    if correctletters == len(secretphrase):
      print("Correct!")
      print("Number of guesses: {}".format(guesses))
      break
    if correctletters != len(secretphrase):
      print("Correct Letters: {}".format(correctletters))
