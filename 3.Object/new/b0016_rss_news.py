import os
import feedparser
import difflib

def dup_delete(news_lists):
    new_index = -1
    for news in news_lists:
        new_index += 1
        diff_index = 0
        for diff_news in news_lists:
            diff_index += 1
            if new_index < diff_index:
                # titel similarity
                similarity = difflib.SequenceMatcher(None, news[0], diff_news[0]).ratio()
                if 0.7 < similarity:
                    del news_lists[diff_index - 1]
                    diff_index -= 1 # delete list element index re-arrange
                else:
                    pass
    return news_lists

def get_rss_news(url):
    feed = feedparser.parse(url)
    ret_lists = []
    for item in feed.entries:
        try:
            #print(f'Item title: {item.title}')
            #print(f'Item description: {item.description}')
            #print(f'Item link: {item.link}')
            #print(f'Item published: {item.published}')
            ret_lists.append([item.title, item.description])
        except:
            continue
    return ret_lists
"""
The New York Times : https://rss.nytimes.com/
CNN : http://edition.cnn.com/services/rss/
"""

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
    print(len(news_lists))
    news_lists = dup_delete(news_lists)
    print(len(news_lists))
    print(news_lists)