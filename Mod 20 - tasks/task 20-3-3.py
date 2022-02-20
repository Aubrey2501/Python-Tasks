
def odd_index(x_data):
    # print(x_data)
    list_ind = []
    if not isinstance(x_data, dict):
        list_ind = [value for index, value in enumerate(x_data) if index % 2 == 0]
    else:
        list_ind = [{value: x_data[value]} for index, value in enumerate(x_data) if index % 2 == 0]
    print(list_ind)


data = []
data.append('О Дивный Новый мир!')
data.append([100, 200, 300, 'буква', 0, 2, 'а'])
data.append(('a', 'b', 'c', 'd'))
data.append({'bcad': 1, 4: 2, 5: 'abc', 6: 4, 7: 'a'})
for i_data in data:
    index_list = []
    index_list = odd_index(i_data)