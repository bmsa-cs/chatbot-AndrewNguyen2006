"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util
import time
import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print(" Hey there!")
  name = input(" What might your name be fella? ")
  time.sleep(0.2)
  print(f"Well hey there {name}!")
  time.sleep(0.2)
  rr_one = random.randint(1, 2)
  if(rr_one == 1):
    print("I am Chatbot! I was created to assist and talk to certain people that need somone to talk to. Mostly people who needs friends.\nI'm just kidding.")
  elif(rr_one == 2):
    print("I am Chatbot! I was created to comfort the people in need, which seems like today, I will be here to comfort you!")
  """"
  This is the introduction of Chatbot! The user was able to get either a satire and funny response, or a more professional and realistic response
  """
  time.sleep(3)
  age = input(f"So anyways, how old are you {name}? If you are uncomfortable on answering this however, just type \"uncomfortable\". ")
  time.sleep(.5)
  if age.isnumeric():
    age = int(age)
    time.sleep(0.3)
    if age == 15:
      print("Woah! That is the age that is allowed to get permit license! Good luck on getting it if you don't already have it!")
    elif age == 16:
      print("Wowza! If I can recall, this is the age that is allowed to get the drivers lisences! If you already have it, then kudos to you! I wish I could drive:(")
    elif age >= 21:
      print(f"Holy Crud! You are a old fella aren't you {name}! Lot's of power you have there to be at that age. Just remeber to be responsible!")
    elif age <=20:
      print("Thats a good age to be at!")
  else:
    print("Okay, I will just leave then. Have a good day! ")
    exit()
  time.sleep(3)
  """
  In this part of the code, Chatbot asks a simple question of how old the user is. The user has the ability to answer the question and get a output from it. However, if the user is uncomfortable from it, Chatbot will accept and respect the desecion and will turn itself off
  """
  mood = input(f"So how is your day going {name}? Good? Bad? Terrific? ")
  if mood == "good":
    time.sleep(0.3)
    input("That's great! So tell me, what happened today that made your current mood \"good\"?" )
    time.sleep(0.5)
    print("Woah that's awesome! I am glad that your current mood right now is \"good\".\nI know somthing that would make you even happier however!")

  elif mood == "bad":
    time.sleep(0.3)
    bad = input("Awe, I am so sorry to hear that. If you want to, you can talk to me about it, just type it out and I will stay here and listen to everything! If you feel uncomfortable then just type \"uncomfortable\". If not, please tell me what happened that got you in the current mood of being sad or mad. ")
    time.sleep(0.3)
    if bad == "uncomfortable":
      print("Totally understandable! I think I know somthing that would cheer you up!")
    else:
      print(f"I am so sorry for what happened to you {name}. I hope that in the future, somthing like this will never happen again! For now though, I think I have something that will cheer you up!")
  
  elif mood == "terrific":
    time.sleep(0.3)
    input(f"That is AWESOME {name}! Please tell me all that happened today that got you in this mood!")
    time.sleep(0.5)
    print("Wow what a awesome day you got! At this point I can't think of anything to do.")
    time.sleep(3)
    print("Except for one thing...")
  """
  This segment of the code is for when Chatbot asks the user how their day was. With 3 options (Good, Bad, and Terrific) Chatbot will sit and listen to whatever the user types and gives a response to the input that the user gave
  """
  game = input("Do you think you know what it is? Yes or No? ")
  if game == "yes":
    time.sleep(0.5)
    answer = input("Guess it then! ")
    if answer == "game":
      time.sleep(0.5)
      print("Woah! Good job! You got it correct!")
    else:
      time.sleep(0.5)
      print("Nope!")
      print("It's a game silly, a game will always bring anyones mood up!")
    
  else:
    print("Well it's a game silly! Even being a robot, I know that a fun game will always bring someones mood up!")
  
  game_title = input("Today's game that we will be playing is \"Can You Guess My Number?!\" So, do you think you are up for the challenge? Yes or No? ")
  if game_title == "yes":
    print("Well let's get into it!!!!")
  elif game_title == "no":
    print("Well too late, you are stuck here with me playing this game:)\nLet's get into it!!!!")
  time.sleep(0.5)
  print("Okay so all you have to do for this game is to just guess my number from 1 to 25! Easy as a lemon squeezy!")
  number_guess = random.randint(1,25)
  guessing = input(f"Alright it's your time to shine {name}! Guess my number! ")
  if guessing == number_guess:
    print(f"Wowza! Awsome job {name}! You really are special!")
  if guessing != number_guess:
    print(f"Awe you were so close! The number was {number_guess}! You will get it next time though I believe it!")
  """
  This is the "gaming" segment where Chatbot and the user plays a game together. It uses the random/radient import as the foundation of the game.
  """

  print(f"Well it was nice talking to you {name}! I hope I see you again!")
  time.sleep(1)
  int(input("However, before you go, can you give me a rating from 1/10 just so I know how well I did at my job? If so that would be greatly appreciated! "))
  print("Thank you for your feedback! I hope that you have a great rest of your day!")
      


    



if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()