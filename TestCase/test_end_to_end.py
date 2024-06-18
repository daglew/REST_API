import requests
import json
import jsonpath


def test_add_new_dat():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\create_new_student.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(api_url, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    api_tech_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\api_tech.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post((api_tech_url, json_request))
    print(response.text)

    api_add_url = "https://thetestingworldapi.com/api/addresses"
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\address.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post((api_add_url, json_request))

    final = "https://thetestingworldapi.com/api/FinalStudentDetails/{10290055}"
    requests.get(final)
    print(response.text)
