import requests
import json
import jsonpath
import openpyxl


def test_adding_lots_of_student_data():
    api_url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\create_new_student.json')
    json_request = json.loads(file.read())

    wk = openpyxl.load_workbook(('C:\\Users\\dagle\\OneDrive\\Dokumenty\\API\\')

    
