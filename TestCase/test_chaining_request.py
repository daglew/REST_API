import json
import jsonpath
import requests


def new_student_add():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:/Users/dagle/OneDrive/Dokumenty/API/student_add.json')
    json_request = json.loads(file.read())
    response = requests.post(api_url, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])


def test_details_get():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"+str(id[0])
    response = requests.get(api_url)
    print(response.text)



