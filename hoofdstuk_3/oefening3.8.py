afstand = int(input("Afstand = "))
klasse = int(input("Klasse = "))

prijs = 0

if afstand < 1000:
    prijs = afstand * 0.25
elif afstand < 2999:
    prijs = afstand * 0.20
else:
    prijs = afstand * 0.12

if klasse == 2:
    prijs *= 0.80
elif klasse == 3:
    prijs *= 1.30

print(prijs)
