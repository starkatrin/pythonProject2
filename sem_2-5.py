#Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . Но теперь количество предикатов не три,
# а генерируется случайным образом от 5 до 25, проверяем это утверждение 100 раз,
# с помощью модуля time выводим на экран , сколько времени отработала программа.

import time
import random
def predicates():
    n = random.randrange(5, 26)
    list_predicates = [random.choice([True,False]) for i in range(n)]
    for i in range(1, len(list_predicates)):
        left = not (list_predicates[i-1] and list_predicates[i])
        right = not list_predicates[i-1] or not list_predicates[i]
        return left == right
def time_100():
    start = time.time()
    i = 1
    while i <= 100:
        result = predicates()
        if result == True:
            print(f'{i} Выражение истинно')
        else:
            print('Выражение ложно')
        i += 1
    end = time.time()
    return (f'Время выполнения {end - start}')

print(time_100())