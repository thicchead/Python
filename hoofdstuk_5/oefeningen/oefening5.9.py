def hotel_kosten(aantal_nachten):
    beginprijs = aantal_nachten * 140.50
    aantal_derde_nachten = aantal_nachten // 3
    korting = aantal_derde_nachten * 140.50
    eindprijs = beginprijs - korting

    return eindprijs


def vliegtuig_kosten(locatie):

    if locatie == "Barcelona":
        prijs = 183
    elif locatie == "Rome":
        prijs = 220
    elif locatie == "Berlijn":
        prijs = 125
    else:
        prijs = 450

    return prijs


def huurauto_kosten(dagen):
    prijs = dagen * 40

    if dagen > 7:
        prijs -= 50
    elif dagen > 3:
        prijs -= 20

    return prijs


def main():
    nachten = int(input("Aantal nachten = "))
    prijs_hotel = hotel_kosten(nachten)
    print(prijs_hotel)

    stad = input("Stad = ")
    prijs_vlucht = vliegtuig_kosten(stad)
    print(prijs_vlucht)

    aantal_dagen = int(input("Aantal dagen = "))
    prijs_auto = huurauto_kosten(aantal_dagen)
    print(prijs_auto)

    totaal = prijs_auto + prijs_hotel + prijs_vlucht
    print(totaal)


if __name__ == '__main__':
    main()
