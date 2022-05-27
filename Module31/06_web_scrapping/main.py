import requests
import re


def get_h4(url):
    info = requests.get(url).content

    # with open('test.txt', 'r') as file:
    #     info = file.read()
    result = re.findall(r'<h3 .*?>(.*?)</h3>', str(info))
    return result


page = 'http://www.columbia.edu/~fdc/sample.html'
print(get_h4(page))

# зачет!
