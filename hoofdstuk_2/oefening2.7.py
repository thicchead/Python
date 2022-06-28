lengte_tapijt = float(input("Lengte tapijt = "))
breedte_tapijt = float(input("Breedte tapijt = "))
prijs_per_meter = float(input("Prijs per vierkante meter = "))
plaatsingskosten = float(input("Plaatsingskosten per vierkante meter = "))

oppervlakte = lengte_tapijt * breedte_tapijt

kostprijs_tapijt = oppervlakte * prijs_per_meter
totale_plaatsingskosten = oppervlakte * plaatsingskosten

totale_kost = kostprijs_tapijt + totale_plaatsingskosten

print(kostprijs_tapijt)
print(totale_plaatsingskosten)
print(totale_plaatsingskosten)
