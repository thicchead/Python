from random import randint


def bewerking():
    #     for i in range(1, 21):
    #         for j in range(1, i + 1):
    #             print(str(i) + " - " + str(j) + " = ")
    i = randint(1, 20)
    j = randint(1, i)
    print(str(i) + " - " + str(j) + " = ")


def main():
    aantal_reeksen = int(input("Aantal reeksen = "))
    if aantal_reeksen == 0:
        aantal_reeksen = 1

    for i in range(1, aantal_reeksen + 1):
        print("reeks " + str(i))
        for j in range(1, 6):
            bewerking()


if __name__ == '__main__':
    main()
