'''Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
'''


def string(text):                             # эта функция помогает преобразовать считанную строку
    text_list = text.split()                  # с многочленом в строку для  правильного
    for i in range(0, len(text_list), 6):     # преобразования многочлен в словарь
        if text_list[i].isdigit() == False:
            text_list.insert(i, '1')
            text_list.insert(i + 1, '*')
        if text_list[i + 3] != '^':
            text_list.insert(i + 3, '^')
            text_list.insert(i + 4, '1')
    if text_list[-1].isdigit() and text_list[-2] == '+':
        return (''.join(text_list) + '*x^0')
    else:
        return (''.join(text_list))


with open('first polynomial.txt', 'w') as first_polynomial: # Вводим первый многочлен и записываем его в файл
    first_polynomial.write(input('Введите первый многочлен в формате a*x^n+b*x^(n-1)+...+c: '))
with open('second polynomial.txt', 'w') as second_polynomial: # Вводим второй многочлен и записываем его в файл
    second_polynomial.write(input('Введите второй многочлен в формате a*x^n+b*x^(n-1)+...+c: '))

with open('first polynomial.txt', 'r') as first_polynomial: # Считываем первый многочлен из файла в переменную
    polynomial1 = first_polynomial.read()
with open('second polynomial.txt', 'r') as second_polynomial: # Считываем второй многочлен из файла в переменную
    polynomial2 = second_polynomial.read()

first_polynomial_dict = {key: int(value) for value, key in
                         list(substring.split('*') for substring in string(polynomial1).split('+'))} # преобразуем первый многочлен в словарь
second_polynomial_dict = {key: int(value) for value, key in
                          list(substring.split('*') for substring in string(polynomial2).split('+'))} # преобразуем второй многочлен в словарь

result_dict = first_polynomial_dict | second_polynomial_dict # создаем третий словарь объединяя словари многочленов
for key1, value1 in result_dict.items(): # ссумируем значения по общему ключу в итоговом словаре
    for key2, value2 in first_polynomial_dict.items():
        if key2 in second_polynomial_dict.keys() and key2 == key1:
            result_dict[key1] = value1 + value2
            break
# Сортируем ключи итогового словаря по степени в ключе
result_dict = dict(sorted(result_dict.items(), key=lambda x: int(x[0].split('^')[1]))[::-1])
result_text =''
for key, value in result_dict.items(): #преобразуем итоговый словарь с получившимся многочленом в строку для записи в файл
    if int(key.split('^')[1]) == 1:
        key = key[0]
    elif int(key.split('^')[1]) == 0:
        key = ''
    if value == 1:
        value = ''
    if type(value) == int:
        result_text += str(value) + '*' + key + '+'
    else:
        result_text += key + '+'
print(result_text[:-2])  #готовый результат

with open('sum of polynomials.txt', 'w') as sum_of_polynomials:
    sum_of_polynomials.write(result_text[:-2]) #

# Ниже предоставлены 2 многочлена сформированных в 4ой задаче ДЗ, которые использовались в качестве примера.

# 3 * x ^ 10 + 4 * x ^ 9 + 4 * x ^ 8 + 6 * x ^ 6 + 2 * x ^ 5 + x ^ 4 + 10 * x ^ 3 + 8 * x ^ 2
# 8 * x ^ 10 + 9 * x ^ 9 + 9 * x ^ 7 + 3 * x ^ 5 + x ^ 4 + 8 * x ^ 3 + 9 * x ^ 2 + x + 7