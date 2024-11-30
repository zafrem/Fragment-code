# ollama install
# https://ollama.com/download/mac
# https://ollama.com/download/linux
# https://ollama.com/download/windows

# ollama start
# ollama run llama3.2

# pip install ollama
# https://github.com/ollama/ollama-python

import feedparser
from ollama import chat
from ollama import ChatResponse


def news_summery(string):
    response: ChatResponse = chat(model='llama3.2:1b', messages=[
      {
        'role': 'user',
        'content': f'I have collected a bunch of news, delete the same ones and summarize them for me. {string}',
      },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)


def get_rss_news(url):
    feed = feedparser.parse(url)
    ret_lists = []
    for item in feed.entries:
        try:
            ret_lists.append([item.title, item.description])
        except:
            continue
    return ret_lists

if '__main__' == __name__:
    news_rss_site = [
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/US.xml",
        "http://rss.cnn.com/rss/edition.rss",
        "http://rss.cnn.com/rss/edition_world.rss"
        ]
    news_lists = []
    for url in news_rss_site:
        news = get_rss_news(url)

        for new in news:
            news_lists.append(new)
    strings = ''
    for news_list in news_lists:
        strings += news_list[0] + ":" + news_list[1] + "\n"
    news_summery(strings)