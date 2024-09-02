def print_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("---------")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verificar colunas
    for i in range(3):
        if [tabuleiro[j][i] for j in range(3)].count(jogador) == 3:
            return True

    # Verificar diagonais
    if [tabuleiro[i][i] for i in range(3)].count(jogador) == 3:
        return True
    if [tabuleiro[i][2 - i] for i in range(3)].count(jogador) == 3:
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

def jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogadores = ['X', 'O']
    jogador_atual = 0

    while True:
        print_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogadores[jogador_atual]}")

        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
            if tabuleiro[linha][coluna] != ' ':
                print("Essa posição já está ocupada. Tente novamente.")
                continue
            tabuleiro[linha][coluna] = jogadores[jogador_atual]
        except (IndexError, ValueError):
            print("Entrada inválida. Tente novamente.")
            continue

        if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
            print_tabuleiro(tabuleiro)
            print(f"Jogador {jogadores[jogador_atual]} venceu!")
            break

        if verificar_empate(tabuleiro):
            print_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = 1 - jogador_atual

# Iniciar o jogo
jogo_da_velha()
