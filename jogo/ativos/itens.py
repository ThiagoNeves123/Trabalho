from jogo.personagens import Player

def potion(hp, status):
    pocoes = {
        "Poção de Vida 1": int(hp * 0.20),
        "Poção de Vida 2": int(hp * 0.40),
        "Poção de força": int(status["fo"] + 1),
        "Poção de força 2": int(status["fo"] + 2),
        "Poção de Defesa": int(status["de"] + 1)
    }
    print(pocoes)

potion(100, {"fo": 10, "de": 5})





