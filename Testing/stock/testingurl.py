import urllib2
import time

urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/AAPL/chartdata;type=quote;range=10d/csv'
sourceCode = urllib2.urlopen(urlToVisit).read().decode()
print sourceCode