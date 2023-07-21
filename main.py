import requests
import json

baseUrl = "https://api.upcitemdb.com/prod/trial/lookup"
parameters = {'upc': '0885909950805'}

response = requests.get(baseUrl, params=parameters)
print(response.url)
content = response.content
header = response.headers
cookies = response.cookies

info = json.loads(content)
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']

infoFile = 'infoOutput.txt'

with open(infoFile, 'w') as file:
    json.dump(info, file)


print(type(info))






