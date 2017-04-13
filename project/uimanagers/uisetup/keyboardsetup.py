from project.resources import pagegraph, var, varloader
from project.resources.page import *


class KeyboardSetUp:
    def __init__(self, uiHandler):
        self.uiHandler = uiHandler
        self.uiHandler.tk.bind("<Tab>", self.toggle_fullscreen)
        self.uiHandler.tk.bind("<Escape>", self.end_fullscreen)
        self.uiHandler.tk.bind("<Control_R>", self.toggle_power)

        self.uiHandler.tk.bind("<Left>", self.left_click)
        self.uiHandler.tk.bind("<Right>", self.right_click)
        self.uiHandler.tk.bind("<Up>", self.up_click)
        self.uiHandler.tk.bind("<Down>", self.down_click)
        self.uiHandler.tk.bind("<BackSpace>", self.enter_click)
        self.uiHandler.tk.bind("<Control_L>", self.toggle_manual_mode)
        self.uiHandler.tk.bind("<Shift_L>", self.toggle_select_mode_for_camera)

        # ---------------------------------- Key Binding Functions ----------------------------------- #

    def toggle_fullscreen(self, event=None):
        self.uiHandler.camera_selection_mode = not self.uiHandler.camera_selection_mode  # Just toggling the boolean
        self.uiHandler.tk.attributes("-fullscreen", self.uiHandler.camera_selection_mode)
        return "break"

    def end_fullscreen(self, event=None):
        self.uiHandler.camera_selection_mode = False
        self.uiHandler.tk.attributes("-fullscreen", False)
        return "break"

    def toggle_power(self, event=None):
        if self.uiHandler.current_page != Page.blank:
            self.uiHandler.change_page(Page.blank)
        else:
            self.uiHandler.change_page(Page.main)

    # ---------------------------------- Manual Mode Functions ----------------------------------- #
    def left_click(self, event=None):
        print "LEFT CLICK HAPPENED"
        self.directional_click(self.uiHandler.key_left)
        return "break"

    def right_click(self, event=None):
        print "RIGHT CLICK HAPPENED"
        self.directional_click(self.uiHandler.key_right)
        return "break"

    def up_click(self, event=None):
        print "UP CLICK HAPPENED"
        self.directional_click(self.uiHandler.key_up)
        return "break"

    def down_click(self, event=None):
        print "DOWN CLICK HAPPENED"
        self.directional_click(self.uiHandler.key_down)
        return "break"

    def directional_click(self, key_click):
        if self.uiHandler.current_page == Page.main:
            self.uiHandler.current_zone = pagegraph.Main[self.uiHandler.current_zone][key_click]
        elif self.uiHandler.current_page == Page.weather:
            self.uiHandler.current_zone = pagegraph.Weather[self.uiHandler.current_zone][key_click]
        elif self.uiHandler.current_page == Page.settings:
            self.uiHandler.current_zone = pagegraph.Settings[self.uiHandler.current_zone][key_click]
        elif self.uiHandler.current_page == Page.news:
            self.uiHandler.current_zone = pagegraph.News[self.uiHandler.current_zone][key_click]
        elif self.uiHandler.current_page == Page.planner:
            self.uiHandler.current_zone = pagegraph.Planner[self.uiHandler.current_zone][key_click]
        return "break"

    def enter_click(self, event=None):
        print "Enter CLICK HAPPENED"
        self.uiHandler.change_page(self.uiHandler.find_page_to_change_to())
        if self.uiHandler.current_page == Page.settings:
            # self.main_page_settings.change_a_setting(self.current_zone)
            self.uiHandler.settings_color_scheme.change_a_setting(self.uiHandler.current_zone,
                                                                  self.uiHandler.settings_font)
            self.uiHandler.settings_font.change_a_setting(self.uiHandler.current_zone, self.uiHandler.return_button,
                                                          self.uiHandler.settings_color_scheme)
            self.uiHandler.settings_update_now.update_smart_mirror(self.uiHandler.current_zone)
            self.uiHandler.update_all_widgets_everything()
        return "break"

    def toggle_manual_mode(self, event=None):
        print "Enter CONTROL HAPPENED"
        varloader.change_other_data('manual_mode', not var.other_data['manual_mode'])
        # todo FINISH THIS

    def toggle_select_mode_for_camera(self, event=None):
        print  "toggling select mode for camera"
        self.camera_select_mode = not self.camera_select_mode
