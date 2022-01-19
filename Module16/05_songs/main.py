violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def is_song_exist(song, violator_songs):
    length = 0
    # TODO Поправьте по аналогии с 3 задачей
    for i_song, i_length in violator_songs:
        if i_song == song:
            length = i_length
            break
    return(length)


songs_num = int(input('Сколько песен выбрать? '))
sum_length = 0
for i in range(songs_num):
    while True:
        print('Название', i + 1, end=' ')
        song = input('песни: ')
        length = is_song_exist(song, violator_songs)
        if length != 0:
            sum_length += length
            break
        else:
            print('Такой песни нет, повторите ввод!')

print('Общее время звучания песен:', round(sum_length, 2))
