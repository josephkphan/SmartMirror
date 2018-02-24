
import json
import feedparser
import requests
import traceback
import time
from webdata import gmap, gstocks, gcalendar
from resources import var, varloader

import threading


class DataGatheringThread(threading.Thread):
    def __init__(self, runnable):
        threading.Thread.__init__(self)
        self.runnable = runnable

    def run(self):
        print '-----Starting Thread to Gather Data--------'
        self.runnable()
        var.update_completed = True
        print '-----Thread FINISHED to Gather Data--------'


# used to gather information from the web.
class WebInfo:
    @staticmethod
    def get_ip():
        try:
            ip_url = "http://jsonip.com/"
            req = requests.get(ip_url, timeout=5)  # todo fix crash when doesnt get request right away
            ip_json = json.loads(req.text)
            return ip_json['ip']
        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get ip." % e
            return None

    def thread_update(self):
        if not var.is_updating:  # Makes sure only one thread is happening at once
            var.is_updating = True
            thread = DataGatheringThread(self.update)
            thread.start()

    def update(self):
        if var.gmap is not None:
            gmap.get_travel_time()
        if var.stocks_list is not None:
            gstocks.get_stocks_data()
        gcalendar.get_calendar_events()  # todo Check if this is enabled? Create a Boolean to enable?? UNCOMMENT
        self.update_location()
        self.update_weather()
        self.update_news()
        print 'UPDATING TIME BITCHES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        var.last_updated = time.time()
        varloader.save_data_to_json_file(var.last_updated, var.file_paths['last_updated'])
        if var.weather_data is None or var.news_data is None:
            print "No instance of weather or news data. Quitting mirror"
            exit()

    def update_location(self):

        # Gets IP information
        temp_ip = self.get_ip()
        # Gets Location information
        try:
            # Get location from web
            location_req_url = "http://freegeoip.net/json/%s" % temp_ip
            r = requests.get(location_req_url,
                             timeout=10)  # todo is point 5 long enough?? WHAT TO DO IF TIMEOUT SIGNAL FAIL???

            location_obj = json.loads(r.text)
            lat = location_obj['latitude']
            lon = location_obj['longitude']
            print lat
            print lon
            if location_obj is not None:
                var.location_data = location_obj
                varloader.save_data_to_json_file(var.location_data, var.file_paths['location'])  # Save to File

        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get Location, " % e
            if not any(var.weather_data):
                exit()

    def update_weather(self):
        if any(var.location_data):
            try:
                # get weather
                lat = str(var.location_data['latitude'])
                lon = str(var.location_data['longitude'])
                key = var.api_tokens['dark_sky_weather']
                print 'lat' + str(lat)
                print 'long' + str(lon)
                print 'token!:' + str(key)
                weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s" % (key, lat, lon)
                r = requests.get(weather_req_url)
                print '---------------------------------------'
                print r
                weather_obj = json.loads(r.text)
                print '--------------------------------------'
                print weather_obj
                if weather_obj is not None:
                    var.weather_data = weather_obj
                    varloader.save_data_to_json_file(var.weather_data, var.file_paths['weather'])
            except Exception as e:
                traceback.print_exc()
                print "Error: %s. Cannot get weather." % e
                if not any(var.weather_data):
                    exit()

    def update_news(self):
        # Gets News information
        try:
            if var.country_code is None:
                headlines_url = "https://news.google.com/news?ned=us&output=rss"
            else:
                headlines_url = "https://news.google.com/news?ned=%s&output=rss" % var.country_code
            feed = feedparser.parse(headlines_url)
            if feed is not None:
                headlines = {}  # Taking out only the headlines and links to those headlines
                links = {}
                # Converting data to Json
                print feed.entries[0].keys()
                counter = 0
                for entry in feed.entries:
                    headlines[str(counter)] = entry.title
                    links[str(counter)] = entry.links
                    counter += 1
                var.news_data['headlines'] = headlines
                var.news_data['links'] = links
                var.news_data['number_of_headlines'] = counter

                varloader.save_data_to_json_file(var.news_data, var.file_paths['news'])
            print [field for field in feed]
            print (entry for entry in feed['entries'])
        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get news." % e
            if not any(var.news_data):
                exit()
