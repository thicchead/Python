def bepaal_leeftijd(gegevens):
    huidige_datum = input("Datum = ")
    geboortedatum = gegevens[5:16]

    # print(geboortedatum)


def check_antwoorden(juist, deelnemer):
    deelnemer_antwoorden = deelnemer[16:26]
    # print(juist)
    # print(deelnemer_antwoorden)
    #
    # print(juist[0])
    # print(deelnemer_antwoorden[0])
    #
    # if juist[0] == deelnemer_antwoorden[0]:
    #     print("juist")
    #
    # print(deelnemer_antwoorden)
    # deelnemer_lijst = []
    # for letter in deelnemer_antwoorden:
    #     deelnemer_lijst.append(letter)
    #
    # print(deelnemer_lijst)
    # print(juist)
    punten = 0

    for i in range(9):
        if juist[i] == deelnemer_antwoorden[i]:
            punten += 2
        elif deelnemer_antwoorden[i] == "E":
            punten += 0
        else:
            punten -= 1

    return punten


def main():
    juiste_antwoorden = []
    antwoorden = input("Juiste antwoorden = ")
    juiste_antwoorden.append(antwoorden)
    # print(juiste_antwoorden)

    deelnemer_gegevens = input("Gegevens = ")

    aantal_punten = check_antwoorden(antwoorden, deelnemer_gegevens)
    print(aantal_punten)

    leeftijd = bepaal_leeftijd(deelnemer_gegevens)
    print(leeftijd)


if __name__ == '__main__':
    main()
