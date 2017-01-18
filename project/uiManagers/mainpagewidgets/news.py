from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, imagecolor


# File Name: news.py
# Purpose: Gathers headlines from news website
class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)

        # Initializing Boolean color for all labels
        self.color_all = selected_off

        # Creating the regular icon photo an tinted photo
        self.image = Image.open("assets/newspaper.png")
        self.image = self.image.resize(var.font_sizes['small_icon'], Image.ANTIALIAS)
        self.image = self.image.convert('RGB')
        self.icon_photo, self.icon_photo_tinted = None, None
        self.icon_photo = ImageTk.PhotoImage(self.image)
        self.icon_photo_tinted = ImageTk.PhotoImage(imagecolor.tint(self.image,var.selected_on))

        # Initializing Labels
        self.icon_label = Label(self, bg=background_color, image=self.icon_photo)
        self.icon_label.image = self.icon_photo
        self.icon_label.pack(side=LEFT, anchor=N)

        self.event_name = event_name
        self.event_name_label = Label(self, text=self.event_name, font=(font_style,  font_sizes['text']), fg=selected_off,
                                      bg=background_color)
        self.event_name_label.pack(side=LEFT, anchor=N)

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode
            if self.color_all == var.selected_off:
                # Image should be white
                self.icon_label.config(image=self.icon_photo)
            else:
                # Image should be selected or tinted
                self.icon_label.config(image=self.icon_photo_tinted)
            # Changes Headline Text
            self.event_name_label.config(foreground=self.color_all)
            # todo add an underline!!!!

    def change_font_size(self):
        # Updating image
        self.image = self.image.resize(var.font_sizes['small_icon'], Image.ANTIALIAS)
        self.image = self.image.convert('RGB')
        self.icon_photo, self.icon_photo_tinted = None, None
        self.icon_photo = ImageTk.PhotoImage(self.image)
        self.icon_photo_tinted = ImageTk.PhotoImage(imagecolor.tint(self.image, var.selected_on))

        self.event_name_label.config(font=(var.font_style,  var.font_sizes['text']))


class News(Frame):
    def __init__(self, parent,num_headlines, *args, **kwargs):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, *args, **kwargs)
        self.num_headlines = num_headlines
        # Initialize Title and container
        self.config(bg=background_color)

        self.title_label = Label(self, text='Headlines', font=(font_style,  font_sizes['title']), fg=selected_off, bg=background_color)
        self.title_label.pack(side=TOP, anchor=W)
        self.headlines_container = Frame(self, bg=background_color)
        self.headlines_container.pack(side=TOP)

        # Initializing color boolean for headlines
        self.color_all = selected_off

        # Initializing empty headlines

        # Initialize headline text
        self.headline = {}
        pass   # used to ignore empty dictionary complaint
        self.update_now()

    def update_now(self):
        # remove all children
        print "UPDATING NEWS INFO ON SCREEN"
        for widget in self.headlines_container.winfo_children():
            widget.destroy()
        self.title_label.config(font=(var.font_style,  var.font_sizes['title']))    # for updating font size

        headlines = var.saved_data['news_headlines']
        # links = var.saved_data['news_links']  # todo make clickable later link should open new window?
        if var.saved_data['news_number_of_headlines'] < self.num_headlines:
            self.num_headlines = var.saved_data['news_number_of_headlines']
        for i in range(0,self.num_headlines):
            self.headline[i] = NewsHeadline(self.headlines_container, headlines[str(i)])
            self.headline[i].pack(side=TOP, anchor=W)

    # ---------------------------------- COLOR CHANGERS ----------------------------------- #

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all=mode
            self.title_label.config(foreground=self.color_all)
            for i in range (0,self.num_headlines):
                self.headline[i].change_color_all(self.color_all)
