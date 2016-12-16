from enum import Enum

# File Name page.py
# An Enum of all the possible pages for UI Manager


class Page(Enum):
    main = 1
    weather = 2
    settings = 3
    news = 4
    none = -1

