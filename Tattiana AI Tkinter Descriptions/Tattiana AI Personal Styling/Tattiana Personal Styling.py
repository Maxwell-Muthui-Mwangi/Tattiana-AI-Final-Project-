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
        tab3 = ttk.Frame(notebook)
        tab4 = ttk.Frame(notebook)

        notebook.add(tab1, text="Content Moderation")
        notebook.add(tab2, text="Fraud Detection")
        notebook.add(tab3, text="Virtual Fashion Try-On")
        notebook.add(tab4, text="Personal Styling")

        # Content Moderation Tab
        self.create_content_moderation_tab(tab1)
        
        # Fraud Detection Tab
        self.create_fraud_detection_tab(tab2)
        
        # Virtual Fashion Try-On Tab
        self.create_virtual_fashion_tryon_tab(tab3)
        
        # Personal Styling Tab
        self.create_personal_styling_tab(tab4)

    def create_content_moderation_tab(self, tab):
        title = ttk.Label(tab, text="Tattiana Content Moderation", font=("Helvetica", 16))
        title.pack(pady=10)

        description_label = ttk.Label(tab, text="Description", font=("Helvetica", 14))
        description_label.pack(anchor=tk.W, padx=10)
        
        description_text = tk.Text(tab, wrap=tk.WORD, height=5, width=70)
        description_text.pack(padx=10, pady=5)
        description_text.insert(tk.END, "Automatically detects and filters inappropriate or harmful content in user-generated content and online communities.")
        description_text.config(state=tk.DISABLED)

        benefits_label = ttk.Label(tab, text="Benefits", font=("Helvetica", 14))
        benefits_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
        
        benefits_text = tk.Text(tab, wrap=tk.WORD, height=5, width=70)
        benefits_text.pack(padx=10, pady=5)
        benefits_text.insert(tk.END, "Safeguards online platforms and communities, ensuring a safe and positive user experience.")
        benefits_text.config(state=tk.DISABLED)

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

    def create_virtual_fashion_tryon_tab(self, tab):
        title = ttk.Label(tab, text="Tattiana Virtual Fashion Try-On", font=("Helvetica", 16))
        title.pack(pady=10)

        description_label = ttk.Label(tab, text="Description", font=("Helvetica", 14))
        description_label.pack(anchor=tk.W, padx=10)
        
        description_text = tk.Text(tab, wrap=tk.WORD, height=5, width=70)
        description_text.pack(padx=10, pady=5)
        description_text.insert(tk.END, "Utilizes augmented reality technology to enable customers to visualize clothing and accessories.")
        description_text.config(state=tk.DISABLED)

        benefits_label = ttk.Label(tab, text="Benefits", font=("Helvetica", 14))
        benefits_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
        
        benefits_text = tk.Text(tab, wrap=tk.WORD, height=5, width=70)
        benefits_text.pack(padx=10, pady=5)
        benefits_text.insert(tk.END, "Enhances the online shopping experience by allowing customers to virtually try on products before purchase.")
        benefits_text.config(state=tk.DISABLED)

    def create_personal_styling_tab(self, tab):
        title = ttk.Label(tab, text="Tattiana Personal Styling", font=("Helvetica", 16))
        title.pack(pady=10)

        description_label = ttk.Label(tab, text="Description", font=("Helvetica", 14))
        description_label.pack(anchor=tk.W, padx=10)
        
        description_text = tk.Text(tab, wrap=tk.WORD, height=5, width=70)
        description_text.pack(padx=10, pady=5)
        description_text.insert(tk.END, "Analyzes users' preferences and fashion trends to offer personalized outfit and accessory recommendations.")
        description_text.config(state=tk.DISABLED)

        benefits_label = ttk.Label(tab, text="Benefits", font=("Helvetica", 14))
        benefits_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
        
        benefits_text = tk.Text(tab, wrap=tk.WORD, height=5, width=70)
        benefits_text.pack(padx=10, pady=5)
        benefits_text.insert(tk.END, "Improves customer satisfaction and engagement by delivering tailored fashion recommendations.")
        benefits_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = TattianaApp()
    app.mainloop()
