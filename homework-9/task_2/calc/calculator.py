from my_token import bot


@bot.message_handler(commands=['start'])
def start_calculator(message):
    bot.send_message(message.chat.id, f'Приветствую, {message.from_user.username}! это калькулятор)')
    sent = bot.send_message(message.chat.id, 'Для работы просто введи выражение, которое ты хочешь вычислить)')
    bot.register_next_step_handler(sent, get_string)


def get_string(message):
    input_string = message.text
    bot.send_message(message.chat.id, 'Сейчас посчитаем)')
    list_of_members = []
    line_num = ''
    general_list = []
    list_of_characters = []
    for i in input_string:
        if i in '()*+-/':
            general_list.append(line_num)
            general_list.append(i)
            line_num = ''
        else:
            line_num += i
    general_list.append(line_num)
    print(list_of_members, list_of_characters)
    for i in range(len(general_list) - 1, -1, -1):
        if general_list[i] == '':
            del general_list[i]
    if 'j' in input_string:
        general_list_revers = general_list[::-1]
        general_list = []
        i = 0
        while i != len(general_list_revers):
            if 'j' in general_list_revers[i]:
                general_list.append(
                    general_list_revers[i + 2] + general_list_revers[i + 1] + general_list_revers[i])
                i += 3
            else:
                general_list.append(general_list_revers[i])
                i += 1
        general_list = general_list[::-1]
        print(list_of_members, list_of_characters)
    for i in general_list:
        if i in '*+-/':
            list_of_characters.append(i)
        else:
            if '+' in i or '-' in i:
                list_of_members.append(complex(i))
            else:
                list_of_members.append(float(i))
    list_of_characters.insert(0, '')
    list_of_characters.append('')
    print(list_of_members, list_of_characters)
    calculator(list_of_members, list_of_characters)
    bot.send_message(message.chat.id, f'Результат: {list_of_members[0]}')


def calculator(data1, data2):
    if len(data1) == 1:
        return data1[0]
    while '*' in data2 or '/' in data2:
        for i, val in enumerate(data2):
            if val == '*' or '/':
                if val == '*':
                    data1[i] = data1[i - 1] * data1[i]
                    del data1[i - 1]
                    data2.remove(data2[i])
                    calculator(data1, data2)
                if val == '/':
                    data1[i] = data1[i - 1] / data1[i]
                    del data1[i - 1]
                    data2.remove(data2[i])
                    calculator(data1, data2)
    while '+' in data2 or '-' in data2:
        for i, val in enumerate(data2):
            if val == '+' or '-':
                if val == '+':
                    data1[i] = data1[i - 1] + data1[i]
                    del data1[i - 1]
                    data2.remove(data2[i])
                    calculator(data1, data2)
                if val == '-':
                    data1[i] = data1[i - 1] - data1[i]
                    del data1[i - 1]
                    data2.remove(data2[i])
                    calculator(data1, data2)


if __name__ == "__main__":
    bot.polling(none_stop=True)