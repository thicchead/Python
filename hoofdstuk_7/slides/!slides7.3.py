def main():
    getallenlijst = []

    getal = int(input("Getal = "))

    while getal != 0:

        # for i in getallenlijst:
        #     if getallenlijst[i] == getal:
        #         print(getallenlijst.index(getal))
        #         getallenlijst.remove(getal)

        if getal in getallenlijst:
            print(getallenlijst.index(getal))
            getallenlijst.remove(getal)
        else:
            getallenlijst.append(getal)

        getal = int(input("Getal = "))

    print(getallenlijst)


if __name__ == '__main__':
    main()
