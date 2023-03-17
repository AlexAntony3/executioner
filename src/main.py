from .utility import input_typing, draw_hangman, clear_screen, \
    pick_putdown, winner_logo, loser, intro_logo, typing, goodbye
from .words import difficulty_level


def rules_prompt():
    """
    Offers user an opportunity to pick if they would like to
    read the instructions or not at the start of the game
    """
    while True:
        try:
            prompt = input_typing("\nDo you want to read the "
                                  "instructions? Y/N?").upper()
            if prompt not in ("Y", "N"):
                raise ValueError("Very simple, Y or N...")
            if prompt == "Y":
                rules()
                break
            word = difficulty_level()
            play_game(word)
            break
        except ValueError as e:
            print(e)


def rules():
    """
    Function to print the rules of the game
    """
    typing("Welcome to Executioner!\nA history based hangman game that "
           "has 3 difficulties, be warned though,\nthey are really tough."
           "\n"
           "\nHere are the instructions:\n"
           "1. First of all, please let all the typewriter\nanimation to "
           "finish before entering anything. If the programme loops \n"
           "press run programme to start again.\n"
           "2. Pick the difficulty you would like\n"
           "3. You are given 6 lives before the man is hanged\n"
           "4. Guess a letter, if it replaces an _ then you guessed "
           "right!\n"
           "5. However, if you guess incorrectly, you lose a life and "
           "\nthe man is prepared to be hanged\n"
           "6. If you guess incorrectly 6 times then the man is EXECUTED!"
           "\n", ""
           )
    word = difficulty_level()
    play_game(word)


def username_prompt():
    """
    function to allow user to enter a username
    """
    while True:
        try:
            username = input_typing("\nNow, lets get familiar, what should I "
                                    "call you?\n")
            if not username.isalpha() or len(username) < 1:
                raise ValueError("\nYour name must contains letters only and "
                                 "atleast 1 character")
            print(f'\nEurgh! {username}, what a disgusting name\n')
            rules_prompt()
            break
        except ValueError as e:
            print(e)


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
    print(f"These are the letters you've guessed so far:{letters_guessed}")

    while guessed is False and lives_left > 0:
        try:
            user_guess = input_typing("\nGo on, guess a letter: ").upper()

            if len(user_guess) == 1 and user_guess.isalpha():
                if user_guess in letters_guessed:
                    raise ValueError("\nThe instructions were at the start of "
                                     "the game...you already guessed that "
                                     "letter, try again \n")
                if user_guess in random_word:
                    clear_screen()
                    print(f"\nLucky guess, {user_guess} is in the secret "
                          "word.\n")
                    letters_guessed.append(user_guess)
                    secret_word_list = list(secret_word)
                    indexed_list = [i for i, letter in enumerate(random_word)
                                    if letter == user_guess]
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
                print("These are the letters you've guessed so far: "
                      f"{letters_guessed}")
            else:
                print("\nThe instructions must've been too hard to follow... "
                      "guess one valid alphabetical character.\n")
        except ValueError as e:
            print(e)

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
        try:
            replay = input("\nDo you want another try? Y/N :").upper()
            if replay not in ("Y", "N"):
                raise ValueError("\nSimple instructions, Y or N...\n")
            if replay == "N":
                goodbye()
                break
            retry = True
            clear_screen()
            main()
            break
        except ValueError as e:
            print(e)


def main():
    """
    main function that runs all other functions
    """
    intro_logo()
    username_prompt()
    play_again()
