import re
from functools import partial
from bot import bot
from api_utils import api_requests, find_city, find_hotels
from config_utils.config import MAX_HOTELS_COUNT, MAX_PHOTOS_COUNT, MESSAGES
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
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
        # просто вызываем get_lowprices и передаем message
        get_lowprices(city_id, dates, adults, children, hotels_count, photos_count, currency, message)
    else:
        bot.reply_to(message, MESSAGES['currency_error'])
        bot.register_next_step_handler(
            message, partial(get_currency, city_id, dates, adults, children, hotels_count, photos_count))


def get_lowprices(city_id: str, dates: tuple, adults: int, children: str, hotels_count: int, photos_count: int,
                  currency: str, message: Message):
    sort_order = "PRICE_LOWEST_FIRST"
    print(f'Модуль find_hotels \n'
          f'city_id: {city_id}, date1: {str(dates[0])}, date2: {str(dates[1])}, adults: {adults}, children: {children},'
          f'\nhotels_count: {hotels_count}, photos_count: {photos_count}, currency: {currency}, sort_order: {sort_order}')

    hotels = find_hotels.get_hotels(city_id, dates, adults, children, hotels_count, photos_count, currency, sort_order)
    if hotels:
        bot.send_message(message.chat.id, 'Подобрали для вас следующие отели:')

    # вывод отелей
    # for hotel in hotels:

    pass
# выводим
