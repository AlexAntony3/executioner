"""
File for words used in the game depending on difficulty
"""
import random
from .utility import input_typing, clear_screen


easy_words = ('axe bow king war bell gun mask hang die '
              'past earl lord guts rat poor rich kill '
              'debt dire time duma pope jail gold rich ').split()

medium_words = ('albion prince queen helots liberty Nobel '
                'praetor mummies anicent fascism monarch '
                'murder witch magic penalty sharp crime ').split()

hard_words = ('guillotine casualties protection liberation '
              'scimitar weapon behead hanged torture execute '
              'revolution archaeology almanac etymology numeral ').split()


def difficulty_level():
    """
    function to set difficulty level of questions
    """
    choice = False
    while not choice:
        difficulty = input_typing("I know you are never going to win. You can "
                                  "try though, so pick a difficulty:\n\nType "
                                  "E for Easy, M for Medium or H for Hard:\n")
        if difficulty.upper() == "E":
            random_word = random.choice(easy_words).upper()
            choice = True
            clear_screen()
            return random_word.upper()
        if difficulty.upper() == "M":
            random_word = random.choice(medium_words).upper()
            choice = True
            clear_screen()
            return random_word.upper()
        if difficulty.upper() == "H":
            random_word = random.choice(hard_words).upper()
            choice = True
            clear_screen()
            return random_word.upper()
        print("clearly, that was too many instructions for you, "
              "enter a valid letter")
