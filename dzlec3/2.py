# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
from math import fabs
N = int(input('Введите количество чисел в массиве: '))
spisok = []
for i in range(N):
    spisok.append(int(input(f'Введите {i+1} элемент: ')))
print(spisok)
X = int(input("Введите число X: "))
mini = 100
index = 0
for i in range(len(spisok)):
    if abs(X - spisok[i]) < mini:
        mini = spisok[i]
        index = i
print(spisok[i])

