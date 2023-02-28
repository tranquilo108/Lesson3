# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Input: 6, [1, 2, 3, 4, 5]
# Output: 5
from random import randint
temp1 = 1000000000
temp2 = 0
def new_func():
    n1 = int(input('Введите количество элементов массива: '))
    n2 = int(input('Введите искомое число: '))
    list1 = [randint(0, 10) for i in range(0, n1)]
    return n2, list1

n2, list1 = new_func()

for i in list1:
    a = abs(i - n2)
    if a < temp1 and a >= 0:
        temp1 = a
        temp2 = i
print('------------------------------')
print(list1)
print(temp2)