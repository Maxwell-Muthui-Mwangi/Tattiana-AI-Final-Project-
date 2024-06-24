import tkinter as tk
from tkinter import ttk
import speech_recognition
import pyttsx3
import threading

# Initialize speech recognizer and text-to-speech engine
recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to start speech recognition
def start_recognition():
    global recognizer
    try:
        with speech_recognition.Microphone() as mic:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio)
        text = text.lower()

        print(f"Recognized: {text}")
        speak(f"You said: {text}")
        text_var.set(f"You said: {text}")  # Update GUI text
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
        speak("Sorry, I couldn't understand what you said")
        text_var.set("Could not understand audio")  # Update GUI text
    except speech_recognition.RequestError as e:
        print(f"Could not request results; {e}")
        speak("Sorry, I'm having trouble processing your request")
        text_var.set("Could not request results")  # Update GUI text
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, something went wrong")
        text_var.set("Error occurred")  # Update GUI text
    finally:
        recognizer = speech_recognition.Recognizer()  # Reset recognizer

# GUI setup
def create_gui():
    global text_var
    root = tk.Tk()
    root.title("Speech Recognition")

    # Frame to hold controls
    frame = ttk.Frame(root, padding="20")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Label to display recognized text
    text_var = tk.StringVar()
    text_label = ttk.Label(frame, textvariable=text_var, wraplength=300)
    text_label.grid(row=0, column=0, padx=10, pady=10)

    # Button to start recognition
    start_button = ttk.Button(frame, text="Start Recognition", command=start_recognition)
    start_button.grid(row=1, column=0, padx=10, pady=10)

    # Button to quit
    quit_button = ttk.Button(frame, text="Quit", command=root.destroy)
    quit_button.grid(row=2, column=0, padx=10, pady=10)

    root.mainloop()

# Start GUI in a separate thread
gui_thread = threading.Thread(target=create_gui)
gui_thread.start()

# Main loop for continuous recognition (running in main thread)
while True:
    try:
        # Use a blocking call to prevent the script from exiting
        # This loop will be empty as tkinter's mainloop runs in the GUI thread
        pass
    except KeyboardInterrupt:
        print("Program stopped by user")
        break
