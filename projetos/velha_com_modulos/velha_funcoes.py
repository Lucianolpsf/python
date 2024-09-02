from os import system

tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def desenhar_tabuleiro():
    system('clear')
    for indice,  i in enumerate(tabuleiro):
        if indice == 2 or indice == 5 or indice == 8:
            print(i)
        else:
            print(i, end=' ')


def jogar(jogada, jogador):
    tabuleiro[jogada] = jogador


def troca_jogador(jogador):
    jog = jogador
    if jog == 'X':
        jog = 'O'
    else:
        jog = 'X'
    return jog


def validar_jogada(jogada):
    if int(jogada) < 0 or int(jogada) > 8:
        return False
    elif tabuleiro[int(jogada)] == 'X' or tabuleiro[int(jogada)] == 'O':
        return False
    else:
        return True


def verifica_vitoria():
    # função refatorada
    combinacoes_vencedoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
        (0, 4, 8), (2, 4, 6)           # diagonais
    ]

    for a, b, c in combinacoes_vencedoras:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return True

    return False


# def verifica_vitoria():
#     # função inicial
#     if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] or
#         tabuleiro[3] == tabuleiro[4] == tabuleiro[5] or
#         tabuleiro[6] == tabuleiro[7] == tabuleiro[8]):
#         return True
#     elif (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] or
#           tabuleiro[1] == tabuleiro[4] == tabuleiro[7] or
#           tabuleiro[2] == tabuleiro[5] == tabuleiro[8]):
#         return True
#     elif (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] or
#           tabuleiro[2] == tabuleiro[4] == tabuleiro[6]):
#         return True
#     else:
#         return False
