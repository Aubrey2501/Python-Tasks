import json
from api_utils.request_to_api import request_to_api
from config_utils.config import HEADERS, PHOTOS_URL


def get_photos(hotel_id: str, photos_count: int):
    response = request_photos(hotel_id)
    if response:
        print('response OK')
        # print(response.text)

        data = json.loads(response.text)
        photos = []
        selection = data['hotelImages']
        if selection:
            for image in selection:
                photo = image['baseUrl'].replace("{size}", "y")
                photos.append(photo)
                if len(photos) >= photos_count:
                    break
            return photos
        else:
            return None

            # # проверка результата
        # print('Модуль get_photos:')
        # for photo in photos:
        #     print(photo)
        #
        # return photos




def request_photos(hotel_id: str):
    """Формирование запроса к API"""

    querystring = {"id": hotel_id}
    return request_to_api(url=PHOTOS_URL, headers=HEADERS, querystring=querystring)


# test
# hotel_id = '525567'
# photos_count = 5
# dates = ('2022-02-20', '2022-03-22')
# adults = 4
# children = '1'
# hotels_count = 10

# currency = 'USD'
# sort_order = 'PRICE_LOWEST_FIRST'
# hotels = get_photos(hotel_id, photos_count=5)