import velha_funcoes as jv

jogador = 'X'
vencedor = False

while not vencedor:

    jv.desenhar_tabuleiro()

    jogada = int(input('Onde deseja jogar?'))

    while not jv.validar_jogada(jogada):
        jv.desenhar_tabuleiro()
        jogada = int(input('Jogada invalida, tente novamente:\n'))

    jv.jogar(jogada, jogador)

    jv.desenhar_tabuleiro()

    vencedor = jv.verifica_vitoria()
    jogador = jv.troca_jogador(jogador)

jogador = jv.troca_jogador(jogador)
print(f'O jogador "{jogador}" venceu')
