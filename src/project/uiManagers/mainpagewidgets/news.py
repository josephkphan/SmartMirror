from Tkinter import *
from PIL import Image, ImageTk

from src.project.resources.var import *


# File Name: news.py
# Purpose: Gathers headlines from news website


class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg=background_color)
        image = Image.open("assets/newspaper.png")

        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg=background_color, image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=N)
        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=(font_style, 18), fg=selected_off,
                                  bg=background_color)
        self.eventNameLbl.pack(side=LEFT, anchor=N)


class News(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.newsPage = 0

        # Initialize Title and container
        self.config(bg=background_color)
        self.title = 'Headlines'
        self.newsLbl = Label(self, text=self.title, font=(font_style, 28), fg=selected_off, bg=background_color)
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg=background_color)
        self.headlinesContainer.pack(side=TOP)

        # Initializing color for headlines
        self.color_headline = {}
        for i in range (0,5):
            self.color_headline[i] = selected_off

        # Initialize headline text
        self.headline = {}
        self.headline[0] = Frame(self, bg=background_color)
        self.headline[0] = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.headline[1] = Frame(self, bg=background_color)
        self.headline[1] = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.headline[2] = Frame(self, bg=background_color)
        self.headline[2] = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.headline[3] = Frame(self, bg=background_color)
        self.headline[3] = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.headline[4] = Frame(self, bg=background_color)
        self.headline[4] = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.update()

    def update(self):
        # remove all children
        print "UPDATING NEWS INFO ON SCREEN"
        for widget in self.headlinesContainer.winfo_children():
            widget.destroy()
        headlines = saved_data['news_headlines']
        links = saved_data['news_links']  # todo make clickable later link should open new window?

        for i in range(0, 5):
            self.headline[i].config(text=headlines[str(i)])
            self.headline[i].pack(side=TOP, anchor=W)

    # ---------------------------------- COLOR CHANGERS ----------------------------------- #

    def change_news_title_to_yellow(self):
        self.newsLbl.config(foreground="yellow")

    def change_news_title_to_white(self):
        self.newsLbl.config(foreground="white")

    def change_headline1_to_yellow(self, headline_num):
        self.headline[headline_num].config(foreground="yellow")

    def change_headline1_to_white(self, headline_num):
        self.headline[headline_num].config(foreground="white")
