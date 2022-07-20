def verander_tekst(tekst):
    for letter in tekst:
        if letter < "a" or letter > "z":
            tekst = tekst.replace(letter, " ")

    print(tekst)


def main():
    originele_string = input("Tekst = ")
    verander_tekst(originele_string)


if __name__ == '__main__':
    main()
