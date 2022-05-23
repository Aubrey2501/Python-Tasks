import json
import functools
import requests

# api = 'https://www.breakingbadapi.com/api/deaths'
# my_info = requests.get(api)
# my_json = json.loads(my_info.text)
#
#
# with open('breakingbad.json', 'w') as file:
#     json.dump( my_json, file, indent=4)

with open('breakingbad.json', 'r') as file:
    lst_dict = json.load(file)
    # print(lst_dict)

sort_lst = sorted(lst_dict, key=lambda x: x.get('season') + x.get('episode'))


print(functools.reduce(lambda count, item: count + item.get('number_of_deaths'), sort_lst, 0))


