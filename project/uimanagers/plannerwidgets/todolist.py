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

        # Initialize to do JSON data
        self.to_do_list_string = {"Clean the house", "Work on the smart mirror", "Wash my clothes"}
        self.to_do_list = []

        # Initializing Labels
        for item in self.to_do_list_string:
            self.to_do_label = Label(self.container, text=item, font=(font_style, font_sizes['text']),
                                     fg=selected_off, bg=background_color)
            self.to_do_label.pack(side=BOTTOM, anchor=N)
            self.to_do_list.append(self.to_do_label)
        self.to_do_title_label = Label(self.container, text="To Do list", font=(font_style, font_sizes['title']),
                                       fg=selected_off, bg=background_color)
        self.to_do_title_label.pack(side=BOTTOM, anchor=N)

        # TODO: Color all each individual item in the to do list
        # TODO: Create check boxes for the todo list
        # TODO: Dynamically load elements into todolist

    def update_now(self):
        print("We just Updated")

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode
            self.to_do_title_label.config(foreground=self.color_all)
            # for item in self.to_do_list:
            #     item.config(foreground=self.color_all)

    def change_color_todolist(self, mode, current_zone):
        if self.color_all != mode:
            self.color_all = mode
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

