'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''

from random import randint

k = int(input('Введите натуральное значение степени: '))
polynomial = ''
with open('polynomial.txt', 'w') as polynomial_txt:
    while k >= 0:
        a = randint(0, 100)
        if a > 1 and k > 1:
            polynomial = polynomial + str(a) + ' * x^' + str(k) + ' + '
        elif a == 1 and k >= 1:
            polynomial = polynomial + 'x^' + str(k) + ' + '
        elif a > 1 and k == 1:
            polynomial = polynomial + str(a) + ' * x ' + ' + '
        elif a != 0 and k == 0:
            polynomial = polynomial + str(a)
        elif a == 0:
            polynomial = polynomial[:-3]
        k -= 1
    polynomial_txt.write(polynomial + ' = 0')
print(polynomial + ' = 0')

