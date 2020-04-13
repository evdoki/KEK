# -*- coding: utf-8 -*-
from tkinter import *
from random import *
from collections import *

dictt = {"dog": "собака","cat": "кот"}

def click():
    if dictt[word] == entry.get():
        label.config(text="Верно")
    else:
        label.config(text="Не верно")
             
window = Tk()

word = choice(Counter(dictt).most_common(2))[0]
word_random = StringVar()
word_random.set(word)

label2 = Label(window, textvariable=word_random)
label2.pack()

frame = Frame(window)
frame.pack()
entry = Entry(frame)
entry.pack()

label = Label(frame)
label.pack()

button = Button(frame, text='Готово!', command=click)
button.pack()

window.mainloop()