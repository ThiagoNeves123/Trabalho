import random

from jogo.ativos import itens, mapa, tesouro
from jogo.mecanica import combate
from jogo.personagens import Player, Monstros

def interagir_item(p, mochila):
    mochila.append(p)
    if not mochila:
        print("Você não possui nenhum item")
        return
    print("Sua mochila: ")
    for i, item in enumerate(mochila, 1):
        print(f"{i}, {item}")
    
    escolha = input("Escolha a sua poção que vai usar(ESC para sair da tela): ")
    if escolha == "X":
        print("Você fechou o seu inventário")
    elif 1 <= int(escolha) <= len(mochila):
        escolha = mochila[int(escolha) - 1]
        print(f"Voce escolheu um item: {escolha}")
    else:
        print("x")
    pass

def movimentar(p1, move, mochila):
    posicao = [0, 0]
    if move.lower() == "w":
        if posicao[1] > 0:
            posicao[1] -= 1
    elif move.lower() == "s":
        if posicao[1] < 9:
            posicao[1] += 1
    elif move.lower() == "d":
        if posicao[0] < 9:
            posicao[0] += 1
    elif move.lower() == "a":
        if posicao[0] > 0:
            posicao[0] -= 1
    if move:
        acao = random.choices(["nada", "item", "monstro"], weights=[0.40, 0.20, 0.40])
        if acao == "nada":
            print(f"{p1}, andou dentro da caverna e não encoutrou nada")
        elif acao == "item":
                roll1 = random.choices(itens.pocoes["Poção de Vida 1", "Poção de Vida 2", "Poção de força 1", "Poção de força 2 ", "Poção de defesa"], weights=[0.50, 0.30, 0.10, 0.05, 0.05])[0]
                potion = roll1
                print(f"Parabéns, o nosso herói achou uma {roll1}")
                mochila.append(potion)
        elif acao == "monstro":
            print("O nosso herói encontrou um monstro")
            return #combate
    return True
    """
    - movimenta o aventureiro
    - se ele andou, seleciona uma das opções: nada, item ou monstro
    - se sorteou monstro, inicializa um monstro e começa um combate
    - se sorteou item, inicializa um item
    - retorna False se o aventureiro morrer, e True nos outros casos
    """


def jogo():
    nome = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
    p1 = Player.p1(nome)
    print(f"Saudações, {nome}! Boa sorte!")
    tes = tesouro.Tesouro()
    mapa.map(p1, tes)

    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break

        if op == "T":
            p1.ver_atributos()
        elif op == "I":
            interagir_item(p1)
        elif op in ["W", "A", "S", "D"]:
            if movimentar(p1, op):
                mapa.map(p1, tes)
            else:
                print("Game Over...")
                break
        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")

        if p1.posicao == tes.posicao:
            print(f"Parabéns, {p1.nome}! Você encontrou o tesouro!")
            break


