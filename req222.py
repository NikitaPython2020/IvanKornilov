import requests

r = requests.get('https://api.vk.com/method/users.get?user_id=1&fields=bdate&v=5.52')

print(r)
