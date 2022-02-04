incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

summ_income = sum(incomes.values())
print('Общий доход за год составил', summ_income, 'рублей')
min_income = min(incomes.values())

for product in incomes:
    if incomes[product] == min_income:
        min_product = product
print('Самый маленький доход у', min_product, end='. ')
print('Он составляет', min_income, 'рублей')
incomes.pop(min_product)
print('Итоговый словарь: ', incomes)
