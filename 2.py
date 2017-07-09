# import pandas
import json
import urllib.request

# data = pandas.read_json('C:/Users/sun/python/2-1.json')
response = urllib.request.urlopen('file:///C:/Users/sun/python/2-2.json')

jsonString = response.read()

jsonObject = json.loads(jsonString.decode())

jsonObject['employees']
jsonObject['employees'][0]
jsonObject['employees'][0]['lastName']

response.close()
