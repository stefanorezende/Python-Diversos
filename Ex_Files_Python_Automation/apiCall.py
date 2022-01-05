import requests
import json

baseURL ='https://api.upcitemdb.com/prod/trial/lookup'
parameters = [{'upc': '012993441012'}, {'upc': '073366118238'}]
for i in range(0,len(parameters)):
    response = requests.get(baseURL, params=parameters[i])
    print(response.url)

    content = response.content
    info = json.loads(content)
    #print(type(info))
    #print(info)

    item = info['items']
    itemInfo = item[0]
    title = itemInfo ['title']
    brand = itemInfo['brand']

    print(title)
    print(brand)