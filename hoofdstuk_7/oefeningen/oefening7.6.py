def bepaal_sterrenbeeld(datum):
    geboortedag = datum.split("/")[0]
    geboortemaand = datum.split("/")[1]
    aantal_dagen = int(geboortemaand) * 30 + int(geboortedag)

    if aantal_dagen >

def main():
    naam = input("Naam = ")
    # totaal_dagen = 365

    while naam != "/":
        voornaam = input("Voornaam = ")
        geboortedatum = input("Geboortedatum = ")
        # geboortedag = geboortedatum.split("/")[0]
        # geboortemaand = geboortedatum.split("/")[1]
        #
        # aantal_dagen = int(geboortemaand) * 30 + int(geboortedag)
        bepaal_sterrenbeeld(geboortedatum)

        naam = input("Naam = ")

    # print(geboortedag)
    # print(aantal_dagen)


if __name__ == '__main__':
    main()
