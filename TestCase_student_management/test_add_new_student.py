import json
import jsonpath
import requests


def test_add_student():
    api_url = 'https://thetestingworldapi.com/'
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\create_new_student_json', 'r')
    json_request = json.loads(file.read())
    response = requests.get(api_url, json_request)
    print(response.text)



