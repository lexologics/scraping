import csv
import datetime
import os
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import Counter
from stop_words import get_stop_words

saved_domains = {
    'lexologics.nl': {
        'tag': 'div',
        'class': 'container'
        },
    'joincfe.com': {
        'tag': 'div',
        'class': 'main-container'
        },
    'tim.blog': {
        'tag': 'div',
        'class': 'content-area'
        },
}

def clean_word(word):
    word = word.replace('!', '')
    word = word.replace('?', '')
    word = word.replace('.', '')
    word = word.replace(':', '')
    word = word.replace(';', '')
    word = word.replace(',', '')
    word = word.replace('(', '')
    word = word.replace(')', '')
    word = word.replace('-', '')
    word = word.replace('2', '')
    word = word.replace('3', '')
    word = word.replace('4', '')
    word = word.replace('5', '')
    word = word.replace('""', '')
    return word


def clean_up_words(words):
    new_words = []
    pkg_stop_words = get_stop_words('en')
    # print(pkg_stop_words)
    my_stop_words = ['the', 'is', 'and']
    for word in words:
        word = word.lower()
        cleaned_word = clean_word(word)
        if word in my_stop_words or word in pkg_stop_words:
            pass
        else:
            new_words.append(cleaned_word)
    return new_words


def fetch_url(url):
    '''
    Request package 1 time
    '''
    response = requests.Response()
    try:
        response = requests.get(url)
        #print(dir(response))
        #print(response.__class__)
    except requests.exceptions.ConnectionError:
        #raise ValueError('Invalid connection')
        print('Invalid connection')
    return response


def validate_url(url):
    http_regex = r'^https?://'  # https or http
    pattern = re.compile(http_regex)
    is_a_match = pattern.match(url)  # regex match or None
    if is_a_match is None:
        raise ValueError('This url does not start with http:// or https://')
    return url


def get_input():
    url = input('What is your url? ')
    if url == 'q':
        return end_program()
    url = append_hhtp(url)
    try:
        validate_url(url)
    except ValueError as err:
        print(err)
        print('(Type "q" to quit)')
        return get_input()
    return url


def append_hhtp(url):
    if not url.startswith('http'):
        return f'http://{url}'
    return url

def soupify(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup    


def get_domain_name(url):
    return urlparse(url).netloc


def get_url_lookup_class(url):
    domain_name = get_domain_name(url)
    lookup_class = {}
    if domain_name in saved_domains:
        lookup_class = saved_domains[domain_name]
    return lookup_class
        

def get_content_data(soup, url):
    lookup_dict = get_url_lookup_class(url)
    if lookup_dict is None:
        return soup.find('body').text
    return soup.find(lookup_dict['tag'], {'class': lookup_dict['class']})


def end_program():
    raise KeyboardInterrupt('Program forced to quit')


def main():
    url = get_input()
    response = fetch_url(url)
    #print(response.status_code)
    if response.status_code not in range(200, 299):
        print(f'code: {response.status_code} - Invalid request, you do not have permission to view this.')
        return None
    response_html = response.text
    #print(response_html)
    soup = soupify(response_html)
    html_text = get_content_data(soup, url)
    print(html_text)


main()

