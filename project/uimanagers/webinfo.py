from project.resources import varloader, var
import json
import feedparser
import requests
import traceback
from project.uimanagers.webdata import gmap, stocks
import pprint


# used to gather information from the web.
class WebInfo:
    def update_gmap(self):
        gmap.get_travel_time()

    def update_stocks(self):
        stocks.get_stocks_data()

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

    def update(self):
        if var.gmap is not None:
            self.update_gmap()
        if var.stocks is not None:
            self.update_stocks()
        if var.location_data is None:
            self.update_location()
        self.update_weather()
        self.update_news()
        varloader.update_last_updated_variable()
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
            varloader.update_location(location_obj)  # Save to File

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
                varloader.update_weather(weather_obj)  # Save to File
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
            varloader.update_news_headlines(feed)  # Save to File
            print [field for field in feed]
            print (entry for entry in feed['entries'])
        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get news." % e
            if not any(var.news_data):
                exit()
