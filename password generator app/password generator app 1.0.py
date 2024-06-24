import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter the desired length of the password:")
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(self, width=20)
        self.length_entry.pack(pady=10)

        self.generate_button = tk.Button(self, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self, text="")
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1")
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
