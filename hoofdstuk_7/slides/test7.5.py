def wijziglijst(mijn_lijst, index, woord):
    if 0 <= index < len(mijn_lijst):
        mijn_lijst[index] = woord


def main():
    lijst = [1, 2, 3, 4, 5]
    te_wijzigen = 2
    nieuw = 9

    wijziglijst(lijst, te_wijzigen, nieuw)

    print(lijst)


if __name__ == '__main__':
    main()
