def main():
    getallenlijst = []
    totaal = 0
    gemiddelde = 0
    kleiner_dan_gemiddelde = 0

    for i in range(1, 11):
        getal = int(input("Getal = "))

        getallenlijst.append(getal)
        totaal += getal

    gemiddelde = totaal / len(getallenlijst)

    for getal in getallenlijst:
        if getal < gemiddelde:
            kleiner_dan_gemiddelde += 1

    print(getallenlijst)
    print(gemiddelde)
    print(kleiner_dan_gemiddelde)


if __name__ == '__main__':
    main()
