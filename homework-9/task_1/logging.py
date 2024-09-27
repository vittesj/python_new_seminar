def log(player: str, num_field: int) -> None:
    with open('log.txt', 'a') as f:
        f.write(f'Ходил {player}, поле {num_field} \n')