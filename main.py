import tkinter
import customtkinter as ctk
import pyttsx3
import random

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")  

engine = pyttsx3.init()
text_to_speak = ''
rate = engine.getProperty('rate') 
engine.setProperty('rate', 150) 

app = ctk.CTk()  
app.geometry("400x240")

def gen_function():
    inp = displayBox.get(1.0, "end-1c")
    engine.say(inp)
    engine.runAndWait()

def down_function():
    inp2 = displayBox.get(1.0, "end-1c")
    engine.save_to_file(inp2, 'tts'+f'{random.randint(1, 10000)}'+'.mp3')
    engine.runAndWait()

button1 = ctk.CTkButton(master=app, text="Generate", command=gen_function)
button1.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

button2 = ctk.CTkButton(master=app, text="Download", command=down_function)
button2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

displayBox = ctk.CTkTextbox(app, width=300, height=150)
displayBox.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

app.mainloop()