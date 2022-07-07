inschrijvingsnummer = int(input("Nummer = "))

aantal_renners = 0
snelste_tijd = 10000000000
snelste_renner = 0
langer_dan_een_uur = 0


while inschrijvingsnummer > 0:
    tijd = int(input("Seconden = "))

    aantal_renners += 1

    if tijd < snelste_tijd:
        snelste_renner = inschrijvingsnummer
        snelste_tijd = tijd

    if tijd // 3600 >= 1:
        langer_dan_een_uur += 1

    inschrijvingsnummer = int(input("Nummer = "))

percentage = (langer_dan_een_uur / aantal_renners) * 100

print(langer_dan_een_uur)
print(aantal_renners)

print(snelste_renner)
print(percentage)
