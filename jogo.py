import random

# --- Definindo cartas do jogo ---
cartas = [
    {"nome": "Leão", "forca": 8, "velocidade": 7, "inteligencia": 6},
    {"nome": "Elefante", "forca": 9, "velocidade": 4, "inteligencia": 7},
    {"nome": "Guepardo", "forca": 5, "velocidade": 10, "inteligencia": 5},
    {"nome": "Coruja", "forca": 4, "velocidade": 6, "inteligencia": 9},
    {"nome": "Urso", "forca": 7, "velocidade": 5, "inteligencia": 6},
    {"nome": "Golfinho", "forca": 6, "velocidade": 7, "inteligencia": 8},
]

# --- Embaralhar e dividir cartas ---
random.shuffle(cartas)
jogador1 = cartas[:3]
jogador2 = cartas[3:]

# --- Função para comparar uma rodada ---
def jogar_rodada(j1_carta, j2_carta, atributo):
    print(f"\nJogador 1: {j1_carta['nome']} ({atributo}={j1_carta[atributo]})")
    print(f"Jogador 2: {j2_carta['nome']} ({atributo}={j2_carta[atributo]})")

    if j1_carta[atributo] > j2_carta[atributo]:
        print("Jogador 1 venceu a rodada!")
        return "jogador1"
    elif j2_carta[atributo] > j1_carta[atributo]:
        print("Jogador 2 venceu a rodada!")
        return "jogador2"
    else:
        print("Empate!")
        return "empate"

# --- Loop principal do jogo ---
rodada = 1
while jogador1 and jogador2:
    print(f"\n--- Rodada {rodada} ---")
    carta_j1 = jogador1.pop(0)
    carta_j2 = jogador2.pop(0)

    print("Atributos disponíveis: forca, velocidade, inteligencia")
    atributo_escolhido = input("Jogador 1, escolha o atributo: ").strip().lower()

    vencedor = jogar_rodada(carta_j1, carta_j2, atributo_escolhido)

    if vencedor == "jogador1":
        jogador1.extend([carta_j1, carta_j2])
    elif vencedor == "jogador2":
        jogador2.extend([carta_j1, carta_j2])
    else:
        # Em caso de empate, as cartas são descartadas
        pass

    rodada += 1

# --- Resultado final ---
if jogador1:
    print("\n🏆 Jogador 1 venceu o jogo!")
else:
    print("\n🏆 Jogador 2 venceu o jogo!")
