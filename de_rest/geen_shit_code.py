woorden = ["liefde", "       geluk", "haat", "licht", "warmte", "geniet van de stilte", "MERRY XMAS", "bezorgdheid",
           "genieten", "veeleisend", "tevredenheid", "HAPPY NEW YEAR", "wraak", "vriendelijkheid", "   baatzucht",
           "hulp bieden", "fijne feestdagen", "2022", "vertrouwen", "     gezelligheid", "haast", "gezondheid",
           "vrolijkheid", "genegenheid", "glimlach"]

str = ""

for woord in woorden:
    woord.split()
    str += woord + ", "

print(str.strip())
