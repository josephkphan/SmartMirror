from Tkinter import *
from project.resources import var


class StartUpText(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP)
        string = 'Good Morning\nGood Looking'
        self.start_up_label = Label(self.container, text=string,
                                    font=(font_style, font_sizes['big_text']), fg=selected_off,bg=background_color)
        self.start_up_label.pack(side=BOTTOM, anchor=S)
