from Tkinter import *
from src.project.resources.var import *
import feedparser
import requests
import traceback


class WebInfo():
    def get_ip(self):
        try:
            ip_url = "http://jsonip.com/"
            req = requests.get(ip_url)
            ip_json = json.loads(req.text)
            return ip_json['ip']
        except Exception as e:
            traceback.print_exc()
            return "Error: %s. Cannot get ip." % e

    def update(self):
        # print  "~~~~~UPDATING INFO~~~~"
        try:

            if country_code == None:
                headlines_url = "https://news.google.com/news?ned=us&output=rss"
            else:
                headlines_url = "https://news.google.com/news?ned=%s&output=rss" % country_code

            feed = feedparser.parse(headlines_url)

        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get news." % e

        try:
            # get location
            location_req_url = "http://freegeoip.net/json/%s" % self.get_ip()
            # print "Location req url : " + location_req_url

            r = requests.get(location_req_url, timeout=.5)  # todo is point 5 long enough??

            location_obj = json.loads(r.text)

            lat = location_obj['latitude']
            lon = location_obj['longitude']

            # print "Lat : " + str(lat) + "  |  Lon : " + str(lon)

            location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])

            # get weather
            weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s" % (
                weather_api_token, lat, lon)
            r = requests.get(weather_req_url)
            weather_obj = json.loads(r.text)

        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get weather." % e

        update_data(weather_obj, location_obj, feed)
