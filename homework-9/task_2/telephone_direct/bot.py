from my_token import bot
from telebot import types
from export_contact import get_search_list
from import_contact import import_file
from input import input_func
from output import search_contact


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Добавить контакт')
    item2 = types.KeyboardButton('Найти контакт')
    item3 = types.KeyboardButton('Импорт контактов')
    item4 = types.KeyboardButton('Экспорт контактов')
    markup.add(item1, item2, item3, item4)
    sent = bot.send_message(message.chat.id, f'Привет, {message.from_user.username}!\n\n Это телефонный справочник. Выбери '
                                          f'действие, которое ты хочешь выполнить.', reply_markup=markup)
    bot.register_next_step_handler(sent, message_reply)


def message_reply(message):
    match message.text:
        case 'Добавить контакт':
            input_func(message)
        case 'Найти контакт':
            search_contact(message)
        case 'Импорт контактов':
            import_file(message)
        case 'Экспорт контактов':
            get_search_list(message)


if __name__ == "__main__":
    bot.polling(none_stop=True)

