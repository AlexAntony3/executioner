# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import easy_words
from words import medium_words
from words import hard_words

# while lives_left > 0:

#     user_guess = input("I know the word, and I know you won't get it, guess
#  a "
#                        "letter:")

#     if user_guess in SecretWord.word:
#         print("hmm, okay that was correct, probably just pure luck.")
#         print(f'{user_guess}', end="")


def draw_hangman(lives_left):
    if lives_left == 6:
        print('''
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========''')
    elif lives_left == 5:
        print(
            '''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========''')
    elif lives_left == 4:
        print(
            '''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========''')
    elif lives_left == 3:
        print('''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                =========''')
    elif lives_left == 2:
        print('''
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                =========''')
    elif lives_left == 1:
        print('''
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                =========''')
    elif lives_left == 0:
        print('''
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                =========''')


def introduction():
    """
    Function to call all aspects of the introduction function
    """
    print("""
        ███████╗██╗░░██╗███████╗░█████╗░██╗░░░██╗
        ██╔════╝╚██╗██╔╝██╔════╝██╔══██╗██║░░░██║
        █████╗░░░╚███╔╝░█████╗░░██║░░╚═╝██║░░░██║
        ██╔══╝░░░██╔██╗░██╔══╝░░██║░░██╗██║░░░██║
        ███████╗██╔╝╚██╗███████╗╚█████╔╝╚██████╔╝
        ╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░
        ████████╗██╗░█████╗░███╗░░██╗███████╗██████╗░
        ╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝██╔══██╗
        ░░░██║░░░██║██║░░██║██╔██╗██║█████╗░░██████╔╝
        ░░░██║░░░██║██║░░██║██║╚████║██╔══╝░░██╔══██╗
        ░░░██║░░░██║╚█████╔╝██║░╚███║███████╗██║░░██║
        ░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
        """)

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


def difficulty_level():
    """
    function to set difficulty level of questions
    """
    difficulty = input(" I know "
                       "you "
                       "are never going to win. You can try though, so "
                       "pick "
                       "a difficulty:\n\nType E for Easy, M for Medium or"
                       " H "
                       "for Hard:\n")
    if difficulty == "E":
        random_word = random.choice(easy_words).upper()
    elif difficulty == "M":
        random_word = random.choice(medium_words).upper()
    elif difficulty == "H":
        random_word = random.choice(hard_words).upper()
    else:
        raise TypeError("clearly, that was too many instructions for you, "
                        "enter a valid letter")

    return random_word


# Pre-requisites

correct_letters = []
incorrect_letters = []
lives_left = 6
secret_word = difficulty_level()

while lives_left > 0:

    user_guess = input("\nGo on, guess a letter: ")

    for letter in secret_word:
        if letter in secret_word:
            print(letter, end="")
        else:
            print("_", end="")
            lives_left -= 1


def main():
    """
    main function that runs all other functions
    """
    introduction()
    username_prompt()
    difficulty_level()


main()
