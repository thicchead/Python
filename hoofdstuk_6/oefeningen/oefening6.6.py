def check_hoogte(hoogte):
    while hoogte < 2 or hoogte > 6.5:
        print("Hoogte is minimum 2 en maximum 6.5 meter.")
        hoogte = float(input("Hoogte = "))

    return hoogte


def check_breedte(breedte):
    while breedte < 2 or breedte > 8:
        print("Breedte is minimum 2 en maximum 8 meter.")
        breedte = float(input("Breedte = "))

    return breedte


def bereken_oppervlakte(hoogte, breedte):
    oppervlakte = hoogte * breedte

    return oppervlakte


def bereken_gewicht(oppervlakte):
    aluminium = 11

    gewicht = oppervlakte * aluminium

    return gewicht


def bepaal_motor(gewicht):

    if gewicht < 150:
        motornaam = "A101"
    elif gewicht < 300:
        motornaam = "A105"
    else:
        motornaam = "X300"

    return motornaam


def bepaal_motorprijs(motor):
    if motor == "A101":
        prijs = 120
    elif motor == "A105":
        prijs = 220.5
    else:
        prijs = 250.5

    return prijs


def bepaal_prijs(oppervlakte, motor, kleur):
    kleur = kleur.upper()

    totale_prijs = oppervlakte * 113.5 + motor

    if kleur == "JA":
        totale_prijs = (oppervlakte * 113.5) * 1.10
        totale_prijs += motor

    return totale_prijs


def genereer_offertenummer(naam, prijs):
    huidig_jaar = 2022

    naam = naam.upper()
    prijs = prijs // 1

    prijs = int(prijs)
    prijs = str(prijs)

    prijs = prijs[::-1]

    offertenummer = str(huidig_jaar) + "_" + naam + "_" + prijs

    return offertenummer


def main():
    naam = input("Naam verkoper = ")
    hoogte = float(input("Hoogte = "))
    breedte = float(input("Breedte = "))
    kleur = input("Speciale kleur gewenst? ")

    correcte_hoogte = check_hoogte(hoogte)
    # print(correcte_hoogte)

    correcte_breedte = check_breedte(breedte)
    # print(correcte_breedte)

    oppervlakte = bereken_oppervlakte(correcte_hoogte, correcte_breedte)
    # print(oppervlakte)

    gewicht = bereken_gewicht(oppervlakte)
    # print(gewicht)

    motor = bepaal_motor(gewicht)

    prijs_motor = bepaal_motorprijs(motor)

    totale_prijs = bepaal_prijs(oppervlakte, prijs_motor, kleur)

    offertenummer = genereer_offertenummer(naam, totale_prijs)

    print(prijs_motor)
    print(totale_prijs)
    print(offertenummer)


if __name__ == '__main__':
    main()
