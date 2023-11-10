import tkinter as tk
from tkinter import ttk, filedialog
import pyttsx3
import random

engine = pyttsx3.init()
text_to_speak = ""
rate = engine.getProperty("rate")
engine.setProperty("rate", 150)

app = tk.Tk()
app.geometry("400x200")
app.title("TTS")


def gen_function():
    inp = displayBox.get(1.0, "end-1c")
    engine.say(inp)
    engine.runAndWait()


def down_function():
    inp2 = displayBox.get(1.0, "end-1c")

    file_path = filedialog.asksaveasfilename(
        defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")]
    )

    if file_path:
        engine.save_to_file(inp2, file_path)
        engine.runAndWait()


button1 = ttk.Button(master=app, text="Generate", command=gen_function)
button1.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

button2 = ttk.Button(master=app, text="Download", command=down_function)
button2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

displayBox = tk.Text(app, width=40, height=6)
displayBox.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

app.mainloop()
