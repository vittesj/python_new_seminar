from my_token import bot


@bot.message_handler(func=lambda message: message.text == 'Добавить контакт' and message.content_type == 'text')
def input_contact(message):
    sent = bot.send_message(message.chat.id, 'Введите через пробел фамилию, имя, номер телефона, описание контакта')
    bot.register_next_step_handler(sent, wait_data)


def wait_data(message):
    bot.send_message(message.chat.id, 'Ok')
    list_data = message.text.split()
    with open("telephone_dictionary.csv", "a") as f:
        f.write(f"{','.join(list_data)}\n")


def input_func(message):
    input_contact(message)




