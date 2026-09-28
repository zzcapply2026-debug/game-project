#Lab 1
#Group #17
#Author: Chujun Zhang
#09/25/2026



from guessing import guessing_game
from rock_paper_scissors_game import rock_paper_scissors
import random

def main():
    '''Displays the game menu in a loop, calling the selected game and letting the user play again, switch games(by returning to the game menu), or quit. Author: Chujun Zhang'''
    
    while True:
        print('Which game do you want to play? 1. Guessing Game 2. Rock Paper Scissors 3. Quit')
        choice = input('Your choice(please enter the number):') 
        if choice == '1':
            guessing_game()
            choice_2= input('Do you want to（1）play again, (2) switch games, or (3) quit? ')
            if choice_2 == '1':
                guessing_game()
            elif choice_2 == '2':
                continue
            elif choice_2 == '3':
                break
            else:
                print("Invalid input. Please try again.")
        elif choice == '2':
            rock_paper_scissors()
            choice_3= input('Do you want to（1） play again, (2) switch games, or (3) quit? ')
            if choice_3 == '1':
                rock_paper_scissors()
            elif choice_3 == '2':
                continue
            elif choice_3 == '3':
                break
            else:
                print("Invalid input. Please try again.")
        elif choice == '3':
            break
        else:
            print('Invalid input.Please try again.')
       
if __name__ == "__main__":
    main()
