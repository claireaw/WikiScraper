import requests
from bs4 import BeautifulSoup

def search(wikiname, searchtype, pagename):

    page = requests.get('https://en.wikipedia.org/wiki/' + pagename)
    # check if provided url needs to be cleaned
    nameString = "https://" + str(wikiname)
    newSoup = BeautifulSoup(page.content, 'html.parser')
    print(newSoup.prettify())
