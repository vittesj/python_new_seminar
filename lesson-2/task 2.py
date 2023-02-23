'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    Пример:
    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

result_list = [1]
factorial = 1
k = '1'
factorial_list = [k]
for i in range(2, int(input()) + 1):
    k = k + '*' + str(i)
    factorial *= i
    result_list.append(factorial)
    factorial_list.append(k)
print(result_list)
print('(' + ', '.join(factorial_list) + ')')