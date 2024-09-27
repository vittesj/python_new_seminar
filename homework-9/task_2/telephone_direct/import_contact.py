from my_token import bot


@bot.message_handler(func=lambda message: message.text == 'Импорт контактов' and message.content_type == 'document')
def import_file(message):
    chat_id = message.chat.id
    sent = bot.send_message(chat_id, "Присылай файл)")
    bot.register_next_step_handler(sent, get_file)

def get_file(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Пожалуй, я сохраню это")
        import_contact(src)
    except Exception as e:
        bot.reply_to(message, e)


def import_contact(data: str) -> None:
    list_contacts = []
    with open(data, "r") as f1:
        while True:
            line = f1.readline()
            if ',' in line:
                contact = tuple(line.split(','))
                list_contacts.append(contact)
            elif '-' in line:
                contact = tuple(line.split('-'))
                list_contacts.append(contact)
            if not line:
                break
    with open('telephone_dictionary.csv', "a") as f2:
        for contact in list_contacts:
            f2.write(f"{','.join(contact)}")
