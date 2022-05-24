import requests
import json

web_page = 'http://www.columbia.edu/~fdc/sample.html'

info = requests.get(web_page)
my_json = json.loads(info.text)

with open('test.json', 'w') as file:
    json.dump(my_json, file, indent=4)