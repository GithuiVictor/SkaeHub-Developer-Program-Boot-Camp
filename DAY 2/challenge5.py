import requests

print('timeout = 0.001')
try:
    re = requests.get('https://www.delish.com/cooking/menus/', timeout = 0.001)
    print(re.text)
except requests.exceptions.RequestException as e:
    print(e)

print('\ntimeout = 0.001')
try:
    re = requests.get('https://www.delish.com/cooking/menus/', timeout = 0.001)
    print('Connected...')
except requests.exceptions.RequestException as e:
    print(e)