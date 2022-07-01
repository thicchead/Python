vertrekuur = int(input("Vertrekuur = "))
vertrekminuut = int(input("Vertrekminuut = "))

duur = int(input("Duur vlucht = "))

aantal_uren = duur // 60
aankomstuur = 0
if aantal_uren + vertrekuur >= 24:
    aankomstuur = (aantal_uren + vertrekuur) % 24
else:
    aankomstuur = aantal_uren + vertrekuur

aankomstminuut = vertrekminuut + (duur % 60)

if aankomstminuut >= 60:
    aankomstuur += 1
    aankomstminuut -= 60

print("Aankomstuur = " + str(aankomstuur))
print("Aankomstminuut = " + str(aankomstminuut))
