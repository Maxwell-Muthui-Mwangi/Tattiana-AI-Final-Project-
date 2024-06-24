import speech_recognition
import pyttsx3

# Initialize speech recognizer and text-to-speech engine
recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop for continuous recognition
while True:
    try:
        # Adjust for ambient noise and capture audio
        with speech_recognition.Microphone() as mic:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic)

        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        text = text.lower()

        # Output recognized text
        print(f"Recognized: {text}")
        speak(f"You said: {text}")

    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
        speak("Sorry, I couldn't understand what you said")

    except speech_recognition.RequestError as e:
        print(f"Could not request results; {e}")
        speak("Sorry, I'm having trouble processing your request")

    except KeyboardInterrupt:
        print("Program stopped by user")
        break

    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, something went wrong")

    finally:
        # Reset recognizer for the next iteration
        recognizer = speech_recognition.Recognizer()
