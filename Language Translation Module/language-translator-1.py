from tkinter import *
from googletrans import Translator
from gtts import gTTS

def translate_language():
    n1 = entry_window.get()
    n2 = Translator()
    n3 = drp_down.get()


    if n3 == "Hindi":
        change = "hi"
    elif n3 == "English":
        change = "en"
    elif n3 == "Spanish":
        change = "Sp"
    elif n3 == "French":
        change = "fr"
    
    text_translate = n2.translate(n1, dest=change)
    text_translate = text_translate.text
    n4 = gTTS(text=text_translate, slow=False, lang=change)
    two_label.config(text=text_translate)

lang_option = [
    "Hindi",
    "Spanish",
    "French"
 ]

tk_window = Tk()
tk_window.geometry("600x300")
tk_window.config(bg="light pink")



entry_window = Entry(tk_window, bg= "black", fg="white", font=("Arial", 20, "bold"))

entry_window.place(x=20, y=40)

drp_down = StringVar()
drp_down.set("Select Language")


list_lang = OptionMenu(tk_window, drp_down, *lang_option)
list_lang.configure(bg ="yellow", fg="black", font=("Arial", 16, "bold"))
list_lang.place(x=400, y=40)


two_label = Label(tk_window, text="\t\t\t\t\t\t", bg="white", fg="red", font=("Arial", 42, "bold"))


two_label.place(x=0, y=120)


two_label = Label(tk_window, text="Translated Language", bg="white", fg="red", font=("Arial", 30, "bold"))
two_label.place(x=180, y=140)



translate_button = Button(tk_window, text=" Translate!", bg="green", fg="white", font=("Arial", 25, "bold"), command=translate_language)
translate_button.place(x=220, y=220)







tk_window.mainloop()