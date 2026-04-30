def save_goals(data):
  #this create the file if it doesn't exist, and addthe textat the end
  with open("my_goals.txt","a")as file:
    file.write(data)
    print("Succes , saving the goal!")

def read_goals():
  try:
    with open("my_goals.txt","r")as file:
      print("SUMMARY OF YOUR GOALS")
      print(file.read())
  except FileNotFoundError:
    print("--YOU DO NOT HAVE ANY GOALS SAVED, LETS DO THE FIRST ONE 😉--")

  #this one try to reed the file, if it doesn't exist, it do not do anything(avoid errors)
read_goals()
    #This program is to see how much money do you earn per hour then how much hours you needs for any goal that you have
user_name =input(" Hi ,please tell me your name , i'm here to help you see if you have saved enough money for your goal at the end of the year, ")
# what you have to do is a kind of program that aks name, ask goal, ask hours that the person work, how much the person earns per hour ,put the if ,else,elif about the progress that you have done for your goal put how many hours you need to work to grt that goal, so this help to know how many hours of work you need to spend to get your goal
def money (message):
  while True:
    try:
      value=float(input(message))
      return value
    except ValueError:
      print("-ERROR-, This doesn't look like a number, please introduce only digits ,👍")
goal= money(f"{user_name}, tell me what is your final goal of the year $")
money_earn_per_hour= money(f"{user_name} can you tell me how much do you earn per hour 💸, thanks -> $")

hours_left_for_the_goal= round(goal/money_earn_per_hour)
print(f"{user_name} the final amount of hour that you need for that goal are {hours_left_for_the_goal} hours,⌛")
days_left= round(hours_left_for_the_goal/24)
print(f"Bro ,{user_name} (fun fact) you have to work for almost {days_left} days with out sleep isn't that wild ☠🤯")
#put the float always when you ask for a number it could be age, money, hours etc.

if money_earn_per_hour>=17:
  print(f"Wow, {user_name} you earn more then the average people in the US ,keep that job 😉")
elif money_earn_per_hour>=12 and money_earn_per_hour<17:
  print(f"You know that, {user_name} you earn the average money in the US , that's grate 👍")
else:
   print(f"Hey, {user_name} let me be honest with you , that job that you have is not even the average of what normal people, have you think about quit your job that people is steelling you ⚠")
if hours_left_for_the_goal<=300:
  print(f"Wow,{user_name} your goal is at the end of the corner , lets go my friend i know you can do this its only {hours_left_for_the_goal} hours,🥳")
elif hours_left_for_the_goal>=600 and hours_left_for_the_goal<1000:
  print(f"{user_name} this is like kind of hard but i know you can do this this its kind of hard but i belive that you have the strenght to keep going 😉")
elif hours_left_for_the_goal >=2000:
  print(f"Hey, {user_name} is a long way but not impossible , good luck 👍 ")
else:
  print(f"Hey, {user_name} keep going is a hard work and a long way to finish but i believe that if you actually want your goal you can do this , good luck👍")
save=input("Do you want to save this resul in your file ? (yes/no)")
if save.lower()=="yes":
  data=f"{user_name}: Goal of {goal} with {hours_left_for_the_goal} hours"
save_goals(data)
