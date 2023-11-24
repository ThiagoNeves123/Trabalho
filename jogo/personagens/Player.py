import random

posicao = [0, 0]
class Player:
    def __init__(self, fo = random.randint(10, 18), de = random.randint(10, 18), hp = random.randint(100, 120)):
        self.de = de
        self.fo = fo
        self.hp = hp
            


    def infoP(self):
        print(f"O seu HP é {self.hp}.")
        print(f"O a sua força é {self.fo} e a sua defesa é {self.de}")



def movimentação(move):
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

if __name__ == "__main__":
    jogador = Player()
    jogador.infoP()
    
    print(posicao)
    movimentação("d")
    print(posicao)
    movimentação("a")
    print(posicao)
    movimentação("s")
    print(posicao)
    movimentação("w")
    print(posicao)
    
