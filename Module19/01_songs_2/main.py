violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

total_duration = 0
num_songs = int(input('Сколько песен выбрать? '))
for i_song in range(num_songs):
    print('Название', i_song + 1, 'песни:', end=' ')
    name_song = input()

    if name_song in violator_songs.keys():
        total_duration += violator_songs[name_song]

print('Общее время звучания:', round(total_duration, 2), 'мин.')

# зачет!
