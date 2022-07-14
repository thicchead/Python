def bereken_kostrpijs(grootte)
    aantal_personen = 0
    aantal_uren = 0
    prijs = 0

    if grootte < 160:
        aantal_personen = 1
        aantal_uren = 1
        prijs = 12.5
    else:
        if grootte > 8 * 160:
            aantal_personen += 1



def main():
    oppervlakte = int(input("Oppervlakte = "))

    while oppervlakte != 0:
        bereken_kostrpijs(oppervlakte)


if __name__ == '__main__':
    main()