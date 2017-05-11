from googlefinance import getQuotes
import json
from project.resources import var, varloader


def get_stocks_data():
    try:
        for stock in var.stocks_list:
            data = json.dumps(getQuotes(str(stock)), indent=2)
            data = json.loads(data)[0]
            print data
            if data is not None:
                var.stock_data[stock] = data
            print 'Pulled ', stock
    except Exception, e:
        print 'Stocks Error', str(e)
    varloader.save_data_to_json_file(var.stock_data, var.file_paths['stock_data'])

#sudo apt install python-pip
# pip install demjson
# sudo pip install googlefinance
