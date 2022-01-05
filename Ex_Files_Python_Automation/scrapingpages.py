import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
count = 1
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_= 'col-lg-4 col-md-6 mb-4')

for item in items:
    itemName = item.find('h4', class_='card-title').text.strip('\n')
    itemPrice = item.find('h5').text
    print('%s) Item Name: %s Price: %s' % (count, itemName, itemPrice))
    count = count + 1

pagination = soup.find('ul', class_='pagination')
pagelinks = pagination.find_all('a', class_='page-link')
urls=[]

for page in pagelinks:
    pageNum = int(page.text) if page.text.isdigit() else None
    if pageNum != None:
        link = page.get('href')
        urls.append(link)

for i in urls:
    response = requests.get(url + i)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_= 'col-lg-4 col-md-6 mb-4')

    for item in items:
        itemName = item.find('h4', class_='card-title').text.strip('\n')
        itemPrice = item.find('h5').text
        print('%s) Item Name: %s Price: %s' % (count, itemName, itemPrice))
        count = count + 1