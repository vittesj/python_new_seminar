'''
Создать телефонный справочник
'''

from controller import input_subscriber, search_subscriber

format = input('С каким форматом вы хотите работать (csv\json): ')
request = input('Что вы хотите сделать (ввести\найти) данные аббонента? ')
if request == 'ввести':
    input_subscriber(format)
elif request == 'найти':
    search_subscriber(format)
