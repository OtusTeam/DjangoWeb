import requests


url = 'http://127.0.0.1:8000/api/categories/'

response = requests.get(url)
assert 401 == response.status_code, response.status_code

login = 'user'
password = 'user'
response = requests.get(url, auth=(login, password))
assert 200 == response.status_code, response.status_code

# Получаем токен
data = {
    'username': 'admin',
    'password': 'admin',
}

url = 'http://127.0.0.1:8000/api-token-auth/'
response = requests.post(url, json=data)

print(response.text)
token = response.json()['token']

headers = {
    'Authorization': f'Token {token}'
}

url = 'http://127.0.0.1:8000/api/categories/'

response = requests.get(url, headers=headers)
assert 200 == response.status_code, response.status_code

url = 'http://127.0.0.1:8000/api/animals/'

login = 'user'
password = 'user'
response = requests.get(url, auth=(login, password))
assert 403 == response.status_code, response.status_code

login = 'foodmaster'
password = 'foodmaster'
response = requests.get(url, auth=(login, password))
assert 200 == response.status_code, response.status_code
