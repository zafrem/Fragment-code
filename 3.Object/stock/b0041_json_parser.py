import json

#References : https://www.alphavantage.co/
source_string = '{"Meta Data": {"economy": "Intraday (5min) open, high, low, ' \
                'close prices and volume", "Symbol": "IBM", "Last Refreshed": ' \
                '"2024-07-12 19:50:00", "Interval": "5min", "Output Size": ' \
                '"Compact", "6. Time Zone": "US/Eastern"}, "Time Series (5min)": ' \
                '{"2024-07-12 19:50:00": {"open": "182.7850", "high": ' \
                '"182.7850", "low": "182.7000", "close": "182.7050", "volume": ' \
                '"40"}, "2024-07-12 19:40:00": {"open": "182.7700", "high": ' \
                '"182.8300", "low": "182.7700", "close": "182.8300", "volume": ' \
                '"527"}, "2024-07-12 19:35:00": {"open": "182.7000", "high": ' \
                '"182.7000", "low": "182.7000", "close": "182.7000", "' \
                'volume": "111"}}}'
json_data = json.loads(source_string)

print(json_data["Meta Data"]["economy"])

for data in json_data["Time Series (5min)"]:
    tmp_data = json_data["Time Series (5min)"][data]
    agv = (float(tmp_data["high"]) + float(tmp_data["low"]))/2
    print(data, "open:", tmp_data["open"], "agv:", agv, "volume:",tmp_data["volume"] )

"""
[Output]
Intraday (5min) open, high, low, close prices and volume
2024-07-12 19:50:00 open: 182.7850 agv: 182.7425 volume: 40
2024-07-12 19:40:00 open: 182.7700 agv: 182.8 volume: 527
2024-07-12 19:35:00 open: 182.7000 agv: 182.7 volume: 111
"""