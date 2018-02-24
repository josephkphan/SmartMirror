FROM python:2

WORKDIR /usr/src/app

COPY . .

RUN apt-get update; apt-get -y install python-opencv


CMD [ "python", "./service-camera.py" ]