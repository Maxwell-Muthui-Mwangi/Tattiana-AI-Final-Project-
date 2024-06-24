import tkinter as tk
from tkinter import messagebox
import random

class RPSGameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Rock-Paper-Scissors Game")
        self.geometry("300x300")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Choose Rock, Paper, or Scissors:")
        self.label.pack(pady=10)

        self.rock_button = tk.Button(self, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(self, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(self, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(pady=5)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self, text="Score - You: 0, Computer: 0")
        self.score_label.pack(pady=10)

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

if __name__ == "__main__":
    app = RPSGameApp()
    app.mainloop()
