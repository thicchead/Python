def bereken_schrikkeljaar(jaar):
    if jaar % 400 == 0:
        return True
    elif jaar % 100 == 0:
        return False
    elif jaar % 4 == 0:
        return True
    else:
        return False


def main():
    jaartal = int(input("Jaar = "))
    print(bereken_schrikkeljaar(jaartal))


if __name__ == '__main__':
    main()
