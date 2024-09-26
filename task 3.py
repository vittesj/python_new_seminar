'''
Создайте программу для игры в ""Крестики-нолики"".
'''

def print_playing_field(playing_field, number, player): # функция печти поля и вставки символа игрока
    for i in playing_field:
        for j in range(len(i)):
            if i[j] == number:
                i[j] = player[1]
        print(' '.join(list(map(str, i))))


def player_change(player):  # Функция смены игрока
    if player == first_player:
        return second_player
    else:
        return first_player


def checking_the_result(list_player, the_winning_field): # функция сравнения результата
    for i in the_winning_field:
        if str(i).strip('[]') in str(list_player).strip('[]'):
            print('win')
            return True
    else:
        return False

def game_player_vs_player(player, counter): # функция игры 2ух игроков
    number = int(input(f'Игрок {player[0]} выберите поле куда поставите {player[1]}: '))
    counter += 1
    player[2].append(number)
    print_playing_field(playing_field, number, player)
    if checking_the_result(sorted(player[2]), the_winning_field) == True:
        return print('Победил игрок: ', player[0])
    elif counter == 9:
        return print('Ничья')
    else:
        player = player_change(player)
        game_player_vs_player(player, counter)


playing_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # наше игровое поле

the_winning_field = [[1, 2, 3], # все варианты победы
                     [4, 5, 6],
                     [7, 8, 9],
                     [1, 4, 7],
                     [2, 5, 8],
                     [3, 6, 9],
                     [1, 5, 9],
                     [3, 5, 7]]
counter = 0 # счетчик для ничьи

if input('Введите против кого будете играть (человек / бот): ') == 'человек':
    list_of_players = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
    first_player = [__import__('random').choice(list_of_players), 'X', []]
    if list_of_players[0] == first_player:
        second_player = [list_of_players[1], 'O', []]
    else:
        second_player = [list_of_players[0], 'O', []]
    for i in playing_field:
        print(' '.join(list(map(str, i))))
    game_player_vs_player(first_player, counter)
else: # вариант игры с ботом, постараюсь реализовать к семинару
    list_of_players = [input('Введите имя игрока: '), 'бот']
    first_player = [__import__('random').choice(list_of_players), 'X', []]
    if list_of_players[0] == first_player:
        second_player = [list_of_players[1], 'O', []]
    else:
        second_player = [list_of_players[0], 'O', []]
    for i in playing_field:
        print(' '.join(list(map(str, i))))
    game_player_vs_bot(first_player, counter)
