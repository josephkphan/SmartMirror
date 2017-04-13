from project.resources import pagegraph, var, varloader
from project.resources.page import *


class KeyboardSetUp:
    def __init__(self, ui_handler):
        self.ui_handler = ui_handler
        self.ui_handler.tk.bind("<Tab>", self.toggle_fullscreen)
        self.ui_handler.tk.bind("<Escape>", self.end_fullscreen)
        self.ui_handler.tk.bind("<Control_R>", self.toggle_power)

        self.ui_handler.tk.bind("<Left>", self.left_click)
        self.ui_handler.tk.bind("<Right>", self.right_click)
        self.ui_handler.tk.bind("<Up>", self.up_click)
        self.ui_handler.tk.bind("<Down>", self.down_click)
        self.ui_handler.tk.bind("<BackSpace>", self.enter_click)
        self.ui_handler.tk.bind("<Control_L>", self.toggle_manual_mode)
        self.ui_handler.tk.bind("<Shift_L>", self.toggle_select_mode_for_camera)

        # ---------------------------------- Key Binding Functions ----------------------------------- #

    def toggle_fullscreen(self, event=None):
        self.ui_handler.camera_selection_mode = not self.ui_handler.camera_selection_mode  # Just toggling the boolean
        self.ui_handler.tk.attributes("-fullscreen", self.ui_handler.camera_selection_mode)
        return "break"

    def end_fullscreen(self, event=None):
        self.ui_handler.camera_selection_mode = False
        self.ui_handler.tk.attributes("-fullscreen", False)
        return "break"

    def toggle_power(self, event=None):
        if self.ui_handler.current_page != Page.blank:
            self.ui_handler.change_page(Page.blank)
        else:
            self.ui_handler.change_page(Page.main)

    # ---------------------------------- Manual Mode Functions ----------------------------------- #
    def left_click(self, event=None):
        print "LEFT CLICK HAPPENED"
        self.directional_click(self.ui_handler.key_left)
        return "break"

    def right_click(self, event=None):
        print "RIGHT CLICK HAPPENED"
        self.directional_click(self.ui_handler.key_right)
        return "break"

    def up_click(self, event=None):
        print "UP CLICK HAPPENED"
        self.directional_click(self.ui_handler.key_up)
        return "break"

    def down_click(self, event=None):
        print "DOWN CLICK HAPPENED"
        self.directional_click(self.ui_handler.key_down)
        return "break"

    def directional_click(self, key_click):
        if self.ui_handler.current_page == Page.main:
            self.ui_handler.current_zone = pagegraph.Main[self.ui_handler.current_zone][key_click]
        elif self.ui_handler.current_page == Page.weather:
            self.ui_handler.current_zone = pagegraph.Weather[self.ui_handler.current_zone][key_click]
        elif self.ui_handler.current_page == Page.settings:
            self.ui_handler.current_zone = pagegraph.Settings[self.ui_handler.current_zone][key_click]
        elif self.ui_handler.current_page == Page.news:
            self.ui_handler.current_zone = pagegraph.News[self.ui_handler.current_zone][key_click]
        elif self.ui_handler.current_page == Page.planner:
            self.ui_handler.current_zone = pagegraph.Planner[self.ui_handler.current_zone][key_click]
        return "break"

    def enter_click(self, event=None):
        print "Enter CLICK HAPPENED"
        self.ui_handler.change_page(self.ui_handler.find_page_to_change_to())
        if self.ui_handler.current_page == Page.settings:
            # self.main_page_settings.change_a_setting(self.current_zone)
            self.ui_handler.settings_color_scheme.change_a_setting(self.ui_handler.current_zone,
                                                                  self.ui_handler.settings_font)
            self.ui_handler.settings_font.change_a_setting(self.ui_handler.current_zone, self.ui_handler.return_button,
                                                          self.ui_handler.settings_color_scheme)
            self.ui_handler.settings_update_now.update_smart_mirror(self.ui_handler.current_zone)
            self.ui_handler.update_all_widgets_everything()
        return "break"

    def toggle_manual_mode(self, event=None):
        print "Enter CONTROL HAPPENED"
        varloader.change_other_data('manual_mode', not var.other_data['manual_mode'])
        # todo FINISH THIS

    def toggle_select_mode_for_camera(self, event=None):
        print  "toggling select mode for camera"
        self.ui_handler.camera_select_mode = not self.ui_handler.camera_select_mode
