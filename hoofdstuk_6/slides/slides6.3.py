def main():
    string_1 = input("Tekst één = ")
    string_2 = input("Tekst twee = ")

    kleinste_string = len(string_1)

    if len(string_2) < len(string_1):
        kleinste_string = string_2

    for letter in range(kleinste_string):
        if string_1[letter] == string_2[letter]:
            print(letter + 1)
            print(str(string_1[letter]))


if __name__ == '__main__':
    main()
