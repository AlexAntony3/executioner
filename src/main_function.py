from artwork import draw_hangman
from words import difficulty_level


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
        print("imple instructions, Y or N...")
        play_again()