from random import randint


def encrypteer(tekst, nummer):

    for letter in tekst:
        nieuw_tekst = ord(letter) + ord(chr(nummer))
        uitkomst = chr(nieuw_tekst)
        print(uitkomst, end="")


def main():
    tekst = input("Tekst die je wil encrypteren = ")
    nummer = randint(1, 12) * 2
    # nummer = 4
    # print(nummer)
    print(nummer)

    encrypteer(tekst, nummer)


if __name__ == '__main__':
    main()
