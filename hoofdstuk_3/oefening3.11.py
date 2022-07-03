aantal_sterren = int(input("Aantal sterren = "))
code = input("Code = ")
aantal_overnachtingen = int(input("Aantal overnachtingen = "))
seizoen = input("Seizoen = ")

prijs = 0

if aantal_sterren == 1:
    prijs = aantal_overnachtingen * 30
elif aantal_sterren == 2 or aantal_sterren == 3:
    prijs = aantal_overnachtingen * 45
else:
    prijs = aantal_overnachtingen * 55

if code == "O":
    prijs *= 1.20
elif code == "H":
    prijs *= 1.50
elif code == "V":
    prijs *= 1.60
else:
    prijs *= 1.60
    prijs += aantal_overnachtingen * 80

if seizoen == "L":
    if code == "O" or code == "H":
        prijs *= 0.90

print(prijs)
