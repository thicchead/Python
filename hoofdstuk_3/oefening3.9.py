getal_een = int(input("Getal één = "))
getal_twee = int(input("Getal twee = "))
bewerkingscode = int(input("Bewerkingscode = "))

resultaat = 0

if bewerkingscode == 1:
    resultaat = getal_een + getal_twee
elif bewerkingscode == 2:
    resultaat = getal_een - getal_twee
elif bewerkingscode == 3:
    resultaat = getal_een * getal_twee
elif bewerkingscode == 4:
    resultaat = getal_een ** 2
elif bewerkingscode == 5:
    resultaat = getal_twee ** 2
else:
    print("Foutieve code")

print(resultaat)
