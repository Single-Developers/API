import requests

API = 'https://singledevelopers.com/logohq?name='

req = requests.post(API+input('Name : ').replace(' ','%20'))

print(req.history[1].url)
