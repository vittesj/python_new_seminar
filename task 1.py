'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

sum = 0
list_numbers = []
for i in range(int(input('Введите длинну списка: '))):
    list_numbers.append(int(input('Введите элемент списка: ')))
    if i % 2 != 0:
        sum += list_numbers[i]
print(sum)

