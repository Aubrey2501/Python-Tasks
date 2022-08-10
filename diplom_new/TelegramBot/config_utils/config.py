import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
RAPID_API_HOST = os.getenv('RAPID_API_HOST')
HEADERS = {"X-RapidAPI-Key": RAPID_API_KEY, "X-RapidAPI-Host": RAPID_API_HOST}
LOCATIONS_URL = "https://hotels4.p.rapidapi.com/locations/v2/search"
PROPERTIES_URL = "https://hotels4.p.rapidapi.com/properties/list"

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('lowprice', "Топ самых дешевых отелей в городе"),
)

MAX_HOTELS_COUNT = 25
MAX_PHOTOS_COUNT = 5

CANCEL_TEXT = '\nДля отмены введите /cancel'

MESSAGES = {
    'start': 'Привет, {0}!\nЧтобы увидеть список команд, введите /help',
    'help': '\n'.join([f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]),
    'cancel': 'Команда отменена.\nЧтобы увидеть список команд, введите /help',
    'lowprice': 'Это поиск самых дешевых отелей.\nДля начала введите город для поиска:' + CANCEL_TEXT,
    'get_hotels_count': 'Введите количество отелей, которое необходимо вывести (не больше {0})'.format(
        MAX_HOTELS_COUNT) + CANCEL_TEXT,
    'cities_error': 'К сожалению, города не найдены. Попробуйте снова.' + CANCEL_TEXT,
    'success_cities': 'Выберете нужный город (район города) из списка',
    'hotels_count_error': 'Количество отелей должно быть числом и меньше {0}'.format(MAX_HOTELS_COUNT),
    'get_photo_count': 'Введите количество фотографий отелей, которое необходимо вывести (не больше {0})'.format(
        MAX_PHOTOS_COUNT) + CANCEL_TEXT,
    'photos_count_error': 'Количество фотографий должно быть числом и меньше {0}'.format(MAX_PHOTOS_COUNT),
    'get_start_date': 'На какие даты будем искать? \nВведите начальную дату (dd/mm/yyyy): ' + CANCEL_TEXT,
    'get_end_date': 'Введите конечную дату (dd/mm/yyyy): ' + CANCEL_TEXT,
    'get_adults_count': 'Сколько взрослых будет проживать в номере?' + CANCEL_TEXT,
    'adults_count_error': 'Количество взрослых должно быть не менее 1 и не более 3 человек',
    'get_children_age': 'Возраст детей (до 13 лет) через запятую (например, 5,11). Если нет, введите "0"' + CANCEL_TEXT,
    'children_age_error': 'Неправильно введены данные. Возраст детей вводится через запятую и не должен'
                            ' превышать 13 лет '
                            '\nЕсли с Вами нет детей, введите "0"' + CANCEL_TEXT,
    'get_date_error': 'Ошибка ввода даты. Попробуйте еще раз' + CANCEL_TEXT,
    'get_currency': 'В какой валюте выводить цены на отели? Валюта по умолчанию USD' + CANCEL_TEXT,
    'currency_error': 'Код валюты должен состоять из трех латинских букв. Попробуйте еще раз'
}
