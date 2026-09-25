#Lab 1
#Group #17
#Author: Chujun Zhang
#09/25/2026



from guessing import guessing_game
from rock_paper_scissors_game import rock_paper_scissors
import random
def main():
    while True:
        print('Which game do you want to play? 1. Guessing Game 2. Rock Paper Scissors 3. Quit')
        choice = input('Your choice(please enter the number):') 
        if choice == '1':
            guessing_game()
            choice_2 = input('Do you want to switch the game? (Y/N)')
            if choice_2 =='Y':
                rock_paper_scissors()
            elif choice_2 =='N':
                break
            else:
                print("Invalid input. Please try again.")
        elif choice == '2':
            rock_paper_scissors()
            choice_3 = input('Do you want to switch the game? (Y/N)')
            if choice_3 =='Y':
                guessing_game()
            elif choice_3 =='N':
                break
            else:
                print("Invalid input. Please try again.")
        elif choice == '3':
            break
        else:
            print('Invalid input.Please try again.')

        

if __name__ == "__main__":
    main()
    
