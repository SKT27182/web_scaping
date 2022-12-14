#!/home/shailja/.virtualenv/my_env/bin/python3

import requests
import bs4
import sys

content =  sys.argv[1]


def display_actual_text(text,para_no):
    text = text[para_no]
    [s.extract() for s in text(['style', 'script', '[document]', 'head', 'title'])]
    visible_text = text.getText()
    print(visible_text)

wiki_url = 'https://en.wikipedia.org/wiki/{}'

request = requests.get(wiki_url.format(content))
soup = bs4.BeautifulSoup(request.text,'lxml')
actual_text=soup.select('p')


# this is to handle if wikipedia don't have any article with this name
try:
    display_actual_text(actual_text,1)
except:
    print(f"Wikipedia does not have an article with this exact name.")
    exit(1)
    
    # wiki_url = 'https://en.wikipedia.org/wiki/Special:Search?go=Go&search={}&ns0=1'

    # request = requests.get(wiki_url.format(content))
    # soup = bs4.BeautifulSoup(request.text,'lxml')
    # #relevant_text=soup.select("div", {"id": "bodyContent"})                          #soup.select('#mw-body')
    # #relevant_text=relevant_text.select("div.searchresults")
    # content = soup.select(".mw-search-result")[0].select('td')[1]
    # title=content.a['title']
    # relevant_text=content.select(".searchresult")[0]
    # [s.extract() for s in relevant_text(['style', 'script', '[document]', 'head', 'title'])]
    # visible_text = relevant_text.getText()
    # print(title)
    # print(visible_text)



# for more data 

show_next = False
para_no = 2

# this is to handle if search is found and reaches to the end of content in wikipidea
try:
    while not show_next:
        show_next = input("!")
        print()
        display_actual_text(actual_text,para_no)
        para_no+=1

except:
    print("End")
    


