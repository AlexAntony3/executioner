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

    return random_word.upper()


# Pre-requisites
def play_game(random_word):

    letters_guessed = []
    lives_left = 6
    secret_word = "_" * len(random_word)
    guessed = False

    username_prompt()

    while guessed is False and lives_left > 0:

        user_guess = input("\nGo on, guess a letter: ").upper()

        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in letters_guessed:
                print("\nThe instructions were at the start of the game..."
                      " you already guessed that letter, try again \n")
            elif user_guess in random_word:
                print(f"\nLucky guess, {user_guess} is in the secret word.\n")
                letters_guessed.append(user_guess)
                secret_word_list = list(secret_word)
                indexed_list = [i for i, letter in enumerate(random_word) if
                                letter == user_guess]
                for index in indexed_list:
                    secret_word_list[index] = user_guess
                secret_word = "".join(secret_word_list)
                if '_' not in secret_word:
                    guessed = True
            else:
                print("\n Putdown. ")
                lives_left -= 1
                letters_guessed.append(user_guess)

            print(secret_word)

    if guessed:
        print("... I didn't expect that to happen, you're not as "
              "dumb as you look. Well done.")
    else:
        print("I told you it was hard. HAHAHA the correct word was: "
              f"{random_word} ")


def main():
    """
    main function that runs all other functions
    """
    word = difficulty_level()
    play_game(word)


main()
