# Lab 1
# Group # 1 7
# Author: Alexey Konovalov
# Date: 09/22/2026


def rock_paper_scissors():
    """Play a Rock-Paper-Scissors game against the computer."""
    
    while True:
        play = input("Do you want to play? ").strip().lower()

        if play not in ["yes", "y"]:
            print("Thanks for playing!")
            break

        user_choice = int(input("Enter your choice: 1. Paper, 2. Scissors, 3. Rock: "))

        if user_choice not in [1, 2, 3]:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        computer_choice = random.randint(1, 3)
        choices = {1: "Paper", 2: "Scissors", 3: "Rock"}

        print(f"You chose {choices[user_choice]}.")
        print(f"Computer chose {choices[computer_choice]}.")

        if user_choice == computer_choice:
            print("It is a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (Y/N): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    rock_paper_scissors()
