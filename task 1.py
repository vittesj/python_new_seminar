'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''

text = input().split()
for i in range(len(text) - 1, -1, -1):
    if 'абв' in text[i].lower():
        del text[i]
print(*text)