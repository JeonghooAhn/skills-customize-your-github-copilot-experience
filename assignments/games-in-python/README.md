
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a simple text-based game in Python that helps students practice strings, loops, conditionals, and user input through a classic hangman-style challenge.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the core game logic for a word-guessing game by selecting a random word and preparing the hidden word display.

#### Requirements
Completed program should:

- Store a list of words for the game to choose from
- Randomly select one word at the start of each round
- Display the word as blanks or underscores such as `_ _ _ _ _`
- Keep the game state organized and easy to update as the player guesses

### 🛠️ Player Guessing Logic

#### Description
Allow the player to enter guesses and update the game based on whether the letter is correct or incorrect.

#### Requirements
Completed program should:

- Ask the user to enter one letter at a time
- Check whether the guessed letter is in the secret word
- Reveal matching letters in the correct positions
- Show the current progress after each guess
- Prevent repeated guesses from counting twice

### 🛠️ Win/Loss Conditions

#### Description
Add the final game rules so the player can win or lose clearly and the program ends appropriately.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining
- End the game when the word is fully guessed
- End the game when the player runs out of attempts
- Print a clear win or lose message at the end
- Include a simple play again option if desired
