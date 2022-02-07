# TODO здесь писать код
def histogramm(string):
    hist = dict()
    for sym in string:
        if sym in hist:
            hist[sym] += 1
        else:
            hist[sym] = 1

    print('Оригинальный словарь частот:')
    for i_sym in sorted(hist.keys()):
        print(i_sym, ':', hist[i_sym])
    return hist

text = input('Введите текст: ').lower()
hist = histogramm(text)

hist_inv = dict()
print('\nИнвертированный словарь частот:')

for i_key in range(min(hist.values()), max(hist.values()) + 1):
    hist_inv[i_key] = [i_sym for i_sym in hist.keys() if hist[i_sym] == i_key]
    print(i_key, ':', hist_inv[i_key])


