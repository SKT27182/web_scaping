#!/usr/bin/env python3

import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Help:Table")

soup = bs4.BeautifulSoup(res.text,'lxml')
table = soup.select('#toc')
for item in table:
	print(item.text)