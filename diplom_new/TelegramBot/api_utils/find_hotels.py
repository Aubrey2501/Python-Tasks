import json
from api_utils.request_to_api import request_to_api
from config_utils.config import PROPERTIES_URL, HEADERS

def get_hotels(city_id: str, dates: tuple, adults: int, children: str, hotels_count: int, photos_count: int,
               currency: str, sort_order: str):
    response = request_hotels(city_id, dates, adults, children, hotels_count, currency, sort_order)
    if response:
        print('response OK')
        print(response.text)

        data = json.loads(response.text)
        hotels = []
        if data['result'] == 'OK':
            selection = data['data']['body']['searchResults']['results']

            # path = os.path.join('.\\database', 'hotels.json')
            # if not os.path.exists(path):
            #     file = open(path, 'w')
            #     file.close()
            #
            # with open(path, 'w') as file:
            #     json.dump(selection, file, indent=4)
            #
            # with open(path, 'r') as file:
            #     selection = json.load(file)

            for hotel in selection:  # Обрабатываем результат
                hotels.append(hotel)
            # # проверка результата
            print('Модуль get_hotel:')
            for hotel in hotels:
                print(hotel)
            return hotels
        else:
            return None

def request_hotels(city_id: str, dates: tuple, adults: int, children: str, hotels_count: int, currency: str,
                   sort_order: str):
    """Формирование запроса к API"""

    querystring = {"destinationId": city_id, "pageNumber": "1", "pageSize": str(hotels_count), "checkIn": str(dates[0]),
                   "checkOut": str(dates[1]), "adults1": str(adults), "children1": children,
                   "sortOrder": sort_order, "locale": "en_US", "currency": currency}
    return request_to_api(url=PROPERTIES_URL, headers=HEADERS, querystring=querystring)


# test
# city_id = '1693814'
# dates = ('2022-02-20', '2022-03-22')
# adults = 4
# children = '1'
# hotels_count = 10
# photos_count = 5
# currency = 'USD'
# sort_order = 'PRICE_LOWEST_FIRST'
# hotels = get_hotels(city_id, dates, adults, children, hotels_count, photos_count, currency, sort_order)