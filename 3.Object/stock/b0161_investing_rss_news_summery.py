# ollama install
# https://ollama.com/download/mac
# https://ollama.com/download/linux
# https://ollama.com/download/windows

# ollama start
# ollama run llama3.2

# pip install ollama
# https://github.com/ollama/ollama-python

from ollama import chat
from ollama import ChatResponse
import feedparser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def get_www_investing_rss_news():
    urls = ["https://www.investing.com/rss/news.rss",
            "https://www.investing.com/rss/market_overview.rss",
            "https://www.investing.com/rss/286.rss",
            "https://www.investing.com/rss/stock.rss",
            "https://ww.investing.com/rss/commodities.rss"]
    ret_lists = []

    for url in urls:
        feed = feedparser.parse(url)
        for item in feed.entries:
            try:
                #print(f'Item title: {item.title}')
                #print(f'Item link: {item.link}')
                #print(f'Item Author: {item.author}')
                #print(f'Item published: {item.published}')
                pass
            except:
                continue
            ret_lists.append([item.title, item.link, item.author, item.published])
    return ret_lists


def get_kr_investing_rss_news():
    urls = ["https://kr.investing.com/rss/news.rss",
            "https://kr.investing.com/rss/market_overview.rss",
            "https://kr.investing.com/rss/286.rss",
            "https://kr.investing.com/rss/stock.rss",
            "https://kr.investing.com/rss/commodities.rss"]
    ret_lists = []

    for url in urls:
        feed = feedparser.parse(url)
        for item in feed.entries:
            try:
                #print(f'Item title: {item.title}')
                #print(f'Item link: {item.link}')
                #print(f'Item Author: {item.author}')
                #print(f'Item published: {item.published}')
                pass
            except:
                continue
            ret_lists.append([item.title, item.link, item.author, item.published])
    return ret_lists

def text_summery(string):
    print(string)
    response: ChatResponse = chat(model='llama3.2:1b', messages=[
      {
        'role': 'user',
        'content': f'I have collected a bunch of news, delete the same ones and summarize them for me. {string}',
      },
    ])

    # or access fields directly from the response object
    print("=====================")
    print(response.message.content)
    print("=====================")
    print(f"Org Msg : Ollama Msg = {str(len(string))} : {str(len(response.message.content))}")

if '__main__' == __name__:
    #lists = get_kr_investing_rss_news()
    #kr_string = ''
    #for title in lists:
    #    kr_string += title[0] + "\n"
    #text_summery(kr_string)
    lists = get_www_investing_rss_news()
    www_string = ''
    for title in lists:
        www_string += title[0] + "\n"
    text_summery(www_string)