def main():
    lijst = [1, -15, 3, 64, 5, 600, 7, 8]

    maximum = -1000
    minimum = 1000
    som = 0

    for cijfer in lijst:
        if cijfer > maximum:
            maximum = cijfer

        if cijfer < minimum:
            minimum = cijfer

        som += cijfer

    print(str(maximum) + " = maximum")
    print(str(minimum) + " = minimum")
    print(str(som) + " = som")


if __name__ == '__main__':
    main()
