'''Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

from decimal import Decimal

list_numbers = []
min = 1
max = 0
for i in range(int(input('Введите длинну списка: '))):
    list_numbers.append(float(input('Введите элемент списка: ')))
    if list_numbers[i] % 1 > max:
        max = Decimal(str(list_numbers[i])) % 1
    elif 0 < list_numbers[i] % 1 < min:
        min = Decimal(str(list_numbers[i])) % 1
print(max - min)

