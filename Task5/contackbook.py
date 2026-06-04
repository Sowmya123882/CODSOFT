from tkinter import *
from tkinter import messagebox, ttk
import json
import os

root = Tk()
root.title("Contact Book")
root.geometry("950x600")
root.config(bg="#f4f6f9")

DATA_FILE = "contacts.json"

contacts = []

def load_contacts():
    global contacts

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                contacts = json.load(file)
            except:
                contacts = []

def save_contacts():
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def clear_fields():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append([name, phone, email, address])

    save_contacts()
    update_contact_list()
    clear_fields()

    messagebox.showinfo("Success", "Contact Added Successfully!")

def update_contact_list(search_text=""):
    contact_list.delete(*contact_list.get_children())

    for index, contact in enumerate(contacts):
        name, phone, email, address = contact

        if (search_text.lower() in name.lower() or
                search_text.lower() in phone.lower() or
                search_text == ""):
            contact_list.insert("", END, iid=index,
                                values=(name, phone, email, address))

def search_contact():
    search_text = search_entry.get()
    update_contact_list(search_text)

def select_contact(event):
    selected = contact_list.focus()

    if selected:
        values = contact_list.item(selected, "values")

        clear_fields()

        name_entry.insert(0, values[0])
        phone_entry.insert(0, values[1])
        email_entry.insert(0, values[2])
        address_entry.insert(0, values[3])

def update_contact():
    selected = contact_list.focus()

    if not selected:
        messagebox.showerror("Error", "Select a contact to update!")
        return

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    contacts[int(selected)] = [name, phone, email, address]

    save_contacts()
    update_contact_list()
    clear_fields()

    messagebox.showinfo("Updated", "Contact Updated Successfully!")

def delete_contact():
    selected = contact_list.focus()

    if not selected:
        messagebox.showerror("Error", "Select a contact to delete!")
        return

    confirm = messagebox.askyesno("Delete", "Are you sure?")

    if confirm:
        contacts.pop(int(selected))

        save_contacts()
        update_contact_list()
        clear_fields()

        messagebox.showinfo("Deleted", "Contact Deleted Successfully!")

title = Label(root,
              text="CONTACT BOOK",
              font=("Arial", 24, "bold"),
              bg="#f4f6f9",
              fg="#1f4e79")

title.pack(pady=15)

left_frame = Frame(root, bg="white", bd=2, relief=RIDGE)
left_frame.place(x=20, y=80, width=350, height=480)

Label(left_frame,
      text="Contact Details",
      font=("Arial", 18, "bold"),
      bg="white",
      fg="#333").pack(pady=10)

# Name
Label(left_frame,
      text="Name",
      font=("Arial", 12),
      bg="white").pack(anchor=W, padx=20)

name_entry = Entry(left_frame, font=("Arial", 12), bd=2)
name_entry.pack(padx=20, pady=5, fill=X)

# Phone
Label(left_frame,
      text="Phone",
      font=("Arial", 12),
      bg="white").pack(anchor=W, padx=20)

phone_entry = Entry(left_frame, font=("Arial", 12), bd=2)
phone_entry.pack(padx=20, pady=5, fill=X)

# Email
Label(left_frame,
      text="Email",
      font=("Arial", 12),
      bg="white").pack(anchor=W, padx=20)

email_entry = Entry(left_frame, font=("Arial", 12), bd=2)
email_entry.pack(padx=20, pady=5, fill=X)

# Address
Label(left_frame,
      text="Address",
      font=("Arial", 12),
      bg="white").pack(anchor=W, padx=20)

address_entry = Entry(left_frame, font=("Arial", 12), bd=2)
address_entry.pack(padx=20, pady=5, fill=X)

# Buttons
Button(left_frame,
       text="Add Contact",
       font=("Arial", 12, "bold"),
       bg="#28a745",
       fg="white",
       command=add_contact).pack(pady=10, ipadx=10)

Button(left_frame,
       text="Update Contact",
       font=("Arial", 12, "bold"),
       bg="#007bff",
       fg="white",
       command=update_contact).pack(pady=5, ipadx=10)

Button(left_frame,
       text="Delete Contact",
       font=("Arial", 12, "bold"),
       bg="#dc3545",
       fg="white",
       command=delete_contact).pack(pady=5, ipadx=10)

Button(left_frame,
       text="Clear Fields",
       font=("Arial", 12, "bold"),
       bg="#6c757d",
       fg="white",
       command=clear_fields).pack(pady=5, ipadx=10)

right_frame = Frame(root, bg="white", bd=2, relief=RIDGE)
right_frame.place(x=390, y=80, width=530, height=480)

Label(right_frame,
      text="Saved Contacts",
      font=("Arial", 18, "bold"),
      bg="white",
      fg="#333").pack(pady=10)

# Search Box
search_frame = Frame(right_frame, bg="white")
search_frame.pack(fill=X, padx=10)

search_entry = Entry(search_frame, font=("Arial", 12), bd=2)
search_entry.pack(side=LEFT, padx=5, fill=X, expand=True)

Button(search_frame,
       text="Search",
       font=("Arial", 11, "bold"),
       bg="#17a2b8",
       fg="white",
       command=search_contact).pack(side=LEFT, padx=5)

# Table
columns = ("Name", "Phone", "Email", "Address")

contact_list = ttk.Treeview(right_frame,
                            columns=columns,
                            show="headings")

for col in columns:
    contact_list.heading(col, text=col)
    contact_list.column(col, width=120)

contact_list.pack(fill=BOTH, expand=True, padx=10, pady=15)

contact_list.bind("<ButtonRelease-1>", select_contact)

# Scrollbar
scrollbar = Scrollbar(contact_list,
                      orient=VERTICAL,
                      command=contact_list.yview)

contact_list.configure(yscroll=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)

load_contacts()
update_contact_list()

# main method
root.mainloop()