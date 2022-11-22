from view import view_data
import json


def log_write_csv(data):
    with open('log.csv', 'a', encoding='utf-8') as telephone_directory:
        telephone_directory.write(str(data))
        telephone_directory.write('\n')


def log_write_json(data):
    with open('log.json', 'w', encoding='utf-8') as lj:
        json.dump(data, lj, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))


def log_read_csv():
    telephone_directory = open('log.csv', 'r', encoding='utf-8')
    return telephone_directory


def log_read_json():
    with open('log.json', 'r', encoding='utf-8') as lj:
        try:
            telephone_directory = json.load(lj)
        except json.decoder.JSONDecodeError:
            telephone_directory = []
    if type(telephone_directory) == None:
        telephone_directory = []
    return telephone_directory
