'''Реализуйте алгоритм перемешивания списка.'''

import random

list_shufle = []
for i in range(int(input('Введите длинну списка: '))):
    list_shufle.append(input('Введите элемент списка: '))
print(list_shufle)
for i in range(len(list_shufle)-1, 0, -1):
    j = random.randint(0, i + 1)
    list_shufle[i], list_shufle[j] = list_shufle[j], list_shufle[i]
print(list_shufle)