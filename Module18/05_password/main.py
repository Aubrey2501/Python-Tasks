# TODO здесь писать код

while True:
    password = input('Придумайте пароль: ')
    is_upper = [True if password[i_symbol].isupper() else False for i_symbol in range(len(password))]
    is_digit = [True if password[i_symbol].isdigit() else False for i_symbol in range(len(password))]
    if is_upper.count(True) == 0 or is_digit.count(True) < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
