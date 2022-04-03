class Cell:
    states = [0, 'x', 'o']

    def __init__(self, index):
        self.state = 0
        self.index = index


class Board:
    def __init__(self):
        self.cell = [Board.cell for Board.cell in range(1, 10)]

    def drow_board(self):
        print()
        print(13 * '-')
        for i in range(3):
            print('|', self.cell[0 + i * 3], '|', self.cell[1 + i * 3], '|', self.cell[2 + i * 3], '|')
            print(13 * '-')
        print()

    def check_win(self):
        win_comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for i_comb in win_comb:
            if self.cell[i_comb[0]] == self.cell[i_comb[1]] == self.cell[i_comb[2]]:
                self.drow_board()
                return self.cell[i_comb[0]]
        return False

    def take_input(self, player_sign):
        valid = False
        while not valid:
            try:
                player_answer = int(input('Куда поставим "{}" ?: '.format(player_sign)))
            except:
                print('Некорректный ввод! Введите число')
                continue
            if player_answer >= 1 and player_answer <= 9:
                if str(self.cell[player_answer - 1]) not in '[xo]':
                    self.cell[player_answer - 1] = player_sign
                    valid = True
                else:
                    print('Эта Клетка уже занята.')
            else:
                print('Такой клетки нет на игровом поле. Введите число от 1 до 9')

    def game_play(self):
        counter = 1
        win = False
        player_1 = Player('Игрок 1')
        player_2 = Player('Игрок 2')
        while not win:
            self.drow_board()
            if counter % 2 != 0:
                player = player_1
            else:
                player = player_2
            sign = player.player_sign
            print('Ходит:', player.name)
            self.take_input(sign)
            counter += 1
            if counter >= 4:
                win_sign = self.check_win()
                if win_sign:
                    print(player.name, 'выиграл!')
                    win = True
                    break
            if counter == 9:
                print('Ничья!')
                break


class Player:
    player = {'Игрок 1': 'x', 'Игрок 2': 'o'}

    def __init__(self, player_name):
        self.name = player_name
        self.player_sign = self.player[player_name]


my_board = Board()
Board.game_play(my_board)






