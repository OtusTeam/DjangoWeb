import pprint
import requests

url = 'http://127.0.0.1:8000/api/shop/categories/'

response = requests.get(url)

pprint.pprint(response.json())

headers = {
    'Accept': 'application/json; version=v2'
}

response = requests.get(url, headers=headers)

pprint.pprint(response.json())

response = requests.get(url + '?version=v2', headers=headers)

pprint.pprint(response.json())