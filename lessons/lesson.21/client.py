import pprint
import requests
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:8000/api/shop/categories/'

response = requests.get(url)

print(response.status_code)
print(response.json())

username = 'admin'
password = 'admin'

# basic = HTTPBasicAuth(username, password)
# response = requests.get(url, auth=basic)

pare = f'{username}:{password}'  # base 64
pare = 'YWRtaW46YWRtaW4='

headers = {
    'Authorization' : f'Basic {pare}'
}

response = requests.get(url, headers=headers)

print(response.status_code)  # 200
pprint.pprint(response.json())


url = 'http://127.0.0.1:8000/api/shop/categories/'

response = requests.get(url)

print(response.status_code)

token = 'e61a587ec537ae8148fc7a10cd1a7580d8e9ab57'

headers = {
    'Authorization' : f'Token {token}'
}

response = requests.get(url, headers=headers)

print(response.status_code)  # 200
pprint.pprint(response.json())


