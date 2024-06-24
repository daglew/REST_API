import requests
from requests.auth import HTTPBasicAuth


def test_authentication():
    response = requests.get('https://github.com/user', autth=HTTPBasicAuth('test.tester.123@interia.pl', 'testowanie.1234'))
    print(response.text)






