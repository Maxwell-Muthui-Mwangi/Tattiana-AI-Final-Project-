import tkinter as tk
from tkinter import ttk

class TattianaApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tattiana AI Project")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Create a notebook for tabs
        notebook = ttk.Notebook(self)
        notebook.pack(pady=10, expand=True)

        # Create tabs
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)

        notebook.add(tab1, text="Tattiana Fraud Detection")
        notebook.add(tab2, text="Other Feature")

        # Fraud Detection Tab
        self.create_fraud_detection_tab(tab1)

    def create_fraud_detection_tab(self, tab):
        title = ttk.Label(tab, text="Tattiana Fraud Detection", font=("Helvetica", 16))
        title.pack(pady=10)

        description_label = ttk.Label(tab, text="Description", font=("Helvetica", 14))
        description_label.pack(anchor=tk.W, padx=10)
        
        description_text = tk.Text(tab, wrap=tk.WORD, height=5, width=70)
        description_text.pack(padx=10, pady=5)
        description_text.insert(tk.END, "Develops machine learning models to detect and prevent fraudulent activities, safeguarding financial transactions.")
        description_text.config(state=tk.DISABLED)

        benefits_label = ttk.Label(tab, text="Benefits", font=("Helvetica", 14))
        benefits_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
        
        benefits_text = tk.Text(tab, wrap=tk.WORD, height=5, width=70)
        benefits_text.pack(padx=10, pady=5)
        benefits_text.insert(tk.END, "Enhances security and trust in online transactions, mitigating the risk of fraud.")
        benefits_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = TattianaApp()
    app.mainloop()
