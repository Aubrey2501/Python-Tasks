import re
from functools import partial
from bot import bot
from api_utils import api_requests, find_city, find_hotels, find_photo
from config_utils.config import MAX_HOTELS_COUNT, MAX_PHOTOS_COUNT, MESSAGES
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
import datetime




def is_cancel(message: Message):
    if message.text == '/cancel':
        bot.reply_to(message, MESSAGES['cancel'])
        return True
    return False


@bot.message_handler(commands=['lowprice'])
def cmd_lowprice(message: Message):
    bot.reply_to(message, MESSAGES['lowprice'])
    bot.register_next_step_handler(message, get_city)


def get_city(message: Message):
    if is_cancel(message):
        return

    city = message.text
    cities = []
    cities = find_city.get_cities(city)
    if not cities:
        bot.reply_to(message, MESSAGES['cities_error'])
        bot.register_next_step_handler(message, get_city)

    else:
        markup = InlineKeyboardMarkup(row_width=1)
        for city in cities:
            markup.add(
                InlineKeyboardButton(text=city['city_name'], callback_data=f'choose_city$${city["city_id"]}')
            )
        bot.send_message(message.chat.id, MESSAGES['success_cities'], reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data.startswith('choose_city'))
def choose_city(callback: CallbackQuery):
    city_id = callback.data.split('$$')[1]

    print('city_id', city_id)

    bot.send_message(callback.from_user.id, MESSAGES['get_start_date'])
    bot.register_next_step_handler_by_chat_id(callback.from_user.id, partial(get_start_date, city_id))


def get_start_date(city_id: str, message: Message):
    if is_cancel(message):
        return

    try:
        start_date = datetime.datetime.strptime(message.text, '%d/%m/%Y').date()
        bot.reply_to(message, MESSAGES['get_end_date'])
        bot.register_next_step_handler(
            message, partial(get_end_date, city_id, start_date))

    except ValueError:
        bot.reply_to(message, MESSAGES['get_date_error'])
        bot.register_next_step_handler(
            message, partial(get_start_date, city_id))


def get_end_date(city_id: str, start_date, message: Message):
    if is_cancel(message):
        return

    try:
        end_date = datetime.datetime.strptime(message.text, '%d/%m/%Y').date()
        if end_date <= start_date:
            raise ValueError
        dates = (start_date, end_date)
        print()
        bot.reply_to(message, MESSAGES['get_adults_count'])
        bot.register_next_step_handler(
            message, partial(get_adults_count, city_id, dates))

    except ValueError:
        bot.reply_to(message, MESSAGES['get_date_error'])
        bot.register_next_step_handler(
            message, partial(get_end_date, city_id, start_date))


def get_adults_count(city_id: str, dates: tuple, message: Message):
    if is_cancel(message):
        return

    try:
        adults = int(message.text)
        if adults > 3:
            raise ValueError()
        bot.reply_to(message, MESSAGES['get_children_age'])
        bot.register_next_step_handler(
            message, partial(get_children_age, city_id, dates, adults))

    except ValueError:
        bot.reply_to(message, MESSAGES['adults_count_error'])
        bot.register_next_step_handler(message, partial(get_adults_count, city_id, dates))


def get_children_age(city_id: str, dates: tuple, adults: int, message: Message):
    if is_cancel(message):
        return

    try:
        children = message.text
        if children == '0':
            children = None
        else:
            children_lst = children.split(',')
            for i_child in children_lst:
                if int(i_child) > 13:
                    raise ValueError()

        bot.reply_to(message, MESSAGES['get_hotels_count'])
        bot.register_next_step_handler(
            message, partial(get_hotels_count, city_id, dates, adults, children))

    except ValueError:
        bot.reply_to(message, MESSAGES['children_age_error'])
        bot.register_next_step_handler(message, partial(get_adults_count, city_id, dates))


def get_hotels_count(city_id: str, dates: tuple, adults: int, children: str, message: Message):
    if is_cancel(message):
        return

    try:
        hotels_count = int(message.text)
        if hotels_count > MAX_HOTELS_COUNT:
            raise ValueError()
        bot.reply_to(message, MESSAGES['get_photo_count'])
        bot.register_next_step_handler(message, partial(get_photos_count, city_id, dates, adults,
                                                        children, hotels_count))

    except ValueError:
        bot.reply_to(message, MESSAGES['hotels_count_error'])
        bot.register_next_step_handler(message, partial(get_hotels_count, city_id, dates, adults, children))


def get_photos_count(city_id: str, dates: tuple, adults: int, children: str, hotels_count: int, message: Message):
    if is_cancel(message):
        return

    try:
        photos_count = int(message.text)
        if photos_count > MAX_PHOTOS_COUNT:
            raise ValueError()

        bot.reply_to(message, MESSAGES['get_currency'])
        bot.register_next_step_handler(
            message, partial(get_currency, city_id, dates, adults, children, hotels_count, photos_count))
    except ValueError:
        bot.reply_to(message, MESSAGES['photos_count_error'])
        bot.register_next_step_handler(
            message, partial(get_photos_count, city_id, dates, adults, children, hotels_count))


def get_currency(city_id: str, dates: tuple, adults: int, children: str, hotels_count: int, photos_count: int,
                 message: Message):
    if is_cancel(message):
        return

    currency = message.text
    pattern = r'[A-Za-z]{3}\b'
    if re.match(pattern, currency):
        currency = currency.upper()
        bot.send_message(message.chat.id, 'Все данные введены верно, пробуем подобрать отели')
        get_lowprices(city_id, dates, adults, children, hotels_count, photos_count, currency, message)
    else:
        bot.reply_to(message, MESSAGES['currency_error'])
        bot.register_next_step_handler(
            message, partial(get_currency, city_id, dates, adults, children, hotels_count, photos_count))


def get_lowprices(city_id: str, dates: tuple, adults: int, children: str, hotels_count: int, photos_count: int,
                  currency: str, message: Message):
    sort_order = "PRICE_LOW_TO_HIGH"
    print(f'Модуль find_hotels \n'
          f'city_id: {city_id}, date1: {str(dates[0])}, date2: {str(dates[1])}, adults: {adults}, children: {children},'
          f'\nhotels_count: {hotels_count}, photos_count: {photos_count}, currency: {currency}, sort_order: {sort_order}')

    hotels = find_hotels.get_hotels(city_id, dates, adults, children, hotels_count, photos_count, currency, sort_order)
    if hotels:
        bot.send_message(message.chat.id, 'Подобрали для вас следующие отели:')
        # вывод отелей
        markup = InlineKeyboardMarkup(row_width=1)

        for hotel in hotels:
            try:
                button_text = f"{hotel['name']}, {int(hotel['starRating'])}\U00002605, " \
                              f"{hotel['ratePlan']['price']['current']} /сут."
            except KeyError:
                button_text = f"{hotel['name']}, {int(hotel['starRating'])}\U00002605, " \
                              f" цена/сут.: н/д"
            markup.add(
                InlineKeyboardButton(text=button_text, callback_data=f'choose_hotel$${hotel["id"]}')
            )
        bot.send_message(message.chat.id, MESSAGES['success_hotels'], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, MESSAGES['request_problem'])
        return

    @bot.callback_query_handler(lambda x: x.data.startswith('choose_hotel'))
    def choose_hotel(callback: CallbackQuery):
        hotel_id = callback.data.split('$$')[1]
        print('hotel_id:', hotel_id)
        bot.send_message(message.chat.id, 'Загружаем данные...')

        print(f'Вызываем модуль find_photos с параметрами: {hotel_id}')
        photos = find_photo.get_photos(hotel_id, photos_count)
        media = []
        for photo in photos:
            media.append(InputMediaPhoto(photo))

        caption = ''

        for hotel in hotels:
            if hotel['id'] == int(hotel_id):
                caption = f"{hotel['name']}, {int(hotel['starRating'])}\U00002605, " \
                          f"\n{hotel.get('address', {}).get('streetAddress', None)} \n" \
                          f"Рейтинг: {hotel.get('guestReviews', {}).get('unformattedRating', 'н/д')}/10"


                rate = f"\n{hotel.get('ratePlan', {}).get('price', {}).get('current', None)} /сут."
                if rate:
                        caption += rate

                landmarks = hotel.get('landmarks', None)
                if landmarks:
                    points = "\nБлижайшие места:"
                    for landmark in landmarks:
                        label = landmark['label']
                        distance = landmark['distance']
                        point = f"\n{label}, расстояние: {distance}"
                        points += point
                    caption += points

                # link = hotel.get('optimizedThumbUrls', {}).get('srpDesktop', None)
                # if link:
                #     caption += f'\n{link}'

                # lat = hotel['coordinate']['lat']
                # lon = hotel['coordinate']['lat']
                # print("Координаты:", lat, lon)

                break

        # media.append(caption)
        bot.send_message(message.chat.id, caption)
        bot.send_media_group(message.from_user.id, media)
        # bot.send_location(message.chat.id, latitude=lat, longitude=lon)

    pass
# выводим
