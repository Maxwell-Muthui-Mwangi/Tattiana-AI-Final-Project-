import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext
import pyttsx3
import docx2txt
import os
import threading

class DocumentReaderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Document Reader")
        self.geometry("800x600")

        self.file_path = None
        self.doc_window = None  # To store reference to document display window

        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 420)  # Default speed of speech
        self.engine.setProperty('volume', 1)  # Default volume (0.0 to 1.0)

        self.create_widgets()
   
        self.label = tk.Label(self, text="Document Reader", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.upload_label = tk.Label(self, text="Uploaded Document: None")
        self.upload_label.pack()

        self.upload_button = tk.Button(self, text="Upload Document", command=self.upload_document)
        self.upload_button.pack(pady=10)

        self.read_button = tk.Button(self, text="Read Document", command=self.read_document)
        self.read_button.pack(pady=10)

        self.sample_button = tk.Button(self, text="Sample My Voice", command=self.sample_voice)
        self.sample_button.pack(pady=10)

        self.download_button = tk.Button(self, text="Download Audio", command=self.download_audio)
        self.download_button.pack(pady=10)

        self.voice_label = tk.Label(self, text="Select Voice:")
        self.voice_label.pack(pady=5)
        self.voice_dropdown = ttk.Combobox(self, values=self.get_available_voices(), state="readonly", width=30)
        self.voice_dropdown.pack()
        self.voice_dropdown.current(0)  # Set default voice

        self.change_voice_button = tk.Button(self, text="Change Voice", command=self.change_voice)
        self.change_voice_button.pack(pady=10)

        # Controls for speed and navigation
        self.speed_label = tk.Label(self, text="Speed (words per minute):")
        self.speed_label.pack(pady=5)
        self.speed_entry = tk.Entry(self)
        self.speed_entry.insert(tk.END, "420")
        self.speed_entry.pack()

        self.speed_button = tk.Button(self, text="Apply Speed", command=self.apply_speed)
        self.speed_button.pack(pady=5)

        self.rewind_button = tk.Button(self, text="Rewind", command=self.rewind_audio)
        self.rewind_button.pack(pady=5)

        self.forward_button = tk.Button(self, text="Forward", command=self.forward_audio)
        self.forward_button.pack(pady=5)

    def get_available_voices(self):
        # Get the list of available voices
        voices = self.engine.getProperty('voices')
        voice_names = [voice.name for voice in voices]
        return voice_names

    def upload_document(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx"), ("All files", "*.*")])
        if self.file_path:
            self.upload_label.config(text=f"Uploaded Document: {os.path.basename(self.file_path)}")
            messagebox.showinfo("File Uploaded", f"Document '{os.path.basename(self.file_path)}' uploaded successfully.")

    def read_document(self):
        if self.file_path:
            try:
                # Convert the document file to text
                text = docx2txt.process(self.file_path)

                # Open a new window to display the document text
                text_area = self.open_document_window(text)

                # Start a new thread to read the text aloud
                threading.Thread(target=self.read_aloud, args=(text,)).start()

            except FileNotFoundError:
                messagebox.showerror("Error", f"File '{os.path.basename(self.file_path)}' not found.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "Please upload a document first.")

    def read_aloud(self, text):
        try:
            # Set properties for the speech
            selected_voice = self.voice_dropdown.get()
            self.engine.setProperty('voice', selected_voice)

            # Set speed based on user input
            speed = int(self.speed_entry.get())
            if speed > 0:
                self.engine.setProperty('rate', speed)

            # Read the text aloud
            self.engine.say(text)
            self.engine.runAndWait()

            # Save synthesized speech to an audio file
            self.save_audio(text)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during speech synthesis: {e}")

    def open_document_window(self, text):
        # Function to display the uploaded document content in a new window
        if not self.doc_window:
            self.doc_window = tk.Toplevel(self)
            self.doc_window.title("Document Viewer")
            self.doc_window.geometry("600x400")

            text_area = scrolledtext.ScrolledText(self.doc_window, wrap=tk.WORD, width=60, height=20)
            text_area.pack(expand=True, fill="both")
            text_area.insert(tk.END, text)
            text_area.config(state=tk.DISABLED)  # Make text read-only

            close_button = tk.Button(self.doc_window, text="Close", command=self.close_document_window)
            close_button.pack(pady=10)

            return text_area  # Return reference to text area widget

    def close_document_window(self):
        # Function to close the document window
        if self.doc_window:
            self.doc_window.destroy()
            self.doc_window = None

    def sample_voice(self):
        # Sample your voice
        try:
            # Speak a sample text to record your voice
            sample_text = "This is a sample text to record your voice."
            self.engine.say(sample_text)
            self.engine.runAndWait()

            # Save the sample voice to an audio file
            self.save_audio(sample_text)

            messagebox.showinfo("Voice Sampled", "Your voice sample has been recorded successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def save_audio(self, text):
        # Save synthesized speech to an audio file
        output_file = "output_voice.wav"
        self.engine.save_to_file(text, output_file)
        self.engine.runAndWait()

    def download_audio(self):
        # Download the speech of the uploaded document
        try:
            if self.file_path:
                # Convert the document file to text
                text = docx2txt.process(self.file_path)

                # Synthesize speech for the text
                selected_voice = self.voice_dropdown.get()
                self.engine.setProperty('voice', selected_voice)
                self.engine.save_to_file(text, "output_voice.wav")
                self.engine.runAndWait()

                # Directly save the file to a predefined location
                default_save_path = os.path.expanduser("~/Downloads/output_voice.wav")
                os.replace("output_voice.wav", default_save_path)
                messagebox.showinfo("Download Successful", f"Speech of '{os.path.basename(self.file_path)}' "
                                                            f"downloaded to {default_save_path}.")
            else:
                messagebox.showerror("Error", "No document uploaded. Please upload a document first.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while downloading the speech: {e}")

    def change_voice(self):
        # Change the voice based on selection
        try:
            selected_voice = self.voice_dropdown.get()
            self.engine.setProperty('voice', selected_voice)
            self.engine.say("Voice changed successfully.")
            self.engine.runAndWait()

            messagebox.showinfo("Voice Changed", f"Voice changed to {selected_voice} successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while changing the voice: {e}")

    def apply_speed(self):
        # Apply speed setting to speech engine
        try:
            speed = int(self.speed_entry.get())
            if speed > 0:
                self.engine.setProperty('rate', speed)
                messagebox.showinfo("Speed Applied", f"Speed set to {speed} words per minute.")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for speed.")

    def rewind_audio(self):
        # Rewind audio by restarting the current text
        try:
            self.engine.stop()
            self.engine.say(self.engine._current_text)
            self.engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while rewinding: {e}")

    def forward_audio(self):
        # Forward audio by skipping ahead
        try:
            self.engine.stop()
            self.engine.skip()
            self.engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while forwarding: {e}")

    def __del__(self):
        # Cleanup resources when application is closed
        if hasattr(self, 'engine'):
            self.engine.stop()

# Main application loop
if __name__ == "__main__":
    app = DocumentReaderApp()
    app.mainloop()
