'''Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

list_numbers = []
for i in range(int(input('Введите длинну списка: '))):
    list_numbers.append(int(input('Введите элемент списка: ')))
list_sum_numbers = []
for i in range((len(list_numbers) + 1) // 2):
    list_sum_numbers.append(list_numbers[i] * list_numbers[-1 - i])
print(list_sum_numbers)