import requests
import matplotlib.pyplot as plt

key = 'SO8SU91FB2QDELT5'
url = f'https://www.alphavantage.co/query?function=NONFARM_PAYROLL&apikey={key}'
r = requests.get(url)
data = r.json()
print(data)
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

plt.plot(month, value, 'bo', label="Month")

plt.xlabel('NoFarm Payroll')
plt.xticks(ticks=month, labels=month, rotation=45)
plt.locator_params(axis='x', nbins=len(month))
plt.ylabel('Value')
plt.legend()

plt.show()
