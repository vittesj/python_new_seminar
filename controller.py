from logging import log_write_csv, log_write_json, log_read_csv, log_read_json
from operation import result_write_scv, result_write_json, init, result_search_csv, result_search_json
from view import number_phone, name, surname, comment, view_data


def input_subscriber(format):
    if input('Для выхода из ввода данных абонента введите "esc", для продолжения нажмите enter: ') == 'esc':
        return
    value_surname = surname()
    value_name = name()
    value_number_phone = number_phone()
    value_comment = comment()
    init(value_surname, value_name, value_number_phone, value_comment)
    if format == 'csv':
        result = result_write_scv()
        log_write_csv(result)
    elif format == 'json':
        result = result_write_json()
        log_write_json(result)
    input_subscriber(format)


def search_subscriber(format):
    if format == 'csv':
        result_search_csv(log_read_csv())
    elif format == 'json':
        result_search_json(log_read_json())
