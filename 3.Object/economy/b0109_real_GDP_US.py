import requests
import matplotlib.pyplot as plt

key = 'SO8SU91FB2QDELT5'
intervals = ['quarterly','annual']
months = [[],[]]
values = [[],[]]
i = 0
for interval in intervals:
    url = f'https://www.alphavantage.co/query?function=REAL_GDP&interval={interval}&apikey={key}'
    r = requests.get(url)
    data = r.json()

    month=months[i]
    value=values[i]
    count = 0
    for item in data['data']:
        month.append(item['date'][:-3])
        value.append(float(item['value']))
        if 120 == count:
            break
        count += 1
    month.reverse()
    value.reverse()
    i+=1



plt.plot(months[1], values[1], 'b-', label="Annual")

month = months[1]
month = list(set(month))
month.sort()

plt.xlabel('Real GDP')
plt.xticks(ticks=month, labels=month, rotation=45)
plt.locator_params(axis='x', nbins=len(month))
plt.ylabel('$')
plt.legend()

plt.show()

plt.plot(months[0], values[0], 'r-', label="Quarterly")
month = months[0]
month = list(set(month))
month.sort()

plt.xlabel('Real GDP')
plt.xticks(ticks=month, labels=month, rotation=45)
plt.locator_params(axis='x', nbins=len(month))
plt.ylabel('$')
plt.legend()

plt.show()
