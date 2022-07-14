def bereken_boete(boeken, dagen):
    totale_boete = (boeken * 0.07) * dagen

    return totale_boete

def main():
    naam = input("Naam = ")
    aantal_brieven = 0

    while naam != 'xx':
        aantal_boeken = int(input("Aantal boeken = "))
        aantal_dagen = int(input("Aantal dagen overschreden = "))
        boete = bereken_boete(aantal_boeken, aantal_dagen)

        if aantal_dagen >= 45:
            aantal_brieven += 1
            boete += 0.84

        print(boete)

        naam = input("Naam = ")


if __name__ == '__main__':
    main()
