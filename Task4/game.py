from tkinter import *
from tkinter import messagebox
import random
# Main Window
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x500")
root.config(bg="white")
# Scores
user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]
# Game Function
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    user_label.config(text="You Chose : " + user_choice)
    computer_label.config(text="Computer Chose : " + computer_choice)
    # Winner Logic
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    result_label.config(text=result)
    # Update Scores
    user_score_label.config(text="Your Score : " + str(user_score))
    computer_score_label.config(text="Computer Score : " + str(computer_score))
# Reset Game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="You Chose : ")
    computer_label.config(text="Computer Chose : ")
    result_label.config(text="Result")
    user_score_label.config(text="Your Score : 0")
    computer_score_label.config(text="Computer Score : 0")
# Heading
title = Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="darkblue"
)
title.pack(pady=20)
# Instructions
instruction = Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 14),
    bg="white"
)
instruction.pack(pady=10)
# Buttons Frame
button_frame = Frame(root, bg="white")
button_frame.pack(pady=20)
# Rock Button
rock_btn = Button(
    button_frame,
    text="Rock",
    width=12,
    height=2,
    font=("Arial", 12, "bold"),
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)
# Paper Button
paper_btn = Button(
    button_frame,
    text="Paper",
    width=12,
    height=2,
    font=("Arial", 12, "bold"),
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)
# Scissors Button
scissors_btn = Button(
    button_frame,
    text="Scissors",
    width=12,
    height=2,
    font=("Arial", 12, "bold"),
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)
# User Choice Label
user_label = Label(
    root,
    text="You Chose : ",
    font=("Arial", 14),
    bg="white"
)
user_label.pack(pady=10)
# Computer Choice Label
computer_label = Label(
    root,
    text="Computer Chose : ",
    font=("Arial", 14),
    bg="white"
)
computer_label.pack(pady=10)
# Result Label
result_label = Label(
    root,
    text="Result",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="green"
)
result_label.pack(pady=20)
# Score Labels
user_score_label = Label(
    root,
    text="Your Score : 0",
    font=("Arial", 14),
    bg="white"
)
user_score_label.pack(pady=5)
computer_score_label = Label(
    root,
    text="Computer Score : 0",
    font=("Arial", 14),
    bg="white"
)
computer_score_label.pack(pady=5)
# Reset Button
reset_btn = Button(
    root,
    text="Reset Game",
    width=15,
    height=2,
    font=("Arial", 12, "bold"),
    bg="lightblue",
    command=reset_game
)
reset_btn.pack(pady=20)
# Exit Button
exit_btn = Button(
    root,
    text="Exit",
    width=15,
    height=2,
    font=("Arial", 12, "bold"),
    bg="tomato",
    command=root.destroy
)
exit_btn.pack(pady=10)
root.mainloop()