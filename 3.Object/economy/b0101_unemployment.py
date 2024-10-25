import requests
import matplotlib.pyplot as plt

key = 'SO8SU91FB2QDELT5'
url = f'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={key}'
r = requests.get(url)
data = r.json()

month=[]
value=[]
count = 0
for item in data['data']:
    month.append(item['date'][:-3])
    value.append(float(item['value']))
    if 120 == count:
        break
    count += 1
month.reverse()
value.reverse()

plt.plot(month, value, 'r-', label="Month")

plt.xlabel('Unemployment')
plt.xticks(ticks=month, labels=month, rotation=45)
plt.locator_params(axis='x', nbins=len(month))
plt.ylabel('%')
plt.legend()

plt.show()
