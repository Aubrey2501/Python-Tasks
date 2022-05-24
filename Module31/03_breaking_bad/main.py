import json
import requests

api = 'https://www.breakingbadapi.com/api/deaths'
my_info = requests.get(api)
my_json = json.loads(my_info.text)


with open('breakingbad.json', 'w') as file:
    json.dump(my_json, file, indent=4)

with open('breakingbad.json', 'r') as file:
    episodes_lst = json.load(file)

max_deaths = max(map(lambda item: item.get('number_of_deaths'), episodes_lst))

for elem in episodes_lst:
    if elem['number_of_deaths'] == max_deaths:
        print('Эпизод сериала с наибольшим количеством смертей:\nСезон: {}, Эпизод: {}, Кол-во смертей в эпизоде: {}'
              .format(elem['season'], elem['episode'], elem['number_of_deaths']))
        break

