import requests

baseUrl = 'https://api.openweathermap.org/data/2.5/weather?'
parameters = {'q': 'Seattle,US', 'APPID': 'b39add481b5b9f4353d9507747e0a8ff'}
response = requests.get(baseUrl, params=parameters)
print(response.content)

