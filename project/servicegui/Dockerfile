FROM josephkphan/smartmirror-rpipythonbase

WORKDIR /usr/src/app

COPY . .

RUN apt-get install libgeos-dev python-pil python-imaging-tk
RUN pip install shapely enum pillow 

# RUN apt-get update && \ 
#     apt-get install --yes --force-yes python-setuptools python-dev build-essential && \
#     apt-get install --yes --force-yes python-shapely && \
#     apt-get install --yes --force-yes python-imaging-tk && \
#     apt-get install --yes --force-yes python-imaging && \
#     apt-get install --yes --force-yes python-enum && \
#     apt-get install --yes --force-yes python-numpy && \
#     apt-get install --yes --force-yes python-feedparser && \
#     apt-get install --yes --force-yes python-requests && \
#     apt-get install --yes --force-yes python-simplejson 

CMD [ "python", "./service-gui.py" ]