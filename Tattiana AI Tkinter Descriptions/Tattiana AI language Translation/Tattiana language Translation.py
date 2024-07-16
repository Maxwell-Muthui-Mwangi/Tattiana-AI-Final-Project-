import tkinter as tk
from tkinter import ttk

class TattianaLanguageTranslationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tattiana Language Translation")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Tattiana Language Translation", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        description_label = tk.Label(self, text="Description:", font=("Arial", 16, "underline"))
        description_label.pack(anchor="w", padx=20, pady=(10, 0))

        description_text = ("Provides real-time translation across multiple languages for text, speech, and documents.")
        description_content = tk.Label(self, text=description_text, font=("Arial", 14), wraplength=560, justify="left")
        description_content.pack(anchor="w", padx=20, pady=(0, 10))

        benefits_label = tk.Label(self, text="Benefits:", font=("Arial", 16, "underline"))
        benefits_label.pack(anchor="w", padx=20, pady=(10, 0))

        benefits_text = ("Facilitates communication in diverse multilingual environments, breaking down language barriers.")
        benefits_content = tk.Label(self, text=benefits_text, font=("Arial", 14), wraplength=560, justify="left")
        benefits_content.pack(anchor="w", padx=20, pady=(0, 10))

if __name__ == "__main__":
    app = TattianaLanguageTranslationApp()
    app.mainloop()
