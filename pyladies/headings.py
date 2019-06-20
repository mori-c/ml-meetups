from bs4 import BeautifulSoup
import requests, regex

def getHeading(sites, topic):
    headings = []
    # links = []
    def getTopThree(site):
        x = 0
        reponse = requests.get(site)
        response.raise_for_status()
        content = BeautifulSoup(response.content, 'html.parser')
        
        hs = content.find_all(regex.compile('^h[1-2]'))
        for h in hs:
            if h.a is not None:
                h1 = h.a.text.strip()
                if topic in h1.lower():
                    x += 1
                    headings.append(h1)
                    # links.append(h.encode('utf-8).decode('ascii', 'ingore').strip())
                    if x == 10:
                        # return (headings, links)
                        return headings
        for site in sites:
            getTopThree
            # return (headings, links)
            return headings

    # def main[]:    
    def test(site, topic):
        reponse = requests.get(site)
        content = BeautifulSoup(response.content, 'html.parser')
        hs = content.find_all('h1')
        return hs
    
    topic = input ('Please enter search topic: ').lower()
    
    rd = 'https://www.reddit.com/r/'+topic
    gphy = 'https://giphy.com/search/'+topic
    sites = [gphy, rd]
    
    # this can be commented out and pasted 
    headings = getHeading(site, topic)
    for h in headings:
        print(h)