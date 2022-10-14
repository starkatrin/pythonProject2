#Задача 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#*Пример:*
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def num_composition(n):
     list_of_comp = []
     factorial = 1
     for i in range(1, n + 1):
          factorial *= i
          list_of_comp.append(factorial)
     return list_of_comp

try:
     n = int(input('Введите целое положительное число:'))
except ValueError:
     print('Необходимо ввести целое положительное число!')
     n = int(input('Введите целое положительное число:'))

print(f'Список произведений чисел 1 до N: {num_composition(n)}')