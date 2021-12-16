def bouncer(age):
  if int(age) >= 21:
    print("Come in")
  if not int(age) >= 21:
    print("scram, junior!")
  if int(age) < 0:
    print("ERROR")


while(True):
  bouncer(input("How old are you?: "))
