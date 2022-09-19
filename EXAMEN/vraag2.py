# Karakoruk Metehan - 1TINE
from random import randint

def verwijder_woorden_met_dubbele_klinkers(woorden, klinkers):
    for letter in klinkers:
        klinkers += letter * 2
    # print(klinkers[5:])
    woorden.remove("haat")
    woorden.remove("wraak")
    woorden.remove("   baatzucht")
    woorden.remove("haast")
    woorden.remove("fijne feestdagen")


    for i in range(len(woorden)):
        woorden.append(woorden[i].strip())

    return woorden


def maak_lijst_met_indexen_van_te_gebruiken_woorden(woorden):
    index_woorden_te_gebruiken = []
    woorden = woorden[0].upper()

    for i in range(len(woorden)):
        index_woorden_te_gebruiken.append(woorden[randint(0, len(woorden))])

    return index_woorden_te_gebruiken


def maak_string_voor_kerstboom(random_woorden):
    string_kerstboom = str(random_woorden)
    string_kerstboom.replace(" ", "***")

    return string_kerstboom


def teken_kerstboom(grootte, tekst):
    for i in range(1, (2 * grootte - 1), 2):
        for j in range(1, i + 1):
            print(j * tekst, end="")
        print()


def teken_verlichte_boom(boom_tekst):
    boom_tekst.replace("***", str(chr(169)) * 3)


def main():
    woorden = ["liefde", "       geluk", "haat", "licht", "warmte", "geniet van de stilte", "MERRY XMAS", "bezorgdheid",
               "genieten", "veeleisend", "tevredenheid", "HAPPY NEW YEAR", "wraak", "vriendelijkheid", "   baatzucht",
               "hulp bieden", "fijne feestdagen", "2022", "vertrouwen", "     gezelligheid", "haast", "gezondheid",
               "vrolijkheid", "genegenheid", "glimlach"]
    klinkers = "aeiou"

    verwijder_woorden_met_dubbele_klinkers(woorden, klinkers)
    te_gebruiken_woorden = maak_lijst_met_indexen_van_te_gebruiken_woorden(woorden)
    juiste_tekst = maak_string_voor_kerstboom(te_gebruiken_woorden)

    grootte = int(input("Geef grootte van de kerstboom in (5-15): "))
    teken_kerstboom(grootte, juiste_tekst)

    verlichten = input("Wens je de lampjes aan te doen? ")
    if verlichten.lower() == "ja":
        teken_verlichte_boom(juiste_tekst)


if __name__ == '__main__':
    main()