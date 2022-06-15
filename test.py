import pyttsx3
from tkinter import *

root = Tk()
# root.geometry("800*500")
e = Entry(root, width=50, borderwidth=7)
e.pack()
text_speech = pyttsx3.init()

def myClick():
    text_speech.say(e.get())
    mylabel = Label(root, text="Enter Text")
    mylabel.pack()

    text_speech.runAndWait()
mybutton = Button(root, text="Speak", command=myClick)
mybutton.pack()

root.mainloop()

