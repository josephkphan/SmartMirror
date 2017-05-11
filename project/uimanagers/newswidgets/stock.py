from Tkinter import *
from project.resources import var


class Stock(Frame):
    def __init__(self, parent, stock_name):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        self.stock_frame = Frame(self, bg=background_color)
        self.stock_frame.pack(side=TOP, anchor=N)

        # Initializing text (raw values) for labels (values to be displayed)
        self.stock_name_text = stock_name
        self.stock_price_text = ''

        # Initializing a color boolean for all labels
        self.color_all = selected_off

        # Initializing Labels
        self.stock_name_label = Label(self.stock_frame, font=(font_style, font_sizes['big_text']), fg=selected_off,
                                      bg=background_color)
        self.stock_name_label.config(text=self.stock_name_text)
        self.stock_name_label.pack(side=TOP, anchor=N)
        self.stock_price_label = Label(self.stock_frame, font=(font_style, font_sizes['big_text']), fg=selected_off,
                                       bg=background_color)
        self.stock_price_label.pack(side=TOP, anchor=N)
        self.update_now()

    def update_now(self):
        stock_price = var.stock_data[self.stock_name_text]['LastTradePrice']

        # Updating daily weather if it doesnt match
        if self.stock_price_label != stock_price:
            self.stock_price_text = stock_price
            self.stock_price_label.config(text=self.stock_price_text)

        self.update_font_size()

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode
            self.stock_name_label.config(foreground=self.color_all)
            self.stock_price_label.config(foreground=self.color_all)

    def update_font_size(self):
        self.stock_name_label.config(font=(var.font_style, var.font_sizes['big_text']))
        self.stock_price_label.config(font=(var.font_style, var.font_sizes['big_text']))
