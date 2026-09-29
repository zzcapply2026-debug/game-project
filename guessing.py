# Lab 1
# Group 17
# Author: Zichen Zheng
# Date: September 22, 2026

import random
def guessing_game():
  
    """ This function runs a guessing game. Author: Zichen Zheng """

    while True:
      number = random.randint(1,100)
      tries = 5

      print("I'm thinking of a number between 1 and 100.")

      while tries > 0:
        guess = int(input("guess what it is? You have " + str(tries) + " tries:"))

        if guess == number:
          print("you got it!")
          break
        elif guess < number:
          print("Nope! Too low.")

        else:
          print("Nope! Too high.")

        tries = tries - 1

      if tries == 0:
        print("you lost. The number was", number)
      
      play_again = input("Do you want to play again? (Y/N)")
      
      if play_again =="N":
        break
  
if __name__== "__main__":
  guessing_game()



