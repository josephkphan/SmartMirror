import socket
import time
import datetime
import sys

sys.path.append("../")

from websync import *
from resources import var, varloader


def web_cron(web_sync):
    '''
    This function periodically updates the mirror's preferences to align with
    the preferences that have been set on the web server
    '''
    print var.last_updated
    while True:
        time.sleep(10) # TODO change to 10s when developing in scenarios

        # Printing the current timestamp for debugging purposes
        curr_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print curr_time

        web_sync.update_all()


if __name__ == '__main__':
    web_sync = WebSync()
    web_cron(web_sync)
