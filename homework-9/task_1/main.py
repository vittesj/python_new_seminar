from crest import *

board = list(range(1,10))

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X", board)
        else:
            take_input("O", board)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                with open('log.txt', 'a') as f:
                    f.write(f'{tmp} выиграл!\n\n')
                win = True
                break
        if counter == 9:
            with open('log.txt', 'a') as f:
                f.write(f'Ничья!\n\n')
            print ("Ничья!")
            break
    draw_board(board)

if __name__ == "__main__":
    main(board)