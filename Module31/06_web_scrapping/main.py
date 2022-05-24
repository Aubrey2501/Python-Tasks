import requests
from bs4 import BeautifulSoup


def get_h4(url):
    info = requests.get(url).content
    soup = BeautifulSoup(info, 'html.parser')
    result = []
    for link in soup.find_all('h3'):
        result.append(link.get_text())
    return result


page = 'http://www.columbia.edu/~fdc/sample.html'
print(get_h4(page))