'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''

divider_num = []
k = 2
num = int(input('Введите натуральное число: '))
while k <= num:
    if num % k == 0:
        divider_num.append(k)
        num //= k
    else:
        k += 1
print(divider_num)