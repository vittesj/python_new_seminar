'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

num = int(input())
num_str = ''
while num >= 2:
    num_str += str(num % 2)
    num //= 2
num_str += str(num)
print(int(num_str[::-1]))