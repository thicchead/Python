def hotel_kosten(aantal_nachten):
    aantal_gratis = (aantal_nachten / 3) * 140.50
    return aantal_nachten * 140.50 - aantal_gratis


def vliegtuig_kosten(stad):
    vliegticket = 0
    if stad == "Barcelona":
        vliegticket = 183
    elif stad == "Rome":
        vliegticket = 220
    elif stad == "Berlijn":
        vliegticket = 125
    elif stad == "Oslo":
        vliegticket = 450

    return vliegticket


def huurauto_kosten(aantal_dagen):
    auto_kosten = aantal_dagen * 40
    if aantal_dagen > 7:
        auto_kosten -= 50
    elif aantal_dagen > 3:
        auto_kosten -= 20

    return auto_kosten


def reis_kosten(stad, aantal_dagen):
    kost1 = hotel_kosten(aantal_dagen - 1)
    kost2 = vliegtuig_kosten(stad)
    kost3 = huurauto_kosten(aantal_dagen)


    if stad == "Barcelona":
        totale_prijs = kost1 + kost2 + kost3
    elif stad == "Rome":
        totale_prijs = kost1 + kost2 + kost3
    elif stad == "Berlijn":
        totale_prijs = kost1 + kost2 + kost3
    elif stad == "Oslo":
        totale_prijs = kost1 + kost2 + kost3
    else:
        totale_prijs = 0
        print("Foute stad ingegeven")

    return totale_prijs


def main():
    dagen = int(input("Aantal dagen = "))
    stad = input("Stad = ")

    print(reis_kosten(stad, dagen))


if __name__ == '__main__':
    main()
