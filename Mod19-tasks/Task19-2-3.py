def histogramm(string):
    hist = dict()
    for sym in string:
        if sym in hist:
            hist[sym] += 1
        else:
            hist[sym] = 1

    print('Гистограмма:')
    for i_sym in sorted(hist.keys()):
        print(i_sym, ':', hist[i_sym])
    print('Максимальная частота:', max(hist.values()))

text = input('Введите текст: ').lower()
histogramm(text)

