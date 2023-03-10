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
## Design

### Logo

![Logo](docs/screenshots/logo.png "Logo")

The logo was designed using ASCII text generator [fsymbols](https://fsymbols.com/generators/carty/ "fsymbols"). This offers the user a bold enterance to the game and stands out as the first thing you see. This text generator and font style will be used for all main texts, such as game over and congratulations. 

### Colour Scheme

The colours used in text is as follows to add more interactivity to the website. 

### Flow Charts

The below flow charts show the process that is to be followed in the development of the application. The flow chart was created using [draw.io](https://app.diagrams.net/ "draw.io"). The validation required at each input point is added to make sure that the game is reactive to all possible outcomes. 

![Process Flow Chart](docs/screenshots/flowchart.png "Process Flow Chart")

---

## Features

### Current Features

### Future Implementations

---

## Bug Fixes

| Bug detected | Action |
|--|--|
|XX|YY|

### Unfixed Bugs

---

## Technologies used

### Langugages

* HTML - supplied by code instutute template
* CSS - supplied by code instutute template
* JavaScript - supplied by code instutute template
* Python

### Libraries

* [fsymbols](https://fsymbols.com/generators/carty/ "fsymbols")

### Tools
* [draw.io](https://app.diagrams.net/ "draw.io")
* [Heroku](https://www.heroku.com/ "Heroku")
* [Git](https://git-scm.com/ "Git")
* [GitHub](https://github.com/ "GitHub")
* [GitPod](https://www.gitpod.io/ "GitPod")
---

## Testing
| Testing |Outcome | Pass or Fail |
|--|--|--|
|XX|YY|Pass|

---

## Concluding statements

---

## Deployments

As a pure python code can only be displayed on a terminal of your own machine or within gitpod, the code-instutute python essentials template is to be used on the workspace so that it can later be deployed to Heroku for user accessibility.

* add `\n` (newline) character for all inputs.
* If for the function of the game, dependancies are required, then all dependancies are to be transferred to **requirements.txt** by typing the following command into the terminal:

>  pip3 freeze > requirements.txt

### Heroku

* **Log in** to your [Heroku](https://www.heroku.com/  "Heroku") account or **sign up** if it's your first time.
* Activate the Heroku Student Pack as per the instructions on the **Deployments module** in the Love Sandwiches project.
* On the home page, click the **Create new app** button.
* Write an **App name** that is unique, the input bar validation will guide you if the app name has been used before or is available.
* Select the **region** that corresponds to where you are situated.
* Click the **Create app** button
* Click on the **settings** tab and click on **config vars** button.
*  Add a Config var with a key of `PORT` and a value of `8000`.
* If there are any sensative information required for the app to function such as emails, this is to be stored in a **.json** file and also added to the **config vars**. 
* Add  **buildpacks** , by clicking **Add buildback** and click on **python** and click **save changes**. 
* Add another buildback and click on **node.js** and click save changes. The order must be **Python** then **node.js**.
*  Click on the **Deploy** section and in the deployment method click on **GitHub**.
* Search for the **respository** to be deployed and click **connect**.
* Scroll further down and in the automatic deploy section, click the **Enable Automatic Deploys** so that for every push from GitHub, the app is automatically updated. 
* Finally click on **Deploy Branch** to deploy the application. 
* Once the application is deployed, click on the **view** button to see the programme running. 
---

## Credits
* [Simen Daehlin](https://www.linkedin.com/in/simendaehlin/ "Simen Daehlin") - Assistance throughout the project

---

## Inspirations