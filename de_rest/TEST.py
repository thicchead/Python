# def bepaal_score(nm, jaar):
#     basisscore = 0
#     juiste_letters = []
#     indexes = []
#
#     for letter in nm:
#         if letter in "cinema":
#             juiste_letters.append(letter)
#
#     for i in range(len(nm)):
#         if nm[i] in "cinema":
#             indexes.append(i + 1)
#
#     for j in range(len(juiste_letters)):
#         list = []
#         asciis = ord(juiste_letters[j])
#         list.append(asciis)
#
#     for let in juiste_letters:
#         print(let)
#
#     for getal in indexes:
#         print(getal)
#
#     for a in list:
#         print(a)
#
# def main():
#     naam = input("Naam = ")
#
#     while naam != "xxx" or naam != "qqq":
#         geboortejaar = int(input("Geboortejaar = "))
#         aantal_bezoeken = int(input("Hoevaak bezoek je kp? "))
#         versnappering = input("Welke snack koop je? ")
#
#         bepaal_score(naam, geboortejaar)
#
#
# if __name__ == '__main__':
#     main()
