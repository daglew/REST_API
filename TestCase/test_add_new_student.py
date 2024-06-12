import json
import jsonpath
import requests


def test_add_data_student():
    api_url = 'https://thetestingworldapi.com/'
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\create_new_student_json', 'r')
    json_request = json.loads(file.read())
    response = requests.get(api_url, json_request)
    print(response.text)


def test_get_data_student():
    api_url = 'https://thetestingworldapi.com/3034'
    response = requests.get(api_url)
    response_json = response.json()
    id = jsonpath.jsonpath(response_json, 'data.id')
    assert id[0] == 3034

