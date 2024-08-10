# http://iteslj.org/questions/
# pip install lxml bs4 requests

import requests, time
import random, os
from enum import Enum
from bs4 import BeautifulSoup as bs

file_name = "iteslj_questions.txt"


class TYPES(Enum):
    GETTING = 1
    RANDOM_SELECT = 2


def iteslj_crawling_questions():
    main_url = 'http://iteslj.org/questions/'
    resp = requests.get(main_url, verify=False)
    soup = bs(resp.text, 'lxml')
    questions = []
    for link in soup.select('tr > td > ul > li > a'):
        print(main_url + link.get('href'))
        in_resp = requests.get(main_url + link.get('href'), verify=False)
        in_soup = bs(in_resp.text, 'lxml')
        for in_link in in_soup.select('div > ul > li'):
            if None == in_link.string:
                continue
            if '?' != in_link.string[-3:-2]:  # Last word ?
                continue
            questions.append(link.get('href')[:-5] + ":" + in_link.string[:-2])
        time.sleep(1)
    return questions


def action_question(types=TYPES.RANDOM_SELECT):
    questions = []

    if TYPES.GETTING == types:
        questions = iteslj_crawling_questions()
        with open(file_name, 'w+') as file:
            file.write('\n'.join(questions))
    elif TYPES.RANDOM_SELECT == types:
        with open(file_name, "r") as file:
            for fi in file:
                ll = [name.strip() for name in fi.split(":")]
                questions.append(ll)
        print(questions[random.randrange(0, len(questions))])
        print(questions[random.randrange(0, len(questions))])
    else:
        pass


if __name__ == '__main__':
    if not os.path.isfile(file_name):
        action_question(TYPES.GETTING)
    action_question(TYPES.RANDOM_SELECT)
