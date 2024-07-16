import tkinter as tk
from tkinter import ttk

class TattianaVirtualAssistantApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tattiana Virtual Assistant")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Tattiana Virtual Assistant", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        description_label = tk.Label(self, text="Description:", font=("Arial", 16, "underline"))
        description_label.pack(anchor="w", padx=20, pady=(10, 0))

        description_text = ("Tattiana serves as an innovative virtual assistant designed to revolutionize "
                            "task management, scheduling, and workflow optimization.")
        description_content = tk.Label(self, text=description_text, font=("Arial", 14), wraplength=560, justify="left")
        description_content.pack(anchor="w", padx=20, pady=(0, 10))

        benefits_label = tk.Label(self, text="Benefits:", font=("Arial", 16, "underline"))
        benefits_label.pack(anchor="w", padx=20, pady=(10, 0))

        benefits_text = ("Seamlessly navigates the complexities of modern work life, enhancing productivity "
                         "and efficiency for users.")
        benefits_content = tk.Label(self, text=benefits_text, font=("Arial", 14), wraplength=560, justify="left")
        benefits_content.pack(anchor="w", padx=20, pady=(0, 10))

if __name__ == "__main__":
    app = TattianaVirtualAssistantApp()
    app.mainloop()
