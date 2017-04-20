from Tkinter import *
from project.resources import imagecolor, var


class ToDoList(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP)

        # Initializing text (raw values) for labels (values to be displayed)
        self.to_do_title_text = ''
        self.to_do_text = ''

        # Initializing a color boolean for all labels
        self.color_all = selected_off

        # Initializing Labels
        self.to_do_title_label = Label(self.container, text="To Do list", font=(font_style, font_sizes['title']),
                                       fg=selected_off, bg=background_color)
        self.to_do_title_label.pack(side=RIGHT, anchor=N)
        self.to_do_label = Label(self.container, text="List Item1", font=(font_style, font_sizes['text']),
                                 fg=selected_off, bg=background_color)
        self.to_do_label.pack(side=RIGHT, anchor=N)

    def update_now(self):
        print("We just Updated")

    # TODO: Place all "todo" items in a todo.json file so and update from there


    # def addListItems(self):
    #     listItems = ["List Item 1", "List Item 2, List Item 3, List Item 4, List Item 5"]
    #     for item in listItems:
    #         self.to_do_label = Label(self.container, text="List Item1", font=(font_style, font_sizes['text']),
    #                                  fg=selected_off, bg=background_color)
    #         self.to_do_label.pack(side=RIGHT, anchor=N)

