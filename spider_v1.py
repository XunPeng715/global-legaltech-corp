import urllib.request
from bs4 import BeautifulSoup
import re

"""Scan the text for http URLs and return a set
    of URLs found, without duplicates"""
html_page = urllib.request.urlopen("http://www.python.org/")
plain_text = html_page.read()
soup = BeautifulSoup(plain_text, "lxml")

urlpattern = r"(https?\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/[^<'\";]*)?)"
matches = re.findall(urlpattern, plain_text.decode('utf8'))

links = set()
for match in matches:
    links.add(match[0])

print(links)