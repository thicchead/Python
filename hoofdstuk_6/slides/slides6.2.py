def main():
    tekst = input("tekst = ")

    # klinkers = "a", "e", "i", "o", "u"
    #
    # for letter in tekst:
    #     if letter in klinkers:
    #         print(letter)

    for i in range(len(tekst)):
        if tekst[i] in "aeiou":
            print(i + 1)


if __name__ == '__main__':
    main()
