import random
def Tesouro():
    while True:
        posicao = [random.randint(0, 10), random.randint(0, 10)]
        if posicao != [0, 0]:
            break

if __name__ == "__main__":
    Tesouro()