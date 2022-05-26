import json
import requests

api_death = 'https://www.breakingbadapi.com/api/deaths'
my_info = requests.get(api_death)
deaths_lst = json.loads(my_info.text)

api_episodes = 'https://www.breakingbadapi.com/api/episodes'
my_info_2 = requests.get(api_episodes)
episodes_lst = json.loads(my_info_2.text)

max_deaths = max(map(lambda item: item.get('number_of_deaths'), deaths_lst))

season_episode = ((elem.get('season'), elem.get('episode'), elem.get('death')) for elem in deaths_lst
                  if elem.get('number_of_deaths') == max_deaths)
season_tup = tuple(season_episode)

season = str(season_tup[0][0])
episode = str(season_tup[0][1])
death = str(season_tup[0][2])

episode_id_gen = (i_elem.get('episode_id') for i_elem in episodes_lst
              if i_elem.get('season') == season and i_elem.get('episode') == episode)

episode_id = tuple(episode_id_gen)[0]

print('Эпизод сериала с наибольшим количеством смертей:\n'
      'ID эпизода: {}, Сезон: {}, Эпизод: {}, Кол-во смертей в эпизоде: {}\n'
      'Список погибших: {}'
      .format(episode_id, season, episode, max_deaths, death))

result = dict()
result['episode_id'] = episode_id
result['season'] = season
result['episode'] = episode
result['max_deaths'] = max_deaths
result['death'] = death

with open('result_file.json', 'w') as file:
    json.dump(result, file, indent=4)
