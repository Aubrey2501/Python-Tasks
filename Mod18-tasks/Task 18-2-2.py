name = input('Имя: ')
debt = input('Долг: ')
massage = '{0}! Привет, {0}! Как дела, {0}? Где мои {1} рублей? {0}!'.format(
    name,
    debt
)
print(massage)