from tkinter import *
import random
import string

root = Tk()
root.title("Password Generator APP")

root.state("zoomed")

root.config(bg="#f5deb3")

title = Label(
    root,
    text="PASSWORD GENERATOR APP",
    font=("Arial", 28, "bold"),
    bg="#f5deb3",
    fg="darkblue"
)
title.pack(pady=30)

frame = Frame(root, bg="white", bd=4, relief=RIDGE)
frame.pack(pady=30)

label = Label(
    frame,
    text="CHOOSE AN OPTION",
    font=("Arial", 16, "bold"),
    bg="lightgray",
    width=30
)
label.pack(pady=20)

selection = ""

def selection_type():
    global selection

    if choice.get() == 1:
        selection = string.ascii_lowercase

    elif choice.get() == 2:
        selection = string.ascii_letters

    elif choice.get() == 3:
        selection = string.ascii_letters + string.digits + string.punctuation

choice = IntVar()

R1 = Radiobutton(
    frame,
    text="WEAK",
    font=("Arial", 14),
    variable=choice,
    value=1,
    command=selection_type,
    bg="white"
)
R1.pack(pady=5)

R2 = Radiobutton(
    frame,
    text="AVERAGE",
    font=("Arial", 14),
    variable=choice,
    value=2,
    command=selection_type,
    bg="white"
)
R2.pack(pady=5)

R3 = Radiobutton(
    frame,
    text="STRONG",
    font=("Arial", 14),
    variable=choice,
    value=3,
    command=selection_type,
    bg="white"
)
R3.pack(pady=5)

lenlabel = Label(
    frame,
    text="Password Length",
    font=("Arial", 14, "bold"),
    bg="white"
)
lenlabel.pack(pady=15)

val = IntVar(value=12)

spinlength = Spinbox(
    frame,
    from_=4,
    to_=32,
    textvariable=val,
    font=("Arial", 14),
    width=10
)
spinlength.pack()

password_label = Label(
    frame,
    text="",
    font=("Arial", 26, "bold"),
    bg="white",
    fg="green"
)
password_label.pack(pady=30)

def generate_password():

    global selection

    if selection == "":
        selection = string.ascii_letters

    password = ""

    for i in range(val.get()):
        password += random.choice(selection)

    password_label.config(text=password)

Button(
    frame,
    text="Generate Password",
    font=("Arial", 14, "bold"),
    bg="blue",
    fg="white",
    padx=15,
    pady=8,
    command=generate_password
).pack(pady=20)

footer = Label(
    root,
    text="Generate Strong & Secure Passwords Easily",
    font=("Arial", 12),
    bg="#f5deb3",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=20)

root.mainloop()