import requests
import json

servers=json.loads(requests.get('https://api.single-developers.software/servers').content)
for server in servers:
    id=str(server)
    ip=servers[str(server)]['ip']
    location=servers[str(server)]['location']
    emoji=servers[str(server)]['emoji']
    print(
f"""◇ Server ID : {id}
◇ Server Host : {ip}
◇ Server Location : {emoji} {location} {emoji}
""")
serverid=input('Server ID : ')

server=json.loads(requests.get(f'https://api.single-developers.software/servers?id={serverid}').content)
status=requests.get(f'https://api.single-developers.software/servers?status={serverid}').content
ip=server['ip']
location=server['location']
emoji=server['emoji']
print(
f"""
◇ Server ID : {serverid}
◇ Server Host : {ip}
◇ Server Location : {emoji} {location} {emoji}
◇ Server Status : {str(status)}"""
)

username=input('User Name : ')
password=input('Password : ')

ssh=serverid+'$'+username+'$'+password
ssh_result=requests.get(f'https://api.single-developers.software/create?ssh={str(ssh)}').content
try:
    json_ssh=json.loads(ssh_result)
    user_name=json_ssh['username']
    passwd=json_ssh['password']
    port=json_ssh['port']
    ex_date=json_ssh['ex_date']
    login=json_ssh['login']
    print(
f"""
◇ Server Location : {emoji} {location} {emoji}
◇ Server Host : {ip}
◇ SSL Port : {port}
◇ User Name : {user_name}
◇ Password : {passwd}
◇ Expire Date : {ex_date}
◇ Login : {login}
<  https://t.me/SingleDevelopers  />"""
)
except:
    print(ssh_result)
