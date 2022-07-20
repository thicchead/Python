def main():
    tekst = "The quick brown fox jumps over de lazy cat"

    tekst = tekst.replace("d", "th")
    print(tekst)

    tekst = tekst.replace("cat", "dog")
    print(tekst)


if __name__ == '__main__':
    main()
