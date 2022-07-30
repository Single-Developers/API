import requests

API = 'https://api.single-developers.software/tiktok?url='

req = requests.get(API+input('◇ TikTok URL :- ')).json()

print('◇ Downloading No Watermark Video....')

with open("no_watermark.mp4", "wb") as handle:
    for data in requests.get(req['no_watermark'], stream=True).iter_content():
        handle.write(data)
        
print('◇ Downloading Watermark Video....')
     
with open("watermark.mp4", "wb") as handle:
    for data in requests.get(req['watermark'], stream=True).iter_content():
        handle.write(data)

print('◇ Download Completed !!!')
