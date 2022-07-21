def main():
    tekst = input("Tekst = ")
    tekst = tekst.lower()

    positie_t = tekst.find("t")
    #    print(positie_t)

    if positie_t == -1:
        print("Geen T of t aanwezig in de input")

    if len(tekst) % 2 == 0:
        print(tekst[:positie_t] + tekst[positie_t:].lower())
    else:
        print(tekst[:positie_t] + tekst[positie_t:].upper())


if __name__ == '__main__':
    main()
