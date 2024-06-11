import json

import jsonpath
import requests

api_url = "https://reqres.in/api/users"


file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\user_create.json', 'r')

input_json = file.read()
json_requests = json.loads(input_json)

response = requests.post(api_url, json_requests)

assert response.status_code == 201

print(response.headers.get('Content-Length'))

response_json = json.loads(response.text)

id = jsonpath.jsonpath(response_json, 'id')

print(id[0])

