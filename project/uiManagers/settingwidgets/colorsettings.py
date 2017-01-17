from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, zone, varLoader
from project.uiManagers.settingwidgets import checkbox


class ColorSettings(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        # Main Page Settings
        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP)
        self.current_color = var.preferences['color']

        # ------------------------- Color ------------------------------ #

        self.color_blue = selected_off
        self.color_green = selected_off
        self.color_orange = selected_off
        self.color_pink = selected_off
        self.color_purple = selected_off
        self.color_red = selected_off
        self.color_yellow = selected_off

        # ------------------------- Keys ----------------------------- #

        self.key_blue = 'blue'
        self.key_green = 'green'
        self.key_pink = 'pink'
        self.key_orange = 'orange'
        self.key_purple = 'purple'
        self.key_red = 'red'
        self.key_yellow = 'yellow'

        # --------------------------- Color labels ------------------------------ #

        self.title_label = Label(self.container, text='Color Scheme:', font=(font_style,  font_sizes['text']),
                                 fg=selected_off, bg=background_color)
        self.title_label.pack(side=TOP, anchor=W)

        self.blue_label = checkbox.CheckBox(self.container, 'Blue', self.key_blue)
        self.blue_label.pack(side=TOP, anchor=W, padx=50)

        self.green_label = checkbox.CheckBox(self.container, 'Green', self.key_green)
        self.green_label.pack(side=TOP, anchor=W, padx=50)

        self.orange_label = checkbox.CheckBox(self.container, 'Orange', self.key_orange)
        self.orange_label.pack(side=TOP, anchor=W, padx=50)

        self.pink_label = checkbox.CheckBox(self.container, 'Pink', self.key_pink)
        self.pink_label.pack(side=TOP, anchor=W, padx=50)

        self.purple_label = checkbox.CheckBox(self.container, 'Purple', self.key_purple)
        self.purple_label.pack(side=TOP, anchor=W, padx=50)

        self.red_label = checkbox.CheckBox(self.container, 'Red', self.key_red)
        self.red_label.pack(side=TOP, anchor=W, padx=50)

        self.yellow_label = checkbox.CheckBox(self.container, 'Yellow', self.key_yellow)
        self.yellow_label.pack(side=TOP, anchor=W, padx=50)

    # --------------------------- Color Methods ------------------------------ #

    def change_color_green(self, mode):
        if self.color_green != mode:
            self.color_green = mode
            self.green_label.change_color_all(mode)

    def change_color_pink(self, mode):
        if self.color_pink != mode:
            self.color_pink = mode
            self.pink_label.change_color_all(mode)

    def change_color_red(self, mode):
        if self.color_red != mode:
            self.color_red = mode
            self.red_label.change_color_all(mode)

    def change_color_blue(self, mode):
        if self.color_blue != mode:
            self.color_blue = mode
            self.blue_label.change_color_all(mode)

    def change_color_yellow(self, mode):
        if self.color_yellow != mode:
            self.color_yellow = mode
            self.yellow_label.change_color_all(mode)

    def change_color_purple(self, mode):
        if self.color_purple != mode:
            self.color_purple = mode
            self.purple_label.change_color_all(mode)

    def change_color_orange(self, mode):
        if self.color_orange != mode:
            self.color_orange = mode
            self.orange_label.change_color_all(mode)

    def change_all_label_colors(self, mode):
        self.change_color_blue(mode)
        self.change_color_green(mode)
        self.change_color_orange(mode)
        self.change_color_pink(mode)
        self.change_color_purple(mode)
        self.change_color_red(mode)
        self.change_color_yellow(mode)

    # --------------------------- Changing Settings ------------------------------ #

    def change_a_setting(self, zone_to_change, other_setting):
        print "~~~~~~~ INSIDE CHANGE A SETTING"
        print zone_to_change

        if zone_to_change == zone.SettingsPage.blue:
            varLoader.change_color_scheme('blue')

        elif zone_to_change == zone.SettingsPage.green:
            varLoader.change_color_scheme('green')

        elif zone_to_change == zone.SettingsPage.orange:
            varLoader.change_color_scheme('orange')

        elif zone_to_change == zone.SettingsPage.pink:
            varLoader.change_color_scheme('pink')

        elif zone_to_change == zone.SettingsPage.purple:
            varLoader.change_color_scheme('purple')

        elif zone_to_change == zone.SettingsPage.red:
            varLoader.change_color_scheme('red')

        elif zone_to_change == zone.SettingsPage.yellow:
            varLoader.change_color_scheme('yellow')

        self.update_all_label_check_boxes()
        self.update_all_box_images()
        other_setting.update_all_label_check_boxes()


    def update_all_label_check_boxes(self):
        self.blue_label.update_colored_boxes()
        self.green_label.update_colored_boxes()
        self.orange_label.update_colored_boxes()
        self.pink_label.update_colored_boxes()
        self.purple_label.update_colored_boxes()
        self.red_label.update_colored_boxes()
        self.yellow_label.update_colored_boxes()

    def update_all_box_images(self):
        self.blue_label.update_check_box_image()
        self.green_label.update_check_box_image()
        self.orange_label.update_check_box_image()
        self.pink_label.update_check_box_image()
        self.purple_label.update_check_box_image()
        self.red_label.update_check_box_image()
        self.yellow_label.update_check_box_image()

    def update_all_font_sizes(self):
        self.title_label.config(font=(var.font_style,  var.font_sizes['text']))
        self.blue_label.update_font_sizes()
        self.green_label.update_font_sizes()
        self.orange_label.update_font_sizes()
        self.pink_label.update_font_sizes()
        self.purple_label.update_font_sizes()
        self.red_label.update_font_sizes()
        self.yellow_label.update_font_sizes()
