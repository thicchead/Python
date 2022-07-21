def main():
    tekst_een = input("Tekst één = ")
    tekst_twee = input("Tekst twee = ")

    if len(tekst_een) < 4:
        while len(tekst_een) != 4:
            tekst_een += "*"

    tekst_een = tekst_een.upper()

    if len(tekst_twee) < 4:
        while len(tekst_twee) != 4:
            tekst_twee += "+"

    tekst_twee = tekst_twee.lower()

    tekst = tekst_een[:4] + tekst_twee[:4]

    print(tekst)


if __name__ == '__main__':
    main()
