from Tkinter import *


class ReturnButton(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.temperatureLbl = Label(self, text="Return", font=('Helvetica', 28), fg="white", bg="black")
        self.temperatureLbl.pack(side=LEFT, anchor=N, padx=25, pady=25)  # todo padding isnt working, fix it
