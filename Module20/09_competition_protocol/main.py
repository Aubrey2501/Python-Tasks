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

dict_res = dict()
for i_nickname in results:
   max_score = min_try = 0
   for i_score, i_try in results[i_nickname]:
        if i_score > max_score:
            max_score = i_score
            min_try = i_try
        elif i_score == max_score and i_try < min_try:
            min_try = i_try
   dict_res[i_nickname] = (max_score, results_num - min_try)

sorted_tuple = sorted(dict_res.items(), key=lambda x: x[1], reverse=True)
dict_res = dict(sorted_tuple)
fin_list = enumerate(dict_res.keys())

for i, i_nickname in fin_list:
    if i < 3:
        print(i + 1, 'место:', i_nickname, dict_res[i_nickname][0])




