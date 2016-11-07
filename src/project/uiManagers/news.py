from Tkinter import *
import feedparser
import traceback
from PIL import Image, ImageTk

import src.project.resources.var
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
        self.config(bg='black')
        self.title = 'Headlines'
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', 28), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP)
        self.headline1 = Frame(self, bg="black")
        self.headline1 = Label(self, font=('Helvetica', 18), fg="white", bg="black")
        self.get_headlines()

    def get_headlines(self):
        try:
            # remove all children
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()
            if src.project.resources.var.country_code == None:
                headlines_url = "https://news.google.com/news?ned=us&output=rss"
            else:
                headlines_url = "https://news.google.com/news?ned=%s&output=rss" % src.project.resources.var.country_code

            feed = feedparser.parse(headlines_url)

            for post in feed.entries[0:5]:
                #headline = NewsHeadline(self.headlinesContainer, post.title)
                self.headline1.config(text=post.title)
                self.headline1.pack(side=TOP, anchor=W)

        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get news." % e

        self.after(600000, self.get_headlines)

    # ---------------------------------- COLOR CHANGERS ----------------------------------- #

    def change_color_to_yellow(self):
        self.newsLbl.config(foreground="yellow")
        self.headline1.config(foreground="yellow")
        # todo figure how to change headlines to yellow

    def change_color_to_white(self):
        self.newsLbl.config(foreground="white")
        self.headline1.config(foreground="white")