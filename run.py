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
    difficulty = input(f'Now {username} you ready to challenge yourself? Pick '
                       'a difficulty:\nType E for Easy, M for Medium or H for'
                       ' Hard:\n')
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
        raise TypeError("Sorry, you have not entered a valid difficulty")


def username_prompt():
    """
    function to allow user to enter a username
    """
    username = input("what would you like to be called?\n")
    return username


def main():
    """
    main function that runs all other functions
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
    user = username_prompt()
    difficulty_level(user)


main()
