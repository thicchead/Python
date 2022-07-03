HUIDIG_JAAR = 2022
BASISBEDRAG = 100

aansluitingsjaar = int(input("Aansluitingsjaar = "))
leeftijd = int(input("Leeftijd = "))

jaarverschil = HUIDIG_JAAR - aansluitingsjaar
jaarkorting = jaarverschil * 2.5

if leeftijd < 21 or leeftijd > 60:
    BASISBEDRAG -= 14.5

BASISBEDRAG -= jaarkorting

if BASISBEDRAG < 62.5:
    BASISBEDRAG = 62.5

print(BASISBEDRAG)
