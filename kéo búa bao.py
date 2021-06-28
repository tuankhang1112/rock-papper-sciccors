import random

while True:
    choices = ["kéo","búa", "bao"]

    máy = random.choice(choices)
    player = None

    while player not in choices:
        player = input("kéo, búa, hay bao: ").lower()

    if player == máy:
        print("máy: ",máy)
        print("người chơi: ",player)
        print("Huề")
    elif player == "búa":
        if máy == "bao":
            print("máy: ", máy)
            print("người chơi: ", player)
            print("Thua kìa haha")
        if máy == "kéo":
            print("máy: ", máy)
            print("người chơi: ", player)
            print("Nhường đó")
        elif player == "kéo":
            if máy == "búa":
                print("máy: ", máy)
                print("người chơi: ", player)
                print("Thua kìa haha")
            if máy == "bao":
                print("máy: ", máy)
                print("người chơi: ", player)
                print("Nhường đó")
            elif player == "bao":
                if máy == "kéo":
                    print("máy: ", máy)
                    print("người chơi: ", player)
                    print("Thua kìa haha")
                if máy == "búa":
                    print("máy: ", máy)
                    print("người chơi: ", player)
                    print("Nhường đó")

    lại = input("Dám chơi lại không, sợ chứ gì! ok hay không").lower()

    if lại != "ok":
        break

print("Thôi bye")










