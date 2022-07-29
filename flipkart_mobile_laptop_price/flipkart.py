import bs4
import requests
import pandas as pd



def fetch_products(item,stars=3):

    df = pd.DataFrame(columns=['Product Name','Price'])

    #base_url valid only for flipkart
    base_url = 'https://www.flipkart.com/search?q={search}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page_no}'

    # search upto starting 10 pages
    pages = 5

    for page_no in range(pages-1):
        request = requests.get(base_url.format(search=item, page_no=page_no))
        soup = bs4.BeautifulSoup(request.text,'lxml')

        products = soup.select('._3pLy-c')  # selecting the products in single page as a list

        for prod_num in range(len(products)):
            rating = float(products[prod_num].select('.col-7-12')[0].select('.gUuXy-')[0].select('._1lRcqv')[0].select('._3LWZlK')[0].getText())
            if rating >= stars:
                prod_name = products[prod_num].select('.col-7-12')[0].select('._4rR01T')[0].getText()
                prod_price = products[prod_num].select('.col-5-12')[0].select('._3tbKJL')[0].select('._25b18c')[0].select('._30jeq3')[0].getText()
                #df = df.append({'Product Name':prod_name,'Price':prod_price}, ignore_index=True)
                df.loc[len(df)] = [prod_name,prod_price]
                
    return df
