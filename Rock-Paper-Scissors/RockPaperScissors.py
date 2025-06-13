import tkinter as tk
from tkinter import ttk
import random

def play(choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if choice == computer_choice:
        start_label.config(text="It's a tie! 😐", font=("Helvetica", 20, "bold"))
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        start_label.config(text="You win! 😊", font=("Helvetica", 20, "bold"))
    else:
        start_label.config(text="Computer wins! 😔", font=("Helvetica", 20, "bold"))

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size and position
window_width = 400
window_height = 350
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Function to handle button clicks
def rock_click():
    play("Rock")

def paper_click():
    play("Paper")

def scissors_click():
    play("Scissors")

# Create label for starting statement
start_label = ttk.Label(root, text="Rock-Paper-Scissors Shoot!!", font=("Helvetica", 20, "bold"))
start_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Create rock, paper, and scissors buttons
rock_button = ttk.Button(root, text="Rock🪨", command=rock_click)
paper_button = ttk.Button(root, text="Paper📄", command=paper_click)
scissors_button = ttk.Button(root, text="Scissors✂️", command=scissors_click)
rock_button.place(relx=0.10, rely=0.4, relwidth=0.2, relheight=0.2)
paper_button.place(relx=0.40, rely=0.4, relwidth=0.2, relheight=0.2)
scissors_button.place(relx=0.70, rely=0.4, relwidth=0.2, relheight=0.2)

# Create label to display result
result_label = ttk.Label(root, text="", font=("Helvetica", 20, "bold"))
result_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

root.mainloop()