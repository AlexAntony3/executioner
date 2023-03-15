"""
    file for artwork that's used in the hangman game.
"""
import time
import sys


def fast_typing(content):
    """
    Function designed to print contents in typewriter format
    in a fast method.
    """
    for char in content:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


def slow_typing(content):
    """
    Function designed to print contents in typewriter format
    in a slow method.
    """
    for char in content:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)


def input_typing(content):
    """
    Function designed to print contents in typewriter format
    in a slow method.
    """
    for char in content:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    value = input()
    return value


def draw_hangman(lives_left):
    """
    Function to draw progressing hangman figure according to lives lost.
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


def intro_logo():
    """
    Function to call the introduction logo
    """
    fast_typing("""
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


def winner_logo():
    """
    function to call the winner logo
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
    function to call the loser logo
    """
    print("""

   ██╗░░░░░░█████╗░░██████╗███████╗██████╗░
   ██║░░░░░██╔══██╗██╔════╝██╔════╝██╔══██╗
   ██║░░░░░██║░░██║╚█████╗░█████╗░░██████╔╝
   ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░██╔══██╗
   ███████╗╚█████╔╝██████╔╝███████╗██║░░██║
   ╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
    """)
