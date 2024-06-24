import json
import jsonpath
import requests


def test_add_data_student():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\create_new_student.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(api_url, json_request)
    print(response.text)


def test_update_data_student():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails/10290056'
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\create_new_student.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(api_url, json_request)
    print(response.text)


def test_get_data_student():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails/10290056'
    response = requests.get(api_url)
    response_json = response.json()
    print(response_json)
    id = jsonpath.jsonpath(response_json, 'data.id')
    assert id[0] == 10290056


def test_delete_student():
    api_url = 'https://thetestingworldapi.com/help/Api/DELETE-api-studentsDetails-id'
    response = requests.delete(api_url)
    print(response.text)

