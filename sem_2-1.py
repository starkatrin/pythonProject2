#Задача 1. Напишите программу, которая принимает на вход вещественное или целое число
# и показывает сумму его цифр. Через строку нельзя решать.

# с единиц:
#def summa(len):
    #summa = 0
    #while n!= 0:
        #a = n % 10
        #n //= 10
        #summa = summa + a
    #return summa

# с первого числового знака(деятки, сотни, тысячи и т.д.):

def length(n):
    len = 0
    while n > 0:
        n //= 10
        len += 1
    return len

def summa(len):
    summa = 0
    while len > 0:
        a = n%(10**(len))// (10**(len-1))
        len -= 1
        summa = summa + a
    return summa

def sum(n):
    sum = 0
    count = 0
    while (n - round(n)) != 0:
        n *= 10
        sum = sum + count
    return sum


try:
    n = int(input('Введите целое число:'))
except ValueError:
    n = float(input('Вы ввели вещественное число. Повторите ввод:'))
    k = n % 1
    while 0 < k < 1:
        n = round(n * 10, 4)
        k = n % 1

len = length(n)
print(f'Сумма цифр введенного числа равна {summa(len)}')