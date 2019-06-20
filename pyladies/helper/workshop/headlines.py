#! /usr/bin/env python3
# go to sites' search url and find latest 3 story headings in results

from bs4 import BeautifulSoup
import requests, regex

def getHeading(sites, topic):
    headings = []
    def getTopThree(site):
        x = 0
        # use requests to handle download of html text
        response = requests.get(site)
        response.raise_for_status()  # download issue will interrupt program, check request status
        # html text downloaded > BeautifulSoup object
        content = BeautifulSoup(response.content, 'html.parser')
        # find html elements in our download (can select CSS, find_all tags, find by string)
        # find all content with h1 and h2 tags using regular expression > list
        # ^h means find all tags that start with the letter h, the number value following can be 1 or 2
        hs = content.find_all(regex.compile('^h[1-2]'))
        for h in hs:
            # get text within link, remove extra white space
            if h.a is not None:
                h1 = h.a.text.strip()
                # make sure heading is about topic
                if topic in h1.lower():
                    x +=1
                    headings.append(h1)
                    if x == 3:
                        return headings
    for site in sites:
        getTopThree(site)
    return headings

def test(site, topic):
    response = requests.get(site)
    content = BeautifulSoup(response.content, 'html.parser')
    hs = content.find_all('h1')
    return hs

topic = input ("Please enter search topic:  ").lower()

bp = "https://www.boredpanda.com/?s="+topic
gz = "https://gizmodo.com/tag/"+topic
bbc = "https://www.bbc.co.uk/search?q="+topic
sites = [gz, bp, bbc]

#headings = test(gz, topic)
headings = getHeading(sites, topic)
for h in headings:
    print(h)

