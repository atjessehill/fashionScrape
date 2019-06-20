import urllib.request
from bs4 import BeautifulSoup as bs
from os.path import join
from io import StringIO, BytesIO
import base64
from PIL import Image

debug = True
scrape_image_folder_path = 'C:/Users/jesse/Desktop/scrapeImages/'

# https://youtu.be/2Rf01wfbQLk
def download_img(item_name, link):

    path = item_name+'.jpg'
    save_folder = join(scrape_image_folder_path, path)

    if 'gif' not in link:
        urllib.request.urlretrieve(link, save_folder)


def scrape_page(page):

    # if debug:
    #     page = 'porter_test.html'

    # soup = bs(open(page), 'html.parser')
    soup = page
    # Item contains each clothing item on the page

    products = soup.find_all('li', attrs={'class': "pl-products-item"})

    # get each product page & image link

    for item in products:
        link = item.find('a').get('href')
        img = item.find('img').get('src')

        link = link.split('product/')[1]
        link = link.split('/')
        link = '_'.join(link)

        img = 'https:' + img
        download_img(link, img)


def crawl_pages(start_link):

    if debug:
        page = 'porter_test.html'

    page = 'https://www.mrporter.com/en-us/mens/sale/all?pn=1&sortBy=discount'

    done = False
    count = 1

    while not done:
        page = urllib.request.urlopen(page)
        done = True
        soup = bs(page, 'html.parser')

        scrape_page(soup)

        links = soup.find_all('a')
        for i in links:
            if i.string == "Next":
                next_page = i.get('href')
                done = False
                count+=1

                page = 'https://www.mrporter.com'+next_page
                print("Moving to next page", page)
                break

    print(count)

def b64_handle():


    print("handl b64")

    # img = 'data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACwAAAAAAQABAAACAkQBADs='
    # encoded = img.split(',')[1]

    #'data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACwAAAAAAQABAAACAkQBADs='
    # decode = 'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;


    encoded = "see above"
    im = Image.open(BytesIO(base64.b64decode(encoded)))
    im.save('atest.png', 'PNG')

# crawl_pages("test")
