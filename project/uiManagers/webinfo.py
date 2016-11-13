from project.resources import varLoader, var
import json
import feedparser
import requests
import traceback


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

    def update(self):
        print "~~~~~UPDATING INFO~~~~"
        weather_obj, location_obj, feed = None, None, None
        temp_ip = self.get_ip()
        print "~~~~~~~~~~~~~IP RETURNED~~~~~~~~~~~"
        print temp_ip
        if temp_ip is not None:
            try:
                if var.country_code is None:
                    headlines_url = "https://news.google.com/news?ned=us&output=rss"
                else:
                    headlines_url = "https://news.google.com/news?ned=%s&output=rss" % var.country_code
                feed = feedparser.parse(headlines_url)

            except Exception as e:
                traceback.print_exc()
                print "Error: %s. Cannot get news." % e

            try:
                # Get location from web
                location_req_url = "http://freegeoip.net/json/%s" % temp_ip
                r = requests.get(location_req_url,
                                 timeout=1)  # todo is point 5 long enough?? WHAT TO DO IF TIMEOUT SIGNAL FAIL???

                location_obj = json.loads(r.text)
                lat = location_obj['latitude']
                lon = location_obj['longitude']

                # get weather
                weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s" % (self.key, lat, lon)
                r = requests.get(weather_req_url)
                weather_obj = json.loads(r.text)

            except Exception as e:
                traceback.print_exc()
                print "Error: %s. Cannot get weather." % e

        varLoader.update_data(weather_obj, location_obj, feed)
