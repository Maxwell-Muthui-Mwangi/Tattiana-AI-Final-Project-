import pyttsx3
import docx2txt
import os

def read_document(file_path):
    try:
        # Check if the file exists 
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        # Convert the document file to text
        text = docx2txt.process(file_path)

        # Initialize the Text-to-Speech engine
        engine = pyttsx3.init()

        # Set properties for the speech
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

        # Read the text aloud
        engine.say(text)
        engine.runAndWait()

        # Cleanup resources
        engine.stop()
        engine.runAndWait()

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    document_path = r'C:\Users\user\Downloads\Final Project Elevate Your Work flow with Tattiana AI.docx'
    read_document(document_path)
