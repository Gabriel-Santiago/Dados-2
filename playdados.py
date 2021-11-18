from random import *

def dado():
    dado = randint(1, 6)
    return dado

def sum_number():
    choose1 = dado()
    choose2 = dado()
    sum = choose1 + choose2

    return choose1, choose2, sum

def choose():
    player = input('''
        Vamos jogar os dados!
        Clique ENTER para continuar!''')

    return player

def player_winner():
    choose()

    player_one_dado1, player_one_dado2, player_one_result = sum_number()
    player_two_dado1, player_two_dado2,player_two_result = sum_number()

    if player_one_result > player_two_result:
        print(f'Dado 1 do player 1 foi {player_one_dado1}\n'
              f'Dado 2 do player 1 foi {player_one_dado2}\n'
              f'A soma foi dos dados foi {player_one_result}')
        print(f'Dado 1 do player 2 foi {player_two_dado1}\n'
              f'Dado 2 do player 2 foi {player_two_dado2}\n'
              f'A soma dos dados foi {player_two_result}')
        print('Player 1 WIN!')
    elif player_one_result < player_two_result:
        print(f'Dado 1 do player 1 foi {player_one_dado1}\n'
              f'Dado 2 do player 1 foi {player_one_dado2}\n'
              f'A soma foi {player_one_result}')
        print(f'Dado 1 do player 2 foi {player_two_dado1}\n'
              f'Dado 2 do player 2 foi {player_two_dado2}\n'
              f'A soma dos dados foi {player_two_result}')
        print('Player 2 WIN!')
    else:
        print(f'Dado 1 do player 1 foi {player_one_dado1}\n'
              f'Dado 2 do player 1 foi {player_one_dado2}\n'
              f'A soma foi {player_one_result}')
        print(f'Dado 1 do player 2 foi {player_two_dado1}\n'
              f'Dado 2 do player 2 foi {player_two_dado2}\n'
              f'A soma dos dados foi {player_two_result}')
        print('EMPATE')

def main():
    player_winner()

main()