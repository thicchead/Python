personeelsnummer = int(input("Nummer = "))

eerste_output = 0
tweede_output = 0

while personeelsnummer != 0:
    geslacht = int(input("Geslacht = "))
    leeftijd = int(input("Leeftijd = "))
    brutoloon = int(input("Brutoloon = "))

    if geslacht > 1:
        print("Fout getal")
        geslacht = int(input("Geslacht = "))

    if geslacht == 0 and leeftijd < 25:
        tweede_output += 1

    if geslacht == 1:
        if leeftijd < 34:
            eerste_output += 1
        if brutoloon >= 1800:
            eerste_output += 1

    personeelsnummer = int(input("Nummer = "))

print(eerste_output)
print(tweede_output)
