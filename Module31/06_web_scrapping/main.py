import requests
import re
from bs4 import BeautifulSoup

# TODO Круто, но задачу можно решить через регулярные выражения.
#  Попробуйте написать паттерн, который бы выделять только текст из "h3"
#  То есть есть примерно такая строка - <h3 id="contents">CONTENTS</h3>
#  Из нее нужно достать только текст "CONTENTS" для этого пригодятся скобочные группы
#  И получается что-то вроде - <h3 .*?>(скобочная группа) закрывающий тег h3
def get_h4(url):
    info = requests.get(url).content
    pattern = ['\<h3 id\=\"contents\"\>CONTENTS\<\/h3>']
    elems = re.findall('^(pattern)')


    # soup = BeautifulSoup(info, 'html.parser')
    # result = []
    # for link in soup.find_all('h3'):
    #     result.append(link.get_text())
    # return result


page = 'http://www.columbia.edu/~fdc/sample.html'
print(get_h4(page))












