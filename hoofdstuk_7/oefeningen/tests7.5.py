def main():
    numlijst = []

    numlijst.append(1)
    numlijst.append(1)
    a = int(input(" = "))

    numlijst.append(a)

    for num in numlijst:
        print(num)

    print(len(numlijst))


if __name__ == '__main__':
    main()
