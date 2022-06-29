# Oefening om 2 variabelen van waarde te veranderen zonder derde hulpvariabele
getal1 = int(input("Getal 1 = "))
getal2 = int(input("Getal 2 = "))

getal1 = getal2 - getal1
getal2 -= getal1
getal1 += getal2

print(getal1)
print(getal2)
