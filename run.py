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
    if difficulty == "E":
        secret_word = random.choice(easy_words).upper()
    elif difficulty == "M":
        secret_word = random.choice(medium_words).upper()
    elif difficulty == "H":
        secret_word = random.choice(hard_words).upper()
    else:
        raise TypeError("clearly, that was too many instructions for you, "
                        "enter a valid letter")
    return secret_word


def username_prompt():
    """
    function to allow user to enter a username
    """
    username = input("\nNow, lets get familiar, what should I call you?\n\n")
    return username


lives_left = 6


def guess_word(secret_word):
    while lives_left > 0:
        user_guess = input("What letter are you going to guess?\n")
        
        if user_guess in secret_word:
            print(user_guess)
            break
        else:
            print("nope")
            break


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
    word = difficulty_level(user)
    guess_word(word)


main()
