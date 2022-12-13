from my_token import bot


@bot.message_handler(func=lambda message: message.text == 'Экспорт контактов' and message.content_type == 'text')
def get_search_list(message):
    chat_id = message.chat.id
    sent = bot.send_message(chat_id, "Введите Имя/Фамилию/телефон контакта, который хотим экспортировать."
                                     "Если несколько контактов - вводим через пробел),"
                                     "в конце добавляем желаемый разделитель (',' или '-' )")
    bot.register_next_step_handler(sent, export_contact)


def export_contact(message):
    chat_id = message.chat.id
    list_contacts = []
    lst = message.text.split()[:-1]
    format_file = message.text.split()[-1]
    with open("telephone_dictionary.csv", "r") as f1:
        for line in f1:
            contact = tuple(line.split(','))
            for el in lst:
                if el in contact:
                    list_contacts.append(contact)
    with open('export_contact3.csv', "w") as f2:
        for contact in list_contacts:
            f2.write(f"{format_file.join(contact)}")
    with open('export_contact3.csv', 'rb') as f:
        file = f.read()
    bot.send_message(chat_id, 'Как говорит Матвеев: "Готовенько!"')
    bot.send_document(chat_id, file, visible_file_name='export.csv')