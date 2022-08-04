from random import randint


def main():
    getallenlijst = []
    groter_dan_5000 = 0
    som = 0

    for i in range(500):
        getallenlijst.append(randint(0, 10000))
    # print(getallenlijst)

    for getal in getallenlijst:
        if getal > 5000:
            groter_dan_5000 += 1

        if groter_dan_5000 < 250:
            if getal > 5000:
                som += getal
        else:
            if getal > 8000:
                som += getal

    print(som)


if __name__ == '__main__':
    main()
