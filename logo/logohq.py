import requests

API = 'https://host.single-developers.software/logohq?name='

req = requests.post(API+input('Name : ').replace(' ','%20'))

print(req.history[1].url)
