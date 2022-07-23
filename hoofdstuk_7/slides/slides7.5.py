def vind_element(mijn_lijst, getal):
    # totaal = 0
    #
    # for element in mijn_lijst:
    #     if element == getal:
    #         print(mijn_lijst[element])
    #         totaal += 1

    print(mijn_lijst.count(getal))

    for i in range(len(mijn_lijst)):
        if getal == mijn_lijst[i]:
            print(i)

    # print(len(mijn_lijst))


def main():
    lijst = [1, 5, 9, 7, 6, 4, 2, 7, 6, 4, 4, 1]
    element = 1

    vind_element(lijst, element)


if __name__ == '__main__':
    main()
