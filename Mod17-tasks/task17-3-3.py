import random

squad1 = [random.randint(50, 80) for _ in range(10)]
squad2 = [random.randint(30, 60) for _ in range(10)]
squad_result = [('Погиб' if squad1[i_damage] + squad2[i_damage] > 100 else 'Выжил') for i_damage in range(10) ]
print(squad1)
print(squad2)
print(squad_result)