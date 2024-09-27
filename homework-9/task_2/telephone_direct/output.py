from my_token import bot


@bot.message_handler(func=lambda message: message.text == 'Найти контакт' and message.content_type == 'text')
def search_contact(message):
    sent = bot.send_message(message.chat.id, 'Введите Имя/Фамилию/телефон')
    bot.register_next_step_handler(sent, output)


def output(message) -> None:
    with open("telephone_dictionary.csv", "r") as f1:
        for line in f1:
            contact = tuple(line.split(','))
            if message.text in contact:
                bot.send_message(message.chat.id, ', '.join(contact))


