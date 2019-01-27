from BeautifulSoup import BeautifulSoup
import urllib2
import re
import json

JSON = {}

html = urllib2.urlopen("https://www.gartner.com/en/research/magic-quadrant")
soup = BeautifulSoup(html)
for link in soup.findAll('a',attrs={'href': re.compile("^https://www.gartner.com/doc/code/")}):
    linkHTML = link.get('href')
    linkHTML = urllib2.urlopen(linkHTML)
    soup = BeautifulSoup(linkHTML)
    titleTag = soup.find('h1',{"itemprop":"name"})
    Summary = soup.find('p',{"class":"summary"},{"itemprop":"description"})
    if hasattr(Summary,'text') and hasattr(titleTag, 'text'):
            JSON[titleTag.text] = Summary.text

with open('parsed.json', 'w') as fp:
    json.dump(JSON, fp)

