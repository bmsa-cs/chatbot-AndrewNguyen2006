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
  print(f"Well hey there {name}!")
  rr_one = random.randint(1, 2)
  if(rr_one == 1):
    print("I am Chatbot! I was created to assist and talk to certain people that need somone to talk to. Mostly people who needs friends. \n I'm just kidding.")
  elif(rr_one == 2):
    print("I am Chatbot! I was created to comfort the people in need, which seems like today, I will be here to comfort you!")
  """"
  This is the introduction of Chatbot! The user was able to get either a satire and funny response, or a more professional and realistic response
  """
  time.sleep(3)
  age = input(f"So anyways, how old are you {name}? If you are uncomfortable on answering this however, just type \"uncomfortable\".")
  if age.isnumeric():
    age = int(age)
    time.sleep(0.3)
    if age == 15:
      print("Woah! That is the age that is allowed to get permit license! Good luck on getting it if you don't already have it!")
    elif age == 16:
      print("Wowza! If I can recall, this is the age that is allowed to get the drivers lisences! If you already have it, then kudos to you! I wish I could dirve:(")
    elif age >= 21:
      print(f"Holy Crud! You are kinda old fella. You are able to drink, drive, vote, and do many others things! Sounds like you have a lot of power in your hands their {name}!")
    elif age <=20:
      print("Thats a good age to be at!")
  else:
    print("Okay, I will just leave then. Have a good day! ")
    exit()
  """
  In this part of the code, Chatbot asks a simple question of how old the user is. The user has the ability to answer the question and get a output from it. However, if the user is uncomfortable from it, Chatbot will accept and respect the desecion and will turn itself off
  """
 


    



if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()