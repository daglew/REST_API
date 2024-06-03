import requests

headers_data = {'T1': 'First_Header', 'T2': 'Second_Header'}
response = requests.get("https://httpbin.org/get", headers=headers_data)
print(response.text)


