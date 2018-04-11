from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import sys

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):

    # This is a function that is inside HTMLParser
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # join root link and abstract link
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]

    # This is a new function that we are creating to get links
    # that our spider() function will call
    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return self.links
        else:
            return []

# using BFS to
def spider(url, maxPages = sys.maxsize):
    pagesToVisit = [url]
    numberVisited = 0
    visitedlinks = set()
    while numberVisited < maxPages and pagesToVisit != []:
        numberVisited = numberVisited +1
        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        visitedlinks.add(url)
        try:
            print(numberVisited, "Visiting:", url)
            parser = LinkParser()
            links = parser.getLinks(url)
            pagesToVisit = pagesToVisit + links
            # print(pagesToVisit)
            print(" **Success!**")
        except:
            print(" **Failed!**")
    return visitedlinks

links = spider("https://www.dreamhost.com", 22)
print(links)