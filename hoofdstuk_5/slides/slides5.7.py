def toon_tafel(getal):
    for i in range(1, 11):
        print(str(i) + " x " + str(getal) + " = " + str(i * getal))


def main():
    nummer = int(input("Getal = "))

    toon_tafel(nummer)


if __name__ == '__main__':
    main()
