'''
urllib - consists of 5 modules

request: open URLs
response: (used internally)
error: request exceptions
parse: useful URL functions
robotparser: robots.txt files
'''

from urllib.request import Request, urlopen
#from bs4 import BeautifulSoup
import requests
from requests_html import HTML

url = ('https://www.lexologics.nl/logics')

req = Request(url)   # , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req,
    cafile="./venv/lib/python3.9/site-packages/certifi/cacert.pem",
    capath="./venv/lib/python3.9/site-packages/certifi/"
).read().decode(),

print(webpage)
#html_text = HTML(html=webpage)
#print(html_text)
