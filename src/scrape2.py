import csv
import datetime
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import Counter 
from stop_words import get_stop_words

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
    #print(pkg_stop_words)
    my_stop_words = ['the', 'is', 'and']
    for word in words:
        word = word.lower()
        cleaned_word = clean_word(word)
        if word in my_stop_words or word in pkg_stop_words:
            pass
        else:
            new_words.append(cleaned_word)
    return new_words

def create_csv_path(csv_path):
    if not os.path.exists(csv_path):
        with open(csv_path, 'w') as csvfile:
            header_columns = ['word', 'count', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=header_columns)
            writer.writeheader() 


static_url = 'https://www.lexologics.nl/logics'
my_url = input('Enter the URL to scrape (or press enter for default): ')
my_html_tag = input('Enter the HTML tag for scraping (or press enter for <body>): ')
my_div_class_tag = ''

if not my_url:
    my_url = static_url
if not my_html_tag:
    my_html_tag = 'body'
elif my_html_tag == 'div':
    my_div_class_tag = input('Which class: ')

print(f'Grabbing {my_url} ...')
domain = urlparse(my_url).netloc
print('via domain', domain)

response = requests.get(my_url)

print("Status is:", response.status_code)

#if response.status_code == 200:
#    print('Go ahead and scrape')
#else:
#    print("You can't scrape this", response.status_code)

if response.status_code != 200:
    print("You can't scrape this", response.status_code)
else:
    print(f'Scraping {my_url}...', response.status_code)
    #print(response.text)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    if my_html_tag == 'body':
        body_ = soup.find('body')  
        print(body_.text)
        print('\nFind', len(body_.text), f'characters in the <{my_html_tag}> tag')
    elif my_html_tag == 'div':
        body_ = soup.find('div', {'class': {my_div_class_tag}}) 
        create_list = list(body_)
        print('\nFind', len(body_), f'object(s) in the list for the <{my_html_tag}> tag')
        
        # Showing 'one' record from tje list
        show = int(input(f'Which record to show 0 / {len(body_)-1}: '))

        if show < int(len(body_)):
            create_list = list(body_)
            print(create_list[show])
        else:
            print('Index out of bound')  

    else:
        body_ = soup.find_all(my_html_tag)
        print('\nFind', len(body_), f'objects in the list for the <{my_html_tag}> tag')
    words = body_.text.split()
    clean_words = clean_up_words(words)
    word_counts = Counter(clean_words)
    print(word_counts.most_common(30))  
    filename = domain.replace('.', '-') + '.csv'
    path = 'csv/' + filename
    time_stamp = datetime.datetime.now()
    create_csv_path(path)
    with open(path, 'a') as csvfile:
            header_columns = ['word', 'count', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=header_columns)
            for word, count in word_counts.most_common(30):
                writer.writerow({
                    'count': count,
                    'word': word,
                    'timestamp': time_stamp
                })
            




