leerlingen = 0
gemiddelde = 0
totaal_leeftijden = 0

while leerlingen < 29:
    leeftijden = int(input("Leeftijd " + str(leerlingen + 1) + " = "))
    totaal_leeftijden += leeftijden
    leerlingen += 1
    gemiddelde = leeftijden / 28

print(gemiddelde)
