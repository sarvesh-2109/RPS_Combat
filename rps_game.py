import random
from art import rock, paper, scissor


def compare(comp, user):
    """Returns the result after comparing it with the computer's choice."""
    if comp == user:
        return "It is a draw."
    elif (comp == "rock" and user == "scissor") or (comp == "scissor" and user == "paper") or (comp == "paper" and user == "rock"):
        return "You lose. Computer won."
    elif (user == "rock" and comp == "scissor") or (user == "scissor" and comp == "paper") or (user == "paper" and comp == "rock"):
        return "You win. Computer lose."


def choice_art(choice):
    """Returns the ASCII art based on the choices made by the computer and the user."""
    if choice == "rock":
        return rock
    elif choice == "paper":
        return paper
    elif choice == "scissor":
        return scissor


def main():
    """Takes user input on choices. Calls the 'compare' function. Prints the result."""
    computer_choice = random.choice(["rock", "paper", "scissor"])
    computer_art = choice_art(computer_choice)
    user_choice = input("Enter any one of the desired elements: Rock, Paper or Scissor:\n").lower()
    user_art = choice_art(user_choice)
    print(f"Your choice is: {user_choice}\n{user_art}")
    print(f"Computer choice is: {computer_choice}\n{computer_art}")
    result = compare(computer_choice, user_choice)
    print(result)
    return


def game():
    """Calls the 'main' function. Ask whether the user wishes to play again"""
    one_more_time = True
    print("Welcome to the Rock, Paper and Scissor game.")
    while one_more_time:
        main()
        continue_game = input("Do you want to play the one more time?: 'y' or 'n'\n").lower()
        if continue_game == 'n':
            print("Thanks for playing.")
            return
        else:
            one_more_time = True


game()