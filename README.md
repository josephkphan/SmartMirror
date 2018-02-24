# Smart Mirror

### Introduction
Nearly everything in our household is turning *smart*. There are smart phones, smart watches, smart tv’s, smart refrigerators, and even smart washing machines. Why not Smart Mirrors?

Our smart mirror will be used to convenience people during their morning routines as they brush, apply makeup, do their hair, and even try on outfits. It will display the weather so you know how to dress; it has the news, stocks, traffic data for you to keep updated, and of course it will have a clock and include traffic data to keep you from running late to work.

### Features
- Hand recognition technology for hands free use
- Automatically turns on when you approach the mirror
- Personalized widgets for the time, weather, and news, calendar, todolist
- Customizable font sizing and coloring of the widgets

### Technologies
- Docker
- Python
- TKinter
- OpenCV Library
- Raspberry Pi
- Google & Darksky APIs 

### Running on Mac
- Install XQuartz: This is to allow the container to access your display to open a GUI. 
``` 
brew cask install xquartz
open -a XQuartz
```
![Setup 1](./screenshots/setup1.png)
In the XQuartz preferences, go to the “Security” tab and make sure you’ve got “Allow connections from network clients" checked. Then Restart your mac for the settings to apply.

- Install Docker
```
brew cask install docker
```

- Start the application 
```
docker-compose up -d
```


### Running on Ubuntu
- Install Docker
```
sudo apt-get update
sudo apt-get install docker-ce
```
- Start the application
```
docker-compose up -d
```

### Application Screenshots
![Screenshot 1](./screenshots/screenshot1.png)
![Screenshot 2](./screenshots/screenshot2.png)
![Screenshot 3](./screenshots/screenshot3.png)
