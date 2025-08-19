from random import choice
from enum import Enum
from art import rock_paper_scissors_art, you_win, you_lose, draw


print("--- Game of Rock Paper Scissors ---")
for item in rock_paper_scissors_art:
       print(item)

class RockPaperScissors(Enum):
        ROCK = 0
        PAPER = 1
        SCISSORS = 2

user_input = int(input("Select 0 for Rock, 1 for Paper or 2 for Scissors: "))
if user_input > 2 or user_input < 0:
       print("Invalid input.")
system_input = choice([0,1,2])

print("You chose: " + rock_paper_scissors_art[user_input])
print("System chose: " + rock_paper_scissors_art[system_input])

if system_input == RockPaperScissors.ROCK.value:
       if user_input == RockPaperScissors.PAPER.value:
              print(you_win)
       elif user_input == 2:
              print(you_lose)
       else:
              print(draw)
elif system_input == RockPaperScissors.PAPER.value:
       if user_input == RockPaperScissors.SCISSORS.value:
              print(you_win)
       elif user_input == RockPaperScissors.ROCK.value:
              print(you_lose)
       else:
              print(draw)
elif system_input == RockPaperScissors.SCISSORS.value:
       if user_input == RockPaperScissors.ROCK.value:
              print(you_win)
       elif user_input == RockPaperScissors.PAPER.value:
              print(you_lose)
       else:
              print(draw)