import requests

API = 'https://single-developers.herokuapp.com?write='

req = requests.post(API+input('Text : ').replace(' ','%20'))

print(req.history[1].url)
