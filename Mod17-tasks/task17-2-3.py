prices = [1.09, 23.56, 57.84, 4.56, 6.78]
# prices = []
# for _ in range(5):
#     price = float(input('Цена на товар: '))
#     prices.append(price)

first_year = int(input('Повышение на первый год: '))
second_year = int(input('Повышение на второй год: '))

first_year_prices = [round(price * (1 + first_year / 100), 2) for price in prices]
second_year_prices = [round(price * (1 + second_year / 100), 2) for price in prices]
print(first_year_prices)
print(second_year_prices)
print('Сумма изначальных цен, цен первого и второго года:', sum(prices), sum(first_year_prices), sum(second_year_prices))

