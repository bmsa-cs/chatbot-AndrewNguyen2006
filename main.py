"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util

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
  print("I am Chatbot! I was created to assist and talk to certain people that need somone to talk to. Mostly people who needs friends.")
  print("I am Chatbot! I was created to comfort the people in need, which seems like today, I will be comforting you!")




if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()