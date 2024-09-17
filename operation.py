from logging import log_read_json


def init(arg1, arg2, arg3, arg4):
    global name
    global surname
    global comment
    global number_phone
    surname = arg1
    name = arg2
    number_phone = arg3
    comment = arg4


def result_write_scv():
    list = [surname, name, number_phone, comment]
    return ';'.join(list)


def result_write_json():
    dict_json = {'surname': surname, 'name': name, 'number_phone': number_phone, 'comment': comment}
    list_json = log_read_json()
    list_json.append(dict_json)
    return list_json


def result_search_csv(read_file_csv):
    serch_surname = input('Введите искомую фамилию: ')
    for i in read_file_csv:
        my_list = i.split(';')
        string = my_list[3]
        my_list[3] = string[:-1]
        if my_list[0] == serch_surname:
            print(*my_list)


def result_search_json(read_file_json):
    serch_surname = input('Введите искомую фамилию: ')
    for i in read_file_json:
        if i['surname'] == serch_surname:
            print("{surname} {name} {number_phone} {comment}".format(**i))



surname = ''
name = ''
comment = ''
number_phone = 0
