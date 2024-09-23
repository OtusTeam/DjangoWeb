import pprint
import requests
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:8000/api/shop/categories/'

response = requests.get(url)

print(response.status_code)

basic = HTTPBasicAuth('user', 'user')
response = requests.get(url, auth=basic)

print(response.status_code)

response = requests.post(url, auth=basic, data={})

print(response.status_code)

basic = HTTPBasicAuth('manager', 'manager')
response = requests.post(url, auth=basic, data={})

print(response.status_code)
print(response.json())

basic = HTTPBasicAuth('manager', 'manager')
response = requests.delete(url, auth=basic)

print(response.status_code)