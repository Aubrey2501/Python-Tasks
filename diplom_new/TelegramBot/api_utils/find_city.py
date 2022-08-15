import json
import re
from api_utils.request_to_api import request_to_api
from config_utils.config import LOCATIONS_URL, HEADERS


def request_city(city):
    querystring = {"query": city, "locale": "en_US", "currency": "USD"}
    return request_to_api(url=LOCATIONS_URL, headers=HEADERS, querystring=querystring)


def get_cities(city):
    response = request_city(city)
    if response:
        pattern = r'(?<="CITY_GROUP",).+?[\]]'
        find = re.search(pattern, response.text)
        cities = list()
        if find:
            suggestions = json.loads(f"{{{find[0]}}}")
            for i_destination in suggestions['entities']:  # Обрабатываем результат
                clear_destination = re.sub("<.*?>", "", i_destination['caption'])
                cities.append({'city_name': clear_destination, 'city_id': i_destination['destinationId']})



        # проверка результата
        print('Модуль find_city:')
        for i_city in cities:
            print(i_city)

        return cities
    else:
        print('find_city module. API does not response')
        return None

