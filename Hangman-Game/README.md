# Hangman Game

This repository contains a simple Hangman game implemented in Python using the `tkinter` library for the graphical user interface (GUI).

## How to Play

Hangman is a word-guessing game. The player tries to guess a word by suggesting letters within a certain number of attempts (lives). Here's how to play:

1. **Installation**
   - Clone this repository:
     ```bash
     git clone https://github.com/VipranshOjha/hangman.git
     ```
   - Ensure you have Python installed.

2. **Run the Game**
   - Navigate to the project directory.
   - Execute the Python script:
     ```bash
     python hangman.py
     ```

3. **Game Rules**
   - You have 6 lives to guess the hidden word.
   - Guess letters by typing them into the provided entry box and clicking "Guess".
   - Each incorrect guess results in losing a life and progresses the hangman graphic.
   - You can use the "Hint" button to reveal a random letter from the word (limited to 2 hints).
   - Try to guess the word before you run out of lives!

## Game Components

- **Word List**
  - The game randomly selects a word from a predefined list stored in `hangman_word_list.py`.

- **GUI Components**
  - The game interface is built using `tkinter`.
  - The main game window includes:
    - Labels for displaying the word blanks, guessed letters, hints, hangman stages, and end game messages.
    - Entry box for inputting guessed letters.
    - Buttons for guessing letters and requesting hints.

- **Stages of Hangman**
  - The hangman graphic progresses through different stages as incorrect guesses are made, representing the player's remaining lives.

## Repository Structure

- `hangman.py`: Main Python script containing the Hangman game logic.
- `hangman_word_list.py`: Module with a list of words for the game to choose from.
- `README.md`: This document explaining the game and its usage.

## Dependencies

- Python 3.x
- `tkinter` (standard library)

## Acknowledgments

This Hangman game was developed by Vipransh Ojha as a fun project to practice Python and GUI programming with `tkinter`.

Enjoy playing the game! If you have any feedback or suggestions, feel free to reach out.
