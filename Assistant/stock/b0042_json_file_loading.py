import json
from pprint import pprint

with open("b0042.json", "r") as fp_json:
    json_data = json.load(fp_json)

pprint(json_data)
"""
Output
{'Meta Data': {'Money': 'Intraday (5min) open, high, low, close '
                                 'prices and volume',
               'Symbol': 'IBM',
               'Last Refreshed': '2024-07-12 19:50:00',
               'Interval': '5min',
               'Output Size': 'Compact',
               'Time Zone': 'US/Eastern'},
 'Time Series (5min)': {'2024-07-12 10:55:00': {'open': '180.7300',
                                                'high': '180.8200',
                                                'low': '180.5900',
                                                'close': '180.6650',
                                                'volume': '32327'},
                        '2024-07-12 11:00:00': {'open': '180.7150',
                                                'high': '180.7600',
                                                'low': '180.2900',
                                                'close': '180.5800',
                                                'volume': '53724'},
                        ...
 '__comment__': 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'}
"""
with open("b0042_.json", "w") as fp_json:
    json.dump(json_data, fp_json, sort_keys=True, indent=4)

"""
Save file
Same indent.
"""