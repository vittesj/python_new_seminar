'''
Данный модуль предназначен для считывания базы из файла и записи обновленной базы в файл
'''
import json


def log_write_json(data: dict) -> None:
    '''
    Данная функция осуществляет запись обновленной базы студентов в файл.
    :param data: dict
    :return: None
    '''
    with open('log.json', 'w', encoding='utf-8') as lj:
        json.dump(data, lj, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))


def log_read_json() -> dict:
    '''
    Данная функция осуществляет чтение базы из файла, в случае, если база пуста - возвращает пустой словарь
    :return: dict
    '''
    with open('log.json', 'r', encoding='utf-8') as lj:
        try:
            telephone_directory = json.load(lj)

        except json.decoder.JSONDecodeError:
            telephone_directory = {}
    if type(telephone_directory) is None:
        telephone_directory = {}
    return telephone_directory
