import requests
import json
import jsonpath


api_url = "https://reqres.in/api/users?page=2"

response = requests.get(api_url)

response_json = json.loads(response.text)
# print(response_json)


for a in range(0, 3):
    first_name = jsonpath.jsonpath(response_json, 'data['+str(a)+'].first_name')
    print((first_name[0]))

