from Tkinter import *

root = Tk()

def printName(event):
    print("TMy Name is Joey")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()

