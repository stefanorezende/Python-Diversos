import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/deal/9eff2d9c?ref=dlx_deals_gd_dcl_img_15_9eff2d9c_dt_sl15_72'
count = 1
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
lista = soup.find('ul', class_= 'a-unordered-list a-nostyle a-horizontal a-spacing-none')

items= lista.find_all('li')

for item in items:
    itemName = item.find('a', class_= 'a-size-base a-color-base a-link-normal a-text-normal').text.strip('\n ')
    itemPriceWhole = item.find('span', class_='a-price-whole').text
    itemPriceFraction = item.find('span', class_='a-price-fraction').text
    print('%s) Item Name: %s Price: R$ %s%s' % (count, itemName, itemPriceWhole, itemPriceFraction))
    count = count+1


pagination = soup.find('ul', class_='a-pagination')
pagelinks = pagination.find_all('a')
urls=[]

for page in pagelinks:
    pageNum = int(page.text) if page.text.isdigit() else None
    if pageNum != None:
        link = page.get('href')
        urls.append(link)

for i in urls:
    response = requests.get(url + i)
    soup = BeautifulSoup(response.text, 'lxml')
    lista = soup.find('ul', class_= 'a-unordered-list a-nostyle a-horizontal a-spacing-none')

    items= lista.find_all('li')

    for item in items:
        itemName = item.find('a', class_= 'a-size-base a-color-base a-link-normal a-text-normal').text.strip('\n ')
        itemPriceWhole = item.find('span', class_='a-price-whole').text
        itemPriceFraction = item.find('span', class_='a-price-fraction').text
        print('%s) Item Name: %s Price: R$ %s%s' % (count, itemName, itemPriceWhole, itemPriceFraction))
        count = count+1