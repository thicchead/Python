def main():
    positieve_getallen = []
    negatieve_getallen = []

    for i in range(10):
        getal = int(input("Getal " + str(i + 1) + " = "))

        if getal < 0:
            negatieve_getallen.append(getal)
        else:
            positieve_getallen.append(getal)

    print(len(positieve_getallen))
    print(len(negatieve_getallen))

    for waarde in positieve_getallen:
        print(waarde)

    kleinste_getal = 0

    for waarde in negatieve_getallen:
        print(waarde)

        if waarde < kleinste_getal:
            kleinste_getal = waarde
    print(kleinste_getal)


if __name__ == '__main__':
    main()
