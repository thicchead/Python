totaal = 0
gemiddelde = 0

for i in range(27):
    leeftijd = int(input("Leeftijd " + str(i+1) + " = "))
    totaal += leeftijd
    gemiddelde = totaal / 27

print(gemiddelde)
