# results_num = 9
#
# results = {
#     'Jack': [(69485, 1), (95715, 6)],
#     'qwerty': [(95715, 2), (197128, 5)],
#     'Alex': [(95715, 3), (93289, 7), (95715, 8)],
#     'M': [(83647, 4), (95715, 9)]
#     }

results = dict()
results_num = int(input('Сколько записей вносится в протокол?: '))
for i in range(results_num):
    while True:
        print(i + 1, 'запись:', end=' ')
        string = input()
        i_score, i_nickname = string.split()
        if i_score.isdigit():
            break
        else:
            print('Ошибка ввода! Повторите.')

    if i_nickname in results:
        i_data = (int(i_score), i + 1)
        results[i_nickname].append(i_data)
    else:
        results[i_nickname] = [(int(i_score), i + 1)]
print(results)

dict_res = dict()
for i_nickname in results:
   max_score = min_try = 0
   for i_data in results[i_nickname]:
        (i_score, i_try) = i_data
        if i_score > max_score:
            max_score = i_score
            min_try = i_try
        elif i_score == max_score and i_try < min_try:
            min_try = i_try
   dict_res[(max_score, results_num - min_try)] = i_nickname

i_place = 0
for i_data in sorted(dict_res, reverse=True)[0:3]:
    i_place += 1
    print(i_place, 'место:', dict_res[i_data], i_data[0])





