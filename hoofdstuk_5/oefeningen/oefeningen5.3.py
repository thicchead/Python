HUIDIG_JAAR = 2022


def bereken_lidgeld(leeftijd, kinderen, aansluitingsjaar, inkomen):
    lidgeld = 100

    waarde_kind = kinderen * 7.5

    jaren_lid = HUIDIG_JAAR - aansluitingsjaar

    if waarde_kind > 35:
        waarde_kind = 35

    if leeftijd > 60:
        lidgeld -= 15

    if kinderen != 0:
        lidgeld -= waarde_kind

    if jaren_lid > 20:
        lidgeld -= 12.5

    if inkomen < 7500:
        lidgeld -= 25

    if lidgeld < 50:
        lidgeld = 50

    return lidgeld


def main():
    naam = input("Naam = ")

    while naam != "x" and naam != "X":
        leeftijd = int(input("Leeftijd = "))
        aantal_kinderen = int(input("Aantal kinderen = "))
        aansluitingsjaar = int(input("Aansluitingsjaar = "))
        inkomen = int(input("Inkomen = "))

        print(bereken_lidgeld(leeftijd, aantal_kinderen, aansluitingsjaar, inkomen))

        naam = input("Naam = ")


if __name__ == '__main__':
    main()
