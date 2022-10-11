# Portfolio Project 3 - Python Essentials
## Welcome to the Hangman Game!
Here you can enjoy yourself and, at the same time, train your spelling with this popular guessing words game.

![Image mockup of the website in a computer, tablet and phone](assets/images/hangman_mockup.png)

## Live Site
[Go to site](https://williams-hangman-game.herokuapp.com/) 

## Repository
[View repository](https://github.com/williamtyn/hangman) 

## Catalouge
<li><a href="#target-group">Target Group</a></li>
<li><a href="#flowchart">Flowchart</a></li>
<li><a href="#how-to-play">How to play</a></li>
<li><a href="#features">Features</a></li>
<ul>
<li><a href="#welcome">Welcome</a></li>
<li><a href="#choose-nickname">Choose nickname</a></li>
<li><a href="#rules">See rules</a></li>
<li><a href="#random">Random word generated</a></li>
<li><a href="#guess-word">Guess word</a></li>
<li><a href="#validation">Validation of input</a></li>
<li><a href="#lives-and-guess">Lives and guesses</a></li>
<li><a href="#win-or-game">Win or Game over</a></li>
<li><a href="#play-again">Play again?</a></li>
</ul>
<li><a href="#user-stories">User stories</a>
<li><a href="#bugs">Bugs</a></li>
<ul>
<li><a href="#solved-bugs">Solved Bugs</a></li>
</ul>
<li><a href="#future-features">Future features</a></li>
<li><a href="#technologies">Technologies</a></li>
<li><a href="#validation">Validation</a></li>
<li><a href="#deployment">Deployment</a></li>
<li><a href="#credits">Credits</a></li>
<ul>
<li><a href="#code-issues">Issues with code</a></li>
<li><a href="#student-support">Student Support</a></li>
<li><a href="#code">Code</a></li></ul>
<li><a href="#acknowledgements">Acknowledgements</a></li></ul>
</li>
</ul>
<br>
<h2 id="target-group">Target Group</h2>
The Hangman game is for both educational use and fun. Because you can train your spelling, one of the main target groups is schools that want a fun way of teaching students the spelling of words.
<br>
<br>
<h2 id="flowchart">Flowchart</h2> 

To have some structure and to be able to understand which codes and functions the program would have, I have created a flowchart using [Lucid](https://lucid.app/).

In the flowchart, you can see the whole process from start to finish. All the code is based on the flowchart, and beyond that, I also added a function to choose a nickname for the player.

![Flowchart image](assets/images/hangman_flowchart.png)

<br>
<h2 id="how-to-play">How to play</h2>

Hangman is a game of words where you guess the secret word as the computer shuffles them.<br>
You can press any letter between A – Z to guess if that letter is in the word.<br>
You have 1 chance to guess the whole word.<br>
If you think you know the word, you can guess it by typing it in.<br>
For each wrong word or letter, you will lose one of your lives.<br>
You have 5 lives to guess the right word before it is Game Over!.<br>

<h2 id="features">Features</h2>
<h3 id="welcome">Welcome</h3>
The player can see the text "Welcome to Hangman Game" and the visual Hangman printed.

![Welcome image](assets/images/features/welcome.png)

<h3 id="choose-nickname">Choose nickname</h3>
The player must choose their nickname and player name to play the game.

![Nickname](assets/images/features/nickname.png)

<h3 id="rules">See rules</h3>
If the player has never played before or doesn´t remember the rules, they get an option to see the rules before they start the game. If the player don´t want to see the rules, the game starts.

![See rules](assets/images/features/see_rules.png)

![Rules](assets/images/features/rules.png)

<h3 id="random">Random words generated</h3>
We collected a list with over 100 different words that the program randomly picks from. The program also hides the letters in the words until the player has guessed the correct letter.

![Random words](assets/images/features/random_words.png)

<h3 id="guess-word">Guess word</h3>
As a player, you can choose to guess a letter from the alphabet or you can guess the word. Every letter you guess gets added to your guessed letters list. If the letter is in the word, the letter gets displayed in the right position and the player doesn´t lose any lives.

![Guess word](assets/images/features/guess_word.png)

<h3 id="validation">Validation of input</h3>
The player can only guess letters between A to Z in the alphabet and receive a message saying "Your guess can only contain letters A - Z. Try again!" if they try anything else. The player doesn´t lose any lives in this case.

![Validation of letters](assets/images/features/validation_only_letters.png)

If the player guesses a letter that they have already guessed, they receive a message saying "You have already guessed (and the letter). The player doesn´t lose any lives in this case.

![Validation already guessed](assets/images/features/validation_guessed.png)

If the letter is in the alphabet, it is not in the previous guesses or in the word. The player loses a life.

![Life loss](assets/images/features/lose_life.png)

<h3 id="lives-and-guess">Lives and guesses</h3>
The player has 5 lives, as mentioned above. If the letter validation is correct and the letter is not in the word, the player loses a life.

All guessed letters get added to the guessed letters list, as the player can always see.

<h3 id="win-or-game">Win or Game over</h3>
The player wins the game when the guess is the correct word and they still have lives left. They can see the print of "You Win" with asterisks.

If the player doesn't have any lives left, they get the message "Game Over" with asterisks.

![Life loss](assets/images/features/gameover.png)

<h3 id="play-again">Play again</h3>
After every run, win or game over, the player gets the question if they want to play again. If they want to play again, the program runs again from the point where it picks a random word.

If a player doesn't want to play again, the program ends.

![Play again](assets/images/features/play_again.png)

<h2 id="user-stories">User stories</h2>

### User Story 1
As a player, I want to play a word game against the computer to improve my spelling of English words.

*The player gets the opportunity to improve their spelling of words in the hangman game. When the players guess a letter, they receive a hint of the word and must use both their vocabulary and spelling to guess the correct word.*


### User Story 2
As a player, I want to be able to choose my own nickname or player name to feel more satisfied if I win the game.

*At the beginning of the game, the player must choose a nickname to be able to play the game. If the player wins, they get the "Congrats" message with their nickname to boost their confidence.*


### User Story 3
As a player, I want to be able to play the game many times with different words to keep practicing my spelling.

*The word list contains a variety of words, which reduces the likelihood of the random word being chosen again while also providing the player with a variety of words to practice spelling with. At the end of each game, the players have the option to play again. " Do you want to play again? Y/N ".*


<h2 id="bugs">Bugs</h2>
If the player wants to change their nickname, they need to end and restart the whole program. If they choose to play again after winning or losing, the game repeats with the same nickname and they don't have an option to change it.

<h3 id="solved-bugs">Solved Bugs</h3>

1. I got stuck in the while loop where the program checks the guesses. When the player guessed the right word, the loop broke, and at the end of the loop, a print with "Game Over" was shown.

*I solved that by changing the structure to return instead. So if the player guesses the right word, the function returns True. If the player loses all lives, the function returns False. By moving out the check for win or loss, I was able to solve the bug.*

2. When deploying, I found that when a player guessed a word that was wrong, all letters were added to the guessed letters list. Because of that, the player couldn't try the letters separated again. Because of that, the player got stuck.

*I solved that by adding a validation for the number of letters in the guess. If the player guesses more than one letter, they're guessing for the word. If the word is wrong, it's game over.*


<h2 id="future-features">Future features</h2>

### Change nickname
In the future, a feature for changing nicknames could be added if someone else wants to play without having to cancel the program and start over.

<h2 id="technologies">Technologies</h2>

* The project was built with [GitPod](https://gitpod.io/) and [GitHub](https://github.com/)<br>
* The project was deployed to [Heroku](https://dashboard.heroku.com/apps)<br>
* Random Words was genereated by [Randomlists.com](https://www.randomlists.com/)<br>
* To check spelling and grammar i used [Free Grammar Checker](https://quillbot.com/grammar-check)<br>
* To make the Readme Mockup i used [Multi Device Mockup Generator](https://techsini.com/multi-mockup/)<br>
* The library that was imported is **random** and **colorama**<br>

<h2 id="validation">Validation</h2>

Because the online validator for PEP8 is currently offline. I´ve followed the steps that Kevin_ci on Code Institute provided.

As a workaround, you can add a PEP8 validator to your Gitpod Workspace directly by following these steps:
1. Run the command pip3 install pycodestyle  Note that this extension may already be installed, in which case this command will do nothing.
2. In your workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
3. Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results (image 1).
4. Select pycodestyle from the list (image 2).
5. PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

After that i worked from start to finish to erase every linting issue in the code.

<h2 id="deployment">Deployment</h2>

1. Log in to Heroku and create a new app.
The first thing when deploying is to log in to [Heroku](https://dashboard.heroku.com/apps) and click **new** then **create app**.

![Create new app](assets/images/create_new_app.png)

2. Give your app a name.
Then you need to select a new name for your app. I named my app "williams-hangman-game". Then select your region and press "Create App".

![App name](assets/images/app_name.png)

3. Add config vars
In the menu you click **settings** and then **Reveal Config Vars**. Input **PORT** as key and **8000** as value, press "Add".

![Config Vars](assets/images/config_vars.png)

4. Add buildpacks
Under config vars you can see **buildpacks**. Click "add buildpacks" and add **python** and **nodejs** (in that order). Click "Save changes".

![Buildpacks](assets/images/buildpacks.png)

5. Deploy section
Go to **Deploy** in menu and choose **GitHub** as your **Deployment Method**. Confirm that you want to connect to GitHub and search your repository name. For this project it is "Hangman". Click "connect" and link your repository to Heroku.

![Deployment Method](assets/images/deployment_method.png)

6. Deploy branch
Click "Deploy Branch" to manual deploy the site.

![Deployment Method](assets/images/deploy_branch.png)

7. App successfully deployed
If everything is OK then you recieve "Your app was successfully deployed" and can click "View".

![Deployment Successfully](assets/images/deployment_success.png)

<h2 id="credits">Credits</h2>
<h3 id="code-issues">Issues with code</h3>

Most of the daily problems were solved thanks to [Stackoverflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/).

<h3 id="code">Code</h3>

A big thanks to [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w&t=423s) with the video for inspiration on how to solve the challenge with getting the hidden words do display the letter when the player guesses right.

<h3 id="acknowledgements">Acknowledgements</h3>

This website was completed as a Portfolio Project 3 for the Fullstack Diploma at [Codeinstitute](https://codeinstitute.net/).
I want to thank my friend Martin for helping me understand some logic with functions at the start of this project.

The project is for educational purposes only and not for public consumption.
<br>
<br>
William Tynér, October 2022.<br>
[LinkedIn](https://www.linkedin.com/in/williamtyner/)