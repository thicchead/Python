EENHEIDSPRIJS = 11.5
BTWPERCENTAGE = 0.21

aantal = int(input("Aantal artikelen = "))

totale_prijs = EENHEIDSPRIJS * aantal * (1 + BTWPERCENTAGE)

if totale_prijs > 1000:
    totale_prijs *= 0.90
else:
    totale_prijs = totale_prijs

print(totale_prijs)
