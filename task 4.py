'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''

with open('text.txt', 'w', encoding='UTF-8') as text:
    text.write(input('Введите текст для сжатия: '))

with open('text.txt', 'r', encoding='UTF-8') as text_line:
    text = text_line.read()

with open('RLE compression.txt', 'w', encoding='UTF-8') as RLE_compression:
    count = 1
    result_text = ''
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result_text += str(count) + text[i-1]
            count = 1
    else:
        result_text += str(count) + text[-1]
    RLE_compression.write(result_text)
