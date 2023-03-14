"""
file that runs the entire game
"""

from src.words import difficulty_level
from src.artwork import draw_hangman
from src.artwork import intro_logo


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


# Pre-requisites
def play_game(random_word):
    """
    Function to use pre-requisite variables to play the game, this includes
    converting the random word into underscores checking if the letter
    entered is within the word and also draw the hangman according to 
    lives lost.
    """

    letters_guessed = []
    lives_left = 6
    secret_word = "_" * len(random_word)
    guessed = False

    draw_hangman(lives_left)
    print(secret_word)

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

            draw_hangman(lives_left)
            print(secret_word)
        else:
            print("\nThe instructions must've been too hard to follow... "
                  "guess one valid alphabetical character.\n")

    if guessed:
        print("... I didn't expect that to happen, you're not as "
              "dumb as you look. Well done.")
    else:
        print("I told you it was hard. HAHAHA the correct word was: "
              f"{random_word} ")


def play_again():
    """
    Function to allow user the option to play again once game is completed.
    """
    replay = input("Do you want another try? Y/N :").upper()

    if replay == "N":
        print("goodbye")
    elif replay == "Y":
        word = difficulty_level()
        play_game(word)
        play_again()
    else:
        print("Simple instructions, Y or N...")
        play_again()


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
