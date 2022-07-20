def main():
    woord = input("Woord = ")
    midden = len(woord) // 2

    if len(woord) % 2 != 0:
        print(woord[:midden] + woord[midden].upper() + woord[midden + 1:])
    else:
        print(woord[:midden - 1] + woord[midden - 1:midden + 1].upper() + woord[midden + 1:])
        # eh


if __name__ == '__main__':
    main()
