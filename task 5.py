'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

list_fibonachi = [0]
list_negafibonachi = []
num = 1
for i in range(int(input())):
    list_fibonachi.append(num + list_fibonachi[i-1])
    num = list_fibonachi[i+1]
    list_negafibonachi.append(list_fibonachi[i+1] * (-1) ** i)
print(list_negafibonachi[::-1] + list_fibonachi)