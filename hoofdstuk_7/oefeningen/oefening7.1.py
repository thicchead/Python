def main():
    getallenlijst = []
    som = 0
    kleiner_dan_gem = 0

    for i in range(15):
        getal = int(input("Getal " + str(i + 1) + " = "))
        getallenlijst.append(getal)
        som += getal
        gemiddelde = som / (i + 1)

        if getal < gemiddelde:
            kleiner_dan_gem += 1

    print(str(kleiner_dan_gem) + " getallen zijn kleiner dan het gemiddelde")

    procent = (kleiner_dan_gem * (100 / 15))
    print("En dat is " + str(procent) + " procent")


if __name__ == '__main__':
    main()
