"""
file that runs the entire game
"""

from src.words import clear_screen, difficulty_level, pick_putdown
from src.artwork import intro_logo, draw_hangman, winner_logo, loser


def username_prompt():
    """
    function to allow user to enter a username
    """
    while True:
        username = input("\nNow, lets get familiar, what should I call you?\n")
        if username.isalpha() and len(username) >= 1:
            print(f'\nEurgh! {username}, what a disgusting name\n')
            rules()
            break
        print("\nYour name must contains letters only and atleast 1 character")


def rules():
    """
    Function to print the rules of the game
    """
    print("Welcome to Executioner!\nA history based hangman game that "
          "has 3 difficulties, be warned though,\nthey are really tough. \n"
          "\nHere are the instructions:\n"
          "1. Pick the difficulty you would like\n"
          "2. You are given 6 lives before the man is hanged\n"
          "3. Guess a letter, if it replaces an _ then you guessed "
          "right!\n"
          "4. However, if you guess incorrectly, you lose a life and "
          "\nthe man is prepared to be hanged\n"
          "5. If you guess incorrectly 6 times then the man is EXECUTED!\n"
          )
    word = difficulty_level()
    play_game(word)


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
    print(f'\nThe Secret Word is : {secret_word}\n')
    print(f'\nYou have {lives_left} lives left.\n')

    while guessed is False and lives_left > 0:

        user_guess = input("\nGo on, guess a letter: ").upper()

        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in letters_guessed:
                print("\nThe instructions were at the start of the game..."
                      " you already guessed that letter, try again \n")
            elif user_guess in random_word:
                clear_screen()
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
                clear_screen()
                print(pick_putdown())
                lives_left -= 1
                letters_guessed.append(user_guess)

            draw_hangman(lives_left)
            print(f'\nThe Secret Word is : {secret_word}\n')
            print(f'\nYou have {lives_left} lives left.\n')
        else:
            print("\nThe instructions must've been too hard to follow... "
                  "guess one valid alphabetical character.\n")

    if guessed:
        print("\n... I didn't expect that to happen, you're not as "
              "dumb as you look. Well done.\n")
        winner_logo()
    else:
        print("\nI told you it was hard. HAHAHA the correct word was: "
              f"{random_word}\n")
        loser()


def play_again():
    """
    Function to allow user the option to play again once game is completed.
    """
    retry = False
    while retry is not True:
        replay = input("\nDo you want another try? Y/N :").upper()

        if replay == "N":
            print("goodbye")
            break
        if replay == "Y":
            retry = True
            clear_screen()
            main()
        else:
            print("\nSimple instructions, Y or N...\n")


def main():
    """
    main function that runs all other functions
    """
    intro_logo()
    username_prompt()
    play_again()


main()
