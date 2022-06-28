afgelegde_km = float(input("Afgelegde km per jaar = "))
verbruik = float(input("Verbruik per 100 km (in liter) = "))
prijs_per_liter = float(input("Prijs van 1 liter brandstof = "))

totale_kosten = ((afgelegde_km / 100) * verbruik) * prijs_per_liter
prijs_per_km = (prijs_per_liter * verbruik) / 100

print(totale_kosten)
print(prijs_per_km)
