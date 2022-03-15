#!/usr/bin/env python3

import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Computer_chess")           #request to the webpage

soup = bs4.BeautifulSoup(result.text,'lxml')         #beautifyig
image = soup.select('.thumbimage')[0]                #selecting the particulr tag/class of the image


image_src = image['src']                              #confirming the source of the image
print(image_src)

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/RS_Chess_Computer.JPG/220px-RS_Chess_Computer.JPG')          #requesting the above image link



file = open('chess.jpg','wb')            #creating a file for saving the image

file.write(image_link.content)            #saving the content of that image
file.close()                              #closing the file