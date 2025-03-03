# -*- coding: utf-8 -*-
"""rock, paper, and scissors .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gxLrMWk2SAyPan-Fc8QAv8SkqYj-MC9r
"""

import random
# Define valid options for the game
options = ["rock", "paper", "scissors"]
def get_computer_choice():
    # Randomly select between rock, paper, and scissors for the computer
    return random.choice(options)
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in options:
            return user_choice
        else:
            print("Invalid choice! Please choose either rock, paper, or scissors.")
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"
def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result
def game():
    user_score = 0
    computer_score = 0
    while True:
        print("\n--- Rock, Paper, Scissors ---")
        result = play_round()
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"\nScore: You {user_score} - {computer_score} Computer")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    game()