'''
Данный модуль содержит в себе функции которые непосредственно совершают операции с базой студентов.
'''
from logging import log_read_json
from view import *


def result_write_json(count: int) -> dict:
    '''
    Данная функция осуществляет добавление нового студента в базу.
    На вход принимает очередной id на выход отдает обновленную базу.
    :param count: int
    :return: dict
    '''
    dict_json = log_read_json()
    dict_json['ID' + str(count)] = {
        "ФИО": {"Фамилия": surname(), "Имя": name(), "Отчество": middle_name()},
        "телефон": {"домашний": number_phone_home(), "рабочий": number_phone_work(),
                    "мобильный": number_phone_mobile()}, "пол": sex(),
        "группа": group()}
    return dict_json


def result_search_json():
    '''
    Данная функция осуществляет поиск по базе студентов.
    На вход ничего не принимает и на выход ничего не выдает
    :return: None
    '''
    text_search = input('Что вы хотите вывести на экран: \nданные всех студентов (всех) \nпоиск студента (один) \n'
                        'поиск по полу (м/ж) \nпоиск по группам (группа)\n')
    if text_search == 'всех':
        return print(*log_read_json().items(), sep='\n')
    elif text_search == 'один':
        FIO_studen = input('Введите фамилию имя и отчество студента через пробел: ').split()
    elif text_search == 'группа':
        search_group = input('Введите номер группы: ')
    for key, value in log_read_json().items():
        if text_search == 'один':
            if FIO_studen[0] == value["ФИО"]["Фамилия"] and FIO_studen[1] == value["ФИО"]["Имя"] and \
                    FIO_studen[2] == value["ФИО"]["Отчество"]:
                text_search_student = input('Вывести всю информацию о студенте (вся) \n'
                                            'вывести номер телефона студента (телефон) \nвывести группу студента (группа)\n')
                if text_search_student == 'вся':
                    print(value.items())
                elif text_search_student == 'группа':
                    print(value["группа"])
                elif text_search_student == 'телефон':
                    telephone_student = input('какиие номера (все/домашний/мобильный/рабочий)\n')
                    if telephone_student == 'все':
                        print(value["телефон"].items())
                    else:
                        print(value.get(telephone_student))
        elif text_search == 'группа':
            if search_group == value["группа"]:
                print(value["ФИО"].values())
        elif text_search == value["пол"]:
            print(value["ФИО"].values())


def result_delete_json() -> dict:
    '''
    Данная функция осуществляет удаление записей из базы студентов.
    На выход отправляет обновленную базу.
    :return: dict
    '''
    dict_json = log_read_json()
    text_delete = input(
        'Введите фамилию имя и отчество студента через пробел, данные которого хотите удалить: ').split()
    count_intro = 0
    for key, value in list(dict_json.items()):
        if text_delete[0] == value["ФИО"]["Фамилия"] and text_delete[1] == value["ФИО"]["Имя"] and \
                text_delete[2] == value["ФИО"]["Отчество"]:
            print(value.items())
            count_intro += 1
            text_correction = input('Вы точно хотите удалить данные этого студента? (да/нет) ')
            if text_correction == 'да':
                dict_json.pop(key)
    if count_intro == 0:
        print('Студент не найден')
    return dict_json


def result_edit_json() -> dict:
    """
        Данная функция осуществляет редактирование записей в базе студентов.
        На выход отправляет обновленную базу.
        :return: dict
        """
    dict_json = log_read_json()
    text_edit = input('Что хотите отредактировать (данные студента/номер группы)')
    if text_edit == 'данные студента':
        FIO_student_edit = input('Введите фамилию имя и отчество студента данные которого '
                                 'хотите отредактировать через пробел: ').split()
    elif text_edit == 'номер группы':
        edit_group = input('Введите номер группы которую хотите отредактировать')
        new_group = input('Введите новый номер группы')
    for key, value in dict_json.items():
        if text_edit == 'номер группы' and value["группа"] == edit_group:
            value["группа"] = new_group
        elif text_edit == 'данные студента' and FIO_student_edit[0] == value["ФИО"]["Фамилия"] and \
                FIO_student_edit[1] == value["ФИО"]["Имя"] and FIO_student_edit[2] == value["ФИО"]["Отчество"]:
            edit_val = input('Введите данные которые хотите отредактировать (ФИО/телефон/группа): ')
            if type(value[edit_val]) is not dict:
                value[edit_val] = input('Введите номер группы')
            else:
                print(value[edit_val])
                for k, val in value[edit_val].items():
                    print(k, val)
                    a = input('нажмите enter чтобы продолжить или введите новыые данные: ')
                    if a == '':
                        continue
                    else:
                        value[edit_val][k] = a
    return dict_json

