# Executioner

## Introduction

Welcome to Executioner, a hangman game with 3 difficulties based on words relating to the pre-19th century when executions were all the craze!. The game is a text-based python game that is ran on a mock terminal in Heroku. The user has to guess the secret word before 6 lives run out and the man is hanged. 

![Screen Displays](docs/screenshots/responsiveness.png "Screen Displays")

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

#### Initial Screen
The initial feature observed by the user is the title: Executioner, a fast typewriter effect is given to the title which offers a fun experience to the user and allows them to know that they are going to be playing a game. Secondly, a slower typewriter effect input statement is present whereby, the user is prompted to enter a name. 
![Initial Screen](docs/screenshots/initial.png "Initial Screen")

#### Username Prompt
The username input prohibits the user to enter a name that is purely alphabetical and also stops the user entering nothing. The invalid entry error message is shown below. Furthermore if a valid entry is inputted by the user, then the next step of the game, which is asking the user if they would like to read instructions. 
![Username Prompt](docs/screenshots/username.png "Username Prompt")

#### Instructions Prompt
After successfully adding a username, the user is prompted to answer the question of "Do you want to read the instructions? Y/N?". The validation provided for this function only allows the user to answer with a "Y" or an "N". If either of those answers are not entered, an error is shown and the user is prompted again to answer the question. If the user answers with a Y, the instructions of the game are provided, if they answer with an N, the user goes onto the next step of the game. 
![Instruction Error](docs/screenshots/instruction_error.png "Instruction Error")
![Instruction](docs/screenshots/instructions.png "Instructions")
![Instruction Skip](docs/screenshots/no_instructions.png "Instruction Skip")

#### Difficulty Prompt
The next step of the game is the ask the user what level of difficulty they would like to play at. The length of the secret word to guess will increase relatively according to what difficulty is selected. (e.g easy, will be words like BELL and hard would be words like GUILLOTINE) There is also validation to this input by only allowing the user to select E, M or H, as shown in the screenshots below:
![Difficulty Error](docs/screenshots/difficulty_error.png "Difficulty Error")
![Difficulty](docs/screenshots/difficulty.png "Difficulty")

#### Game Screen
The game screen compromises of multiple variables that the user requires to be able to play game whilst being UX friendly. As typically observed in hangman, a visible and transitional hanging of a man is presented. Other features presented ara:
* The secret word that the user has to guess is presented as underscores, which updates if the letter guessed is in the secret word.
* If the letter guessed is not in the secret word, a randomly chosen putdown is presented to the user. This improves the overall interactibility of the game as well as the user interphase. 
* The number of lives left for the user is also presented, this added with the hangman progression allows the user to know how much of the game is remaining. If the user guesses an incorrect letter, the number of lives go down. 
* All letters guessed by the user is also presented to the user, so they are aware of letters guessed. This helps the user from guessing the same letter again.
* An input is presented to the user to enter a letter as a guess to check if it is in the secret word. This letter is fed through to all the other variables within the game screen.
* Finally, validation is provided to the user to stop them from entering in an invalid response and the input is offered again.
![Game Screen Correct](docs/screenshots/gamescreen_correct.png "Game Screen Correct")
![Game Screen Incorrect](docs/screenshots/gamescreen_incorrect.png "Game Screen Incorrect")
Validation
![Game Screen Error](docs/screenshots/gamescreen_error.png "Game Screen Error")

#### End Screen
The end screen is one of the final aspects that the user will meet before the game is finished. The end screen offers two outcomes, either the user is successful or unsuccessful. If the user guesses the word correctly, the user is met with a message and a custom font "WINNER". If the user does not guess the word within the number of lives (6) the user is met with another message and the custom font stating "LOSER". 
![Winner](docs/screenshots/winner.png "Winner")
![Loser](docs/screenshots/loser.png "Loser")

The Final feature of the game is a question to ask the user if wants to retry the game. If a user would like to retry, they enter "Y" and the game is restarted. If the user does not, they are greeted with an animated message saying goodbye and an option to press run programme if they do want to restart the game after the game is finished. Moreover, as seen throughout the game, validation is added to make sure the valid responses are limited to "Y" or "N" and if neither of those entries are added, the user is greeted with an error message. 
![Goodbye](docs/screenshots/goodbye.png "Goodbye")
Validation
![Retry Validation](docs/screenshots/retry_validation.png "Retry Validation")

### Future Implementations
* In the future, given more time I would like to improve adding designs and colour to the webpage, this would entice a user to stay on the page and recommend the page to others.
* With more time and resources, I would like to implement a feature to share scores with others on social media.
* With more time and resources, I would like to add a hint function to each word for user's who require additional help. 
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

### Tools
* [draw.io](https://app.diagrams.net/ "draw.io")
* [Heroku](https://www.heroku.com/ "Heroku")
* [Git](https://git-scm.com/ "Git")
* [GitHub](https://github.com/ "GitHub")
* [GitPod](https://www.gitpod.io/ "GitPod")
* [fsymbols](https://fsymbols.com/generators/carty/ "fsymbols")
* [AmIResponsive](https://ui.dev/amiresponsive "AmIResponsive")
* [Python Linter](https://pep8ci.herokuapp.com/ "Python Linter")
---

## Testing
| Testing |Outcome | Pass or Fail |
|--|--|--|
|XX|YY|Pass|

---

## Concluding statements
In conclusion, I am very proud of what I have built. Throughout the project, there were multiple errors I ran across which took a lot of time to fix, but it was worth it. The game I designed handles all invalid inputs, provides feedback to the user and replicates a classical game that is known by everyone around the globe. The game is intuitive and easy to use. My parents who are the least tech-savvy people I know, was able to play the game without any further instructions. 

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