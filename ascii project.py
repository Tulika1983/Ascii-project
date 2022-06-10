# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 08:38:52 2022

@author: ARIJIT MONDAL
"""

from tkinter import *

root = Tk()
root.title("Ascii and Encryption")

root.geometry("400x400")
root.configure(background = "snow")

enter_word = Entry(root)
enter_word.place(relx=0.5 ,rely=0.4 ,anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg = "light yellow", fg = "black")
label2 = Label(root, text = "Encrypted value : ", bg = "green", fg = "black")

def asciiandencryptionConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        encrypted = ascii - 1
        label2["text"] += str(chr(encrypted)) + " "
        
btn = Button(root, text  = "Display the ascii code and encrypted value", command = asciiandencryptionConverter, bg = "cyan", fg = "black")
btn.place(relx =0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()
