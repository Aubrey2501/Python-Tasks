class Cell:
    states = {0: 'free', 1: 'cross', 2: 'zero'}
    def __init__(self, x):
        self.state = 0
        self.index = x

class Board:
    def __init__(self):
        self.cells = [Cell(x) for x in range(1, 10)]

class Player:
    names = ['Игрок', 'Компьютер']
    def __init__(self, i):
        self.name = self.names[i]
        self.cells = []

# my_board = Board()
# for cell in my_board.cells:
#     print(cell.index)
#
# for i in range(2):
#     player = Player(i)
#     print(player.name, player.cells)


def drow_board(board):
    print(13 * '-')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(13 * '-')

def take_input(player_token):
    valid = False
    while not valid:
        try:
            player_answer = int(input('Куда поставим {} ?: '.format(player_token)))
        except:
            print('Некорректный ввод! Введите число')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if str(board[player_answer - 1]) not in '[xo]':
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('Эта Клетка уже занята.')
        else:
            print('Такой клетки нет на игровом поле. Введите число от 1 до 9')

def check_win(board):
    win_comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i_comb in win_comb:
        if board[i_comb[0]] == board[i_comb[1]] == board[i_comb[2]]:
            drow_board(board)
            return board[i_comb[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        drow_board(board)
        if counter % 2 != 0:
            take_input('o')
        else:
            take_input('x')
        counter += 1
        if counter > 4:
            win_token = check_win(board)
            if win_token:
                print(win_token, 'выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break

board = [_ for _ in range(1, 10)]
main(board)