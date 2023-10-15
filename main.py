#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo 

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  turns = 10
elif difficulty == "hard":
  turns = 5
else:
  print("Not a valid difficulty, please restart and choose again")

number = random.randint(1, 100)

print(f"You have {turns} attempts remaining to guess the number.")

def guess_once():
  """Make one time guess of the number, and do a comparison"""
  global turns 
  guess = int(input("Make a guess: "))
  if guess == number:
    print(f"You got it! The answer was {number}.")
  elif guess > number:
    print("Too high.")
    turns -= 1
    if turns == 0:
      print("You've run out of guesses, you lose")
    else :
      print("Guess again.")
      print(f"You have {turns} attempts remaining to guess the number.")
      guess_once()
  else :
    print("Too low.")
    turns -= 1
    if turns == 0:
      print("You've run out of guesses, you lose")
    else :
      print("Guess again.")
      print(f"You have {turns} attempts remaining to guess the number.")
      guess_once()

guess_once()