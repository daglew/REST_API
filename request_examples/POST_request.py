import json
import requests

api_url = "https://reqres.in/api/users"


file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\user_create.json','r')
json_input = file.read()
requests_json = json.loads(json_input)

response = requests.post(api_url, requests_json)
print(response.content)

