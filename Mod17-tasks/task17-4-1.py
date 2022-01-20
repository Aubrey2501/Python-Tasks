import random
original_prices = [random.randint(-15, 15) for _ in range(10)]

new_prices = [(price if price > 0 else 0) for price in original_prices]
print(original_prices)
print(new_prices)

print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))

