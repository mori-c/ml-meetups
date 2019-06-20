#! /usr/bin/env python3
# many websites don't allow for web scraping (see site robots.txt)

from bs4 import BeautifulSoup
import random
import urllib.request


def getPusheen(pageNum, x):
    # site will verify the User Agent to prevent abnormal visits, the following is a solution
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"
    opener = AppURLopener()
    url = 'https://pusheen.com/category/comics/page/'+pageNum
     # use AppURLopener instance to handle download of html text
    response = opener.open(url)
    # html text downloaded > BeautifulSoup object
    soup = BeautifulSoup(response, 'html.parser')

    # print(soup) 
   
    print(image)   # feedback check to see url

    # use to check output and compare to browser inspector
    # find html elements in our download (can select CSS, find_all regex, find string)
    #image = soup.find('a', attrs={'class':'rl-gallery-link'}).img['src']
    # copy network object denoted by URL to a local file
    #print(image)
    #opener.retrieve(image, 'stuff/pusheen_'+str(x)+'.gif')
    

pages = [] 

def numGifs(num):
     # get requested quantity of unique page numbers
    my_list = list(range(1,28))
    random.shuffle(my_list)
    for x in range(num):
        val = my_list[x]
        pages.append(str(val))

user_input = input ("How many pusheens are desired? ")
try:
   val = int(user_input)
   print("Getting "+ str(val) + " gifs")
   numGifs(val)
   x = 0
   for p in pages:
        x += 1
        getPusheen(p, x)
except ValueError:
   print("That's not an integer")

print("MEOW!")
