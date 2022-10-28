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

def player_change(player): # Функция смены игрока
    if player == list_of_players[0]:
        return list_of_players[1]
    else:
        return list_of_players[0]

def game_player_vs_player(candies, player): # игрок против игрока
    print(f'Осталось {candies} конфет')
    players_move = int(input(f'Игрок {player} введите колличество конфет от 1-28: '))
    if candies - players_move == 0:
        return print('Победил игрок:', player)
    else:
        player = player_change(player)
        game_player_vs_player(candies - players_move, player)

def game_player_vs_easy_bot(candies, player): # игрок против простого бота
    print(f'Осталось {candies} конфет')
    if player == 'бот':
        if 0 < candies <= 28:
            players_move = candies
        elif 29 < candies <= 57:
            players_move = candies - 29
            print('бот делает ход', players_move)
        else:
            players_move = random.randint(1, 28)
            print('бот делает ход', players_move)
    else:
        players_move = int(input(f'Игрок {player} введите колличество конфет от 1-28: '))
    if candies - players_move == 0:
        return print('Победил игрок:', player)
    else:
        player = player_change(player)
        game_player_vs_easy_bot(candies - players_move, player)

def game_player_vs_hard_bot(candies, player): # игрок против сложного бота
    print(f'Осталось {candies} конфет')
    if player == 'бот':
        if candies % 29 == 0:
            players_move = random.randint(1, 28)
            print('бот делает ход', players_move)
        else:
            players_move = candies % 29 # ответ на вопрос какой должен быть первый ход чтобы выиграть.
            print('бот делает ход', players_move)
    else:
        players_move = int(input(f'Игрок {player} введите колличество конфет от 1-28: '))
    if candies - players_move == 0:
        return print('Победил игрок:', player)
    else:
        player = player_change(player)
        game_player_vs_hard_bot(candies - players_move, player)

# Меню
candies = int(input('Введите колличество конфет на столе: '))
if input('Введите против кого будете играть (человек / бот): ') == 'человек':
    list_of_players = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
    first_player = random.choice(list_of_players) # жеребьевка
    print('В результате жеребьевки первым ходит игрок: ', first_player)
    game_player_vs_player(candies, first_player)
else:
    if input('Выберете уровень сложности (простой / сложный): ') == 'простой':
        list_of_players = [input('Введите имя игрока: '), 'бот']
        first_player = random.choice(list_of_players)
        print('В результате жеребьевки первым ходит игрок: ', first_player)
        game_player_vs_easy_bot(candies, first_player)
    else:
        list_of_players = [input('Введите имя игрока: '), 'бот']
        first_player = random.choice(list_of_players)
        print('В результате жеребьевки первым ходит игрок: ', first_player)
        game_player_vs_hard_bot(candies, first_player)