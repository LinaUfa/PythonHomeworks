# Задача 2: Найдите сумму цифр трехзначного числа.

# print("Введите число: ")
# number = int(input())
# summa = 0
# while number > 0:
#     x = number % 10
#     summa = summa + x
#     number = number // 10
# print(summa)    

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.

# print("Введите общее количество журавликов: ")
# summa = int(input())
# petya = summa // 6 
# sergey = petya
# katya = petya*4
# print (f"Петя - {petya},Катя - {katya},Сергей - {sergey}")

# Задача 6: Счастливый билет. 385916 -> yes

# print("Введите номер билета: ")
# number = int(input())
# left = (number // 100000 + (number // 10000 % 10) + (number // 1000 % 100 % 10))
# right = (number % 1000 // 100 + (number % 1000 // 10 % 10) + (number % 1000 % 100 % 10))
# if left == right:
#     print('Yes')
# else: print ('No')

# Задача 8: Требуется определить, можно ли от шоколадки размером n x m
# долек отломить k долек.

# m = int(input('Введите размер шоколадки - длину: '))
# n = int(input('Введите размер шоколадки - ширину: ')) 
# k = int(input('Введите количество долек шоколадки: '))
# if k % m == 0 or k % n == 0:
#     print('Шоколадку возможно разделить:)')
# else: print('Шоколадку невозможно разделить:(')

