def cumulative_sum(mijn_lijst):
    # cum_sum = 0
    #
    # for getal in mijn_lijst:
    #     cum_sum += getal
    #
    # for i in range(len(mijn_lijst)):
    #     mijn_lijst[i] == cum_sum

    for i in range(1, len(mijn_lijst)):
        mijn_lijst[i] += mijn_lijst[i - 1]

    print(mijn_lijst)


def main():
    lijst = [1, 2, 3, 4, 5, 6, 7, 8]

    cumulative_sum(lijst)


if __name__ == '__main__':
    main()
