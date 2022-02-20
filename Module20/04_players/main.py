players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

list_player = []
for i_player, i_scores in players.items():
    l_player = list(i_player)
    l_player.extend(list(i_scores))
    list_player.append(tuple(l_player))
print(list_player)


