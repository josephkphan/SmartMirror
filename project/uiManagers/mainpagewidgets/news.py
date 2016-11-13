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
        self.event_name = event_name
        self.event_name_label = Label(self, text=self.event_name, font=(font_style, 18), fg=selected_off,
                                      bg=background_color)
        self.event_name_label.pack(side=LEFT, anchor=N)


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
        for widget in self.headlines_container.winfo_children():
            widget.destroy()
        headlines = var.saved_data['news_headlines']
        links = var.saved_data['news_links']  # todo make clickable later link should open new window?

        for i in range(0, 5):
            self.headline[i].config(text=headlines[str(i)])
            self.headline[i].pack(side=TOP, anchor=W)

    # ---------------------------------- COLOR CHANGERS ----------------------------------- #

    def change_color_news_title(self, mode):
        if self.color_title != mode:
            self.color_title = mode
            self.news_label.config(foreground=mode)

    def change_headline_on(self, mode, headline_num):
        if self.color_headline[headline_num] != mode:
            self.color_headline[headline_num] = mode
            self.headline[headline_num].config(foreground=self.color_headline[headline_num])
