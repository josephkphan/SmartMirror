from Tkinter import *
from project.resources import imagecolor, var, zone


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

        # TODO: Create a json for all todo items
        # Initialize to do JSON data
        self.to_do_list_string = ["Clean the house", "Work on smart mirror", "Wash my clothes", "Buy a Car", "Get your shit together"]
        self.to_do_list = []

        # Initializing Labels
        self.to_do_title_label = Label(self.container, text="To Do List", font=(font_style, font_sizes['big']),
                                       fg=selected_off, bg=background_color)
        self.to_do_title_label.pack(side=TOP, anchor=N)
        for item in self.to_do_list_string:
            print (item)
            self.to_do_label = Label(self.container, text=item, font=(font_style, font_sizes['text']),
                                     fg=selected_off, bg=background_color)
            self.to_do_label.pack(side=TOP, anchor=N)
            self.to_do_list.append(self.to_do_label)

    def update_now(self):
        self.update_font_size()
        #TODO: Remake the todo list based on online updates

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode
            self.to_do_title_label.config(foreground=self.color_all)
            for to_do_item in self.to_do_list:
                to_do_item.config(foreground=self.color_all)

    def change_color_todolist(self, mode, current_zone):
        if self.color_all != mode:
            self.color_all = mode
            if current_zone == zone.PlannerPage.todolist:
                self.to_do_title_label.config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.todo0:
                self.to_do_list[0].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.todo1:
                self.to_do_list[1].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.todo2:
                self.to_do_list[2].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.todo3:
                self.to_do_list[3].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.todo4:
                self.to_do_list[4].config(foreground=self.color_all)

    def update_font_size(self):
        self.to_do_title_label.config(font=(var.font_style, var.font_sizes['big']))
        for to_do_item in self.to_do_list:
            to_do_item.config(font=(var.font_style, var.font_sizes['text']))