import random
from replit import clear 
from art import logo 

#creating a list of numbers from 1 to 100
numbers = []
for number in range(1, 101):
  numbers.append(number)

#randomly selected computer number
selected_number = random.choice(numbers)

#Created a funtion that would compare the numbers and print a statement
def compare_numbers(computer_number, user_number):
  """
  This function compares a user selected number to a computer generated number
  """
  if user_number > computer_number:
    return "Too high"
  elif user_number < computer_number:
    return "Too low"


def guess_the_number():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    lives = 10
  else:
    lives = 5

  game_end = False
  while not game_end:
    print(f"You have {lives} attempts remaning to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess != selected_number:
      print(compare_numbers(selected_number, user_guess))
      print("Guess again.")
      lives -= 1
      if lives == 0:
        print("You have run out of guesses, you lose.")
        game_end = True
    elif user_guess == selected_number:
      print(f"You got it! The answer was {user_guess}")
      game_end = True

  #This is a recurssion to replay the game until the program is stopped
  play_game = input("Type 'p' to play the 'Guess the number' game: ")
  if play_game == 'p':
    clear()
    guess_the_number()

guess_the_number()