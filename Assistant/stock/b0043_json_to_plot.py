import json
import matplotlib.pyplot as plt
import datetime

with open("b0043_IBM.json", "r") as fp_json:
    ibm_data = json.load(fp_json)

with open("b0043_AAPL.json", "r") as fp_json:
    aapl_data = json.load(fp_json)

with open("b0043_TSLA.json", "r") as fp_json:
    tsla_data = json.load(fp_json)

data_lsts = [[],[],[]]
open_lsts = [[],[],[]]
high_lsts = [[],[],[]]
low_lsts = [[],[],[]]
close_lsts = [[],[],[]]
volume_lsts = [[],[],[]]

tmp_datas = [ibm_data, aapl_data, tsla_data]
i = 0
for tmp_lsts in [ibm_data["Time Series (Daily)"],aapl_data["Time Series (Daily)"],
                           tsla_data["Time Series (Daily)"]]:
    for _date in tmp_lsts:
        tmp_data = tmp_lsts[_date]
        data_lsts[i%3].append(datetime.datetime.strptime(_date, '%Y-%m-%d'))
        open_lsts[i%3].append(float(tmp_data['open']))
        high_lsts[i%3].append(float(tmp_data['high']))
        low_lsts[i%3].append(float(tmp_data['low']))
        close_lsts[i%3].append(float(tmp_data['close']))
        volume_lsts[i%3].append(float(tmp_data['volume']))
    i+=1


plt.plot(data_lsts[0], open_lsts[0], 'b--', label="IBM")
plt.plot(data_lsts[1], open_lsts[1], 'r--', label="AAPL")
plt.plot(data_lsts[2], open_lsts[2], 'g--', label="TSLA")

plt.xlabel('Time')
plt.ylabel('Open')
plt.xticks(ticks=data_lsts[0], labels=data_lsts[0], rotation=25)
plt.locator_params(axis='x', nbins=10)
plt.legend()

plt.show()