def verander_tekst(txt):
    for letter in txt:
        if letter < "a" or letter > "z":
            txt = txt.replace(letter, " ")

    return txt


def main():
    tekst = input("Tekst = ")
    print(verander_tekst(tekst))


if __name__ == '__main__':
    main()
