players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

# a_rest = [players_dict.get('name') for player in players_dict if players_dict.get('team') == 'A']
# print(a_rest)

a_rest = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'
]
print(a_rest)

b_training = [player['name']
              for player in players_dict.values() 
              if player['team'] == 'B' and player['status'] == 'Training']
print(b_training)

c_travel = [player['name']
            for player in players_dict.values()
            if player['team'] == 'C' and player['status'] == 'Travel']

print(c_travel)