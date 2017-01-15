from project.resources import varLoader, var
import json
import feedparser
import requests
import traceback
import pprint


# used to gather information from the web.
class WebInfo:
    def __init__(self):
        self.key = var.weather_api_token

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

    # Updates the information for Weather, and Newsheadlines
    def update(self):
        weather_obj, location_obj, feed = None, None, None

        # Gets IP information
        temp_ip = self.get_ip()
        print temp_ip
        if temp_ip is not None:

            # Gets News information
            try:
                if var.country_code is None:
                    headlines_url = "https://news.google.com/news?ned=us&output=rss"
                else:
                    headlines_url = "https://news.google.com/news?ned=%s&output=rss" % var.country_code
                feed = feedparser.parse(headlines_url)
                print [field for field in feed]
                print (entry for entry in feed['entries'])
            except Exception as e:
                traceback.print_exc()
                print "Error: %s. Cannot get news." % e

            # Gets weather information
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

                # get weather
                weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s" % (self.key, lat, lon)
                r = requests.get(weather_req_url)
                print '---------------------------------------'
                print r
                weather_obj = json.loads(r.text)
                print '--------------------------------------'
                print weather_obj
                 
            except Exception as e:
                traceback.print_exc()
                print "Error: %s. Cannot get weather." % e

        varLoader.update_data(weather_obj, location_obj, feed)

