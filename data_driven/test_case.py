import json
import jsonpath
import openpyxl
from data_driven import library
import requests


def test_add_multiple_students():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\create_new_student.json')
    json_request = json.loads(file.read())

    obj = library.Common('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\table2.xlsx')
    col = obj.fetch_column_count()
    row = obj.fetch_column_count()
    key_list = obj.fetch_key_names()

    for i in range(2, row+1):
        updated_json_request = obj.update_request_with_data(i, json_request, key_list)
        response = requests.post(api_url, updated_json_request)
        print(response)

