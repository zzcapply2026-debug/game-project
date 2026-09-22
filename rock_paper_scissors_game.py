# Lab 1
# Group # 1 7
# Author: Alexey Konovalov
# Date: 09/22/2026


#not completed yet

import random


def rock_paper_scissors():
    """Play a Rock-Paper-Scissors game against the computer."""
    while True:
        play = input("Do you want to play? ").strip().lower()

        if play not in ["yes", "y"]:
            print("Thanks for playing!")
            break
