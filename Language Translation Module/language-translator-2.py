import tkinter as tk
from tkinter import Entry, StringVar, OptionMenu, Label, Button
from googletrans import Translator
from gtts import gTTS

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Language Translator")
        self.root.configure(bg="light pink")

        self.create_widgets()

    def create_widgets(self):
        self.entry_window = Entry(self.root, bg="black", fg="white", font=("Arial", 20, "bold"))
        self.entry_window.place(x=20, y=40)

        # List of languages supported by Google Translate
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
        self.list_lang.configure(bg="yellow", fg="black", font=("Arial", 16, "bold"))
        self.list_lang.place(x=400, y=40)

        self.translate_button = Button(self.root, text="Translate!", bg="green", fg="white", font=("Arial", 25, "bold"), command=self.translate_language)
        self.translate_button.place(x=220, y=220)

        self.two_label_title = Label(self.root, text="Translated Text", bg="white", fg="red", font=("Arial", 30, "bold"))
        self.two_label_title.place(x=180, y=140)

        self.two_label = Label(self.root, text="", bg="white", fg="red", font=("Arial", 18))
        self.two_label.place(x=50, y=180, width=500)

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

        self.two_label.config(text=translated_text)

        # Text-to-Speech conversion
        tts = gTTS(text=translated_text, slow=False, lang=dest_lang)
        tts.save("translated_audio.mp3")  # Save the translated text to an audio file

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
