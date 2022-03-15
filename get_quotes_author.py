#!/usr/bin/env python3

import requests
import bs4

base_url = "https://quotes.toscrape.com/page/{}/"

authors = set()
quotations = []

for page_num in range(1,2):
    page = requests.get(base_url.format(page_num))
    soup = bs4.BeautifulSoup(page.text,'lxml')

    boxes = soup.select(".quote")    #selected all the quotes boxes
    for box in boxes:
        author = box.select('span')[1].select('small')[0].getText()
        quotation = box.select('span')[0].getText()

        authors.add(author)
        quotations.append(quotation)


print("Authors are: ")
print(authors)
print('\n')
print("Quotations are: ")
print(quotations)
print('\n')

top10 = soup.select(".tag-item")
for i in range(10   ):
    print(top10[i].select('a')[0].getText())


