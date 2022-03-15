#!/usr/bin/env python3

import requests   #to send request to the server
import bs4        #beautify the text

result = requests.get("https://en.wikipedia.org/wiki/Main_Page")    #returns the requests.models.Response type

result.text            #returns the whole html code without formatting


soup = bs4.BeautifulSoup(result.text,'lxml')              #return the class 'bs4.BeautifulSoup'

print(soup.select('h1')[1].getText())           #returns the text inside the h1 heading
