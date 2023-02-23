'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
'''

import random

n = int(input('Введите длинну списка: '))
list_count = []
with open('text.txt', 'w', encoding='UTF-8') as count_txt:
    for i in range(n):
        count_txt.write(str(i) + '\n')
        list_count.append(random.randint(-n, n))
print(list_count) # проверим созданный список
with open('text.txt', 'r', encoding='UTF-8') as count_txt:
    count = count_txt.read()
    print(count) # проверим как записались индексы в файл
    list_index = []
    for i in count:
        if i.isdigit():
            list_index.append(i)
    num1 = int(random.choice(list_index)) # сгенерируем случайный индекс из файла для первого числа
    num2 = int(random.choice(list_index)) # сгенерируем случайный индекс из файла для второго числа
    print(list_count[num1], list_count[num2]) # выведим числа списка которые будем перемножать
    print(list_count[num1] * list_count[num2]) # конечный искомый итог