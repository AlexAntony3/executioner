# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import easy_words
from words import medium_words
from words import hard_words


class SecretWord():
    """
    Obtain a random secret word from the difficulty based choice words list.
    """
    def __init__(self):

        difficulty = input('Now are you ready to challenge yourself? Pick a'
                           'difficulty: Type E for Easy, M for Medium or H for'
                           'Hard :')
        if difficulty.upper() == "E":
            self.word = random.choice(easy_words)
            return word.upper()
        elif difficulty.upper() == "M":
            self.word = random.choice(medium_words)
            return word.upper()
        elif difficulty.upper() == "H":
            self.word = random.choice(hard_words)
            return word.upper()
        else:
            raise TypeError("Sorry, you have not entered a valid difficulty")
