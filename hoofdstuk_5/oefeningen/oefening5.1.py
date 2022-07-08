def main():
    waarde_euro = float(input("Waarde van de euro in dollar = "))
    bedrag = float(input("Bedrag = "))

    while bedrag != 0:
        resultaat = bedrag * waarde_euro

        print(resultaat)

        bedrag = float(input("Bedrag = "))


if __name__ == '__main__':
    main()
