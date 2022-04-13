import requests

API = 'https://host.single-developers.software?write='

req = requests.post(API+input('Text : ').replace(' ','%20'))

print(req.history[1].url)
