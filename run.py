# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import easy_words
from words import medium_words
from words import hard_words


def difficulty_level(username):
    """
    function to set difficulty level of questions
    """
    difficulty = input(f"Eurgh {username}, what a disgusting name. I know you "
                       "are never going to win. You can try though, so pick "
                       f"a difficulty:\n\nType E for Easy, M for Medium or H "
                       "for Hard:\n")
    if difficulty.upper() == "E":
        word = random.choice(easy_words)
        print(word.upper())
    elif difficulty.upper() == "M":
        word = random.choice(medium_words)
        print(word.upper())
    elif difficulty.upper() == "H":
        word = random.choice(hard_words)
        print(word.upper())
    else:
        raise TypeError("clearly, that was too many instructions for you, "
                        "enter a valid letter")


def username_prompt():
    """
    function to allow user to enter a username
    """
    username = input("\nNow, lets get familiar, what should I call you?\n\n")
    return username


def introduction():
    """
    Function to call all aspects of the introduction function
    """
    print("""
        ███████╗██╗░░██╗███████╗░█████╗░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗███████╗██████╗░
        ██╔════╝╚██╗██╔╝██╔════╝██╔══██╗██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝██╔══██╗
        █████╗░░░╚███╔╝░█████╗░░██║░░╚═╝██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║█████╗░░██████╔╝
        ██╔══╝░░░██╔██╗░██╔══╝░░██║░░██╗██║░░░██║░░░██║░░░██║██║░░██║██║╚████║██╔══╝░░██╔══██╗
        ███████╗██╔╝╚██╗███████╗╚█████╔╝╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║███████╗██║░░██║
        ╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
    """)
    print("Welcome to Executioner! A history based hangman game that has 3 "
          "difficulties, be warned though, they are really tough. \n")
    print("Here are the instructions:\n"
          "1. Enter a username\n"
          "2. Pick the difficulty you would like\n"
          "3. You are given 6 lives before the man is hanged\n"
          "4. Guess a letter, if it replaces an _ then you guessed right!\n"
          "5. However, if you guess incorrectly, you lose a life and the man "
          "is prepared to be hanged\n"
          "6. If you guess incorrectly 6 times then the man is EXECUTED!")


def main():
    """
    main function that runs all other functions
    """
    introduction()
    user = username_prompt()
    difficulty_level(user)


main()
