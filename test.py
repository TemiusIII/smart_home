import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re

link_of_srch = search(input() + ' википедия', num_results=0)
print(link_of_srch)
html_text = requests.get(link_of_srch[0]).text
soop = BeautifulSoup(html_text, 'html.parser')
info = soop.find('p').get_text().split('.')[0]
print(info[:info.find('(')-1] + info[info.find(')')+1:])