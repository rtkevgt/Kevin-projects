user_name=input("Please , tell me your name 😉")

while True:
  try:
    amount_of_coffees=int(input(f"{user_name}, tell me how many coffee's did you buy?"))
    if amount_of_coffees<=0:
      print("ERROR TRY AGAIN!")
    else:
      print("VALID ANSWER")
      break
  except ValueError:
    print("ERROR TRY AGAIN!")

while True:
  try:
    price_of_each_coffee=float(input(f"Hi {user_name}, please tell me the price of each coffee? THANKS😄 $"))
    if price_of_each_coffee<=0:
      print("ERROR TRY AGAIN!")
    else:
      print("VALID ANSWER")
      break
  except ValueError:
    print("ERROR TRY AGAIN!")

total=amount_of_coffees*price_of_each_coffee
print(f"THE FINAL AMOUNT OF MONEY THAT YOU SPEND ON COFFEE WAS--> ${total} ☕")
