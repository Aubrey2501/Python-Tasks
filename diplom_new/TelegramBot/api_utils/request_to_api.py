import requests
from requests import HTTPError, ReadTimeout
from config_utils.config import HEADERS, LOCATIONS_URL


def request_to_api(url, querystring, headers=HEADERS):
	try:
		response = requests.get(url=url, params=querystring, headers=headers, timeout=10)
		if response.status_code == requests.codes.ok:
			print('Модуль request_to_api отработал нормально')
			return response

	except TimeoutError:
		print('Ошибка таймаута')
		return None

	except ReadTimeout:
		print('Ошибка обращения к API: таймаут')
		return None

	except HTTPError:
		print(f'Ошибка адреса: {url}. Сервер не отвечает')
		return None


