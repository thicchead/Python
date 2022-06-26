# Oefening om totale ticketprijs te berekenen

PRIJS_VOLWASSENEN = 11
PRIJS_KINDEREN = 6

aantal_volwassenen = int(input("Aantal volwassenen = "))
aantal_kinderen = int(input("Aantal kinderen = "))

totale_prijs = (aantal_volwassenen * PRIJS_VOLWASSENEN) + (aantal_kinderen * PRIJS_KINDEREN)

print("De totale prijs voor " + str(aantal_volwassenen) + " volwassenen en " + str(aantal_kinderen) + " kinderen is = " + str(totale_prijs) + " euro")
