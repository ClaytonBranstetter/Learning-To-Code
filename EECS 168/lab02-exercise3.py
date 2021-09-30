print("============================")
print("WELCOME TO THE RESTAURANT")
print("============================")

count_pasta = 0
count_gcheese = 0
count_pie = 0
q_pasta = input("Do you want Cold Pasta? (y/n): ").upper()
if q_pasta == "Y":
  count_pasta = int(input("How many?: "))
price_pasta = 2.50

q_gcheese =input("Do you want Grilled Cheese? (y/n): ").upper()
if q_gcheese == "Y":
  count_gcheese = int(input("How many?: "))
price_gcheese = 5.55

q_pie = input("Do you want Pie? (y/n): ").upper()
if q_pie == "Y":
  count_pie = int(input("How many?: "))
price_pie = 3.00

age = int(input("How old are you?: "))
if age <= 5:
  price_pie = 0
subtotal = 0

if count_pasta > 0:
  print("{} Cold Pasta @ ${} ==> ${:.2f}".format(count_pasta, price_pasta, (count_pasta * price_pasta)))
  subtotal += (count_pasta * price_pasta)

if count_gcheese > 0:
  print("{} Grilled Cheese @ ${} ==> ${:.2f}".format(count_gcheese, price_gcheese, (count_gcheese * price_gcheese)))
  subtotal += (count_gcheese * price_gcheese)

if count_pie > 0:
  print("{} Pie @ ${} ==> ${:.2f}".format(count_pie, price_pie, (count_pie * price_pie)))
  subtotal += (count_pie * price_pie)

print("Subtotal: ${:.2f}".format(subtotal))
tax = subtotal * .08
print("Tax: ${:.2f}".format(tax))
discount = 0
if age >= 55:
  discount = (subtotal + tax) * (1 - .55)
if discount > 0:
  print("Discount: ${:.2f}".format(discount))
print("============================")
total = subtotal + tax - discount
print("Total: ${:.2f}".format(total))
print("Please come again!")
