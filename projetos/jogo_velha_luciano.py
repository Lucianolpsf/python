import os

jogador = 'x'

tabuleiro = ['0','1','2','3','4','5','6','7','8']

def desenha_tabuleiro():
    os.system('clear')
    for i , item in enumerate(tabuleiro):
        if i == 3 or i == 6:
            print('\n-------')
        
        if (i == 1 or i == 4 or i == 7 )and i < 8:
            print(f'| {item} |', end='')
        elif i == 8:
            print(item)
        else:
            print(item, end='')
    
def troca_jogador():
    jog = jogador
    if jog == 'x':
        jog = 'o'
    else:
        jog = 'x'
    return jog

def jogar(jogada):
    tabuleiro[int(jogada)] = jogador

def validar_jogada(jogada):
    if int(jogada) < 0 or int(jogada) > 8:
        return False
    elif tabuleiro[int(jogada)] == 'x' or tabuleiro[int(jogada)]== 'o':
        return False
    else:
        return True

def verificar_vitoria():
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] or
        tabuleiro[3] == tabuleiro[4] == tabuleiro[5] or
        tabuleiro[6] == tabuleiro[7] == tabuleiro[8]):
        return True
    elif (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] or
          tabuleiro[1] == tabuleiro[4] == tabuleiro[7] or
          tabuleiro[2] == tabuleiro[5] == tabuleiro[8]):
        return True
    elif (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] or
          tabuleiro[2] == tabuleiro[4] == tabuleiro[6]):
        return True
    else:
        return False

while True:
    desenha_tabuleiro()
    jogada = input('Infome onde quer jogar:\n')

    # valida = validar_jogada(jogada)
    while validar_jogada(jogada) == False:
        desenha_tabuleiro()
        jogada = input('Jogada invalida, tente novamente:\n')

    jogar(jogada)
    
    if verificar_vitoria() == True:
        jogar(jogada)
        desenha_tabuleiro()
        print('Você venceu!!!')
        break

    jogador = troca_jogador()
