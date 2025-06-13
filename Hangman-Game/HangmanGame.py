import tkinter as tk
import random
import hangman_word_list
import emoji

# Initialize tkinter
root = tk.Tk()
root.title("Hangman")

# Stages
stages = [''' 
  +---+
  |   |
 😭   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
 😱   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
 😨   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
 😓   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
 😥   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
 🥲    |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Chosen word
chosen_word = random.choice(hangman_word_list.word_list)

# Display blanks
display = ["_" for _ in chosen_word]

# Guessed letters
guessed_letters = []

# Lives
lives = 6

# Number of hints used
hints_used = 0

# Label to display word
word_label = tk.Label(root, text=" ".join(display), font=("Arial", 18))
word_label.pack(anchor=tk.CENTER)

# Function to handle guess
def guess_letter():
    global lives
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    
    if guess in guessed_letters:
        # Letter already guessed, do nothing
        return
    
    guessed_letters.append(guess)
    guessed_label.config(text="Guessed Letters: " + ", ".join(guessed_letters))
    
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        word_label.config(text=" ".join(display))
    else:
        lives -= 1
        hangman_label.config(text=stages[lives])
        if lives == 0:
            end_game("You lose. The word was: " + chosen_word)

    if "_" not in display:
        end_game("You win!")

# Function to provide hint
def give_hint():
    global hints_used
    if hints_used < 2:
        # Find all positions where the letter is present in the word
        hint_positions = [pos for pos, char in enumerate(chosen_word) if char not in guessed_letters]

        if hint_positions:
            # Randomly choose one of the positions and reveal the letter
            hint_position = random.choice(hint_positions)
            display[hint_position] = chosen_word[hint_position]
            word_label.config(text=" ".join(display))
            hints_used += 1
            if hints_used == 2:
                hint_button.config(state=tk.DISABLED)
        else:
            hint_label.config(text="No hint available. You've guessed all the letters!")
    else:
        hint_label.config(text="You've used all available hints.")

# Function to end the game
def end_game(message):
    end_label.config(text=message)
    guess_entry.config(state=tk.DISABLED)

# Entry for guessing letters
guess_entry = tk.Entry(root, font=("Arial", 14))
guess_entry.pack(anchor=tk.CENTER)

# Button to submit guess
guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack(anchor=tk.CENTER)

# Button to get hint
hint_button = tk.Button(root, text="Hint", command=give_hint)
hint_button.pack(anchor=tk.CENTER)

# Label for guessed letters
guessed_label = tk.Label(root, text="Guessed Letters: ", font=("Arial", 14))
guessed_label.pack(anchor=tk.CENTER)

# Label for hint
hint_label = tk.Label(root, text="", font=("Arial", 14))
hint_label.pack(anchor=tk.CENTER)

# Label for hangman stages
hangman_label = tk.Label(root, text="", font=("Arial", 14))
hangman_label.pack(anchor=tk.CENTER)

# Label for end game message
end_label = tk.Label(root, text="", font=("Arial", 18))
end_label.pack(anchor=tk.CENTER)

# Run the GUI
root.mainloop()
