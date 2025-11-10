import random

# Tamanho do tabuleiro
TAMANHO = 5

# Cria o tabuleiro
def criar_tabuleiro():
    return [["~" for _ in range(TAMANHO)] for _ in range(TAMANHO)]

# Mostra o tabuleiro na tela
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

# Posição aleatória do navio
def posicionar_navio():
    return [random.randint(0, TAMANHO - 1), random.randint(0, TAMANHO - 1)]

# Função principal do jogo
def jogar():
    print("🚢 BATALHA NAVAL 🚢")
    print("------------------")
    tabuleiro = criar_tabuleiro()
    navio = posicionar_navio()
    tentativas = 5

    while tentativas > 0:
        mostrar_tabuleiro(tabuleiro)
        print(f"Tentativas restantes: {tentativas}")
        linha = int(input("Escolha uma linha (0 a 4): "))
        coluna = int(input("Escolha uma coluna (0 a 4): "))

        if linha == navio[0] and coluna == navio[1]:
            print("💥 BOOM! Você acertou o navio!")
            tabuleiro[linha][coluna] = "X"
            break
        else:
            print("🌊 Errou! Tente novamente.")
            tabuleiro[linha][coluna] = "O"
            tentativas -= 1

    if tentativas == 0:
        print("😢 Fim de jogo! Você não encontrou o navio.")
        print(f"O navio estava em: {navio}")

    mostrar_tabuleiro(tabuleiro)

# Iniciar o jogo
if __name__ == "__main__":
    jogar()
