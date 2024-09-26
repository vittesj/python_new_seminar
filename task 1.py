'''Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
    Пример:
    2+2 => 4;
    1+2*3 => 7;
    1-2*3 => -5;
'''

import re


def function1(data1, data2):
    if len(data1) == 1:
        return print(*data1)
    while '*' in data2 or '/' in data2:
        for i, val in enumerate(data2):
            if val == '*' or '/':
                if val == '*':
                    data1[i] = int(data1[i - 1]) * int(data1[i])
                    del data1[i - 1]
                    data2.remove(data2[i])
                    function1(data1, data2)
                if val == '/':
                    data1[i] = int(data1[i - 1]) / int(data1[i])
                    del data1[i - 1]
                    data2.remove(data2[i])
                    function1(data1, data2)
    while '+' in data2 or '-' in data2:
        for i, val in enumerate(data2):
            if val == '+' or '-':
                if val == '+':
                    data1[i] = int(data1[i - 1]) + int(data1[i])
                    del data1[i - 1]
                    data2.remove(data2[i])
                    function1(data1, data2)
                if val == '-':
                    data1[i] = int(data1[i - 1]) - int(data1[i])
                    del data1[i - 1]
                    data2.remove(data2[i])
                    function1(data1, data2)


line_list = input()
list1 = re.split('[*/+-]+', line_list)
list2 = re.split('[0-9]+', line_list)
function1(list1, list2)

# 2*2/2+2-2