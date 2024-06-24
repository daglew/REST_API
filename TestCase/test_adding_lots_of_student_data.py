import requests
import json
import jsonpath


def test_adding_lots_of_student_data():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\create_new_student.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(api_url, json_request)
    print(response.status_code)
    assert response.status_code == 201
    
