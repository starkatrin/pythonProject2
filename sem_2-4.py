#Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N,
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

import math

def distance(n, coord):
    sum = 0
    for i in range(n):
        sum += ((coord[2][i]) - float(coord[1][i]))**2
    return round(math.sqrt(sum), 2)

def points(n):
    coord = []
    coord_1 = [0] * n
    coord_2 = [0] * n
    for i in range(n):
        coord_1[i] = float(input(f'Введите координату {i + 1} первой точки: '))
        coord_2[i] = float(input(f'Введите координату {i + 1} второй точки: '))
        coord.append(coord_1)
        coord.append(coord_2)
    return coord
try:
    n = (int(input('Введите мерность пространства: ')))
    coord = points(n)
    print(f'Расстояние между первой и второй точками равно {distance(n, coord)}')
except ValueError:
    print('Введите целое число!')


