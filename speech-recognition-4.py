import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio)
        text = text.lower()

        print(f"Recognized: {text}")
        speak(f"You said: {text}")

    except sr.UnknownValueError:
        print("Could not understand audio")
        speak("Sorry, I couldn't understand what you said")

    except sr.RequestError as e:
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
        recognizer = sr.Recognizer()
