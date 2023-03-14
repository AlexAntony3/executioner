"""
file that runs the entire game
"""

from src.words import difficulty_level
from src.artwork import intro_logo
from src.main_function import play_again, play_game


def rules():
    """
    Function to print the rules of the game
    """
    print("Welcome to Executioner! A history based hangman game that "
          "has 3 "
          "difficulties, be warned though, they are really tough. \n"
          "Here are the instructions:\n"
          "1. Enter a username\n"
          "2. Pick the difficulty you would like\n"
          "3. You are given 6 lives before the man is hanged\n"
          "4. Guess a letter, if it replaces an _ then you guessed "
          "right!\n"
          "5. However, if you guess incorrectly, you lose a life and "
          "the man "
          "is prepared to be hanged\n"
          "6. If you guess incorrectly 6 times then the man is "
          "EXECUTED!"
          )


def username_prompt():
    """
    function to allow user to enter a username
    """
    username = input("\nNow, lets get familiar, what should I call you?\n")

    print(f'Eurgh! {username}, what a disgusting name')


def main():
    """
    main function that runs all other functions
    """
    intro_logo()
    rules()
    username_prompt()
    word = difficulty_level()
    play_game(word)
    play_again()


main()
