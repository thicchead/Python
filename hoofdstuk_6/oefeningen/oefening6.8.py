def main():
    grootte = int(input("Grootte = "))
    beginletter = input("Beginletter = ")

    grootte += 1
    beginletter = beginletter.upper()
    beginletter = ord(beginletter)

    for i in range(1, grootte):
        for j in range(1, i + 1):
            print(chr(beginletter), end=" ")
            beginletter += 1
            if beginletter > 90:
                beginletter = 65
            # print(chr(beginletter) + chr(1), end=" ")
        print()


if __name__ == '__main__':
    main()

# begint met letter
# 	tekst --> ascii
# 	ascii + 1
# 	ascii --> tekst
