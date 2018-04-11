import urllib.request
from bs4 import BeautifulSoup
import re

"""Scan the text for http URLs and return a set
    of URLs found, without duplicates"""
html_page = urllib.request.urlopen("http://www.python.org/")
plain_text = html_page.read()
soup = BeautifulSoup(plain_text, "lxml")