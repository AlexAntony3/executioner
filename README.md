# Executioner

## Introduction

Welcome to Executioner, a hangman game with 3 difficulties based on words relating to the pre-19th century when executions were all the craze!. The game is a text-based python game that is ran on a mock terminal in Heroku. The user has to guess the secret word before 6 lives run out and the man is hanged. 

[picture of different screen sizes]

### How to play
The game is pretty simple so there's not too much to it
* Enter your username
* Pick a difficulty.
* Guess a letter, if the letter is uncovered you have guessed correctly, if not you have lost a life!
* Guess incorrectly 6 times and that's it GAME OVER!
* Guess the word correctly and you can add some chicken to your dinner because: WINNER WINNER, CHICKEN DINNER!

---

## UX (user experience)

### Goals
* 3 levels of difficulty, the harder the difficulty the more letters there are to guess. 
* Numerically track the amount of lives left in the game.
* Interactive input requirement for the user with validation.
* Feedback for success or failure.
* Clear instructions displayed.

### User's Stories
* As a user, I want to be able to select a difficulty I require. 
* As a user, I expect the underscores of the hidden word is the same length as the secret word. 
* As a user, I want to have feedback if the same letter has already been guessed
* As a user, I want an underscore to convert to the guessed letter if the guessed letter is contained in the secret word. 
* As a user, I want to see the man hanged when all lives are lost. 

### Site Owner's Goals
* If an invalid input is entered e.g. 1, 2, 3 etc. validation is required to inform the user to enter a valid input. 
* Feedback should be presented to the user, when a correct or incorrect letter is entered. 
* When lives are lost a progressional display must be present leading to the final hanged man when all lives are lost.
* The user can replay the game at different or a the same difficulty upon completion. 

### Expectation
* I expect feedback to be visible when inputted by the user.
* I expect all input to have validation to make sure the user can only enter the required input. 
* I expect the user to be able to enter a username and have feedback associated to the feedback. 
* I expect text to be spaces and formatted in a modern format. 

### Requirements
* Validation is required for all user inputs.
* Difficulty must be able to be selected by selecting E, M or H for (easy, medium or hard respectively)
* All secret answers must be related to the pre-19th century theme. 
* Lives remaining must be presented after each guess.

---


