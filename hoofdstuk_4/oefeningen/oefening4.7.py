hoogste_temperatuur = -1000
totaal = 0
gemiddelde = 0

for i in range(1, 11):
    temperatuur = int(input("Temperatuur dag " + str(i) + " = "))

    if temperatuur > hoogste_temperatuur:
        hoogste_temperatuur = temperatuur

    totaal += temperatuur
    gemiddelde = totaal / 10


print(hoogste_temperatuur)
print(gemiddelde)
