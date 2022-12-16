'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''

import random
from my_token import bot
from telebot import types


quantity_player = 0
candies = 120
list_of_players = []
player = None


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}! Это игра в конфеты. Правила такие.'
                                      f'На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.'
                                      f'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.'
                                      f'Все конфеты оппонента достаются сделавшему последний ход.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('PvP')
    item2 = types.KeyboardButton('Easy bot')
    item3 = types.KeyboardButton('Hard bot')
    markup.add(item1, item2, item3)
    sent = bot.send_message(message.chat.id, 'Выбери режим игры', reply_markup=markup)
    bot.register_next_step_handler(sent, message_reply)


def message_reply(message):
    global list_of_players
    list_of_players.append(message.from_user.username)
    match message.text:
        case 'PvP':
            # global player
            bot.send_message(message.chat.id, 'Вы выбрали режим двух игроков')
            bot.send_message(message.chat.id, f'Осталось {candies} конфет')
            list_of_players.append('Player 2')
            first_player = random.choice(list_of_players)
            if first_player == list_of_players[1]:
                list_of_players = list_of_players[::-1]
            bot.send_message(message.chat.id, f'Первым ходит {first_player}')
            sent = bot.send_message(message.chat.id, f'Игрок {first_player}, введите колличество конфет от 1-28')
            bot.register_next_step_handler(sent, game_player_vs_player)

        case 'Easy bot':
            list_of_players.append('бот')
            bot.send_message(message.chat.id, 'Вы выбрали режим легкого бота')
            bot.send_message(message.chat.id, f'Осталось {candies} конфет')
            first_player = random.choice(list_of_players)
            if first_player == list_of_players[1]:
                list_of_players = list_of_players[::-1]
            sent = bot.send_message(message.chat.id, f'Игрок {first_player}, введите колличество конфет от 1-28')
            bot.register_next_step_handler(sent, game_player_vs_easy_bot)
        case 'Hard bot':
            list_of_players.append('бот')
            bot.send_message(message.chat.id, 'Вы выбрали режим сложного бота')
            bot.send_message(message.chat.id, f'Осталось {candies} конфет')
            first_player = random.choice(list_of_players)
            if first_player == list_of_players[1]:
                list_of_players = list_of_players[::-1]
            bot.send_message(message.chat.id, f'Первым ходит {first_player}')
            sent = bot.send_message(message.chat.id, f'Игрок {first_player}, введите колличество конфет от 1-28')
            bot.register_next_step_handler(sent, game_player_vs_hard_bot)


@bot.message_handler(func=lambda message: message.text == 'PvP' and message.content_type == 'text')
def game_player_vs_player(message): # игрок против игрока
    global player
    global candies
    global list_of_players
    player = list_of_players[0]
    players_move = int(message.text)
    sent = bot.send_message(message.chat.id, f'Игрок {player}, взял {message.text} конфет.')

    if candies - players_move <= 0:
        bot.send_message(message.chat.id, f'Победил игрок{player}')
    else:
        list_of_players = list_of_players[::-1]
        candies -= players_move
        bot.send_message(message.chat.id, f'Осталось {candies} конфет')
        bot.register_next_step_handler(sent, game_player_vs_player)


@bot.message_handler(func=lambda message: message.text == 'Easy bot' and message.content_type == 'text')
def game_player_vs_easy_bot(message): # игрок против простого бота
    global player
    global candies
    global list_of_players
    player = list_of_players[0]
    bot.send_message(message.chat.id, f'Осталось {candies} конфет')
    if player == 'бот':
        if 0 < candies <= 28:
            players_move = candies
            bot.send_message(message.chat.id, f'Бот, взял {players_move} конфет.')
        elif 29 < candies <= 57:
            players_move = candies - 29
            bot.send_message(message.chat.id, f'Бот, взял {players_move} конфет.')
        else:
            players_move = random.randint(1, 28)
            bot.send_message(message.chat.id, f'Бот, взял {players_move} конфет.')
    elif player != 'бот':
        players_move = int(message.text)
        sent = bot.send_message(message.chat.id, f'Игрок {player}, взял {message.text} конфет.')
    if candies - players_move <= 0:
        bot.send_message(message.chat.id, f'Победил игрок{player}')
    else:
        list_of_players = list_of_players[::-1]
        candies -= players_move
        sent = bot.send_message(message.chat.id, f'Осталось {candies} конфет')
        if player == 'бот':
            game_player_vs_easy_bot(message)
        else:
            bot.register_next_step_handler(sent, game_player_vs_easy_bot)


@bot.message_handler(func=lambda message: message.text == 'Hard bot' and message.content_type == 'text')
def game_player_vs_hard_bot(message): # игрок против сложного бота
    global player
    global candies
    global list_of_players
    player = list_of_players[0]
    bot.send_message(message.chat.id, f'Осталось {candies} конфет')
    if player == 'бот':
        if candies % 29 == 0:
            players_move = random.randint(1, 28)
            bot.send_message(message.chat.id, f'Бот, взял {players_move} конфет.')
        else:
            players_move = candies % 29
            bot.send_message(message.chat.id, f'Бот, взял {players_move} конфет.')
    else:
        players_move = int(message.text)
        sent = bot.send_message(message.chat.id, f'Игрок {player}, взял {message.text} конфет.')
    if candies - players_move <= 0:
        bot.send_message(message.chat.id, f'Победил игрок{player}')
    else:
        list_of_players = list_of_players[::-1]
        candies -= players_move
        sent = bot.send_message(message.chat.id, f'Осталось {candies} конфет')
        if player == 'бот':
            game_player_vs_hard_bot(message)
        else:
            bot.register_next_step_handler(sent, game_player_vs_hard_bot)


if __name__ == "__main__":
    bot.polling(none_stop=True)