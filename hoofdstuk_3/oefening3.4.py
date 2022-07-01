getal_een = float(input("Getal één = "))
getal_twee = float(input("Getal twee = "))

kleinste_getal = 0
grootste_getal = 0

if getal_een > getal_twee:
    kleinste_getal = getal_twee
    grootste_getal = getal_een
else:
    kleinste_getal = getal_een
    grootste_getal = getal_twee
print(kleinste_getal)

kwadraat = kleinste_getal ** 2
print(kwadraat)

if kleinste_getal == 0:
    print("Deling door 0 gaat niet")
else:
    print(grootste_getal / kleinste_getal)
    