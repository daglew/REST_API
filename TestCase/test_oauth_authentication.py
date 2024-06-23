import json
import requests
import jsonpath


def test_oath():
    url_token = 'http://thetestingworldapi.com/token'
    data = {'grant_type': 'password', 'username': 'admin', "password": 'adminpass'}
    response = requests.post(url_token, data)
    value_token = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Authorization': 'Bearer' + value_token}
    api_url = 'http://thetestingworldapi.com/api/stdetails/10290055'
    response = requests.get(api_url, headers=auth)
    print(response.text)





