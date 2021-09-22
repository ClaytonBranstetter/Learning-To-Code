# ---user input---
name = input("Whats your name? ")
age = int(input("How old are you? "))
year = int(input("What year is it? "))
# NOTE - If you don't specify as int it'll save as string and won't be able to calculate
# calculating how many years passed
newyear = 3000 - year
# adding years passed to current age
age = newyear + age
# ---output---
print("Welcome " + name + " in the year 3000 you will be", age, "years old!")