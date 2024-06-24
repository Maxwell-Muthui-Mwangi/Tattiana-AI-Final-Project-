import tkinter as tk
from tkinter import Entry, StringVar, OptionMenu, Label, Button, Text, filedialog
from googletrans import Translator
from gtts import gTTS
import os

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Language Translator")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # Entry for manual text input
        self.entry_window = Entry(self.root, bg="white", fg="black", font=("Arial", 18))
        self.entry_window.place(x=20, y=20, width=600, height=40)

        # Button to upload a text file
        self.upload_button = Button(self.root, text="Upload File", bg="#4CAF50", fg="white", font=("Arial", 12), command=self.upload_file)
        self.upload_button.place(x=640, y=20, width=120, height=40)

        # Dropdown for selecting language
        lang_options = [
            "Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Azerbaijani", "Basque", "Belarusian",
            "Bengali", "Bosnian", "Bulgarian", "Catalan", "Cebuano", "Chichewa", "Chinese (Simplified)",
            "Chinese (Traditional)", "Corsican", "Croatian", "Czech", "Danish", "Dutch", "English", "Esperanto",
            "Estonian", "Filipino", "Finnish", "French", "Frisian", "Galician", "Georgian", "German", "Greek",
            "Gujarati", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew", "Hindi", "Hmong", "Hungarian", "Icelandic",
            "Igbo", "Indonesian", "Irish", "Italian", "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Kinyarwanda",
            "Korean", "Kurdish (Kurmanji)", "Kyrgyz", "Lao", "Latin", "Latvian", "Lithuanian", "Luxembourgish", "Macedonian",
            "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi", "Mongolian", "Myanmar (Burmese)", "Nepali",
            "Norwegian", "Odia (Oriya)", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian", "Russian",
            "Samoan", "Scots Gaelic", "Serbian", "Sesotho", "Shona", "Sindhi", "Sinhala", "Slovak", "Slovenian", "Somali",
            "Spanish", "Sundanese", "Swahili", "Swedish", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Turkish", "Turkmen",
            "Ukrainian", "Urdu", "Uyghur", "Uzbek", "Vietnamese", "Welsh", "Xhosa", "Yiddish", "Yoruba", "Zulu"
        ]

        self.drp_down = StringVar()
        self.drp_down.set("Select Language")
        self.list_lang = OptionMenu(self.root, self.drp_down, *lang_options)
        self.list_lang.configure(bg="#2196F3", fg="white", font=("Arial", 14))
        self.list_lang.place(x=640, y=80, width=140, height=40)

        # Button to initiate translation
        self.translate_button = Button(self.root, text="Translate!", bg="#FF9800", fg="white", font=("Arial", 18), command=self.translate_language)
        self.translate_button.place(x=640, y=140, width=140, height=40)

        # Text area for displaying translated text
        self.translated_text_area = Text(self.root, bg="white", fg="black", font=("Arial", 14), wrap=tk.WORD)
        self.translated_text_area.place(x=20, y=80, width=600, height=480)

        # Button for text-to-speech
        self.tts_button = Button(self.root, text="Text-to-Speech", bg="#FF5722", fg="white", font=("Arial", 12), command=self.text_to_speech)
        self.tts_button.place(x=640, y=200, width=140, height=40)

        # Button to copy translated text to clipboard
        self.copy_button = Button(self.root, text="Copy", bg="#607D8B", fg="white", font=("Arial", 12), command=self.copy_translated_text)
        self.copy_button.place(x=640, y=550, width=140, height=40)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                self.entry_window.delete(0, tk.END)
                self.entry_window.insert(0, file_content)

    def translate_language(self):
        input_text = self.entry_window.get()
        translator = Translator()
        selected_lang = self.drp_down.get()

        # Google Translate language codes for all languages
        lang_code = {
            "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Armenian": "hy", "Azerbaijani": "az",
            "Basque": "eu", "Belarusian": "be", "Bengali": "bn", "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca",
            "Cebuano": "ceb", "Chichewa": "ny", "Chinese (Simplified)": "zh-CN", "Chinese (Traditional)": "zh-TW",
            "Corsican": "co", "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dutch": "nl", "English": "en", "Esperanto": "eo",
            "Estonian": "et", "Filipino": "tl", "Finnish": "fi", "French": "fr", "Frisian": "fy", "Galician": "gl",
            "Georgian": "ka", "German": "de", "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha",
            "Hawaiian": "haw", "Hebrew": "iw", "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu", "Icelandic": "is",
            "Igbo": "ig", "Indonesian": "id", "Irish": "ga", "Italian": "it", "Japanese": "ja", "Javanese": "jw",
            "Kannada": "kn", "Kazakh": "kk", "Khmer": "km", "Kinyarwanda": "rw", "Korean": "ko", "Kurdish (Kurmanji)": "ku",
            "Kyrgyz": "ky", "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb",
            "Macedonian": "mk", "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Maori": "mi",
            "Marathi": "mr", "Mongolian": "mn", "Myanmar (Burmese)": "my", "Nepali": "ne", "Norwegian": "no", "Odia (Oriya)": "or",
            "Pashto": "ps", "Persian": "fa", "Polish": "pl", "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro",
            "Russian": "ru", "Samoan": "sm", "Scots Gaelic": "gd", "Serbian": "sr", "Sesotho": "st", "Shona": "sn",
            "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Spanish": "es",
            "Sundanese": "su", "Swahili": "sw", "Swedish": "sv", "Tajik": "tg", "Tamil": "ta", "Tatar": "tt", "Telugu": "te",
            "Thai": "th", "Turkish": "tr", "Turkmen": "tk", "Ukrainian": "uk", "Urdu": "ur", "Uyghur": "ug", "Uzbek": "uz",
            "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu"
        }

        dest_lang = lang_code.get(selected_lang, "en")  # Default to English if selected language not found

        translated_text = translator.translate(input_text, dest=dest_lang)
        translated_text = translated_text.text

        self.translated_text_area.delete('1.0', tk.END)  # Clear previous text
        self.translated_text_area.insert(tk.END, translated_text)

    def text_to_speech(self):
        translated_text = self.translated_text_area.get('1.0', tk.END)
        dest_lang = self.drp_down.get()

        lang_code = {
            "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Armenian": "hy", "Azerbaijani": "az",
            "Basque": "eu", "Belarusian": "be", "Bengali": "bn", "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca",
            "Cebuano": "ceb", "Chichewa": "ny", "Chinese (Simplified)": "zh-CN", "Chinese (Traditional)": "zh-TW",
            "Corsican": "co", "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dutch": "nl", "English": "en", "Esperanto": "eo",
            "Estonian": "et", "Filipino": "tl", "Finnish": "fi", "French": "fr", "Frisian": "fy", "Galician": "gl",
            "Georgian": "ka", "German": "de", "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha",
            "Hawaiian": "haw", "Hebrew": "iw", "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu", "Icelandic": "is",
            "Igbo": "ig", "Indonesian": "id", "Irish": "ga", "Italian": "it", "Japanese": "ja", "Javanese": "jw",
            "Kannada": "kn", "Kazakh": "kk", "Khmer": "km", "Kinyarwanda": "rw", "Korean": "ko", "Kurdish (Kurmanji)": "ku",
            "Kyrgyz": "ky", "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb",
            "Macedonian": "mk", "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Maori": "mi",
            "Marathi": "mr", "Mongolian": "mn", "Myanmar (Burmese)": "my", "Nepali": "ne", "Norwegian": "no", "Odia (Oriya)": "or",
            "Pashto": "ps", "Persian": "fa", "Polish": "pl", "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro",
            "Russian": "ru", "Samoan": "sm", "Scots Gaelic": "gd", "Serbian": "sr", "Sesotho": "st", "Shona": "sn",
            "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Spanish": "es",
            "Sundanese": "su", "Swahili": "sw", "Swedish": "sv", "Tajik": "tg", "Tamil": "ta", "Tatar": "tt", "Telugu": "te",
            "Thai": "th", "Turkish": "tr", "Turkmen": "tk", "Ukrainian": "uk", "Urdu": "ur", "Uyghur": "ug", "Uzbek": "uz",
            "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu"
        }

        dest_lang_code = lang_code.get(dest_lang, "en")  # Default to English if selected language not found

        tts = gTTS(text=translated_text, slow=False, lang=dest_lang_code)
        tts.save("translated_audio.mp3")  # Save the translated text to an audio file

        # Optionally, play the saved audio using your system's default player
        os.system("start translated_audio.mp3")

    def copy_translated_text(self):
        translated_text = self.translated_text_area.get('1.0', tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(translated_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
