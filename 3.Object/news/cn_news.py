import os
from bs4 import BeautifulSoup as bs
from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib3
urllib3.disable_warnings()
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
os.environ['WDM_SSL_VERIFY'] = '0'


def google_trans(str, target):
    translator = Translator()
    translation = translator.translate(str, dest=target)
    return translation.text


def cn_news():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://xueqiu.com/'
    driver.get(url + '?category=snb_article')
    driver.implicitly_wait(10)
    resp = driver.page_source
    driver.close()

    soup = bs(resp, 'lxml')

    titles , ktitles, etitles, links = [], [], [], []

    i = 0
    for link in soup.select('#app > div > div > div > div > div > div > table > tr > td > a'):
        if None == link.string:
            continue
        titles.append(link.string)
        estring = google_trans(link.string, "en")
        etitles.append(estring)
        ktitles.append(google_trans(estring, 'ko'))
        links.append(link.href)
        i += 1
        if 5 == i:
            break
    data = {'title': titles, 'ktitle': ktitles, 'etitle':etitles, 'link':links}
    return data

if '__main__' == __name__:
    datas = cn_news()
    for data in datas.keys():
        print(datas[data])