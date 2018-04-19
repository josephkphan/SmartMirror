FROM josephkphan/smartmirror-pythonbase

WORKDIR /usr/src/app

COPY . .

RUN pip install requests simplejson 

# CMD [ "python", "./service-websync.py", "--noauth_local_webserver" ]
CMD [ "python", "./service-websync.py"]