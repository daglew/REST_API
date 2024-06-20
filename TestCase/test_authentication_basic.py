import requests
from requests.auth import HTTPBasicAuth


def test_authentication():
    response = requests.get('https://github.com/user', HTTPBasicAuth(''))
    print(response.text)






