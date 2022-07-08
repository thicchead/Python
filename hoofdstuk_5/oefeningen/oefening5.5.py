def controleer(nummer):
    miljoenen = nummer // 1000000 * 1000000
    nummer -= miljoenen
    tweede_getal = nummer // 100000

    duizenden = nummer // 10000 * 10000
    nummer -= duizenden
    vierde_getal = nummer // 1000

    honderden = nummer // 100 * 100
    nummer -= honderden
    laatste_twee = nummer

    eerste_vorm = str(tweede_getal) + str(vierde_getal)
    tweede_vorm = str(laatste_twee)

    if eerste_vorm == tweede_vorm:
        return "Gratis"
    else:
        return "Niet gratis"


def main():
    lidnummer = int(input("Lidnummer = "))
    antwoord = controleer(lidnummer)
    print(antwoord)


if __name__ == '__main__':
    main()
