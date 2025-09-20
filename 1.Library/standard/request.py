import requests
from bs4 import BeautifulSoup as HtmlParser

if '__main__' == __name__:
    my_header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/125.0.0.0 Safari/537.36'}
    response = requests.get('https://www.bbc.com/',headers = my_header)
    soup = HtmlParser(response.text, "html.parser" )
    html = soup.select_one('a > div > div > div > div > h2')  #See image below
    print(html)
    print(html.text)