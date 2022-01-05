import requests

API = 'https://single-developers.herokuapp.com/logohq?name=%20'

req = requests.post(API)

print(req.history[1].url)
