# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import easy_words
from words import medium_words
from words import hard_words


def difficulty_level():
    """
    function to set difficulty level of questions
    """
    difficulty = input('Now are you ready to challenge yourself? Pick a'
                       'difficulty: Type E for Easy, M for Medium or H for'
                       'Hard :')
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


difficulty_level()
