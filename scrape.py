import urllib.request
from bs4 import BeautifulSoup as bs

html_page = 'porter_test'

soup = bs(open('porter_test.html'), 'html.parser')

# Item contains each clothing item on the page

products = soup.find_all('li', attrs={'class': "pl-products-item"})

# get each product page & image link

for item in products:
    link = item.find('a').get('href')
    img = item.find('img').get('src')

    print(link)
    print(img, '\n')