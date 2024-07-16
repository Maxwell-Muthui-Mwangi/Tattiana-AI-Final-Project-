import tkinter as tk
from tkinter import ttk

class TattianaEmotionalIntelligenceChatbotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tattiana Emotional Intelligence Chat-bot")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Tattiana Emotional Intelligence Chat-bot", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        description_label = tk.Label(self, text="Description:", font=("Arial", 16, "underline"))
        description_label.pack(anchor="w", padx=20, pady=(10, 0))

        description_text = ("Enhances customer interactions by understanding and responding to users' emotions, "
                            "boosting satisfaction levels.")
        description_content = tk.Label(self, text=description_text, font=("Arial", 14), wraplength=560, justify="left")
        description_content.pack(anchor="w", padx=20, pady=(0, 10))

        benefits_label = tk.Label(self, text="Benefits:", font=("Arial", 16, "underline"))
        benefits_label.pack(anchor="w", padx=20, pady=(10, 0))

        benefits_text = ("Improves customer engagement and loyalty by providing empathetic and personalized support.")
        benefits_content = tk.Label(self, text=benefits_text, font=("Arial", 14), wraplength=560, justify="left")
        benefits_content.pack(anchor="w", padx=20, pady=(0, 10))

if __name__ == "__main__":
    app = TattianaEmotionalIntelligenceChatbotApp()
    app.mainloop()
