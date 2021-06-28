# import requests
# import json

# #get URL response
# response = requests.get('https://www.delish.com/cooking/menus/')
# print (response)

# data = dresponse.parseJson()

# #convert response from JSON to dict
# # with open(response) as d:
# #     dictData = json.load(d)
# #     print(d)
# # converted_response = json.dumps(response)
# # print(converted_response)

import urllib.request as request
import json

with request.urlopen('http://data.nba.net/prod/v2/2018/teams.json') as response:
    source = response.read()
    data = json.loads(source)
    print(data)