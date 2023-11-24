def map(personagem, tesouro):
    for y in range(10):
        for x in range(10):
            if personagem == [x, y]:
                print("*", end=" ")
            elif tesouro == [x, y]:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

if __name__ == "__main__":
    map([0, 0], [2, 4])
    print("-" * 19)
    map([2, 1], [5, 0])