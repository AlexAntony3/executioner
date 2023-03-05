# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


class Secretword():
    """
    Obtain a random secret word from the difficulty based choice words list. 
    """
    def __init__(self):
        if difficulty_choice.upper() == "E":
            self.word = random.choice(easy_words_list)
        elif difficulty_choice.upper() == "M":
            self.word = random.choice(medium_words_list)
        elif difficulty_choice.upper() == "H":
            self.word = random.choice(hard_words_list)