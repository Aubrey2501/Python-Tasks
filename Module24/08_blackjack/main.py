import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def info_rank(self):
        return self.rank

    def __str__(self):
        return '{} {}'.format(self.rank, self.suit)

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def deck_info(self):
        for card in self.cards:
            print(card)

    def mix_card(self):
        random.shuffle(self.cards)

    def one_card(self):
        if not self.cards:
            return 'no card'
        return random.choice(self.cards)

    def pull_cards(self, number):
        return [self.one_card() for _ in range(number)]

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
        self.count = 0

    def count_points(self):
        for card in player.cards:
            self.count += 1
            if card.rank == 'Туз':
                if self.points > 10:
                    i_rank = 1
                else:
                    i_rank = 10
            else:
                i_rank = rank[card.rank]
            self.points += i_rank
            print('Карта {}: {}'.format(self.count, card))
        return self.points



rank = {'Туз': 1, 'Король': 10, 'Дама': 10, 'Валет': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
suit = ['червей', 'бубён', 'крестей', 'пик']
cards = [Card(s, r) for s in suit for r in rank]
deck = Deck(cards)

# while True:
names = ['Игрок', 'Компьютер']
players = []
for i in range(2):
    player = Player(names[i])
    print('\nИграет {}'.format(player.name))
    deck.mix_card()
    count = 0
    player.cards = deck.pull_cards(2)
    player.points = player.count_points()
    print('Всего очков:', player.points)
    players.append(player)

for player in players:
    print('\nИграет {}'.format(player.name))
    while True:
        if player.name == 'Игрок':
            answer = input('Тянуть еще одну карту? ').lower()
            if answer == 'да':
                player.cards = deck.pull_cards(1)
                player.points = player.count_points()
                print('Всего очков:', player.points)
                if player.points > 21:
                    player.points = 0
                    print('Перебор!')
                    break
            else:
                break

        elif player.name == 'Компьютер':
            if player.points >= 18:
                break
            else:
                player.cards = deck.pull_cards(1)
                player.points = player.count_points()
                print('Всего очков:', player.points)
                if player.points > 21:
                    print('Перебор!')
                    player.points = 0
                    break

print()
if players[0].points > players[1].points:
    print('Победил Игрок!')
elif players[0].points < players[1].points:
    print('Игрок проиграл!')
else:
    print('Ничья')










