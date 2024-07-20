import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry widget for displaying the result
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons for the calculator
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            if button == '=':
                tk.Button(root, text=button, padx=20, pady=20, command=self.calculate).grid(row=row_val, column=col_val, columnspan=2, sticky="nsew")
                col_val += 2
            elif button == 'C':
                tk.Button(root, text=button, padx=20, pady=20, command=self.clear).grid(row=row_val, column=col_val, sticky="nsew")
                col_val += 1
            else:
                tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky="nsew")
                col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        current_text = self.result_var.get()
        new_text = current_text + str(char)
        self.result_var.set(new_text)

    def clear(self):
        self.result_var.set("")

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except:
            messagebox.showerror("Error", "Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
