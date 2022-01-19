N = int(input('Кол-во друзей: '))
K = int(input('Кол-во долговых расписок: '))
friends = []
for ind in range(N):
    friends.append([ind + 1, 0])

for ind in range(K):
    print('\nРасписка', ind + 1)
    borrower = int(input('Кому: '))
    creditor = int(input('От кого: '))
    loan = int(input('Сколько: '))

    for i in range(N):
        if friends[i][0] == creditor:
            friends[i][1] += loan
        elif friends[i][0] == borrower:
            friends[i][1] -= loan

print('\nБаланс друзей: ')
for i in range(N):
    print(friends[i][0], ':', friends[i][1])

# зачет!
