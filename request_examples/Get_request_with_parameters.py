import requests

parameter = {'name': 'kasia', 'email': 'kasiabasia@gmail.com', 'number': '+48123456789'}

response = requests.get('https://httpbin.org/get', params=parameter)

print(response.text)
