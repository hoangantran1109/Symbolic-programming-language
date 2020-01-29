import nltk
import urllib
import bs4
from bs4 import BeautifulSoup
from collections import defaultdict

#python -m unittest -vhw10_crawling/test_analysis.py
from nltk.corpus import stopwords


def get_html(url):
    return urllib.request.urlopen(url).read().decode("utf-8")

def get_text(html):
    #TODO create the list of clean paragraphs (no HTML markup) from the given html
    #TODO return paragraphs as a string. Hint: join the list of paragraphs by newline
    soup = BeautifulSoup(html, "html.parser")
    text = [i.get_text() for i in soup.find_all('p')]
    return ('\n').join(text)

    

def get_headline(html):
    #TODO return the headline of html
    soup = BeautifulSoup(html,"html.parser")
    return soup.find('h1').get_text()

def get_normalized_tokens(text):
    #TODO tokenize the text with NLTK and return list of lower case tokens without stopwords
    stop_words = set(stopwords.words('english'))
    word_tokens = nltk.word_tokenize(text.lower())
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence


def get_pos_dict(tokens):
    #TODO return a dictionary of homographs (a dictionary of words and their possible POS)
    #return nltk.pos_tag(tokens)
    d = defaultdict(set)
    pos_tag = nltk.pos_tag(tokens)
    for k, v in pos_tag:
        d[k].add(v)
    return d
def filter_dict_homographs(word_dict_h):
    #TODO delete an entry from dictionary, if not a homograph
    homographs = dict((w, tags) for w, tags in word_dict_h.items() if len(tags) > 1)
    return homographs

def find_homographs(tokens):
    #TODO return a dictionary which holds homographs'''
    pos_dict = get_pos_dict(tokens)
    return filter_dict_homographs(pos_dict)

