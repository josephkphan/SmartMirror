FROM josephkphan/smartmirror-pythonbase

WORKDIR /usr/src/app

COPY . .

RUN pip install feedparser requests simplejson googlefinance httplib2 apiclient google-api-python-client


CMD [ "python", "./service-web.py", "--noauth_local_webserver" ]