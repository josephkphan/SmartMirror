#! /usr/bin/python

import os

# What your libraries your system should already have:
#   - math
#   - json
#   - time
#   - Datetime
#   - traceback

# If you want to test. run in terminal 'python'
# type in import [LIBRARY NAME]
# if you see just 
# >
# then it found an existing library

# Update computer
os.system("sudo apt-get update && time sudo apt-get dist-upgrade")

# Install pip
os.system("sudo apt-get install python-setuptools python-dev build-essential")

# Install Shapely
os.system("sudo apt-get install python-shapely")

# Install PIL
os.system("sudo apt-get install python-imaging-tk")
os.system("sudo apt-get install python-imaging")

# Install enum
os.system("sudo apt-get install python-enum")

# Install numpy
os.system("sudo apt-get install python-numpy")

# Install feedparser
os.system("sudo apt-get install python-feedparser")

# Install requests
os.system("sudo apt-get install python-requests")

# Install simple json
os.system("sudo apt-get install python-simplejson")


# Install Google Client Services
# os.system("pip install --upgrade google-api-python-client")


# Install RPI.GPIO
# .... TODO FINISH LATER     https://goo.gl/QpUyRZ

# Install openCV
os.system("sudo apt-get install python-opencv")

# Install Google Api Client (for calendar)
os.system("sudo pip install --upgrade google-api-python-client")

os.system("sudo apt install python-pip")

os.system("pip install demjson")

os.system("sudo pip install googlefinance")


# ------------------- WHAT EVERY USER NEEDS TO DO --------------------- #
# Register for a Weather API Key at https://darksky.net/dev/ and store the key 
# in a key.txt file

