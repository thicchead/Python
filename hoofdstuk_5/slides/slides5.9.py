from random import randint


def main():
    print(randint(0, 10))

    for i in range(0, 11):
        print(randint(1, 9))

    print(randint(-20, 100) * 10)

    print(randint(0, 999) / 10)


if __name__ == '__main__':
    main()