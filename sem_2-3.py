#Задача 3. Напишите программу, в которой пользователь будет задавать две строки,
#а программа - определять количество вхождений одной строки в другой.
# COUNT или FIND нельзя юзать! говорил же на семинаре.

str_1 = input('Введите строку 1:')
str_2 = input('Введите подстроку, которую будем искать:')

count = 0
for i in range(len(str_1)):
    if str_1[i:i+len(str_2)] == str_2:
        count += 1
print(count)
