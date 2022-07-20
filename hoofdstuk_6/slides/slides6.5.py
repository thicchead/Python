def main():
    naam = input("Naam = ")
    voornaam = input("Voornaam = ")

    voornaam = voornaam[0].upper() + ". "
    naam = naam[0].upper() + naam[1:].lower()

    nieuwe_naam = voornaam + naam

    print(nieuwe_naam)


if __name__ == '__main__':
    main()
