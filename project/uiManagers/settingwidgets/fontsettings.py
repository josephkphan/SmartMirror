from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, zone, varLoader
from project.uiManagers.settingwidgets import checkbox


class FontSettings(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)
        font_sizes = var.font_sizes
        # Main Page Settings
        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP)
        self.current_color = var.preferences['color']

        # ------------------------- Color ------------------------------ #

        self.color_small = selected_off
        self.color_medium = selected_off
        self.color_large = selected_off

        # ------------------------- Keys ----------------------------- #

        self.key_small = 'small'
        self.key_medium = 'medium'
        self.key_large = 'large'

        # --------------------------- Color labels ------------------------------ #

        self.title_label = Label(self.container, text='Font Size:', font=(font_style, font_sizes['text']),
                                 fg=selected_off, bg=background_color)
        self.title_label.pack(side=TOP, anchor=W)

        self.small_label = checkbox.CheckBox(self.container, 'Small', self.key_small)
        self.small_label.pack(side=TOP, anchor=W, padx=50)

        self.medium_label = checkbox.CheckBox(self.container, 'Medium', self.key_medium)
        self.medium_label.pack(side=TOP, anchor=W, padx=50)

        self.large_label = checkbox.CheckBox(self.container, 'Large', self.key_large)
        self.large_label.pack(side=TOP, anchor=W, padx=50)

    # --------------------------- Color Methods ------------------------------ #

    def change_color_small(self, mode):
        if self.color_small != mode:
            self.color_small = mode
            self.small_label.change_color_all(mode)

    def change_color_medium(self, mode):
        if self.color_medium != mode:
            self.color_medium = mode
            self.medium_label.change_color_all(mode)

    def change_color_large(self, mode):
        if self.color_large != mode:
            self.color_large = mode
            self.large_label.change_color_all(mode)

    def change_all_label_colors(self, mode):
        self.change_color_small(mode)
        self.change_color_medium(mode)
        self.change_color_large(mode)

    # --------------------------- Changing Settings ------------------------------ #

    def change_a_setting(self, zone_to_change, return_button, color_settings):
        print "~~~~~~~ INSIDE CHANGE A SETTING"
        print zone_to_change

        if zone_to_change == zone.SettingsPage.small:
            varLoader.change_font_size('small')

        elif zone_to_change == zone.SettingsPage.medium:
            varLoader.change_font_size('medium')

        elif zone_to_change == zone.SettingsPage.large:
            varLoader.change_font_size('large')

        self.update_all_label_font_sizes()
        return_button.update_font_size()
        color_settings.update_all_font_sizes()
        self.update_all_label_check_boxes()
        self.update_all_box_images()

    def update_all_label_check_boxes(self):
        self.small_label.update_colored_boxes()
        self.medium_label.update_colored_boxes()
        self.large_label.update_colored_boxes()

    def update_all_box_images(self):
        self.small_label.update_check_box_image()
        self.medium_label.update_check_box_image()
        self.large_label.update_check_box_image()

    def update_all_label_font_sizes(self):
        self.title_label.config(font=(var.font_style, var.font_sizes['text']))
        self.small_label.update_font_sizes()
        self.medium_label.update_font_sizes()
        self.large_label.update_font_sizes()
