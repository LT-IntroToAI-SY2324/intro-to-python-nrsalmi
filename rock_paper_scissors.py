# We will write a rock paper scissors game in class - Complete it in this file
import random

def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins. Better luck next time."

def play_game():
    print("Welcome to Rock Paper Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You: {user_choice} VS Computer: {computer_choice}.")
    result = winner(user_choice, computer_choice)
    print(result)

play_game()