#!/usr/bin/env python3

import requests
import bs4

#...................Get the title of each book which has the rating more than 2 star
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

for page_num in range(1,51):             #itterating through all pages

    request = requests.get(base_url.format(page_num))   #requesting the particular page 
    soup = bs4.BeautifulSoup(request.text,'lxml')

    books = soup.select('.product_pod')        #finding the product_pod class
    #print(books[1])
    #exit(11)
    for book in books:
        if [] != book.select('.star-rating.Two'):    #if a class name conatain a whitespace then cover it by dot(.)

            '''Check that the book has two rating or not
            'star-rating Two' in str(example)'''

            title = book.select('a')[1]['title']   #get the title which is in the form of href after the image's link
            print(title)
