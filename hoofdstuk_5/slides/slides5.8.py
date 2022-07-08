def berekening(bedrag):
    # eerste_deel = bedrag
    # tweede_deel = bedrag - 25000
    # derde_deel = bedrag - 55000
    # if bedrag <= 25000:
    #     return eerste_deel * 1.384
    # elif bedrag <= 55000:
    #     return tweede_deel * 1.5 + eerste_deel * 1.384
    # else:
    #     return derde_deel * 1.6 + tweede_deel * 1.5 + eerste_deel * 1.384
    if bedrag >= 55000:
        belasting = ((bedrag - 55000) * 0.6) + (25000 * 0.384) + (30000 * 0.5)
    elif bedrag >= 25000:
        belasting = ((bedrag - 25000) * 0.5) + (25000 * 0.384)
    else:
        belasting = bedrag * 0.384
    return belasting


def main():
    belastbaar_bedrag = int(input("Bedrag = "))
    belasting = berekening(belastbaar_bedrag)

    print(belasting)


if __name__ == '__main__':
    main()
