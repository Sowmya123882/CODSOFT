from tkinter import *
from tkinter import messagebox
# WINDOW
window = Tk()
window.title("Professional To-Do List")
window.geometry("500x550")
window.config(bg="#F4F6F9")
window.resizable(False, False)
#  FUNCTIONS
def add_task():
    task = entry_box.get()
    if task.strip() != "":
        listbox.insert(END, "• " + task)
        entry_box.delete(0, END)
        status_label.config(
            text="Task Added Successfully",
            fg="green"
        )
    else:
        status_label.config(
            text="Please Enter a Task",
            fg="red"
        )
def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
        status_label.config(
            text="Task Deleted Successfully",
            fg="green"
        )
    else:
        status_label.config(
            text="Select a Task First",
            fg="red"
        )
def clear_tasks():
    listbox.delete(0, END)
    status_label.config(
        text="All Tasks Cleared",
        fg="green"
    )
# TITLE 
title_label = Label(
    window,
    text="TO-DO LIST",
    font=("Helvetica", 24, "bold"),
    bg="#F4F6F9",
    fg="#2C3E50"
)
title_label.pack(pady=20)
#  FRAME 
main_frame = Frame(
    window,
    bg="white",
    bd=2,
    relief=SOLID
)
main_frame.pack(padx=25, pady=10, fill=BOTH, expand=True)
# ENTRY
entry_box = Entry(
    main_frame,
    font=("Arial", 14),
    width=28,
    bd=2,
    relief=GROOVE
)
entry_box.pack(pady=20, padx=20, ipady=8)
# BUTTON FRAME
button_frame = Frame(main_frame, bg="white")
button_frame.pack(pady=10)
# Add Button
add_button = Button(
    button_frame,
    text="Add Task",
    font=("Arial", 12, "bold"),
    bg="#3498DB",
    fg="white",
    width=12,
    bd=0,
    cursor="hand2",
    command=add_task
)
add_button.grid(row=0, column=0, padx=10)
# Delete Button
delete_button = Button(
    button_frame,
    text="Delete Task",
    font=("Arial", 12, "bold"),
    bg="#E74C3C",
    fg="white",
    width=12,
    bd=0,
    cursor="hand2",
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=10)
# Clear Button
clear_button = Button(
    button_frame,
    text="Clear All",
    font=("Arial", 12, "bold"),
    bg="#2ECC71",
    fg="white",
    width=12,
    bd=0,
    cursor="hand2",
    command=clear_tasks
)
clear_button.grid(row=0, column=2, padx=10)
# LISTBOX 
listbox = Listbox(
    main_frame,
    font=("Arial", 13),
    width=40,
    height=12,
    bd=2,
    relief=GROOVE,
    selectbackground="#3498DB",
    activestyle="none"
)
listbox.pack(pady=20)
#  STATUS LABEL 
status_label = Label(
    window,
    text="Manage Your Daily Tasks Efficiently",
    font=("Arial", 11),
    bg="#F4F6F9",
    fg="#7F8C8D"
)
status_label.pack(pady=10)
# RUN WINDOW
window.mainloop()