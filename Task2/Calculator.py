from tkinter import *
from tkinter import messagebox
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("500x750")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        # Expression
        self.expression = ""
        self.input_text = StringVar()

        # ================= DISPLAY =================
        display_frame = Frame(self.root, bg="white")
        display_frame.pack(fill="both", padx=20, pady=20)

        self.display = Entry(
            display_frame,
            textvariable=self.input_text,
            font=("Segoe UI", 32, "bold"),
            bg="#f3f4f6",
            fg="black",
            bd=0,
            justify=RIGHT,
            insertbackground="black"
        )

        self.display.pack(fill="both", ipady=25)

        button_frame = Frame(self.root, bg="white")
        button_frame.pack(expand=True, fill="both", padx=15, pady=15)

        # Grid Configuration
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)

        for j in range(4):
            button_frame.columnconfigure(j, weight=1)

        # Buttons Layout
        buttons = [
            ["C", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        # Create Buttons
        for row, row_values in enumerate(buttons):

            col = 0

            for button in row_values:

                # Default Colors
                bg_color = "#ffffff"
                fg_color = "black"

                # Operator Colors
                if button in ["÷", "×", "-", "+", "%"]:
                    bg_color = "#dbeafe"
                    fg_color = "#1d4ed8"

                elif button == "=":
                    bg_color = "#22c55e"
                    fg_color = "white"

                elif button == "C":
                    bg_color = "#ef4444"
                    fg_color = "white"

                elif button == "⌫":
                    bg_color = "#facc15"
                    fg_color = "black"

                # Button Command
                action = lambda x=button: self.on_button_click(x)

                btn = Button(
                    button_frame,
                    text=button,
                    command=action,
                    font=("Segoe UI", 20, "bold"),
                    bg=bg_color,
                    fg=fg_color,
                    activebackground="#e5e7eb",
                    activeforeground="black",
                    relief=FLAT,
                    bd=1,
                    cursor="hand2"
                )

                # Proper Grid Arrangement
                if button == "0":

                    btn.grid(
                        row=row,
                        column=col,
                        columnspan=2,
                        sticky="nsew",
                        padx=8,
                        pady=8,
                        ipadx=10,
                        ipady=15
                    )

                    col += 2

                else:

                    btn.grid(
                        row=row,
                        column=col,
                        sticky="nsew",
                        padx=8,
                        pady=8,
                        ipadx=10,
                        ipady=15
                    )

                    col += 1

        footer = Label(
            self.root,
            text="Professional Calculator using Python Tkinter",
            bg="white",
            fg="gray",
            font=("Segoe UI", 11)
        )

        footer.pack(pady=10)

    def on_button_click(self, value):

        # Clear
        if value == "C":

            self.expression = ""
            self.input_text.set("")

        # Backspace
        elif value == "⌫":

            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)

        # Calculate
        elif value == "=":

            try:

                expression = self.expression.replace("×", "*").replace("÷", "/")

                result = str(eval(expression))

                self.input_text.set(result)

                self.expression = result

            except:

                messagebox.showerror("Error", "Invalid Expression")

                self.expression = ""
                self.input_text.set("")

        # Add Values
        else:

            self.expression += str(value)

            self.input_text.set(self.expression)

root = Tk()

Calculator(root)

root.mainloop()