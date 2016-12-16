from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var


# File Name: news.py
# Purpose: Gathers headlines from news website
class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)
        image = Image.open("assets/newspaper.png")

        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.icon_label = Label(self, bg=background_color, image=photo)
        self.icon_label.image = photo
        self.icon_label.pack(side=LEFT, anchor=N)

        self.color_event_name = selected_off
        self.event_name = event_name
        self.event_name_label = Label(self, text=self.event_name, font=(font_style, 18), fg=selected_off,
                                      bg=background_color)
        self.event_name_label.pack(side=LEFT, anchor=N)

    def change_color_event_name(self, mode):
        if self.color_event_name != mode:
            self.color_event_name = mode
            self.event_name_label.config(foreground=self.color_event_name)
            # todo add an underline!!!!


class News(Frame):
    def __init__(self, parent, *args, **kwargs):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, *args, **kwargs)
        self.news_page = 0  # used to alternate news title todo implement this!!

        # Initialize Title and container
        self.config(bg=background_color)
        self.title = 'Headlines'
        self.news_label = Label(self, text=self.title, font=(font_style, 28), fg=selected_off, bg=background_color)
        self.news_label.pack(side=TOP, anchor=W)
        self.headlines_container = Frame(self, bg=background_color)
        self.headlines_container.pack(side=TOP)

        # Initializing color for headlines
        self.color_title = selected_off
        self.color_headline = {}
        for i in range(0, 5):
            self.color_headline[i] = selected_off

        # Initialize headline text
        self.headline = {}
        pass
        self.update()

    def update(self):
        # remove all children
        print "UPDATING NEWS INFO ON SCREEN"
        for widget in self.headlines_container.winfo_children():
            widget.destroy()
        headlines = var.saved_data['news_headlines']
        # links = var.saved_data['news_links']  # todo make clickable later link should open new window?

        for i in range(0, 5):
            self.headline[i] = NewsHeadline(self.headlines_container, headlines[str(i)])
            self.headline[i].pack(side=TOP, anchor=W)

    # ---------------------------------- COLOR CHANGERS ----------------------------------- #

    def change_color_news_title(self, mode):
        if self.color_title != mode:
            self.color_title = mode
            self.news_label.config(foreground=mode)

    def change_color_headline(self, mode, headline_num):
        self.headline[headline_num].change_color_event_name(mode)
