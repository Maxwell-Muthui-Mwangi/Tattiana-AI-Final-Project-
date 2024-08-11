from PIL import Image
import pytesseract

# Ensure that the Tesseract executable is in your PATH, or specify the path explicitly
# pytesseract.pytesseract.tesseract_cmd = r'path_to_your_tesseract_executable'


def extract_text_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    
    # Split the text into words
    words = text.split()
    
    return words

# Example usage
image_path = 'C:\Users\user\Documents\Tattiana AI  (Final Project)\Extract words From Image\WhatsApp Image 2024-07-18 at 8.25.45 PM (1).jpeg'
words = extract_text_from_image(image_path)

# Print the extracted words
print(words)
