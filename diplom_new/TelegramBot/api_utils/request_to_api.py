import requests
from requests import HTTPError
from config_utils.config import HEADERS, LOCATIONS_URL


# def api_request(*args): # тут параметры в каком-то виде: город, расстояние, цены, тд.

def request_to_api(url, querystring, headers=HEADERS):
	response = requests.get(url=url, params=querystring, headers=headers, timeout=10)
	try:
		if response.status_code == requests.codes.ok:
			print('Модуль request_to_api отработал нормально')
			return response

	except TimeoutError:
		print('Ошибка таймаута')
		return None
	except HTTPError:
		print(f'Ошибка адреса: {url}. Сервер не отвечает')
		return None


