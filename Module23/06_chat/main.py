def view_chat(file):
    try:
        chat_file = open(file, 'r', encoding='utf-8')
        for i_line in chat_file:
            print(i_line.replace('\n', ''))
    except FileNotFoundError:
        print('История чата пуста \n')

def add_comment(file, nick):
    chat_file = open(file, 'a', encoding='utf-8')
    comment = input('Введите сообщение: ')
    chat_file.write('{name}: {massage}\n'.format(name=nick, massage=comment))

nickname = input('Введите свой никнейм: ')
filename = 'chat.txt'
while True:
    command = input('\nВведите команду: 1 - просмотреть чат, 2 - ввод сообщения, 3 - выйти из чата: ')
    if command == '1':
        view_chat(filename)
    elif command == '2':
        add_comment(filename, nickname)
    elif command == '3':
        break
    else:
        print('Ошибка команды! Повторите ввод')

