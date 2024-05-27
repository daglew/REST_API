import requests

api_url = "https://reqres.in/api/users?page=2"

respone = requests.delete(api_url)

print(respone.status_code)

assert respone.status_code == 204

