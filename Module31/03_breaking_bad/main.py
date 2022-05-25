import json
import requests

api_death = 'https://www.breakingbadapi.com/api/deaths'
my_info = requests.get(api_death)
deaths_lst = json.loads(my_info.text)

api_episodes = 'https://www.breakingbadapi.com/api/episodes'
my_info_2 = requests.get(api_episodes)
episodes_lst = json.loads(my_info_2.text)

max_deaths = max(map(lambda item: item.get('number_of_deaths'), deaths_lst))

for elem in deaths_lst:
    if elem['number_of_deaths'] == max_deaths:
        season = str(elem['season'])
        episode = str(elem['episode'])
        episode_id = (i_elem['episode_id'] for i_elem in episodes_lst
                      if i_elem['season'] == season and i_elem['episode'] == episode)

        print('Эпизод сериала с наибольшим количеством смертей:\n'
              'ID эпизода: {}, Сезон: {}, Эпизод: {}, Кол-во смертей в эпизоде: {}'
              .format(list(episode_id)[0], season, episode, elem['number_of_deaths']))
        break

