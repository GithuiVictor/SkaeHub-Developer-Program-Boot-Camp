import requests
from requests.api import request

response = requests.get('https://www.delish.com/cooking/menus/')
print('The Response is: \n', response.text)

print("\nTHe Content: \n", response.content)

filtered_response = requests.get('https://api.github.com/eventts', stream = True)
print('\nRaw Data: \n', filtered_response.raw)
print('\nRaw Data: \n', filtered_response.raw.read(10))