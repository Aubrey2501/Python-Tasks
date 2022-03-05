def factorial(num):
    if num == 1:
        return 1

    else:
        fact_num = num * factorial(num - 1)
        return fact_num


num = 5
print((factorial(num)))