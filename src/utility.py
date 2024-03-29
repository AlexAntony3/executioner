"""
    The functions on this file help to form all
    graphical aspects and effects of the game.
"""
import time
import sys
import os
import random


def clear_screen():
    """
    Function to clear the screen using imported os.
    """
    os.system("clear")


def typing(content, speed):
    """
    Print contents in typewriter format
    in two speeds method.
    """
    for char in content:
        sys.stdout.write(char)
        sys.stdout.flush()
        if speed == "fast":
            time.sleep(0.005)
        else:
            time.sleep(0.03)


def input_typing(content):
    """
    Print contents in typewriter format
    in a slow method for inputs.
    """
    for char in content:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    value = input()
    return value


def pick_putdown():
    """
    A list of putdowns to be used when user answers incorrectly
    """
    putdowns = ["Another one bites the dust",
                "You're really bad at this",
                "I could do better with my eyes closed",
                "This is a true tragedy",
                "You Suck!",
                "Why would you even guess that letter?",
                "Maybe I should make an extra easy version for you"]

    putdown = random.choice(putdowns)
    return putdown


def draw_hangman(lives_left):
    """
    Draw progressing hangman figure according to lives lost.
    """
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
               /|\\  |
                    |
                    |
                =========''')
    elif lives_left == 1:
        print('''
                +---+
                |   |
                O   |
               /|\\  |
               /    |
                    |
                =========''')
    elif lives_left == 0:
        print('''
                +---+
                |   |
                O   |
               /|\\  |
               / \\  |
                    |
                =========''')


def intro_logo():
    """
    Introduction logo
    """
    typing("""
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
        """, "fast")


def winner_logo():
    """
    Winner logo
    """
    print("""

  ░██╗░░░░░░░██╗██╗███╗░░██╗███╗░░██╗███████╗██████╗░
  ░██║░░██╗░░██║██║████╗░██║████╗░██║██╔════╝██╔══██╗
  ░╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
  ░░████╔═████║░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██║░╚███║███████╗██║░░██║
  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
    """)


def loser():
    """
    Loser logo
    """
    print("""

   ██╗░░░░░░█████╗░░██████╗███████╗██████╗░
   ██║░░░░░██╔══██╗██╔════╝██╔════╝██╔══██╗
   ██║░░░░░██║░░██║╚█████╗░█████╗░░██████╔╝
   ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░██╔══██╗
   ███████╗╚█████╔╝██████╔╝███████╗██║░░██║
   ╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
    """)


def goodbye():
    """
    Goodbye Logo for users that don't want to play
    again and additional text
    """
    typing("""
░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝
           psshhttt! if you do want to play again, press
           the run program button above
           """, "fast")
