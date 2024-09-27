'''Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности.
'''

sequence_of_numbers = []
numbers_list = []
for i in range(int(input('Введите длину последовательности чисел: '))):
    num = int(input('Введите число последовательности: '))
    if num in sequence_of_numbers or num in numbers_list:
        numbers_list.append(num)
    else:
        sequence_of_numbers.append(num)
print([i for i in sequence_of_numbers if not i in numbers_list])