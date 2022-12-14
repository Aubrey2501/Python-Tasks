LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# это шифр Цезаря, где все символы сдвинуты на позицию влево, плюс в словах поменян порядок слов.

def encrypt(message, key):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            translated = translated + LETTERS[num + key]
        else:
            translated = translated + symbol
    return translated


input_text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

key = int(input('Введите сдвиг: '))  # key = -1

print('Зашифрованный текст: ', input_text)
new_text = encrypt(input_text, key)
print('\nРасшифрованный текст: ', new_text)
# TODO Отлично, но после слова с символом "/" циклический сдвиг увеличивается на один
#  и очередное слово содержит заглавную букву.
#  Самый простой способ - это использовать функции "chr" и "ord"
#  chr - https://pythonz.net/references/named/chr/
#  ord - https://pythonz.net/references/named/ord/
#  Например, слово: vujgvmCfb
#  Смещение: -3
#  Длина слова: 9
#  Расчет смещения от длины: -3 % 9 = 6
#  Соединяем части срезами: слово[6:] и слово[:6] получим Cfbvujgvm
#  В цикле с "chr" и "ord" делаем расшифровку применяя эти функции к буквам:
#  Символ "C" -  chr(ord("C") - 1) получим символ "B"
#  1 действие: ord("C")
#    - получаем числовое представление для указанного символа из таблицы юникода, для данного случая получится 66
#  2 действие: chr(66)
#    - получаем символ (в виде строки), чья позиция кода для юникода равна указанному целому получим символ "B"
#  И если простись циклом по всему тексту используя поочередно эти функции получим слово Beautiful

