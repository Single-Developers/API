import requests

API = 'https://single-developers.herokuapp.com/wallpaper?search='

req = requests.post(API+input('Search : ').replace(' ','%20'))

print(req.history[1].url)
