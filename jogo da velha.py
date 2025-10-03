tabuleiro = [' ' for _ in range(9)]

def imprimir_tabuleiro():
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print('---------')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print('---------')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')

def verificar_ganhador():
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != ' ':
            return tabuleiro[i]
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != ' ':
            return tabuleiro[i]
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != ' ':
        return tabuleiro[0]
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != ' ':
        return tabuleiro[2]
    return None

def jogar():
    jogador_atual = 'X'
    while True:
        imprimir_tabuleiro()
        print(f'Jogador {jogador_atual}, escolha uma posição (1-9):')
        posicao = int(input()) - 1
        if tabuleiro[posicao] != ' ':
            print('Posição ocupada, escolha outra!')
            continue
        tabuleiro[posicao] = jogador_atual
        ganhador = verificar_ganhador()
        if ganhador is not None:
            imprimir_tabuleiro()
            print(f'Jogador {ganhador} ganhou!')
            break
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

jogar()

