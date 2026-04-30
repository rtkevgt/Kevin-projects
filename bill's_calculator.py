def saved_bills(data):

  with open("my_bills.txt","a")as file:
    file.write(data+"\n")
    print("SUCCEES,SAVING YOUR BILLS 💸")
def read_bills():
    total=0
    try:
      with open("my_bills.txt","r")as file:
        print("--SUMMARY OF YOUR BILLS--")
        for line in file:
          line=line.strip()
          if line:
            print(line)
            if"$" in line:
              parts=line.split("$")
              price=float(parts[1])
              total+=price
      print(f"---TOTAL MONEY SPENT: ${total}---")
    except FileNotFoundError:
      print("You don't have any bills saved , put here your first one 😉")
user_name=input("Hi , who is adding bills today ?")

def bills(message):
    while True:
      try:
        value=float(input(message))
        return value
      except ValueError:
       print("Sorry, ONLY THE VALUE OF YOUR BILL , THANKS 😁")

def clear_bills():
          with open("my_bills.txt","w")as file:
            pass
while True:
  try:
      print("---MENU OF BILLS---")
      print("1:Add a new bill")
      print("2:Look into the bill summary")
      print("3:Exit 🛑")
      print("4:Clear bills 🧹")
      choice=input(f"{user_name},please select one option 😎 ")

      if choice=="1":
         name_of_the_bill=input(f"Tell me what did you buy {user_name},? ")
         price=bills(f"What was the price of {name_of_the_bill} $")
         data=f"{name_of_the_bill}:= ${price}\n"
         saved_bills(data)
      elif choice=="2":
       read_bills()
      elif choice=="3":
       print("SEE YOU LATER 😉")
       break
      elif choice=="4":
       clear_bills()
       print("--ALL BILLS DELATED--")
      else:
       print("INVALID, OPCION TRY AGAIN")
  except Exception as e:
      print(f"SOMTHING WRONG HAPPENS: {e}")
      print("LETS TRY AGAIN...")

