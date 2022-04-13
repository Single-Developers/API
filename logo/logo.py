import requests

API = 'https://host.single-developers.software/logo?name='

req = requests.post(API+input('Name : ').replace(' ','%20'))

print(req.history[1].url)
