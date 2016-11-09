from Tkinter import *
import feedparser
import traceback
from PIL import Image, ImageTk

from src.project.resources.var import *


# File Name: news.py
# Purpose: Gathers headlines from news website


class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')
        image = Image.open("assets/newspaper.png")

        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg='black', image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=N)
        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', 18), fg="white", bg="black")
        self.eventNameLbl.pack(side=LEFT, anchor=N)


class News(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.newsPage = 0
        self.config(bg='black')
        self.title = 'Headlines'
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', 28), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP)

        self.headline = {}
        self.headline[0] = Frame(self, bg="black")
        self.headline[0] = Label(self, font=('Helvetica', 18), fg="white", bg="black")
        self.headline[1] = Frame(self, bg="black")
        self.headline[1] = Label(self, font=('Helvetica', 18), fg="white", bg="black")
        self.headline[2] = Frame(self, bg="black")
        self.headline[2] = Label(self, font=('Helvetica', 18), fg="white", bg="black")
        self.headline[3] = Frame(self, bg="black")
        self.headline[3] = Label(self, font=('Helvetica', 18), fg="white", bg="black")
        self.headline[4] = Frame(self, bg="black")
        self.headline[4] = Label(self, font=('Helvetica', 18), fg="white", bg="black")
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
