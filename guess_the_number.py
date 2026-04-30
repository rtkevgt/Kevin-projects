print("Hello , lets play a little game ,🔢--Guess the secret number--🔢")
user_name=input("Who is playing this wonderfull game today? ")
secret_number=7
while True:
  try:
    number=float(input(f"Lets do this {user_name}, Guess.... The....Number....----->"))
    if number>secret_number:
      print("mmmmm, no , 😉 try again!!")
    elif number<secret_number:
     print("mmmmmm, Guess, 😁 try again!!")
    else:
      print("mmmmmm, Yes , YOU.....WIN.....CONGRATS 🥳")
      break
  except ValueError:
    print("-Hey-, Im so sorry but only, PUT NUMBERS! 😄")
