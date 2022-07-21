def bepaal_prijs(volwassenen, kinderen, sterren, code, kindercode):
    twee_letters = code[:2].upper()
    print(twee_letters)
    prijs_per_nacht = 0

    if twee_letters == "HI":
        prijs_per_nacht = 70
    elif sterren == 5 or sterren == 4:
        prijs_per_nacht = 60
    elif sterren == 3 and twee_letters == "BR" or twee_letters == "AN":
        prijs_per_nacht = 60
    elif sterren == 3:
        prijs_per_nacht = 56
    else:
        prijs_per_nacht = 48

    if kindercode == "A":
        if sterren == 1 or sterren == 2:
            prijs_per_nacht = prijs_per_nacht * volwassenen
        if twee_letters != "BR":
            prijs_per_nacht = prijs_per_nacht * volwassenen
    else:
        prijs_per_nacht = prijs_per_nacht * volwassenen + prijs_per_nacht * 0.5 * kinderen

    return prijs_per_nacht


def main():
    hotelcode = input("Hotelcode = ")

    while hotelcode != "/":
        aantal_volwassenen = int(input("Aantal volwassenen = "))
        aantal_kinderen = int(input("Aantal kinderen = "))
        aantal_sterren = int(input("Aantal sterren = "))
        kindercode = input("Kindercode = ")
        kindercode = kindercode.upper()

        if chr(65) > kindercode > chr(90):
            print("Foute kindercode")

        prijs = bepaal_prijs(aantal_volwassenen, aantal_kinderen, aantal_sterren, hotelcode, kindercode)

        print(hotelcode.upper() + aantal_sterren * "*")
        print(prijs)
        print(prijs / 2)

        hotelcode = input("Hotelcode = ")


if __name__ == '__main__':
    main()
