import requests
import urllib3
urllib3.disable_warnings()
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

key = 'SO8SU91FB2QDELT5'
url = f'https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey={key}'
r = requests.get(url, verify=False)
datas = r.json()
print(f"{datas['name']} - {datas['interval']} ({datas['unit']})")
for data in datas['data']:
    print(f"{data['date']} : ${data['value']}")
