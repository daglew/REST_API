import json

import jsonpath
import requests

api_url = "https://reqres.in/api/users/2"


file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\user_create.json', 'r')
input_json = file.read()
json_requests = json.loads(input_json)

response = requests.put(api_url, json_requests)

assert response.status_code == 200

response_json = json.loads(response.text)
updated = jsonpath.jsonpath(response_json, 'updatedAt')

print(updated[0])
