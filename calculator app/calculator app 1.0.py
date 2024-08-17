import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")
        self.geometry("300x300")

        self.create_widgets()

    def create_widgets(self):
        self.num1_entry = tk.Entry(self, width=20)
        self.num1_entry.pack(pady=10)



        self.num2_entry = tk.Entry(self, width=20)
        self.num2_entry.pack(pady=10)

        self.result_label = tk.Label(self, text="", width=20)
        self.result_label.pack(pady=10)

        self.add_button = tk.Button(self, text="Add", command=self.add)
        self.add_button.pack(pady=5)

        self.subtract_button = tk.Button(self, text="Subtract", command=self.subtract)
        self.subtract_button.pack(pady=5)

        self.multiply_button = tk.Button(self, text="Multiply", command=self.multiply)
        self.multiply_button.pack(pady=5)

        self.divide_button = tk.Button(self, text="Divide", command=self.divide)
        self.divide_button.pack(pady=5)

    def get_numbers(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = add(num1, num2)
            self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = subtract(num1, num2)
            self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = multiply(num1, num2)
            self.result_label.config(text=f"Result: {result}")

    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = divide(num1, num2)
            self.result_label.config(text=f"Result: {result}")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
